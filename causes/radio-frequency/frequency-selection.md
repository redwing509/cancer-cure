# Frequency selection: why these bands?

**Status:** Outline and method only. This is the **lead question** of the radio-frequency branch. The citation-checked evidence review is not in this file yet and will arrive in a later pull request.

**This is not medical advice.** Read the [disclaimer in the README](../../README.md).

## Question

Why did companies and regulators put widely used products — including microwave ovens, Wi-Fi, cellular, PCS, and later 5G systems — at or near frequencies that are sometimes said to **affect the human body most**? Was that overlap deliberate, incidental, or overstated?

This file has no preferred answer. The question is to be tested against **primary sources**. Do not start from the conclusion that product bands were chosen because they couple most strongly to the body. Engineering reasons, historical spectrum allocations, cost, and any **documented** industry influence are all in scope. Evidence of influence is to be reported **exactly as documented** — a filing or a committee seat is not, by itself, proof that a band was chosen to maximize biological effect. If the opened sources do not support a claimed motive, write `NOT FOUND` or quote the limitation.

The related cancer-causation review stays in [`README.md`](README.md) in this folder. Keep “which frequencies were chosen, and why” distinct from “do those exposures cause cancer.” If this file or the later evidence PR discusses a cancer endpoint, follow the per-case rule in [`METHOD.md`](../../METHOD.md) and organize that discussion by cancer type and body site; do not treat RF exposure as one universal cause of cancer.

## Starting leads to open and check

The frequencies, years, and committee names below are a **search list**, not findings. Do not copy limit values, auction prices, absorption-peak frequencies, or membership lists from memory. Quote primary pages. If a source cannot be opened legitimately, write `NOT FOUND` or “paywalled; no legitimate open copy found.”

### 1. Whole-body resonance and SAR peaks

Open ICNIRP guidelines, FCC RF-exposure rules, and the underlying dosimetry papers they cite. A lead to check is that whole-body resonance and the **lowest** basic restrictions or reference levels are often discussed in a range **around 30–300 MHz**. Quote where the opened documents say the limits are lowest, what they give as the reason (for example whole-body resonance or SAR), and over what frequency range. Then compare those frequencies, as quoted, with the bands actually used for consumer and occupational products. Do not treat a gap or an overlap as proof of motive.

### 2. ITU Atlantic City 1947 ISM allocations (including 2.45 GHz)

Open the 1947 International Telecommunication Union Radio Regulations and Atlantic City conference documents, or a later official reprint that can be opened legitimately. Quote which industrial, scientific, and medical (ISM) frequencies were allocated, including whether 2.45 GHz (or the exact figure the document uses) appears, and any stated rationale. Later ISM revisions belong in a clearly dated follow-on subsection.

### 3. FCC auction and licensing history

Open FCC rulemakings, auction reports, and licensing rules for **cellular**, **PCS**, **Wi-Fi** (including unlicensed Part 15 or successor rules), and **5G** bands actually used in the United States. Quote the stated purpose of each allocation or auction, the band edges as published, and whether the service was licensed or unlicensed. Parallel regulators in other countries may be added when a primary record is opened, and must be labeled as such.

### 4. Engineering reasons for each band

For each major band in the opened records, quote what the engineering or regulatory source gives as the reason for using it: propagation, antenna size, bandwidth, interference, unlicensed access, equipment cost, coexistence with an existing ISM or radar allocation, or other stated factors. Do not invent a “typical” reason when the source is silent.

### 5. Industry lobbying and filings

Search official dockets and comment files (FCC ECFS and similar) for industry and trade-association filings that bear on these allocations or on exposure limits. Quote the filer, the date, and the request as written. Report any documented evidence of industry influence exactly as it appears in the record. Do not infer an unstated motive. If no relevant filing is found for a band, write `NOT FOUND`.

### 6. How IEEE C95.1 and ICNIRP limits were set, and who sat on those committees

Open the IEEE C95.1 standards (and major revisions) and the ICNIRP RF guidelines. Quote how the limits were described as having been derived, including thermal versus non-thermal endpoints if the document discusses them. Record committee rosters, affiliations, and any published conflict-of-interest or funding disclosures **as printed**. Industry affiliation, government affiliation, or academic affiliation is to be copied, not used as a stand-in for a conclusion that the limit was or was not captured.

### 7. The water-absorption claim about 2.45 GHz

A common claim is that 2.45 GHz was chosen because it is the peak absorption frequency of water. A counter-claim is that the liquid-water dielectric absorption peak is near **about 20 GHz**, not 2.45 GHz. Both are leads to check, not results of this outline. Open primary dielectric-property references and any official or historical rationale for the microwave-oven / ISM frequency. Quote the peak frequency the source actually reports, the temperature and conditions, and the rationale for 2.45 GHz if one is stated. Do not settle the “myth” question in this outline.

## Planned file layout for the evidence PR

1. Pass 1 — SOURCES OPENED (primary sources first: ITU, FCC, ICNIRP, IEEE, and peer-reviewed dielectric or dosimetry papers)
2. Resonance, SAR, and where the opened limit documents are most restrictive
3. 1947 ISM allocations and later official revisions
4. FCC (and other regulator) cellular, PCS, Wi-Fi, and 5G licensing and auctions
5. Stated engineering reasons, band by band
6. Documented industry filings and influence, quoted from the record
7. IEEE C95.1 and ICNIRP: derivation of limits and committee membership as published
8. Water absorption and the 2.45 GHz rationale
9. Assessment — what the opened evidence can and cannot support about *why* these bands were chosen, kept separate from the cancer-causation question
10. Open questions and `NOT FOUND` areas

## How the physical claims will be tested

Programs that could test absorption, skin depth, and coupling across bands are listed in [`TOOLS.md`](TOOLS.md). They are candidates only; installs need a separate owner OK. An in-repo script, `tools/frequency_absorption`, now computes skin depth and a simplified whole-body SAR *estimate* per opened product band from the opened Gabriel 1996 4-Cole-Cole parameters. The table and plot are in [`frequency-absorption.md`](frequency-absorption.md) (with [`frequency-absorption-method.md`](frequency-absorption-method.md)). The output is a first-order estimate, not a finding about why a band was chosen, and not a ranking of “safer” frequencies. That claim remains a claim to test.

A model result can support or weaken a claim about *which frequencies couple more strongly*. It cannot, by itself, establish the historical motive for choosing a band. Keep those questions separate.

## Method

Follow [`METHOD.md`](../../METHOD.md). Prefer primary documents over secondary summaries. Quote measured or officially stated figures only. Stay neutral. No Sci-Hub, Library Genesis, or raw paywalled PDFs.

Until the evidence PR is checked and merged, this file has **no conclusion**.
