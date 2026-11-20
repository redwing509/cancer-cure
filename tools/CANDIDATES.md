# Tool candidates

This list is **candidates only**. Installing any tool, including one already listed here, still needs a separate OK from the repository owner. A row here is not permission to install, download a new package, or accept a license.

Country surveys look for open-source software we could run ourselves: tumor-growth simulators, drug-screening and docking tools, genomics pipelines, and similar research programs. Each candidate must have a verifiable official link, a license as stated on that page or in the citation, and a short sourced note on what it does. The citation-honesty rules in [`METHOD.md`](../METHOD.md) apply. Do not invent tools or URLs.

Verified finds are appended here, **de-duplicated by name plus official URL**, with the country they were found in. Public country notes may mention the same tools by name, license, official URL, and citation.

Status key: `candidate` = found and citation-checked, not installed; `installed` = installed only after an explicit owner OK, with the date of that OK in the notes.

| Name | Developer | What it does | License | Official URL | Citation / notes | Status | Found in |
|---|---|---|---|---|---|---|---|
| fastp | OpenGene | Ultra-fast all-in-one FASTQ preprocessor (QC, adapters, trimming, filtering, splitting, merging), as stated on the official GitHub repository record | MIT | https://github.com/OpenGene/fastp | GitHub API license field SPDX MIT, confirmed in the China country-note check (19 Nov 2026, Pacific Time). City-level affiliation from the survey draft was not independently re-opened from a paper in that pass. | candidate | China |
| clusterProfiler | Guangchuang Yu and contributors | Universal enrichment tool for omics data (ORA and GSEA), as stated on the Bioconductor package page | Artistic-2.0 | https://bioconductor.org/packages/clusterProfiler/ | License and description confirmed on the official Bioconductor page in the China country-note check (19 Nov 2026, Pacific Time). | candidate | China |
| CB-Dock | Liu et al. (Sichuan University; Shanghai Center for Bioinformation Technology) | Blind-docking web server: cavity detection plus Autodock Vina, as stated in the opened paper | Freely available web server; no named OSI license on the opened paper page | http://cao.labshare.cn/cb-dock/ | Paper: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7471403/ (PMC7471403). Server URL is quoted from that paper; live availability was not separately re-tested. Not an installable local package under a named OSI license. | candidate | China |
