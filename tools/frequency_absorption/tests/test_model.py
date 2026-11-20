"""Unit tests for the frequency-versus-absorption script (stdlib unittest)."""

from __future__ import annotations

import csv
import math
import tempfile
import unittest
from pathlib import Path

from tools.frequency_absorption.bands import PRODUCT_BANDS
from tools.frequency_absorption.cole_cole import (
    TISSUES,
    complex_relative_permittivity,
    effective_conductivity,
)
from tools.frequency_absorption.constants import (
    EPSILON_0,
    MU_0,
    RHO_CONVENTIONAL_KG_M3,
    SPEED_OF_LIGHT,
)
from tools.frequency_absorption.generate import CSV_COLUMNS, generate, rows_for_bands

def assert_rel_close(test, a, b, rel=1e-9, msg=None):
    scale = max(abs(a), abs(b), 1e-30)
    test.assertAlmostEqual(a, b, delta=rel * scale, msg=msg)


from tools.frequency_absorption.plane_wave import (
    FCC_TOOL_FMAX_HZ,
    FCC_TOOL_FMIN_HZ,
    _alpha_closed_form,
    plane_wave_estimates,
    skin_depth,
    wavenumber,
)


class ConstantsTests(unittest.TestCase):
    def test_epsilon0_matches_opened_nist_2022(self):
        # Quote from https://physics.nist.gov/cgi-bin/cuu/Value?ep0
        # opened 19 Nov 2026: "8.854 187 8188 x 10-12 F m-1"
        self.assertEqual(EPSILON_0, 8.8541878188e-12)

    def test_mu0_consistent_with_epsilon0_and_c(self):
        self.assertAlmostEqual(MU_0, 1.0 / (EPSILON_0 * SPEED_OF_LIGHT**2), places=30)

    def test_rho_is_labeled_conventional(self):
        self.assertEqual(RHO_CONVENTIONAL_KG_M3, 1000.0)


class ColeColeTests(unittest.TestCase):
    def test_muscle_table_row_copied(self):
        m = TISSUES["muscle"]
        self.assertEqual(m.eps_inf, 4.0)
        self.assertEqual(m.delta_eps, (50.0, 7000.0, 1.2e6, 2.5e7))
        self.assertEqual(m.sigma_ionic, 0.2000)
        # τ1 = 7.23 ps from Table 1
        self.assertAlmostEqual(m.tau_s[0], 7.23e-12, places=20)

    def test_dry_skin_has_only_two_dispersions(self):
        s = TISSUES["skin_dry"]
        self.assertEqual(s.delta_eps[2], 0.0)
        self.assertEqual(s.delta_eps[3], 0.0)
        self.assertEqual(s.sigma_ionic, 0.0002)

    def test_frequency_must_be_positive(self):
        with self.assertRaises(ValueError):
            complex_relative_permittivity(TISSUES["muscle"], 0.0)
        with self.assertRaises(ValueError):
            plane_wave_estimates(TISSUES["muscle"], -1.0)

    def test_high_frequency_permittivity_approaches_eps_inf(self):
        # At 100 GHz the first (ps) dispersion is not fully relaxed, but ε'
        # must lie between ε∞ and ε∞+Δε1 and be much closer to ε∞ than to static.
        eps = complex_relative_permittivity(TISSUES["muscle"], 100e9)
        self.assertGreater(eps.real, TISSUES["muscle"].eps_inf)
        self.assertLess(eps.real, TISSUES["muscle"].eps_inf + TISSUES["muscle"].delta_eps[0])

    def test_low_frequency_ionic_term_dominates_imaginary_part(self):
        # At the 10 Hz lower edge of the opened PMB model range, the ionic
        # term σ_i/(ωε0) accounts for nearly all of ε''. Residual low-frequency
        # Cole-Cole (β/δ) loss is expected and is a few parts in 10^2 here.
        f = 10.0
        eps = complex_relative_permittivity(TISSUES["muscle"], f)
        omega = 2 * math.pi * f
        ionic = TISSUES["muscle"].sigma_ionic / (omega * EPSILON_0)
        self.assertGreater(-eps.imag, 0.98 * ionic)
        self.assertLess(-eps.imag, 1.05 * ionic)

    def test_effective_conductivity_recovers_ionic_limit_at_low_frequency(self):
        sigma = effective_conductivity(TISSUES["muscle"], 10.0)
        self.assertGreater(sigma, TISSUES["muscle"].sigma_ionic)
        self.assertLess(sigma, TISSUES["muscle"].sigma_ionic * 1.05)

    def test_permittivity_imaginary_part_is_non_positive(self):
        for key in TISSUES:
            for f in (13.56e6, 915e6, 2450e6, 5.8e9, 28e9):
                eps = complex_relative_permittivity(TISSUES[key], f)
                self.assertLessEqual(eps.imag, 1e-9, msg=f"{key} at {f}")
                self.assertGreater(effective_conductivity(TISSUES[key], f), 0.0)


