# Tools

This folder holds two related watchlists and one in-repo comparison tool.

**Nothing here is an install plan.** Installing a third-party program, downloading a new package, or accepting a license needs a separate OK from the repository owner. See [`METHOD.md`](../METHOD.md).

## Candidate lists

- [`CANDIDATES.md`](CANDIDATES.md) — open-source cancer research software found in the country surveys (tumor-growth simulators, drug-screening and docking tools, genomics pipelines, and similar). Candidates only.
- [`../causes/radio-frequency/TOOLS.md`](../causes/radio-frequency/TOOLS.md) — open-source programs and published tissue-parameter sources that could test claims in the radio-frequency frequency-selection work (FDTD solvers, dielectric datasets, and related calculators). Candidates only.

## In-repo tool: frequency-versus-absorption comparison

**Status:** Implemented in `frequency_absorption/` (this pull request). It is not merged to `main` until the repository owner approves.

**Module:** `tools/frequency_absorption` (run `python3 -m tools.frequency_absorption` from the repository root; Python 3.10 or later, stdlib only).

**Purpose:** compare, band by band, a transparent first-order estimate of how strongly RF energy couples into tissue, so claims that some product bands were chosen over “safer” frequencies can be tested against published tissue parameters. “Safer frequency” is treated as a **claim to test**, not as a result of the script. The script:

1. Uses only the opened 4-Cole-Cole formulas and Table 1 parameters from Gabriel, Lau and Gabriel, *Phys. Med. Biol.* 41 (1996) 2271–2293 (publisher PDF and DOI quoted in the method note). The FCC page https://www.fcc.gov/general/body-tissue-dielectric-parameters is cited for the same model lineage (AFOSR-TR-96) and for the public calculator’s 10–6000 MHz window. **IT’IS parameters are not bundled** (download terms were not confirmed).
2. Computes **skin depth** as a function of frequency from those parameters, with the formula and the source of each constant quoted in the code comments and in [`../causes/radio-frequency/frequency-absorption-method.md`](../causes/radio-frequency/frequency-absorption-method.md).
3. Computes a **simplified whole-body SAR estimate** per representative product band named in opened allocation records (ISM, cellular, Broadband PCS, Wi-Fi / U-NII, 3.45 GHz and 3.7 GHz Service, and Upper Microwave Flexible Use / 5G), clearly labeled as a plane-wave half-space estimate, not a full-wave simulation of a person or a device. Each row is tied to one Gabriel tissue / body site (repository rule t1201u).
4. Writes a table and a plot next to [`../causes/radio-frequency/frequency-selection.md`](../causes/radio-frequency/frequency-selection.md): [`../causes/radio-frequency/frequency-absorption.md`](../causes/radio-frequency/frequency-absorption.md), [`.csv`](../causes/radio-frequency/frequency-absorption.csv), [`.png`](../causes/radio-frequency/frequency-absorption.png), and [`.svg`](../causes/radio-frequency/frequency-absorption.svg).

This script is **not** a substitute for an approved openEMS, Meep, or gprMax run, and it cannot by itself prove why a band was chosen. It is **not** a medical or regulatory conclusion.

**License:** MIT, to match this repository.

**Review and publish rules:** any code for this tool must go through the full review set used on this account’s software projects — Claude, the controller, CodeRabbit, gitleaks, and trufflehog — **before it is pushed**. It lands on a branch as a pull request. The pull request needs the repository owner’s approval. Public GitHub publication follows that merge, not a direct push to `main`.

**Still not in this code PR:** installing third-party FDTD solvers on a new machine as part of the repository, bundling IT’IS or other datasets whose terms have not been quoted, or presenting model output as a medical or regulatory conclusion.
