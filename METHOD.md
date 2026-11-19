# Method

This file is the working method for every country note in `countries/`, for tool candidates in `tools/`, and for investigations under `investigations/`. The [disclaimer in the README](README.md) applies to every page: this is not medical advice, and no entry is a cure unless a cited study shows one.

## Evidence scale

Each study is given **one** evidence level, taken from the design described in the opened source, not from how impressive the result sounds. If the paper’s design is unclear, say so and use the lower of the plausible levels.

| Level | What it means | Typical source |
|---|---|---|
| **In vitro** | Cells, organoids, or other systems outside a living animal or human | Laboratory paper |
| **Animal** | Living non-human animals | Preclinical in vivo study |
| **Case report** | One patient or a very small uncontrolled series described as cases | Case report or case series |
| **Observational** | Cohort, case-control, or similar non-randomized clinical observation | Observational clinical study |
| **Early trial** | First-in-human, Phase I, Phase II, single-arm, or other early interventional trial | Registered or published early trial |
| **RCT** | Randomized controlled trial in humans | Phase III or other randomized trial |
| **Systematic review** | Systematic review or meta-analysis of primary studies | Cochrane or other systematic review |

Use the **highest design the opened source actually is**, not the highest design it cites. A systematic review is labeled systematic review; the individual trials it includes, if entered separately, keep their own levels. Animal work inside a paper that also has a clinical arm should be split or clearly labeled so a cell or mouse result is not presented as a human result.

## What an entry must contain

Every study entry uses the fields in [`countries/ENTRY_TEMPLATE.md`](countries/ENTRY_TEMPLATE.md):

1. **Compound or therapy** — the name as given in the source, plus a short English gloss if the original name is in another language
2. **Country** — the country this note is about; label international collaborations
3. **Study type** — the design in the authors’ terms, plus the evidence level
4. **Population** — who or what was studied (cell line, animal model, patient group, sample size), copied from the source
5. **Measured result (quoted)** — the outcome **exactly as quoted** from the opened source, with quotation marks
6. **Link or DOI** — a URL and/or DOI that a reader can open without using a piracy site
7. **Evidence level** — one value from the scale above
8. **Negative / null results** — what did not work, was not significant, was harmful, or was retracted; write `not reported in the opened source` if the source is silent, never invent a positive spin

## Citation honesty

These rules are the same ones used on the other research projects in this account (James, 15 Nov 2026, t1084u). They apply to country notes, tool candidates, and investigations.

1. **Quote plus locator.** Every factual claim includes a direct quote of the supporting sentence and that source’s URL or DOI. Drop any claim that lacks both.
2. **`NOT FOUND`, never a guess.** When a search finds nothing, write `NOT FOUND` and say what was searched. Never fill gaps from memory.
3. **Copy, don’t recall.** Do not write numbers, institution names, author names, dates, or product, formula, or trial names unless they are copied from a source opened for that check.
4. **Two passes on a fresh search.** Pass 1 is only a **SOURCES OPENED** list (URL or DOI, title, one quote, and `full text` / `abstract only` / `not opened`). Pass 2 writes findings only from that list.
5. **Say how the source was opened.** Never describe, quote, or give numbers from content that was not opened. If only the abstract was opened, quote the abstract and mark the rest unseen.
6. **Paywalls.** Look for a legitimate alternate copy (author preprint, thesis, university repository, conference slides, or a later open paper that quotes the numbers). Do **not** use Sci-Hub, Library Genesis, or similar sites. If only a paywalled record exists, cite the bibliographic data, label it `not opened` or `abstract only`, and mark unseen numbers as “paywalled; no legitimate open copy found”.
7. **No raw paywalled PDFs** in this public repository. The public notes are summaries, short quotes, numbers, and links only.

## Country notes

- One country per file, under `countries/`, named `NN-<slug>.md` (for example `01-china.md`).
- Search in that country’s native or main research language. Write the note in English. Keep original titles, with an English translation in parentheses.
- Include work led in that country, or carried out there. If a local author is only a co-author on work done elsewhere, say so. Label foreign partnerships.
- After a draft is written, a checker who is not the draft author verifies each citation against an opened page before the note is proposed for merge.
- Country notes arrive on a branch as a pull request. Merges to `main` need the repository owner’s approval.

Each country note has three parts:

1. **Therapies and compounds** — natural and traditional therapies studied against cancer, using the entry template and evidence scale.
2. **Programs and organizations studying cancer causes** — named groups, institutes, or formal programs, with a link and a short sourced note on what they study (causes, not only treatments). Official pages and published descriptions only.
3. **Open-source software we could run** — tumor-growth simulators, drug-screening and docking tools, genomics pipelines, and similar tools from that country’s groups or used in that country’s literature. For each tool record name, developer, what it does, license, official download or repository URL, and the citation where it appears. Verifiable links only; no invented tools. If none are found, write `NOT FOUND` and what was searched.

Verified tools are also appended, de-duplicated, to [`tools/CANDIDATES.md`](tools/CANDIDATES.md). That list is **candidates only**. Installing any tool still needs a separate OK from the repository owner. A row in the list is not permission to install, download a new package, or accept a license.

## What “cure” means here

Do not call a compound or therapy a cure in our own voice. If a cited study uses the word “cure,” “complete remission,” “disease-free,” or similar, quote that wording, name the population, and keep the evidence level in view. Long-term remission in a defined disease is not automatically a general cancer cure.

## Investigations

Some questions cut across countries and need a dedicated file under `investigations/`. They use the same citation-honesty rules and the same evidence scale. The write-up gathers published evidence on **both sides** of the claim, quotes measured results only, and does not announce a conclusion before the sources have been opened and checked.

The first investigation is [`investigations/cancer-fungus-hypothesis.md`](investigations/cancer-fungus-hypothesis.md): whether cancer is a fungus, including claims about sodium bicarbonate treatment. The outline and method are in that file now. The full, citation-checked evidence review will come in a later pull request. Evidence decides.