class SkinDepthTests(unittest.TestCase):
    def test_complex_k_matches_closed_form_alpha(self):
        for key in TISSUES:
            for f in (27.12e6, 915e6, 2450e6, 24.125e9):
                k = wavenumber(TISSUES[key], f)
                self.assertGreaterEqual(k.real, 0.0)
                self.assertLessEqual(k.imag, 0.0)
                alpha_k = -k.imag
                alpha_cf = _alpha_closed_form(TISSUES[key], f)
                assert_rel_close(self, alpha_k, alpha_cf, rel=1e-9, msg=f"{key} {f}")

    def test_skin_depth_decreases_from_hf_radio_to_microwave_for_muscle(self):
        d_27 = skin_depth(TISSUES["muscle"], 27.12e6)
        d_915 = skin_depth(TISSUES["muscle"], 915e6)
        d_5800 = skin_depth(TISSUES["muscle"], 5800e6)
        self.assertGreater(d_27, d_915)
        self.assertGreater(d_915, d_5800)

    def test_fat_skin_depth_not_equal_to_muscle(self):
        # Per-case: two tissues at the same frequency must not be collapsed.
        f = 915e6
        d_m = skin_depth(TISSUES["muscle"], f)
        d_f = skin_depth(TISSUES["fat_not_infiltrated"], f)
        self.assertGreater(abs(d_m - d_f) / max(d_m, d_f), 1e-3)


class PlaneWaveTests(unittest.TestCase):
    def test_sar_scales_linearly_with_s0(self):
        a = plane_wave_estimates(TISSUES["muscle"], 915e6, s0=1.0)
        b = plane_wave_estimates(TISSUES["muscle"], 915e6, s0=2.0)
        assert_rel_close(self, b.surface_sar_estimate_w_kg, 2 * a.surface_sar_estimate_w_kg, rel=1e-12)
        assert_rel_close(self, b.sar_avg_0p30m_w_kg, 2 * a.sar_avg_0p30m_w_kg, rel=1e-12)
        assert_rel_close(self, b.absorbed_power_density_w_m2, 2 * a.absorbed_power_density_w_m2, rel=1e-12)

    def test_reflection_and_absorption_bounds(self):
        for band in PRODUCT_BANDS:
            est = plane_wave_estimates(TISSUES["muscle"], band.freq_hz)
            self.assertGreaterEqual(est.reflection_coeff_mag, 0.0)
            self.assertLessEqual(est.reflection_coeff_mag, 1.0)
            self.assertGreaterEqual(est.absorbed_power_density_w_m2, 0.0)
            self.assertLessEqual(est.absorbed_power_density_w_m2, 1.0 + 1e-12)
            self.assertGreater(est.surface_sar_estimate_w_kg, 0.0)
            self.assertGreater(est.sar_avg_0p30m_w_kg, 0.0)
            self.assertLessEqual(est.sar_avg_0p30m_w_kg, est.surface_sar_estimate_w_kg + 1e-18)

    def test_fcc_window_flag(self):
        inside = plane_wave_estimates(TISSUES["muscle"], 915e6)
        self.assertFalse(inside.outside_fcc_tool_range)
        outside = plane_wave_estimates(TISSUES["muscle"], 24.125e9)
        self.assertTrue(outside.outside_fcc_tool_range)
        self.assertFalse(outside.outside_pmb_model_range)
        self.assertEqual(FCC_TOOL_FMIN_HZ, 10e6)
        self.assertEqual(FCC_TOOL_FMAX_HZ, 6000e6)


class BandsTests(unittest.TestCase):
    def test_every_band_has_a_source_url_and_positive_frequency(self):
        keys = [b.key for b in PRODUCT_BANDS]
        self.assertEqual(len(keys), len(set(keys)))
        for band in PRODUCT_BANDS:
            self.assertTrue(band.source_url.startswith("https://"))
            self.assertGreater(band.freq_hz, 0)
            self.assertTrue(band.citation)
            self.assertTrue(band.opened_range)

    def test_opened_ism_and_cellular_centers(self):
        by_key = {b.key: b for b in PRODUCT_BANDS}
        self.assertAlmostEqual(by_key["ism_27p12"].freq_hz, 27.12e6)
        self.assertAlmostEqual(by_key["ism_915"].freq_hz, 915e6)
        self.assertAlmostEqual(by_key["cellular_ul"].freq_hz, 836.5e6)
        self.assertAlmostEqual(by_key["cellular_dl"].freq_hz, 881.5e6)
        self.assertAlmostEqual(by_key["wifi_2400"].freq_hz, 2441.75e6)


class GenerateTests(unittest.TestCase):
    def test_csv_columns_and_row_count(self):
        rows = rows_for_bands()
        self.assertEqual(len(rows), len(PRODUCT_BANDS) * len(TISSUES))
        for row in rows:
            self.assertEqual(set(row), set(CSV_COLUMNS))
            self.assertIn("not applicable", row["cancer_type"])
            self.assertTrue(row["body_site"])

    def test_reproducible_outputs(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            pa = generate(Path(a))
            pb = generate(Path(b))
            self.assertEqual(pa["csv"].read_bytes(), pb["csv"].read_bytes())
            self.assertEqual(pa["md"].read_bytes(), pb["md"].read_bytes())
            self.assertEqual(pa["svg"].read_bytes(), pb["svg"].read_bytes())
            self.assertEqual(pa["png"].read_bytes(), pb["png"].read_bytes())
            self.assertGreater(pa["png"].stat().st_size, 1000)
            # PNG signature
            self.assertTrue(pa["png"].read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
            with pa["csv"].open(newline="", encoding="utf-8") as fh:
                reader = csv.DictReader(fh)
                self.assertEqual(reader.fieldnames, CSV_COLUMNS)
                recs = list(reader)
            self.assertEqual(len(recs), len(PRODUCT_BANDS) * len(TISSUES))


if __name__ == "__main__":
    unittest.main()
