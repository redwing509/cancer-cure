# 04 · Japan (first bite-size slice: sources)

**This is not medical advice.** See the [README disclaimer](../README.md). Each entry states its own cancer type, body site and evidence level; a result in one type or site is not a result in another (per-case rule in [`METHOD.md`](../METHOD.md)).

Status: first bite-size slice (sources and per-source verification), citation-checked 27 Nov 2026. Not the full country note; no extract step yet.

Languages searched: Japanese (日本語) first, English only to confirm a source already found. Quotes are given in Japanese with a labeled English translation.

Method: Hermes bite-size jobs on NVIDIA NIM Nemotron 3.5 Super VL, then a separate citation check against the opened sources. Raw job files: [`04-japan-data/`](04-japan-data/).

Headline: an MHLW-funded report found that rikkunshito (六君子湯) improved cancer cachexia via reduced ghrelin resistance in an animal model with transplanted human gastric-cancer cells (animal evidence; stomach). The 2009 JSPM guideline summarizes PSK (Krestin) studies, including null results in breast and esophageal cancer.


All four recorded URLs opened with curl. S01 was checked in the PDF and S02–S04 in the HTML. Each retained case below has its own cancer type, site and evidence level.

## S01 · 2009 Japanese Society for Palliative Medicine guideline

Keep the dated guideline’s descriptions and study summaries. Drop the concatenated harvest quotation and any inference of current authorization.

- **Postoperative gastric cancer · Stomach · Historical guideline indication.** “術後胃がん、治癒切除後結腸・直腸がんにおける化学療法との併用 （生存期間の延長）”  
  **translation** — In combination with chemotherapy for postoperative gastric cancer and for colon and rectal cancer after curative resection (prolongation of survival). [Guideline, printed p. 24](https://www.jspm.ne.jp/files/guideline/cam_pdf/cam01.pdf)
- **Resected colon cancer · Colon · Historical guideline indication.** The same excerpt above expressly names “結腸”. **translation** — Colon. The quoted indication is adjunctive chemotherapy after resection. [Guideline, printed p. 24](https://www.jspm.ne.jp/files/guideline/cam_pdf/cam01.pdf)
- **Resected rectal cancer · Rectum · Historical guideline indication.** The same excerpt above expressly names “直腸”. **translation** — Rectum. The quoted indication is adjunctive chemotherapy after resection. [Guideline, printed p. 24](https://www.jspm.ne.jp/files/guideline/cam_pdf/cam01.pdf)
- **Small-cell lung cancer · Lung · Historical guideline indication.** “小細胞肺がんにおける化学療法との併用（奏功期間の延長）”  
  **translation** — In combination with chemotherapy for small-cell lung cancer (prolongation of response duration). [Guideline](https://www.jspm.ne.jp/files/guideline/cam_pdf/cam01.pdf)
- **Breast cancer · Breast · Historical guideline summary of clinical studies.** “乳がんにおける化学療法とクレスチンの併用療法に有効性は認められず”  
  **translation** — Efficacy was not observed for chemotherapy combined with Krestin in breast cancer. [Guideline, CQ-7](https://www.jspm.ne.jp/files/guideline/cam_pdf/cam01.pdf)
- **Esophageal cancer · Esophagus · Historical guideline summary of clinical studies.** “食道がんにおいても生存期間に差はなく”  
  **translation** — There was also no difference in survival duration in esophageal cancer. [Guideline, CQ-7](https://www.jspm.ne.jp/files/guideline/cam_pdf/cam01.pdf)
- **Adult acute non-lymphocytic leukemia · Hematologic, anatomic site unspecified · Historical guideline summary of clinical studies.** “成人急性非リンパ性白血病の維持化学療法へのクレスチン併用療法で寛解期間、生存期間ともに延長は認められなかった”  
  **translation** — Adding Krestin to maintenance chemotherapy in adult acute non-lymphocytic leukemia did not prolong remission duration or survival. [Guideline, CQ-7](https://www.jspm.ne.jp/files/guideline/cam_pdf/cam01.pdf)

## S02–S03 · National Cancer Center Japan

- **S02 · Type and site unspecified · Editorial history only.** “クレスチンが経過措置品目に移行したことから関連する記述を削除しました。”  
  **translation** — We removed the related text because Krestin moved to transitional listing. Keep the dated editorial note only. Drop the claim that the change established an efficacy verdict. [Immunotherapy page, update history](https://ganjoho.jp/public/dia_tre/treatment/immunotherapy/immu02.html)
- **S03 · Type and site unspecified · General patient information.** The cited fragments are recoverable. Drop the entry from the case evidence because it gives no specific cancer type or body site. [Patient information page](https://ganjoho.jp/public/dia_tre/cam/health_food_products.html)

## S04 · MHLW-funded research report

- **Gastric cancer · Stomach origin of transplanted cells · Animal cachexia model.** The report describes “ヒト胃がん細胞移植がん悪液質動物モデル” and states “六君子湯は、LIF抑制ではなく、グレリン抵抗性の改善を介してがん悪液質を改善することを明らかにした。”  
  **translation** — Animal model of cancer cachexia with transplanted human gastric cancer cells. The investigators found that rikkunshito improved cancer cachexia through reduced ghrelin resistance, without LIF suppression. [Research report](https://mhlw-grants.niph.go.jp/project/22523)
- **Pancreatic cancer · Pancreas · Trial initiation, supportive-care endpoint.** “臨床研究では、膵がん患者を対象として臨床試験を開始した。” The protocol names “悪液質進行抑制効果”.  
  **translation** — In the clinical research, a trial was started in patients with pancreatic cancer. The protocol assesses an effect on slowing cachexia progression. [Research report](https://mhlw-grants.niph.go.jp/project/22523)
- **Uterine cancer · Uterus, subsite unspecified · Randomized phase II protocol and initiation.** “シスプラチンを含む化学療法を施行される子宮がん患者の食欲不振に対する六君子湯の効果―無作為化第Ⅱ相比較試験” and “プロトコール作成を行い、臨床研究に着手した。”  
  **translation** — Effect of rikkunshito on loss of appetite in patients with uterine cancer undergoing chemotherapy containing cisplatin, randomized phase II comparative study. The protocol was prepared and clinical research began. [Research report](https://mhlw-grants.niph.go.jp/project/22523)

Drop any human efficacy inference from study initiation or any tumor response inference from cachexia and appetite endpoints.
