"""Build the Markdown, CSV, SVG and PNG tables next to frequency-selection.md."""

from __future__ import annotations

import csv
import math
from pathlib import Path

from .bands import PRODUCT_BANDS
from .cole_cole import TISSUES
from .constants import RHO_CONVENTIONAL_KG_M3, S0_W_M2
from .plane_wave import (
    FCC_TOOL_FMAX_HZ,
    FCC_TOOL_FMIN_HZ,
    PMB_MODEL_FMAX_HZ,
    PMB_MODEL_FMIN_HZ,
    WHOLE_BODY_SLAB_M,
    plane_wave_estimates,
    skin_depth,
)
from .plot import write_png_from_svg_raster, write_svg

# Default location specified in tools/README.md: sit next to
# causes/radio-frequency/frequency-selection.md
REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT_DIR = REPO_ROOT / "causes" / "radio-frequency"

# Log-spaced sweep used for the plot (inside the PMB model range, starting
# at the FCC tool floor so the left axis is the public-calculator window).
SWEEP_FMIN_HZ = 10e6
SWEEP_FMAX_HZ = 100e9
SWEEP_POINTS = 241  # 40 steps per decade over 6 decades

# Tissues drawn on the plot and in the compact Markdown table.
PLOT_TISSUES = ("muscle", "skin_dry", "skin_wet", "fat_not_infiltrated")


def _fmt_freq(hz: float) -> str:
    if hz >= 1e9:
        v = hz / 1e9
        return f"{v:g} GHz"
    v = hz / 1e6
    return f"{v:g} MHz"


def _fmt_len(m: float) -> str:
    if not math.isfinite(m):
        return "inf"
    if m >= 1:
        return f"{m:.3g} m"
    if m >= 1e-2:
        return f"{m*100:.3g} cm"
    if m >= 1e-3:
        return f"{m*1e3:.3g} mm"
    return f"{m*1e6:.3g} µm"


def _fmt_sci(x: float, sig: int = 3) -> str:
    if x == 0:
        return "0"
    return f"{x:.{sig}e}"


def _range_flag(est) -> str:
    if est.outside_pmb_model_range:
        return "outside PMB 10 Hz–100 GHz model range"
    if est.outside_fcc_tool_range:
        return "outside FCC calculator 10–6000 MHz window; inside PMB model range"
    return "inside FCC calculator 10–6000 MHz window"


def sweep_frequencies() -> list[float]:
    n = SWEEP_POINTS
    log0, log1 = math.log10(SWEEP_FMIN_HZ), math.log10(SWEEP_FMAX_HZ)
    return [10 ** (log0 + (log1 - log0) * i / (n - 1)) for i in range(n)]


def rows_for_bands():
    rows = []
    for band in PRODUCT_BANDS:
        for key in TISSUES:
            tissue = TISSUES[key]
            est = plane_wave_estimates(tissue, band.freq_hz)
            rows.append(
                {
                    "band_key": band.key,
                    "service": band.service,
                    "representative_frequency": _fmt_freq(band.freq_hz),
                    "frequency_hz": f"{band.freq_hz:.6e}",
                    "opened_range": band.opened_range,
                    "source_url": band.source_url,
                    "citation": band.citation,
                    "tissue": tissue.name,
                    "cancer_type": "not applicable (dosimetry estimate, not an epidemiology finding)",
                    "body_site": tissue.body_site_note,
                    "eps_real": f"{est.eps_real:.6g}",
                    "eps_imag": f"{est.eps_imag_neg:.6g}",
                    "sigma_eff_S_per_m": f"{est.sigma_eff:.6g}",
                    "skin_depth_m": f"{est.skin_depth_m:.6e}",
                    "skin_depth_display": _fmt_len(est.skin_depth_m),
                    "reflection_coeff_mag": f"{est.reflection_coeff_mag:.6g}",
                    "absorbed_power_density_W_per_m2": _fmt_sci(est.absorbed_power_density_w_m2),
                    "surface_SAR_estimate_W_per_kg": _fmt_sci(est.surface_sar_estimate_w_kg),
                    "SAR_avg_one_skin_depth_W_per_kg": _fmt_sci(est.sar_avg_one_skin_depth_w_kg),
                    "simplified_whole_body_SAR_estimate_W_per_kg": _fmt_sci(est.sar_avg_0p30m_w_kg),
                    "rho_kg_per_m3": str(int(RHO_CONVENTIONAL_KG_M3)),
                    "rho_note": "conventional 1000 kg m^{-3}; not a Gabriel 1996 measured density",
                    "S0_W_per_m2": str(S0_W_M2),
                    "whole_body_slab_m": str(WHOLE_BODY_SLAB_M),
                    "frequency_range_flag": _range_flag(est),
                    "band_note": band.note,
                }
            )
    return rows


