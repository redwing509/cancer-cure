"""Plane-wave skin depth and a simplified absorption estimate.

These are first-order estimates for a normally incident plane wave on a
homogeneous half-space of one Gabriel tissue. They are not a whole-body
human phantom, not a device-antenna simulation, and not a substitute for
openEMS or Meep.

Skin depth (power e-folding of the field is 1/α, power 1/(2α)):

    A time-harmonic field ~ exp(jωt) propagating in +z as exp(-j k z) has
    complex wavenumber

        k = ω √(μ0 ε0 ε̂(ω))

    with the square-root branch chosen so that Re(k) ≥ 0 and Im(k) ≤ 0
    (decay in +z). The field skin depth is

        δ = 1 / α ,   α = -Im(k).

    Equivalently, writing ε̂ = ε' - jε'' with ε', ε'' real and ε'' ≥ 0,

        α = ω √(μ0 ε0 ε'/2)  √(√(1+(ε''/ε')^2) - 1)

    when ε' > 0 (standard lossy-dielectric identity; both forms are
    computed and checked against each other in the unit tests).

    The half-space and the decay exp(-α z) are the standard textbook
    treatment of a lossy medium; this script does not invent a new
    formula. No tissue-specific skin-depth table from a second paper is
    bundled here.

Surface field and SAR *estimate*:

    In air (lossless), an rms field E_i,rms and power density S0 are
    related by S0 = |E_i,rms|^2 / η0, with η0 = √(μ0/ε0).

    At normal incidence from air (η0) onto the half-space (η = √(μ0/ε_c),
    ε_c = ε0 ε̂), the electric-field reflection coefficient is

        Γ = (η - η0) / (η + η0)

    and the transmitted surface field (continuous tangential E) is
    E_t,rms = (1 + Γ) E_i,rms. Inside the half-space the field decays as
    exp(-α z).

    The specific absorption rate at a point is the standard definition

        SAR = σ_eff |E_rms|^2 / ρ

    used in radiofrequency dosimetry (σ_eff |E|^2 is volumetric dissipated
    power; dividing by mass density yields W kg^{-1}). 47 CFR § 2.1093,
    opened via LII on 19 Nov 2026
    (https://www.law.cornell.edu/cfr/text/47/2.1093), refers portable-device
    evaluations to the "SAR limits specified in § 1.1310" for 100 kHz to
    6 GHz, but the opened excerpt of § 2.1093 does not reprint the
    algebraic definition. This script therefore uses the standard
    definition above, with ρ set to the conventional 1000 kg m^{-3}
    (see constants.py), and labels every SAR column as an *estimate*.

    A "simplified whole-body SAR estimate" is reported as the depth
    average of this half-space SAR over a 0.30 m slab,

        SAR_avg(d) = (1/d) ∫_0^d SAR(0) exp(-2α z) dz
                   = SAR(0) * (1 - exp(-2α d)) / (2α d)

    with d = 0.30 m chosen only as a body-scale length (about a torso
    depth), *not* as an anatomical model, *not* as an ICNIRP or FCC
    averaging mass, and *not* as evidence that a frequency is safer.
    The table also reports surface SAR, the average over one field skin
    depth, and the absorbed power density (1 - |Γ|^2) S0, which does not
    depend on ρ.

Incident S0 = 1 W m^{-2} is a normalization, not an exposure limit.
Results scale linearly with S0.
"""

from __future__ import annotations

import cmath
import math
from dataclasses import dataclass

from .cole_cole import TissueParameters, complex_relative_permittivity, effective_conductivity
from .constants import EPSILON_0, MU_0, RHO_CONVENTIONAL_KG_M3, S0_W_M2


# Body-scale slab thickness used only for the "simplified whole-body"
# average. Labeled in every output. Metres.
WHOLE_BODY_SLAB_M = 0.30

# FCC public calculator frequency window, from the opened FCC page:
# "The tool calculates parameters for frequencies between 10-6,000 MHz."
# https://www.fcc.gov/general/body-tissue-dielectric-parameters
FCC_TOOL_FMIN_HZ = 10e6
FCC_TOOL_FMAX_HZ = 6000e6

# PMB 1996 model range as stated in the opened paper: 10 Hz to 100 GHz.
PMB_MODEL_FMIN_HZ = 10.0
PMB_MODEL_FMAX_HZ = 100e9


def _eta0() -> float:
    return math.sqrt(MU_0 / EPSILON_0)


def wavenumber(tissue: TissueParameters, freq_hz: float) -> complex:
    """k = ω √(μ0 ε0 ε̂), branch Re(k) ≥ 0, Im(k) ≤ 0."""
    omega = 2.0 * math.pi * freq_hz
    eps = complex_relative_permittivity(tissue, freq_hz)
    k = omega * cmath.sqrt(MU_0 * EPSILON_0 * eps)
    # Keep the decaying-in-+z branch, Im(k) ≤ 0. For a passive tissue
    # (Im(ε̂) ≤ 0) the principal square root already has Re(k) ≥ 0 and
    # Im(k) ≤ 0; the flip is only a guard. Do not flip again to restore
    # Re(k), which would undo the decaying branch.
    if k.imag > 0:
        k = -k
    return k


