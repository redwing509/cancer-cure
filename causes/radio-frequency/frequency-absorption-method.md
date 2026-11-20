# Method note: frequency-versus-absorption script

**Not medical advice. Not a regulatory determination.** This note quotes the
formulas and source URLs used by `tools/frequency_absorption`. The script
does not invent tissue parameters, band edges, or physical constants. It
does not bundle IT'IS data. It cannot show why a product band was chosen,
and it cannot show that a frequency is “safer.” “Safer frequency” remains
a **claim to test** against opened sources and the assumptions below.

Cancers are not always caused by one thing, and they can be caused by
different things in different areas of the body (repository rule t1201u).
This comparison is organized by Gabriel Table 1 **tissue / body site**. It
is a dosimetry estimate, not an epidemiology finding, so cancer type is
not applicable. Results are never collapsed into one cause or one
whole-body “the cancer” number.

## 1. Tissue dielectric model

Opened source (19 Nov 2026, Pacific Time): S Gabriel, R W Lau and C Gabriel,
“The dielectric properties of biological tissues: III. Parametric models
for the dielectric spectrum of tissues,” *Phys. Med. Biol.* 41 (1996)
2271–2293.

- Publisher PDF: https://iopscience.iop.org/article/10.1088/0031-9155/41/11/003/pdf
- DOI: https://doi.org/10.1088/0031-9155/41/11/003

Equation (4), as stated in the opened paper (the typographic “1ε” of the
PDF is Δε):

> the spectrum of a tissue may therefore be more appropriately described
> in terms of multiple Cole-Cole dispersion
>
> ε̂(ω) = ε∞ + Σ<sub>n</sub> Δε<sub>n</sub> / [1 + (jωτ<sub>n</sub>)<sup>(1−α<sub>n</sub>)</sup>] + σ<sub>i</sub> / (jωε<sub>0</sub>)
>
> which, with a choice of parameters appropriate to each tissue, can be
> used to predict the dielectric behaviour over the desired frequency
> range.

The opened paper states that the spectrum was modelled “from 10 Hz to
100 GHz” and that “In practice, the model can be used at all frequencies
in the specified range.” It also notes that the fit “represents a good
fit to the data rather then a unique solution based on a mathematical
argument.”

Parameter rows actually used (`muscle`, `Skin (dry)`, `Skin (wet)`,
`Fat (not infiltrated)`, `Fat (infiltrated)`) are copied from **Table 1**
of that paper into `tools/frequency_absorption/cole_cole.py`. Time
constants use the Table 1 units: τ<sub>1</sub> in ps, τ<sub>2</sub> in ns,
τ<sub>3</sub> in μs, τ<sub>4</sub> in ms. The table column σ is the ionic
conductivity σ<sub>i</sub> of equation (4), in S m<sup>−1</sup>. Dry skin
has Δε<sub>3</sub> = Δε<sub>4</sub> = 0 in the table, so those terms are
omitted.

The FCC Body Tissue Dielectric Parameters page, opened the same day at
https://www.fcc.gov/general/body-tissue-dielectric-parameters, states
that its public calculator uses the 4-Cole-Cole model “as described in
‘Compilation of the Dielectric Properties of Body Tissues at RF and
Microwave Frequencies’ by Camelia Gabriel in U.S. Air Force Report
AFOSR-TR-96,” and that “The tool calculates parameters for frequencies
between 10-6,000 MHz.” The AFOSR-TR-96 PDF could not be opened from DTIC
in this pass. Frequencies outside 10–6000 MHz are labeled in the output
and still use the opened PMB 1996 model, not an extrapolation invented
here.

IT'IS tissue databases are **not** used. Their download terms were not
confirmed (see [TOOLS.md](TOOLS.md)).

Effective conductivity used in the absorption estimate includes dielectric
loss as well as σ<sub>i</sub>:

> σ<sub>eff</sub> = ω ε<sub>0</sub> ε'' , ε'' = −Im(ε̂)

## 2. Physical constants

- Vacuum electric permittivity ε<sub>0</sub> = 8.8541878188 × 10<sup>−12</sup> F m<sup>−1</sup>,
  NIST 2022 CODATA recommended value, opened 19 Nov 2026 at
  https://physics.nist.gov/cgi-bin/cuu/Value?ep0
  (quote: “Numerical value  8.854 187 8188 x 10-12 F m-1”).
- Speed of light in vacuum c = 299792458 m s<sup>−1</sup> (exact SI).
- Magnetic constant μ<sub>0</sub> = 1/(ε<sub>0</sub> c<sup>2</sup>), so the
  impedance of free space is consistent with the opened ε<sub>0</sub>.

Mass density ρ is **not** taken from Gabriel 1996 (Table 1 does not report
it). The script uses a conventional 1000 kg m<sup>−3</sup> only to express
a SAR *estimate* in W kg<sup>−1</sup>, and every output column says so.

## 3. Skin depth and plane-wave estimates

For a time-harmonic field ~ exp(jωt) traveling in +z as exp(−j k z),

> k = ω √(μ<sub>0</sub> ε<sub>0</sub> ε̂(ω))