CSV_COLUMNS = [
    "band_key",
    "service",
    "representative_frequency",
    "frequency_hz",
    "opened_range",
    "source_url",
    "citation",
    "tissue",
    "cancer_type",
    "body_site",
    "eps_real",
    "eps_imag",
    "sigma_eff_S_per_m",
    "skin_depth_m",
    "skin_depth_display",
    "reflection_coeff_mag",
    "absorbed_power_density_W_per_m2",
    "surface_SAR_estimate_W_per_kg",
    "SAR_avg_one_skin_depth_W_per_kg",
    "simplified_whole_body_SAR_estimate_W_per_kg",
    "rho_kg_per_m3",
    "rho_note",
    "S0_W_per_m2",
    "whole_body_slab_m",
    "frequency_range_flag",
    "band_note",
]


def write_csv(path: Path, rows) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _md_table(headers, data_rows) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in data_rows:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def write_markdown(path: Path, rows) -> None:
    compact_tissues = [TISSUES[k].name for k in PLOT_TISSUES]
    # One compact table per tissue for readability, plus a band list.
    parts = []
    parts.append("# Frequency-versus-absorption comparison (first-order estimate)")
    parts.append("")
    parts.append(
        "> **Not medical advice. Not a regulatory determination.** This table "
        "is a first-order plane-wave estimate for a homogeneous tissue "
        "half-space. It is not a whole-body human phantom, not a model of a "
        "phone or tower, and not a substitute for openEMS or Meep. It cannot "
        "show why a product band was chosen, and it cannot show that a "
        "frequency is “safer.” “Safer frequency” is treated here as a **claim "
        "to test** against opened sources and the model assumptions listed "
        "below, not as a result of this script."
    )
    parts.append("")
    parts.append("## Per-case rule (t1201u)")
    parts.append("")
    parts.append(
        "Cancers are not always caused by one thing, and they can be caused "
        "by different things in different areas of the body. Every cause and "
        "claimed cure in this repository is recorded by **cancer type** and "
        "**body site**. This page is a dosimetry *estimate*, not an "
        "epidemiology finding, so **cancer type** is marked not applicable. "
        "Each row is still tied to one Gabriel Table 1 **tissue / body site** "
        "(muscle, dry skin, wet skin, or fat). Results are not averaged into "
        "one “the body” number, and they are not a claim about cancer at any "
        "site."
    )
    parts.append("")
    parts.append("## What was computed")
    parts.append("")
    parts.append(
        f"- Dielectric parameters from the 4-Cole-Cole model and Table 1 of "
        f"Gabriel, Lau and Gabriel, *Phys. Med. Biol.* 41 (1996) 2271–2293, "
        f"opened as the publisher PDF "
        f"(https://iopscience.iop.org/article/10.1088/0031-9155/41/11/003/pdf, "
        f"DOI https://doi.org/10.1088/0031-9155/41/11/003). The FCC page "
        f"https://www.fcc.gov/general/body-tissue-dielectric-parameters "
        f"states that its public calculator uses the same model (AFOSR-TR-96) "
        f"and is limited to 10–6000 MHz. Frequencies outside that window are "
        f"labeled; they still use the opened PMB model, which the paper "
        f"states covers 10 Hz–100 GHz."
    )
    parts.append(
        "- Field skin depth δ = 1/α for a normally incident plane wave on a "
        "homogeneous half-space of that one tissue."
    )
    parts.append(
        f"- A **simplified whole-body SAR estimate**: the depth average of "
        f"SAR(z) = σ |E(z)|² / ρ over a {WHOLE_BODY_SLAB_M:.2f} m slab, with "
        f"incident power density S0 = {S0_W_M2:g} W m⁻² (a normalization, "
        f"not a limit) and ρ = {int(RHO_CONVENTIONAL_KG_M3)} kg m⁻³ "
        f"(a conventional water-like density; Gabriel 1996 Table 1 does not "
        f"report mass density). Surface SAR and the average over one skin "
        f"depth are listed for context. The 0.30 m length is a body-scale "
        f"illustration, not an anatomical model and not an FCC or ICNIRP "
        f"averaging mass."
    )
    parts.append(
        "- Representative frequencies are midpoints (or identified ISM "
        "centers) of bands **named in opened allocation records** (ISM, "
        "cellular, Broadband PCS, Wi-Fi / U-NII, 3.45 GHz and 3.7 GHz "
        "Service, Upper Microwave Flexible Use). Full citations are in "
        "[frequency-absorption-method.md](frequency-absorption-method.md) "
        "and in the CSV."
    )
    parts.append(
        "- IT'IS parameters are **not** used. This script is MIT-licensed "
        "and is not a medical or regulatory conclusion."
    )
    parts.append("")
    parts.append("How to regenerate (from the repository root, stdlib only):")
    parts.append("")
    parts.append("```")
    parts.append("python3 -m tools.frequency_absorption")
    parts.append("```")
    parts.append("")
    parts.append("See [frequency-absorption-method.md](frequency-absorption-method.md) for quoted formulas and source URLs.")
    parts.append("")
    parts.append("## Plot")
    parts.append("")
    parts.append(
        "![Field skin depth versus frequency for four Gabriel Table 1 tissues, "
        "with dashed vertical markers at the representative product-band "
        "frequencies](frequency-absorption.png)"
    )
    parts.append("")
    parts.append(
        "An SVG copy of the same figure is in "
        "[frequency-absorption.svg](frequency-absorption.svg). "
        "The dashed lines mark the representative product-band frequencies in "
        "the table; they are not absorption peaks."
    )
    parts.append("")
    parts.append("## Band list (opened records)")
    parts.append("")
    band_headers = ["Service", "Representative frequency", "Opened range", "Citation"]
    band_rows = []
    seen = set()
    for band in PRODUCT_BANDS:
        if band.key in seen:
            continue
        seen.add(band.key)
        band_rows.append([band.service, _fmt_freq(band.freq_hz), band.opened_range, band.citation])
    parts.append(_md_table(band_headers, band_rows))
    parts.append("")

    headers = [
        "Representative frequency",
        "Service",
        "Skin depth",
        "Surface SAR estimate (W kg⁻¹)",
        "SAR average over one skin depth (W kg⁻¹)",
        "Simplified whole-body SAR estimate, 0.30 m slab (W kg⁻¹)",
        "Absorbed power density (W m⁻²)",
        "Frequency-range flag",
    ]
    for tname in compact_tissues:
        parts.append(f"## {tname}")
        parts.append("")
        trows = [r for r in rows if r["tissue"] == tname]
        data = []
        for r in trows:
            data.append(
                [
                    r["representative_frequency"],
                    r["service"],
                    r["skin_depth_display"],
                    r["surface_SAR_estimate_W_per_kg"],
                    r["SAR_avg_one_skin_depth_W_per_kg"],
                    r["simplified_whole_body_SAR_estimate_W_per_kg"],
                    r["absorbed_power_density_W_per_m2"],
                    r["frequency_range_flag"],
                ]
            )
        parts.append(_md_table(headers, data))
        parts.append("")
        site = next(r["body_site"] for r in trows)
        parts.append(f"*Body site:* {site}")
        parts.append("")
        parts.append(
            f"Incident S0 = {S0_W_M2:g} W m⁻²; ρ = {int(RHO_CONVENTIONAL_KG_M3)} kg m⁻³ "
            f"(conventional). Estimates scale linearly with S0."
        )
        parts.append("")

    parts.append("## What this does not show")
    parts.append("")
    parts.append(
        "- It does not show that any product band was chosen because it "
        "couples more, or less, to tissue."
    )
    parts.append(
        "- It does not rank frequencies as safer or more dangerous."
    )
    parts.append(
        "- It does not replace a full-wave simulation of a person and a device, "
        "and it does not use IT'IS voxel models."
    )
    parts.append(
        "- Fat (infiltrated) is included in the CSV but omitted from the "
        "compact tables above to keep the page short; regenerate the CSV to "
        "inspect it."
    )
    parts.append("")
    parts.append(
        "Machine-readable values: [frequency-absorption.csv](frequency-absorption.csv). "
        "Method and quoted formulas: [frequency-absorption-method.md](frequency-absorption-method.md)."
    )
    parts.append("")
    path.write_text("\n".join(parts), encoding="utf-8")