def _alpha_closed_form(tissue: TissueParameters, freq_hz: float) -> float:
    """α from the real-arithmetic identity, used as a cross-check."""
    omega = 2.0 * math.pi * freq_hz
    eps = complex_relative_permittivity(tissue, freq_hz)
    eps_p = eps.real
    eps_pp = -eps.imag
    if eps_p <= 0:
        # Fall back to the complex-k form for pathological ε'.
        return -wavenumber(tissue, freq_hz).imag
    tan2 = (eps_pp / eps_p) ** 2
    return omega * math.sqrt(MU_0 * EPSILON_0 * eps_p / 2.0) * math.sqrt(math.sqrt(1.0 + tan2) - 1.0)


def skin_depth(tissue: TissueParameters, freq_hz: float) -> float:
    """Field skin depth δ = 1/α, metres. Returns math.inf if α is zero."""
    alpha = -wavenumber(tissue, freq_hz).imag
    if alpha <= 0.0:
        return math.inf
    return 1.0 / alpha


@dataclass(frozen=True)
class PlaneWaveEstimates:
    freq_hz: float
    tissue_name: str
    eps_real: float
    eps_imag_neg: float  # ε'' = -Im(ε̂)
    sigma_eff: float
    skin_depth_m: float
    reflection_coeff_mag: float
    absorbed_power_density_w_m2: float
    surface_sar_estimate_w_kg: float
    sar_avg_one_skin_depth_w_kg: float
    sar_avg_0p30m_w_kg: float
    outside_fcc_tool_range: bool
    outside_pmb_model_range: bool


def _sar_depth_average(sar_surface: float, alpha: float, depth_m: float) -> float:
    """Average of SAR(0) exp(-2αz) from 0 to d."""
    if depth_m <= 0:
        raise ValueError("depth must be positive")
    two_a_d = 2.0 * alpha * depth_m
    if two_a_d == 0.0:
        return sar_surface
    if two_a_d > 700.0:
        # exp(-two_a_d) underflows; the (1-exp)/x limit is 1/x.
        return sar_surface / two_a_d
    return sar_surface * (1.0 - math.exp(-two_a_d)) / two_a_d


def plane_wave_estimates(tissue: TissueParameters, freq_hz: float,
                         s0: float = S0_W_M2) -> PlaneWaveEstimates:
    if freq_hz <= 0:
        raise ValueError("frequency must be positive")
    if s0 < 0:
        raise ValueError("incident power density must be non-negative")
    eps = complex_relative_permittivity(tissue, freq_hz)
    sigma = effective_conductivity(tissue, freq_hz)
    k = wavenumber(tissue, freq_hz)
    alpha = -k.imag
    delta = math.inf if alpha <= 0.0 else 1.0 / alpha

    # Intrinsic impedance of the tissue; branch consistent with k.
    # η = √(μ0 / (ε0 ε̂)) = μ0 ω / k   (when k ≠ 0), which keeps the branch.
    omega = 2.0 * math.pi * freq_hz
    eta = (MU_0 * omega) / k
    eta0 = _eta0()
    gamma = (eta - eta0) / (eta + eta0)
    e_i_rms = math.sqrt(s0 * eta0) if s0 > 0 else 0.0
    e_t_rms = abs(1.0 + gamma) * e_i_rms
    sar0 = (sigma * (e_t_rms ** 2) / RHO_CONVENTIONAL_KG_M3) if s0 > 0 else 0.0
    # Power transmittance for a lossless incident medium: 1 - |Γ|^2.
    absorbed = (1.0 - abs(gamma) ** 2) * s0
    sar_delta = _sar_depth_average(sar0, alpha, delta) if math.isfinite(delta) else sar0
    sar_body = _sar_depth_average(sar0, alpha, WHOLE_BODY_SLAB_M)

    return PlaneWaveEstimates(
        freq_hz=freq_hz,
        tissue_name=tissue.name,
        eps_real=eps.real,
        eps_imag_neg=-eps.imag,
        sigma_eff=sigma,
        skin_depth_m=delta,
        reflection_coeff_mag=abs(gamma),
        absorbed_power_density_w_m2=absorbed,
        surface_sar_estimate_w_kg=sar0,
        sar_avg_one_skin_depth_w_kg=sar_delta,
        sar_avg_0p30m_w_kg=sar_body,
        outside_fcc_tool_range=not (FCC_TOOL_FMIN_HZ <= freq_hz <= FCC_TOOL_FMAX_HZ),
        outside_pmb_model_range=not (PMB_MODEL_FMIN_HZ <= freq_hz <= PMB_MODEL_FMAX_HZ),
    )

