"""4-Cole-Cole tissue dielectric model.

The model and the parameter rows below are copied from an opened copy of:

    S Gabriel, R W Lau and C Gabriel, "The dielectric properties of biological
    tissues: III. Parametric models for the dielectric spectrum of tissues,"
    Phys. Med. Biol. 41 (1996) 2271-2293.
    DOI: https://doi.org/10.1088/0031-9155/41/11/003
    Opened as publisher PDF from
    https://iopscience.iop.org/article/10.1088/0031-9155/41/11/003/pdf
    on 19 Nov 2026, Pacific Time.

The FCC Body Tissue Dielectric Parameters page states that its public
calculator uses the same 4-Cole-Cole model "as described in 'Compilation of
the Dielectric Properties of Body Tissues at RF and Microwave Frequencies'
by Camelia Gabriel in U.S. Air Force Report AFOSR-TR-96," and that "The tool
calculates parameters for frequencies between 10-6,000 MHz."
    https://www.fcc.gov/general/body-tissue-dielectric-parameters
    Opened 19 Nov 2026, Pacific Time.

The AFOSR-TR-96 PDF could not be opened from DTIC in this pass (HTTP 403 /
maintenance). Parameter values in this file are therefore taken from the
opened 1996 *Physics in Medicine & Biology* paper (same authors and model),
not from memory and not from IT'IS.

Equation (4) of the opened paper (quoted, with the typographic '1ε' of the
PDF equal to Δε):

    "the spectrum of a tissue may therefore be more appropriately described
    in terms of multiple Cole-Cole dispersion

        ε̂(ω) = ε∞ + Σ_n  Δε_n / [1 + (jωτ_n)^(1-α_n)]  +  σ_i / (jωε_0)

    which, with a choice of parameters appropriate to each tissue, can be
    used to predict the dielectric behaviour over the desired frequency
    range."

The paper states that the spectrum was modelled "from 10 Hz to 100 GHz" and
that "In practice, the model can be used at all frequencies in the specified
range." It also notes the fit "represents a good fit to the data rather then
a unique solution based on a mathematical argument" (typo "then" in the
source).

Table 1 heading: "Parameters of equation (4) used to predict the dielectric
properties of tissues in figures 1(a)-(q)." Only the rows actually used by
this tool are stored below, copied from that table. σ in the table is the
ionic conductivity σ_i of equation (4), in S m^{-1} as used throughout the
paper (see also Table 2, which labels σ as S m^{-1}).

IT'IS tissue parameters are intentionally not bundled: download terms were
not confirmed (see causes/radio-frequency/TOOLS.md).
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .constants import EPSILON_0


# Time-constant units in Table 1: τ1 in ps, τ2 in ns, τ3 in μs, τ4 in ms.
_PS = 1e-12
_NS = 1e-9
_US = 1e-6
_MS = 1e-3


@dataclass(frozen=True)
class TissueParameters:
    """One row of Gabriel et al. (1996) Table 1, plus a body-site label."""

    name: str
    body_site_note: str
    eps_inf: float
    delta_eps: tuple[float, float, float, float]
    tau_s: tuple[float, float, float, float]
    alpha: tuple[float, float, float, float]
    sigma_ionic: float  # S m^{-1}


# Rows copied from Table 1 of Gabriel, Lau and Gabriel, Phys. Med. Biol. 41
# (1996) 2271-2293, opened publisher PDF on 19 Nov 2026. Missing τ and α
# entries in the dry-skin row are stored as 0 because Δε3 and Δε4 are 0.0
# in the table (those Cole-Cole terms are identically zero).
TISSUES: dict[str, TissueParameters] = {
    "muscle": TissueParameters(
        name="Muscle",
        body_site_note=(
            "Table 1 row 'Muscle'. A homogeneous-muscle half-space is a "
            "common first-order proxy, not a model of a particular organ."
        ),
        eps_inf=4.0,
        delta_eps=(50.0, 7000.0, 1.2e6, 2.5e7),
        tau_s=(7.23 * _PS, 353.68 * _NS, 318.31 * _US, 2.274 * _MS),
        alpha=(0.10, 0.10, 0.10, 0.00),
        sigma_ionic=0.2000,
    ),
    "skin_dry": TissueParameters(
        name="Skin (dry)",
        body_site_note="Table 1 row 'Skin (dry)'. Superficial tissue; not whole-body.",
        eps_inf=4.0,
        delta_eps=(32.0, 1100.0, 0.0, 0.0),
        tau_s=(7.23 * _PS, 32.48 * _NS, 0.0, 0.0),
        alpha=(0.00, 0.20, 0.0, 0.0),
        sigma_ionic=0.0002,
    ),
    "skin_wet": TissueParameters(
        name="Skin (wet)",
        body_site_note="Table 1 row 'Skin (wet)'. Superficial tissue; not whole-body.",
        eps_inf=4.0,
        delta_eps=(39.0, 280.0, 3.0e4, 3.0e4),
        tau_s=(7.96 * _PS, 79.58 * _NS, 1.59 * _US, 1.592 * _MS),
        alpha=(0.10, 0.00, 0.16, 0.20),
        sigma_ionic=0.0004,
    ),
    "fat_not_infiltrated": TissueParameters(
        name="Fat (not infiltrated)",
        body_site_note=(
            "Table 1 row 'Fat (not infiltrated)'. Adipose tissue; not a "
            "whole-body average."
        ),
        eps_inf=2.5,
        delta_eps=(3.0, 15.0, 3.3e4, 1.0e7),
        tau_s=(7.96 * _PS, 15.92 * _NS, 159.15 * _US, 7.958 * _MS),
        alpha=(0.20, 0.10, 0.05, 0.01),
        sigma_ionic=0.0100,
    ),
    "fat_infiltrated": TissueParameters(
        name="Fat (infiltrated)",
        body_site_note="Table 1 row 'Fat (infiltrated)'. Adipose tissue; not whole-body.",
        eps_inf=2.5,
        delta_eps=(9.0, 35.0, 3.3e4, 1.0e7),
        tau_s=(7.96 * _PS, 15.92 * _NS, 159.15 * _US, 15.915 * _MS),
        alpha=(0.20, 0.10, 0.05, 0.01),
        sigma_ionic=0.0350,
    ),
}


def complex_relative_permittivity(tissue: TissueParameters, freq_hz: float) -> complex:
    """Return ε̂(ω) from equation (4) of the opened Gabriel et al. (1996) paper."""
    if freq_hz <= 0:
        raise ValueError("frequency must be positive")
    omega = 2.0 * math.pi * freq_hz
    j = 1j
    eps = complex(tissue.eps_inf, 0.0)
    for de, tau, alpha in zip(tissue.delta_eps, tissue.tau_s, tissue.alpha, strict=True):
        if de == 0.0:
            continue
        eps += de / (1.0 + (j * omega * tau) ** (1.0 - alpha))
    eps += tissue.sigma_ionic / (j * omega * EPSILON_0)
    return eps


def effective_conductivity(tissue: TissueParameters, freq_hz: float) -> float:
    """Total effective conductivity σ_eff = ω ε0 ε'' , with ε'' = -Im(ε̂).

    This includes both the ionic term σ_i and the dielectric-loss part of
    the Cole-Cole dispersions. Units: S m^{-1}.
    """
    omega = 2.0 * math.pi * freq_hz
    eps = complex_relative_permittivity(tissue, freq_hz)
    return omega * EPSILON_0 * (-eps.imag)