def write_plots(out_dir: Path) -> None:
    freqs = sweep_frequencies()
    series = {}
    dmin, dmax = math.inf, 0.0
    for key in PLOT_TISSUES:
        tissue = TISSUES[key]
        pts = []
        for f in freqs:
            d = skin_depth(tissue, f)
            pts.append((f, d))
            if math.isfinite(d) and d > 0:
                dmin = min(dmin, d)
                dmax = max(dmax, d)
        series[tissue.name] = pts
    # Pad a little on a log axis.
    depth_min = 10 ** math.floor(math.log10(dmin) - 0.05)
    depth_max = 10 ** math.ceil(math.log10(dmax) + 0.05)
    markers = [(b.freq_hz, b.service) for b in PRODUCT_BANDS]
    title = "Field skin depth vs frequency (Gabriel 1996 4-Cole-Cole tissues)"
    subtitle = (
        "Homogeneous half-space, normally incident plane wave. "
        "Dashed lines: representative product bands from opened allocation records. "
        "Not a whole-body phantom; not a safety ranking."
    )
    write_svg(
        out_dir / "frequency-absorption.svg",
        series,
        freq_min=SWEEP_FMIN_HZ,
        freq_max=SWEEP_FMAX_HZ,
        depth_min=depth_min,
        depth_max=depth_max,
        band_markers=markers,
        title=title,
        subtitle=subtitle,
    )
    write_png_from_svg_raster(
        out_dir / "frequency-absorption.png",
        series,
        freq_min=SWEEP_FMIN_HZ,
        freq_max=SWEEP_FMAX_HZ,
        depth_min=depth_min,
        depth_max=depth_max,
        band_markers=markers,
        title=title,
        subtitle=subtitle,
    )


def generate(out_dir: Path | None = None) -> dict[str, Path]:
    out_dir = Path(out_dir) if out_dir is not None else DEFAULT_OUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = rows_for_bands()
    csv_path = out_dir / "frequency-absorption.csv"
    md_path = out_dir / "frequency-absorption.md"
    write_csv(csv_path, rows)
    write_markdown(md_path, rows)
    write_plots(out_dir)
    return {
        "csv": csv_path,
        "md": md_path,
        "svg": out_dir / "frequency-absorption.svg",
        "png": out_dir / "frequency-absorption.png",
    }
