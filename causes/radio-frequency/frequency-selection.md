# Frequency selection: why these bands?

**Status:** Citation-checked findings from official and primary pages opened on 19 Nov 2026, America/Los_Angeles (Pacific Time), after Hermes job `20261119-184934-cancer-cure-rf-band-selection-history`. This is **not** a conclusion that any band was chosen to maximize or minimize coupling to the body. Where a source could not be opened, the claim was dropped.

**This is not medical advice.** Read the [disclaimer in the README](../../README.md).

**Per-case rule (t1201u):** cancers are not always caused by one thing, and they can be caused by different things in different areas of the body. Every cause and claimed cure is treated on its own, by **cancer type** and **body site**. This note is mostly about band-allocation and dosimetry history, not epidemiology. No cancer study was opened in this pass, so no cancer type or site is assigned to a result here.

## Question

Why did companies and regulators put widely used products — including microwave ovens, Wi-Fi, cellular, PCS, and later 5G systems — at or near frequencies that are sometimes said to **affect the human body most**? Was that overlap deliberate, incidental, or overstated?

The opened allocation records do **not** state a biological or tissue-absorption reason for choosing the bands below. Overlap between a product band and a dosimetry range is recorded as a comparison, not as a motive.

## 1. What opened dosimetry texts say, compared with opened product bands

ICNIRP (1998), official PDF, divides absorption in the human body into four frequency ranges (Durney et al. 1985, as cited there):

- “frequencies from about 100 kHz to less than about 20 MHz, at which absorption in the trunk decreases rapidly with decreasing frequency, and significant absorption may occur in the neck and legs;”
- “frequencies in the range from about 20 MHz to 300 MHz, at which relatively high absorption can occur in the whole body, and to even higher values if partial body (e.g., head) resonances are considered;”
- “frequencies in the range from about 300 MHz to several GHz, at which significant local, nonuniform absorption occurs;” and
- “frequencies above about 10 GHz, at which energy absorption occurs primarily at the body surface.”

The same pages state: ““Standard Reference Man” (ICRP 1994), if not grounded, has a resonant absorption frequency close to 70 MHz.” For taller people the resonant frequency is “somewhat lower,” and “for shorter adults, children, babies, and seated individuals it may exceed 100 MHz.” “The values of electric field reference levels are based on the frequency-dependence of human absorption.” Source: https://www.icnirp.org/cms/upload/publications/ICNIRPemfgdl.pdf

ICNIRP (2020), official PDF, uses a dosimetric split near 6 GHz: “below about 6 GHz, where EMFs penetrate deep into tissue (and thus require depth to be considered), it is useful to describe this in terms of “specific energy absorption rate” (SAR)”; “above 6 GHz, where EMFs are absorbed more superficially (making depth less relevant), it is useful to describe exposure in terms of the density of absorbed power over area (W m−2), which we refer to as “absorbed power density” (Sab).” It also states: “86% of the power at 6 and 300 GHz is absorbed within 8 and 0.2 mm of the surface respectively (Sasaki et al. 2017).” On the whole-body thermal basis: exposures “resulting in a whole-body average SAR of approximately 6 W kg−1, within the 100 kHz to 6 GHz range, over at least a 1-hour interval under thermoneutral conditions… is required to induce a 1°C body core temperature rise in human adults,” and “ICNIRP has adopted a conservative position and uses 4 W kg−1 averaged over 30 min as the radiofrequency EMF exposure level corresponding to a body core temperature rise of 1°C.” Source: https://www.icnirp.org/cms/upload/publications/ICNIRPrfgdl2020.pdf

The FCC Body Tissue Dielectric Parameters page states that “A 4-Cole-Cole Model, as described in “Compilation of the Dielectric Properties of Body Tissues at RF and Microwave Frequencies” by Camelia Gabriel in U.S. Air Force Report AFOSR-TR-96, is used to compute the values,” and “The tool calculates parameters for frequencies between 10-6,000 MHz.” Source: https://www.fcc.gov/general/body-tissue-dielectric-parameters

FCC OET Bulletin 65, Appendix C, states: “Maximum energy absorption is usually expected in the more absorptive high water-content tissues near the surface of the head or body.” That sentence is about where energy is expected in the body, not about why a band was allocated. Source: https://transition.fcc.gov/bureaus/oet/info/documents/bulletins/oet65/oet65c.pdf