with the square-root branch chosen so that Re(k) ≥ 0 and Im(k) ≤ 0. The
field skin depth is δ = 1/α with α = −Im(k). Equivalently, writing
ε̂ = ε' − jε'' with ε' > 0 and ε'' ≥ 0,

> α = ω √(μ<sub>0</sub> ε<sub>0</sub> ε'/2) √( √(1+(ε''/ε')²) − 1 )

The unit tests check that the two forms agree. This is the standard
homogeneous-medium result, not a new tissue formula.

A normally incident plane wave in air, with incident power density
S<sub>0</sub> = 1 W m<sup>−2</sup> (a **normalization, not a limit**), has
rms field E<sub>i,rms</sub> = √(S<sub>0</sub> η<sub>0</sub>),
η<sub>0</sub> = √(μ<sub>0</sub>/ε<sub>0</sub>). At the air–tissue interface,

> Γ = (η − η<sub>0</sub>) / (η + η<sub>0</sub>), η = μ<sub>0</sub> ω / k

> E<sub>t,rms</sub> = |1+Γ| E<sub>i,rms</sub>

Inside the half-space, |E(z)| = |E<sub>t</sub>| exp(−α z). The specific
absorption rate *estimate* at a point is the standard definition

> SAR = σ<sub>eff</sub> |E<sub>rms</sub>|² / ρ

47 CFR § 2.1093, opened via LII at
https://www.law.cornell.edu/cfr/text/47/2.1093 on 19 Nov 2026, refers
portable-device evaluations to the “SAR limits specified in § 1.1310” for
100 kHz to 6 GHz, but the opened excerpt does not reprint this algebra.
The script therefore uses the standard definition above and labels every
SAR column as an estimate.

The **simplified whole-body SAR estimate** in the table is only the depth
average of that half-space SAR over a 0.30 m slab:

> SAR<sub>avg</sub>(d) = SAR(0) (1 − exp(−2αd)) / (2αd), d = 0.30 m

This 0.30 m length is a body-scale illustration chosen for this script,
**not** a formula copied from an opened ICNIRP or FCC whole-body standard,
**not** an anatomical phantom, and **not** an official averaging mass. A
homogeneous half-space has no body size or orientation, so this estimate
**cannot represent whole-body resonance** (the 30–300 MHz lead in
[frequency-selection.md](frequency-selection.md)) and must not be read as
a ranking of “safer” frequencies.

The table also reports surface SAR, the average over one field skin depth,
and the absorbed power density (1 − |Γ|²) S<sub>0</sub>, which does not
depend on ρ. Results scale linearly with S<sub>0</sub>.

This is not a substitute for openEMS or Meep, which remain the tools for
device-and-body geometry (see [TOOLS.md](TOOLS.md)).

## 4. Product bands

Representative frequencies are ISM centers from the opened § 18.301 table,
or arithmetic midpoints of a single opened interval. They are not claimed
to be the only channel in the service. Official pages opened on 19 Nov 2026
(Pacific Time):

| Service | Record | URL opened |
| --- | --- | --- |
| ISM | 47 CFR § 18.301 | https://www.ecfr.gov/current/title-47/chapter-I/subchapter-A/part-18/subpart-C/section-18.301 |
| Cellular | 47 CFR § 22.905 | https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-22/subpart-H/section-22.905 |
| Broadband PCS | 47 CFR § 24.229 | https://www.law.cornell.edu/cfr/text/47/24.229 (LII copy of the e-CFR; direct eCFR was CAPTCHA-blocked later the same day) |
| Wi-Fi / Part 15 | 47 CFR § 15.247 | https://www.law.cornell.edu/cfr/text/47/15.247 (LII) |
| U-NII / Wi-Fi | 47 CFR § 15.407 | https://www.law.cornell.edu/cfr/text/47/15.407 (LII) |
| 3.45 GHz and 3.7 GHz Service | 47 CFR § 27.5 | https://www.law.cornell.edu/cfr/text/47/27.5 (LII) |
| Upper Microwave Flexible Use (5G) | 47 CFR § 30.4 | https://www.law.cornell.edu/cfr/text/47/30.4 (LII) |

ISM centers used: 13.56, 27.12, 40.68, 915, 5800 MHz; 24.125 and 61.25 GHz.
The same § 18.301 table lists 122.50 GHz and 245.00 GHz, which exceed the
100 GHz PMB model range and are omitted. 13.56 MHz is inside the FCC
calculator window (10–6000 MHz). Frequencies above 6000 MHz are labeled
as outside that window and still inside the PMB model range. The opened
paper describes the 4-Cole-Cole fit as a good fit rather than a unique
solution; millimetre-wave rows (24–61 GHz) apply that same opened model
and should not be read as new measurements.

## 5. How to run

From the repository root, Python 3.10 or later, stdlib only (no
third-party package is required):

```
python3 -m unittest discover -s tools/frequency_absorption/tests -t .
python3 -m tools.frequency_absorption
```

Outputs (also committed so the figures can be read without running the
script):

- [frequency-absorption.md](frequency-absorption.md)
- [frequency-absorption.csv](frequency-absorption.csv)
- [frequency-absorption.png](frequency-absorption.png)
- [frequency-absorption.svg](frequency-absorption.svg)

License: MIT, same as the repository.
