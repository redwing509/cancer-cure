# Claim template

Copy this file to `claims/<slug>.md` for each claim. Follow [`METHOD.md`](../METHOD.md). This is not medical advice; see the [README disclaimer](../README.md).

```md
# Claim: <short title>

**Status:** outline / evidence draft / citation-checked

## The claim

> (quote the claimant’s wording once a source is opened; otherwise describe the claim as a question to be checked and mark unsourced wording)

## Who makes it

- Name, group, clinic, or paper, as the opened source states
- Link or DOI

## Evidence for

Quoted, linked findings that appear to support the claim. Use the country entry fields where a clinical or laboratory study is involved (population, measured result quoted, evidence level, source opened as).

## Evidence against

Quoted, linked findings that contradict, fail to replicate, or limit the claim, including harms, withdrawals, and retractions. If none were found after a search, write `NOT FOUND` and what was searched. Do not omit this section.

## Evidence level

One value from the project scale, based on the highest design actually opened, not the level the claimant implies.

## Simulation plan

- Question a model could test (for example a tumor-growth or pharmacokinetic question that would support or weaken part of the claim)
- Candidate open-source model (name, official URL, license), preferably one already listed in `tools/CANDIDATES.md`
- What result would count as support, and what would count as a failed test
- **Installs and runs need a separate OK from the repository owner.** This section is a plan, not a result.
- If no suitable model is known: `NOT FOUND` and what was searched

## Sources opened

Pass 1 list: URL or DOI, title, one quote, and `full text` / `abstract only` / `not opened`.
```