A first-order, per-tissue numerical comparison of skin depth and a labeled simplified SAR *estimate* across these product bands is in [`frequency-absorption.md`](frequency-absorption.md). That output is not a whole-body resonance model and is not a safety ranking.

**Comparison, not motive.** 2.45 GHz sits above the 20–300 MHz whole-body-absorption range in ICNIRP 1998 and below the “above about 10 GHz” surface-absorption range; it falls in the “300 MHz to several GHz” local-absorption range, and below the 6 GHz SAR / absorbed-power-density switch in ICNIRP 2020. Cellular and Broadband PCS (824–894 MHz and 1850–1995 MHz as opened below) fall in that same “several GHz” local-absorption range. The millimetre-wave bands (24.25–40 GHz and neighbouring assignments) are in the range where ICNIRP 1998 says absorption “occurs primarily at the body surface” and where ICNIRP 2020 uses absorbed power density. **No opened allocation or rulemaking record in this pass states that a band was selected because of where tissue absorption peaks.**

## 2. 1947 ISM designations and later official text

The official ITU Library & Archives scan of the *Radio Regulations, annexed to the International Telecommunication Convention (Atlantic City, 1947)* was opened and text-extracted (https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/1.7.48.en.100.pdf). Article 5 footnotes designate frequencies “for industrial, scientific and medical purposes” and require radiocommunication services operating within the stated limits to “accept any harmful interference” from that equipment. The opened footnotes include:

- 13 560 kc/s, emissions confined within ±0.05% of that frequency;
- 27 120 kc/s, within ±0.6%;
- 40.68 Mc/s, within ±0.05%;
- 915 Mc/s **in Region 2**, within ±25 Mc/s (the scan’s OCR prints “±25 Me/s” at that line);
- 2 450 Mc/s **in Region 2, Australia, New Zealand, Northern Rhodesia, Southern Rhodesia, the Union of South Africa, the territory under mandate of Southwest Africa, and the United Kingdom**, within ±50 Mc/s;
- 5 850 Mc/s, same country and region list, within ±75 Mc/s.

In 1947, 2 450 Mc/s was therefore a **regional and listed-country** ISM designation, not a worldwide one, in the opened text. Those footnotes do **not** state a water-absorption or tissue-coupling reason for the choice of frequency.

Later official U.S. text, 47 CFR § 2.106 footnote 5.150 (CFR edition current as of 1 October 2024, https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol1/xml/CFR-2024-title47-vol1-sec2-106.xml), lists: “13 553-13 567 kHz (centre frequency 13 560 kHz), 26 957-27 283 kHz (centre frequency 27 120 kHz), 40.66-40.70 MHz (centre frequency 40.68 MHz), 902-928 MHz in Region 2 (centre frequency 915 MHz), 2400-2500 MHz (centre frequency 2450 MHz), 5725-5875 MHz (centre frequency 5800 MHz), and 24-24.25 GHz (centre frequency 24.125 GHz)” as “also designated for industrial, scientific and medical (ISM) applications,” and states that “Radiocommunication services operating within these bands must accept harmful interference which may be caused by these applications.” The footnote gives no biological rationale.

47 CFR § 18.301 (same CFR edition, https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol1/xml/CFR-2024-title47-vol1-sec18-301.xml) says ISM equipment “may be operated on any frequency above 9 kHz except as indicated in § 18.303,” and that the listed bands “in accordance with § 2.106 of the rules, are designated for use by ISM equipment,” including 915 MHz ± 13.0 MHz, 2450 MHz ± 50.0 MHz, 5800 MHz ± 75.0 MHz, and 24.125 GHz ± 125.0 MHz. The printed amendment history of that section is “[85 FR 38740, June 26, 2020].”

A discrepancy worth recording, without inventing a reason: footnote 5.150 spans 2400-2500 MHz and 5725-5875 MHz, while 47 CFR § 15.247 operates in 2400-2483.5 MHz and 5725-5850 MHz, and § 18.301 permits 2450 ± 50 MHz and 5800 ± 75 MHz. The opened sections do not explain the difference.

