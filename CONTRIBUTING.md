# Contributing to Cancer Cure

Contributions are welcome: additional published sources, corrections to quotes or numbers, better open links for a cited paper, missing negative or null results, research programs and organizations that study cancer causes, open-source tool candidates (with a license and an official URL), evidence for or against investigation or cure claims, sourced cause and incidence notes, and improvements to the method or templates.

This repository is **not medical advice**. Do not submit treatment recommendations, dosing instructions, or claims that a compound cures cancer unless you are quoting a cited study and filling every required entry field, including **cancer type**, **body site**, evidence level, and negative/null results. Do not submit a finding as a universal cause or cure of cancer.

## How to submit

Open an issue to discuss your contribution, or fork the repository and open a pull request targeting `main`. Include a clear description, why the change helps, and the opened source (URL or DOI) for every factual claim. Quote the supporting sentence. Identify authorship and any third-party licenses.

Do not submit:

- secrets, personal information, or patient-identifying details
- copyrighted PDFs or other full-text publisher files
- material from Sci-Hub, Library Genesis, or similar sites
- unsourced anecdotes presented as clinical evidence
- invented or reconstructed citations, DOIs, or numbers
- a request to install software or to run a simulation. Tool rows in `tools/CANDIDATES.md` and simulation plans in `claims/` are candidates only; installing or running any tool needs a separate OK from the owner

## Review

Every outside submission starts as **submitted / unvalidated**. The owner, @redwing509, reviews it and decides whether it belongs in the project. Corrections may be requested, and inclusion can be declined when evidence is incomplete or a source cannot be opened legitimately. Approval must apply to the latest changes. Nothing is merged automatically.

`main` requires a pull request, an approving owner review, and resolved review discussions. New changes dismiss stale approvals. Do not request write access to bypass review.

Follow [`METHOD.md`](METHOD.md) (including the per-case rule), [`countries/ENTRY_TEMPLATE.md`](countries/ENTRY_TEMPLATE.md), and [`claims/TEMPLATE.md`](claims/TEMPLATE.md). Keep the README disclaimer intact. On contested claims, including cure claims, the cancer-as-fungus investigation, incidence trends, and radio-frequency fields, submit supporting and opposing sources; do not omit inconvenient results. Organize causes and claims by cancer type and body site. Incidence notes must address age, life expectancy, and diagnosis rates, not crude counts alone, and must be broken out by type and site where the source does.

## Coding process (adopted Nov 22, 2026)

These four practices apply to coding work on this project. They do not
replace or weaken the full review set, frozen pass rules, or James's
merge approval, which still come first. Following them does not
authorize a push or a merge.

Source: [obra/superpowers](https://github.com/obra/superpowers), pinned at
`22f0b463e7a5e579904dd6211a520321035526f7` (v7.0.2), MIT License,
Copyright (c) 2025 Jesse Vincent. Adapted guides and that LICENSE:
`docs/superpowers-adopted`. Full text: `docs/superpowers-adopted/CODING-PROCESS.md`. Exact brief
addenda: `docs/superpowers-adopted/BRIEF-TEXT.md` and `docs/superpowers-adopted/templates/`.

1. **Test-first** — For bug fixes and new behavior, write the new test
   first and run it. It must fail for the missing behavior or
   still-present bug, not a typo or a compile error in the test. Only
   then write the smallest production change. Skip typo-only and
   docs-only work. Do not edit a frozen pass rule to match a new
   result. If production code was written before that failing run,
   delete it and start from the tests.
2. **Bite-sized written plans** — For fixes that touch more than one
   behavior, more than one production file, or a "must not change"
   control case, write a short plan first. Include the goal and finding
   id, exact file paths, each behavior as its own task (failing test
   and assertions first), and a Review Focus list with a test for the
   control case most likely to be missed. Skip one-line typo or
   docs-only fixes.
3. **Receiving official review findings** — When Claude, the
   controller, PR-Agent, CodeRabbit, gitleaks, trufflehog, a board
   note, or rb.py returns findings, read the complete list before
   changing code. Verify each finding against this repo, the relevant
   toolchain, frozen pass rules, and any decision James already made.
   Accept, accept with a smaller fix, or push back with a file, test,
   and reason. If a finding conflicts with a decision James already
   made, stop and ask him. Implement accepted items one at a time and
   re-run the relevant tests after each. Informal reviews do not
   replace the official set.
4. **Systematic debugging** — For a failing gate or harness error whose
   root cause is not already written in an approved finding: (1) read
   the full error, reproduce it, and check recent diffs, pins, inputs,
   and the environment; (2) diff against a working neighbor and read
   the solver syntax or gate contract if the failure is in generated
   input; (3) test one hypothesis and one variable; (4) write a failing
   test or known-solution assertion first, apply one root-cause fix,
   and re-run the original failing command plus surrounding checks. Do
   not relax a tolerance or a frozen pass rule. If three attempts fail,
   stop and discuss. Never print secrets; do not leave temporary debug
   prints in the submitted change.

Not adopted: the upstream plugin, hooks, telemetry, mandatory
brainstorming before every already-approved fix, extra helper agents
per task, and any flow that would skip the review set or James's merge
approval.
