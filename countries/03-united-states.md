# 03 · United States (first bite-size slice)

**This is not medical advice.** See the [README disclaimer](../README.md). Each entry states its own cancer type, body site and evidence level; a result in one type or site is not a result in another (per-case rule in [`METHOD.md`](../METHOD.md)).

Status: first bite-size slice, citation-checked 27 Nov 2026. Not the full country note.

Languages searched: English (US official sources: NCI, NCCIH, ClinicalTrials.gov, NCI DCCPS).

Method: Hermes bite-size jobs (sources → verify → extract) on NVIDIA NIM Nemotron 3.5 Super VL, then a separate citation check against the opened sources. Raw job files: [`03-united-states-data/`](03-united-states-data/).

Headline: an NCCIH-reported compound from *Oplopanax horridus* (devil's club) inhibited colon-cancer xenograft growth in mice (animal evidence; colon) and showed activity in one colorectal cell line (in vitro; colorectum). No human efficacy evidence was found in this slice.


All four URLs opened with curl. HTML text and the ClinicalTrials.gov JSON record were checked directly.

- **S01 · Type and site unspecified · NCI definition only.** “Complementary and alternative medicine (CAM) is the term for medical products and practices that are not part of standard medical care.” Keep as terminology. [NCI](https://www.cancer.gov/about-cancer/treatment/cam)
- **S02a · Colon cancer · Colon origin, mouse xenograft · Animal evidence.** The source identifies “Mice with transplanted human colon cancer cells” and reports “tumor growth inhibition occurred in a dose-related manner.” The joined extract quotation is replaced with two verbatim excerpts. Drop any extrapolation to patients. [NCCIH](https://www.nccih.nih.gov/research/research-results/compound-in-north-american-botanical-oplopanax-horridus-inhibits-colorectal-tumor-growth-in-mouse-model-and-human-cells)
- **S02b · Colorectal cancer · Colorectum, subsite unspecified · In vitro evidence.** “One of them (HCT-116) showed a significant sensitivity to oplopantriol A.” The surrounding paragraph identifies two human colorectal cancer cell lines. Drop any inference of clinical activity or established p53 causality. [NCCIH](https://www.nccih.nih.gov/research/research-results/compound-in-north-american-botanical-oplopanax-horridus-inhibits-colorectal-tumor-growth-in-mouse-model-and-human-cells)
- **S03 · Colon cancer · Colon · Interventional registration only.** “This clinical trial will investigate the ability of plant exosomes to more effectively deliver curcumin to normal colon tissue and colon tumors.” The title begins “Phase I Clinical Trial”, and the API records `"phases":["NA"]`, `"overallStatus":"UNKNOWN"` and `"hasResults":false`. Keep the planned delivery objective and registry fields. Drop any inference of delivery success or clinical efficacy. [ClinicalTrials.gov API](https://clinicaltrials.gov/api/v2/studies/NCT01294072?format=json)
- **S04 · Type and site unspecified · NCI program description only.** “Supporting research to better understand cancer causes and outcomes and to translate findings into clinical and public health interventions.” Keep as program scope. [NCI DCCPS](https://cancercontrol.cancer.gov/)