ITU-R Recommendation SM.1056 (1994), https://www.itu.int/dms_pubrec/itu-r/rec/sm/R-REC-SM.1056-0-199407-S!!PDF-E.pdf, discusses limits on radiation from ISM equipment and recalls the Radio Regulations definition of ISM applications (equipment designed to generate and use RF energy locally “for industrial, scientific, medical, domestic or similar purposes, excluding applications in the field of telecommunications”). It is a radiation-limit recommendation. No sentence was found in the opened recommendation that selects an ISM centre frequency because of tissue or water absorption.

## 3. FCC cellular, PCS, Wi-Fi and millimetre-wave assignments, as opened

Figures are copied from the 2024 official govinfo XML. Licensed vs unlicensed is as the cited part states. Auction prices, close dates, and winners were **not** opened and are not quoted. No non-U.S. regulator’s band plan was opened in this pass.

| Service, as named in the opened record | Edges as published | Source |
| --- | --- | --- |
| ISM operating frequencies | 915 MHz ± 13.0 MHz; 2450 MHz ± 50.0 MHz; 5800 MHz ± 75.0 MHz; 24.125 GHz ± 125.0 MHz (and the lower and higher centres listed in § 18.301) | 47 CFR § 18.301 |
| Part 15 unlicensed (heading of § 15.247) | 902-928 MHz, 2400-2483.5 MHz, and 5725-5850 MHz | 47 CFR § 15.247, https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol1/xml/CFR-2024-title47-vol1-sec15-247.xml |
| Cellular Radiotelephone Service | Block A: 869-880 MHz paired with 824-835 MHz, and 890-891.5 MHz paired with 845-846.5 MHz; Block B: 880-890 MHz paired with 835-845 MHz, and 891.5-894 MHz paired with 846.5-849 MHz | 47 CFR § 22.905, https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol2/xml/CFR-2024-title47-vol2-sec22-905.xml |
| Broadband PCS | Block A: 1850-1865 MHz paired with 1930-1945 MHz; Block B: 1870-1885 / 1950-1965 MHz; Block C: 1895-1910 / 1975-1990 MHz; Block D: 1865-1870 / 1945-1950 MHz; Block E: 1885-1890 / 1965-1970 MHz; Block F: 1890-1895 / 1970-1975 MHz; and 1910-1915 MHz paired with 1990-1995 MHz | 47 CFR § 24.229, https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol2/xml/CFR-2024-title47-vol2-sec24-229.xml |
| U-NII / 5 GHz and 6 GHz unlicensed | Opened bands in § 15.407 include 5.15-5.25 GHz, 5.25-5.35 GHz, 5.47-5.725 GHz, 5.725-5.850 GHz, 5.850-5.895 GHz, and 5.925-7.125 GHz | 47 CFR § 15.407, https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol1/xml/CFR-2024-title47-vol1-sec15-407.xml |
| Upper Microwave Flexible Use Service | 24.25-24.45 GHz and 24.75-25.25 GHz; 27.5-28.35 GHz; 37-38.6 GHz (with 37.0-37.6 GHz site-specific shared with eligible Federal entities); 38.6-40 GHz; 47.2-48.2 GHz | 47 CFR § 30.4, https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol2/xml/CFR-2024-title47-vol2-sec30-4.xml |

Purpose sentences in the opened parts are administrative, not propagation justifications:

