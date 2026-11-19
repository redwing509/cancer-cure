# Tools

This folder holds two related watchlists, and the plan for one in-repo tool.

**Nothing here is an install plan.** Installing a third-party program, downloading a new package, or accepting a license needs a separate OK from the repository owner. See [`METHOD.md`](../METHOD.md).

## Candidate lists

- [`CANDIDATES.md`](CANDIDATES.md) — open-source cancer research software found in the country surveys (tumor-growth simulators, drug-screening and docking tools, genomics pipelines, and similar). Candidates only.
- [`../causes/radio-frequency/TOOLS.md`](../causes/radio-frequency/TOOLS.md) — open-source programs and published tissue-parameter sources that could test claims in the radio-frequency frequency-selection work (FDTD solvers, dielectric datasets, and related calculators). Candidates only.

## Planned in-repo tool: frequency-versus-absorption comparison

**Status:** Plan only. No source code is in the repository yet.

**Proposed name:** a frequency-versus-absorption comparison script (final module name to be chosen in the code pull request).

**Purpose:** compare, band by band, a transparent first-order estimate of how strongly RF energy couples into tissue, so claims that some product bands were chosen over “safer” frequencies can be tested against published tissue parameters. The script would:

1. Take published tissue dielectric parameters (for example the FCC Gabriel 4-Cole-Cole calculator at https://www.fcc.gov/general/body-tissue-dielectric-parameters, and the IT’IS database only if its download terms, once opened, allow that use).
2. Compute **skin depth** as a function of frequency from those parameters, with the formula and the source of each constant quoted in the code comments and in a short method note.
3. Compute a **whole-body SAR estimate** per representative product band (for example ISM, cellular, PCS, Wi-Fi, and 5G bands named in opened allocation records), clearly labeled as an estimate from a published simplification, not a full-wave simulation of a person or a device.
4. Write a table and a plot that sit next to [`../causes/radio-frequency/frequency-selection.md`](../causes/radio-frequency/frequency-selection.md), so absorption-versus-frequency can be compared with the historical and regulatory record.

This script is **not** a substitute for an approved openEMS, Meep, or gprMax run, and it cannot by itself prove why a band was chosen.

**License:** MIT, to match this repository, if and when the code is added.

**Review and publish rules:** any code for this tool must go through the full review set used on this account’s software projects — Claude, the controller, CodeRabbit, gitleaks, and trufflehog — **before it is pushed**. It lands on a branch as a pull request. The pull request needs the repository owner’s approval. Public GitHub publication follows that merge, not a direct push to `main`.

**Not in the first code PR (when one is later opened):** installing third-party FDTD solvers, bundling IT’IS or other datasets whose terms have not been quoted, or presenting model output as a medical or regulatory conclusion.
