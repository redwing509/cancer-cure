# Cancer Cure — an evidence-graded research collection

> **This is not medical advice, and it is not a list of cures.**
> Nothing in this repository diagnoses, treats, or replaces care from a qualified oncologist.
> No entry is a “cure” unless a cited study itself reports a cure, and even then the quote, the population, and the evidence level are shown so readers can judge the claim.
> **Do not start, stop, or replace cancer treatment on the basis of these notes.** Talk with your oncologist before changing any treatment, including herbs, supplements, or traditional therapies, which can interact with chemotherapy, radiotherapy, surgery, and immunotherapy, and can cause harm.

This project collects **published research from around the world** on natural and traditional compounds and therapies that have been **studied against cancer**. The aim is an honest, source-linked record: what was tested, in whom or in what model, what the paper actually reported (including negative and null results), and how strong the study design was.

It also records, country by country, **research programs and organizations that study cancer causes**, and **open-source software we could run** (tumor-growth simulators, drug-screening and docking tools, genomics pipelines, and similar). Those tools are candidates only. Installing any of them needs a separate OK from the repository owner.

A dedicated investigation tests the claim that **cancer is a fungus**, including the baking-soda treatment associated with Tullio Simoncini. Separate tracks collect **other seemingly credible cure claims** and research on **what causes cancer**, including why reported incidence changed over the last century, and a dedicated radio-frequency (RF) electromagnetic-field branch. Those questions are open until the cited evidence is in. Evidence decides; this project does not start from a preferred answer.

Traditional use is not the same thing as clinical evidence. A laboratory result is not a human result. A small early trial is not a large randomized trial. A rise in crude case counts is not, by itself, a rise in age-specific risk. This repository is built to keep those distinctions visible.

## Start here

- [`METHOD.md`](METHOD.md) — how entries are written, the evidence scale, the citation rules, and how programs, tools, claims, and causes are recorded
- [`countries/ENTRY_TEMPLATE.md`](countries/ENTRY_TEMPLATE.md) — the fields every study entry must fill
- [`countries/`](countries/) — one file per country, added through pull requests after a citation check
- [`claims/INDEX.md`](claims/INDEX.md) — seemingly credible cure claims, one file per claim, with evidence for and against and a simulation plan
- [`causes/`](causes/) — research on cancer causes, including [`causes/incidence-trends.md`](causes/incidence-trends.md) and candidate-cause files
- [`causes/radio-frequency/`](causes/radio-frequency/) — radio-frequency electromagnetic fields as their own branch, led by [`causes/radio-frequency/frequency-selection.md`](causes/radio-frequency/frequency-selection.md) (why product bands sit where they do)
- [`tools/CANDIDATES.md`](tools/CANDIDATES.md) — open-source research software found in the surveys (candidates only; installs need a separate OK)
- [`investigations/cancer-fungus-hypothesis.md`](investigations/cancer-fungus-hypothesis.md) — outline and method for testing the “cancer is a fungus” claim (full evidence review is a later pull request)
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to suggest a correction or a new source

## What belongs here

In scope: peer-reviewed papers, registered trials, systematic reviews, and official reports about plants, minerals, formulas, diets, and other traditional or naturally derived therapies studied for cancer prevention, treatment, symptom control, or quality of life. Isolated compounds that come from a traditional practice (for example a well-studied plant alkaloid or mineral) are in scope when the source is cited.

Also in scope:

- In each country note and in `tools/CANDIDATES.md`: research programs and organizations that study **cancer causes**, and open-source tools we could later run ourselves, each with a link, a license, and a short note on what it does.
- In `claims/`: seemingly credible cure claims, with quoted evidence for and against, an evidence level, and a simulation plan that names an open-source model only as a candidate (installs need a separate OK).
- In `causes/`: sourced research on causes, an incidence-trends note that **adjusts for age, life expectancy, and diagnosis rates**, and one file per candidate cause. Radio-frequency exposure has its own folder.

Out of scope for the public notes: copyrighted PDFs, paywalled full text, material from Sci-Hub, Library Genesis, or similar sites, unpublished anecdotes presented as fact, and any instruction to self-treat.

## Honesty rules in brief

- Every factual claim needs a direct quote plus a URL or DOI, taken from a source that was opened (full text or abstract). If that cannot be done, the claim is dropped or marked `NOT FOUND`.
- Numbers, author names, institution names, dates, and product or formula names are copied from an opened source, not recalled from memory.
- Negative, null, harmful, and retracted findings are recorded, not omitted.
- Research is searched in the country’s native or main research language. Notes are written in English; original titles are kept.
- On contested claims, including whether cancer is a fungus, whether a named therapy is a cure, and whether radio-frequency fields cause cancer, both supporting and opposing published evidence are collected. The write-up does not pre-judge the result.
- Historical incidence must be discussed with age-standardized rates and with changes in life expectancy and diagnosis, not crude counts alone.

## License

The software and repository tooling, if any, are under the MIT License — see [`LICENSE`](LICENSE).

Original research summaries and documentation in this repository are also licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Short quotations from papers remain the copyright of their authors and publishers.

## Improvements welcome

Open an issue or a pull request from a fork. Every change is reviewed before it is merged. See [CONTRIBUTING.md](CONTRIBUTING.md).