- 47 CFR § 22.1: “The purpose of these rules is to establish the requirements and conditions under which radio stations may be licensed and used in the Public Mobile Services.” (https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol2/xml/CFR-2024-title47-vol2-sec22-1.xml)
- 47 CFR § 24.1: “This part states the conditions under which portions of the radio spectrum are made available and licensed for PCS.” (https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol2/xml/CFR-2024-title47-vol2-sec24-1.xml)
- 47 CFR § 30.1: “As of December 14, 2016, Local Multipoint Distribution Service licenses for the 27.5-28.35 GHz band, and licenses issued in the 38.6-40 GHz band under part 101 of this chapter shall be reassigned to the Upper Microwave Flexible Use Service.” (https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol2/xml/CFR-2024-title47-vol2-sec30-1.xml)
- 47 CFR § 30.301 (Subpart D): “Upper Microwave Flexible Use Service subject to competitive bidding.” “Mutually exclusive initial applications for Upper Microwave Flexible User Service licenses are subject to competitive bidding.” (https://www.govinfo.gov/content/pkg/CFR-2024-title47-vol2/xml/CFR-2024-title47-vol2-part30.xml)

## 4. Stated engineering and policy reasons, only as the opened record says

**Unlicensed 915 MHz, 2.4 GHz, and 5.7 GHz.** FCC *Second Report and Order*, “Amendment of Part 15 of the Commission’s Rules Regarding Spread Spectrum Devices,” ET Docket No. 99-231, FCC 02-151, adopted 16 May 2002, released 30 May 2002 (https://docs.fcc.gov/public/attachments/FCC-02-151A1.pdf), states the objective “to improve spectrum sharing by unlicensed devices operating in the 915 MHz (902 - 928 MHz), 2.4 GHz (2400 - 2483.5 MHz), and 5.7 GHz (5725 – 5850 MHz) bands,” and records that “the original rules were crafted in a manner to highlight the interference immunity characteristics of spread spectrum devices, even at the expense of higher speeds.” The reason given in that order is interference immunity and sharing, not tissue coupling. The order treats these as operation in already-designated ISM / Part 15 bands (see footnote 5.150 and § 15.247). Nothing in the opened §§ 15.247 or 2.106, or in FCC 02-151, states a penetration or absorption reason for choosing 2.4 GHz rather than another ISM band.

**5 GHz U-NII.** § 15.407 is a technical power and spectral-density rule. No sentence stating *why those frequencies were chosen* was found in the opened section.

**Cellular and PCS.** Only the purpose sentences in §§ 22.1 and 24.1 were found in the opened CFR text. No antenna-size, bandwidth, or cost rationale is stated there.

**Millimetre-wave flexible use.** Besides the 14 December 2016 reassignment in § 30.1, the opened *Use of Spectrum Bands Above 24 GHz for Mobile Radio Services* Report and Order, FCC 16-89 (https://docs.fcc.gov/public/attachments/FCC-16-89A1.pdf), adopts “new upper microwave flexible use licenses authorizing mobile operations” in 27.5-28.35 GHz (county licenses) and 38.6-40 GHz (Partial Economic Area licenses), as a “general framework applied across three licensed bands to make a substantial amount of spectrum available” and “the basis for how we will pursue flexible use licensing in additional mmW bands going forward.” That is a stated flexible-use / mobile-licensing reason. A footnote describes NYU Wireless research as including “propagation measurements and models, radiation and biological health effects, mmW MAC layer design and other component technology development.” That describes a research center’s work. It is **not** a statement that the Commission chose 28 or 39 GHz because of biological absorption. A search of the opened order did not find a sentence allocating a band because it is a tissue- or water-absorption peak.

## 5. Documented industry filings, as quoted in an opened Commission order

FCC 02-151, paragraph 14, records company positions in ET Docket 99-231 on whether the U-NII rules should be extended to 2.4 GHz:

- “Intersil suggests that we modify the U-NII band rules to allow for digitally modulated devices at 2.4 GHz.”
- “On the other hand, Apple, Silicon Wave, and Intel object to modifying the U-NII rules.”
- “Apple states that the Commission should first identify the exact rule changes and explain what it believes the effect of those changes would be.”
- “Intel notes that the power spectral density limitation for 2.4 GHz spread spectrum devices is higher than the limits for devices operating under the U-NII rules.”

Paragraph 15: “At this time, we decline to modify the U-NII rules to add the 915 MHz and 2.4 GHz bands.”

These are filings, as quoted by the Commission, about which rule part and power limits should govern 2.4 GHz devices. No filer in the quoted text asks for a band because it couples to tissue. Direct ECFS comment files were not opened; names and positions are those printed in the order only. FCC 02-151 footnote 9 cites a 1985 First Report and Order, GEN Docket 81-413; that 1985 order was not opened and is not quoted.

## 6. ICNIRP membership, as published; IEEE C95.1 not opened

IEEE Std C95.1-2019 (text, roster, affiliations, and conflict-of-interest disclosures) was **not opened**. No statement is made here about how those limits were derived or who sat on the committee.

The ICNIRP Commission page, opened at https://www.icnirp.org/en/about-icnirp/commission/index.html, states: “The Commission membership consists of a Chairperson, Vice-Chairperson and up to 12 members.” “In carrying out their voluntary work for the Commission they do not represent either their countries of origin or their institutes. ICNIRP members are required to declare any personal interests in relation to their activities for ICNIRP. Members’ declarations of personal interests are available below along the member’s profile.” “Members are elected to the Commission from nominations received by current members, the Executive Council of the International Radiation Protection Association (IRPA), the IRPA Associate Societies, and by national and international public bodies for radiation protection following an open call for nominations published on the ICNIRP website.” The declaration files themselves were not opened, so their contents are not quoted. ICNIRP 2020’s thermal derivation of the 4 W kg−1 / 30 min figure is quoted in section 1.

## 7. Water absorption and the “2.45 GHz was chosen because it is water’s peak” claim

The claim is **not stated in any opened allocation record.** Footnote 5.150 describes 2400-2500 MHz as an ISM designation with an interference-acceptance rule; § 18.301 lists 2450 MHz as an ISM operating frequency; § 15.247 uses 2400-2483.5 MHz for unlicensed devices. **NOT FOUND:** a sentence in those records, or in FCC 02-151, saying the band was chosen for water absorption.

A counter-lead is supported only by an opened **author preprint**, not a peer-reviewed permittivity standard: Daniel C. Elton, arXiv:1704.01667, “The Debye relaxation peak dominates the dielectric absorption spectrum of water. The peak is centered at ≈ 20 GHz (0.66 cm−1) and spans six decades of frequency.” Sources: https://arxiv.org/pdf/1704.01667 and https://ar5iv.labs.arxiv.org/html/1704.01667. The peer-reviewed Ellison 2007 permittivity paper was not opened (paywalled; no legitimate open copy found), so no figure is quoted from it.

The OET 65 Appendix C sentence about “high water-content tissues” is about where SAR is expected in the body, not about why a band was allocated.

## 8. Cancer epidemiology

No cancer epidemiology study and no IARC monograph text was opened in this pass, so none is cited and none is summarized. ICNIRP 1998 does state, as a guidelines conclusion and without naming a cancer type or body site: “Induction of cancer from long-term EMF exposure was not considered to be established.” That is not treated here as a site-specific epidemiology finding (t1201u). Nothing in this note asserts that RF fields do or do not cause cancer at any site.

## 9. What this can and cannot support about *why* the bands were chosen

The opened record supports: 1947 and later official ISM designations with an interference-acceptance rule and no printed biological rationale; later unlicensed use of those ISM-adjacent bands for spreading-spectrum sharing (FCC 02-151); cellular, PCS, and millimetre-wave assignments published as licensed services, with millimetre-wave flexible-use / mobile licensing stated in FCC 16-89 and competitive bidding stated in 47 CFR § 30.301; and ICNIRP dosimetry ranges that do **not** place 2.45 GHz at the ~70 MHz whole-body resonance.

The opened record does **not** support a finding that companies or regulators chose these product bands because they affect the body most, or because 2.45 GHz is liquid water’s dielectric absorption peak. Industry participation quoted above is about rule parts and power limits, not a documented biological motive.

## 10. Still open or not found

- Direct ECFS filings (only Commission quotations in FCC 02-151 were opened).
- FCC auction prices, close dates, and winners.
- IEEE C95.1-2019 text, roster, and disclosures.
- The 1985 First Report and Order, GEN Docket 81-413.
- Ellison 2007 permittivity figures.
- The IARC RF monograph.
- A published official explanation of 2400-2500 MHz vs 2400-2483.5 MHz.
- Whether ICNIRP 2020 treats “non-thermal” studies as a basis for limits: the opened extract considers “those referred to as ‘low-level’ and ‘non-thermal’” when determining thresholds, but that passage was not read as settling the question.
- Non-U.S. allocations and limits.

## How the physical claims can be tested

Programs that can test absorption, skin depth, and coupling across bands are listed in [`TOOLS.md`](TOOLS.md). openEMS and Meep are installed on `mail` under `/opt/cancer-tools/` after the owner’s 19 Nov 2026 approval (t1207s6108); further installs still need a separate OK. The in-repo script `tools/frequency_absorption` computes skin depth and a simplified SAR *estimate* per opened product band from the opened Gabriel 1996 parameters. See [`frequency-absorption.md`](frequency-absorption.md). That output cannot, by itself, establish the historical motive for choosing a band.

## Method

Follow [`METHOD.md`](../../METHOD.md). Prefer primary documents. Quote only what was opened. Stay neutral. No Sci-Hub, Library Genesis, or raw paywalled PDFs in this repository.
