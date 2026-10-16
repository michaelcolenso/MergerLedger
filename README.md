# MergerLedger

**Every public FTC merger enforcement action since 1996 — what happened, who prevailed, and the primary evidence.**

MergerLedger is starting as a data feasibility project, not a web app. Milestone M0 asks one question:

> Can FTC merger enforcement records be transformed reproducibly into defensible transaction outcomes at scale?

## M0 feasibility gate

1. Acquire and preserve the official FTC Merger Enforcement Actions CSV and data dictionary.
2. Validate and profile the source fields before designing the normalized schema.
3. Draw a representative 50-matter sample across fiscal years and action types.
4. Follow FTC case URLs and collect primary-source evidence.
5. Classify legal result, transaction result, and MergerLedger outcome separately.
6. Record rule/version, evidence, confidence, and review status for every classification.
7. Measure deterministic classification coverage and manual-review burden.

**Initial go/no-go target:** about 80% of the representative sample classifiable reliably from FTC structured data plus linked primary sources. This is a feasibility threshold, not a claim about the full dataset.

## Official sources

- FTC datasets: https://search.ftc.gov/policy-notices/open-government/data-sets
- Merger actions CSV: https://search.ftc.gov/system/files/ftc_gov/data/FTC-Merger-Enforcement-Actions.csv
- Data dictionary: https://search.ftc.gov/system/files/ftc_gov/data/FTC-Merger-Enforcement-Actions-dictionary.csv

## Principles

- Preserve raw government data unchanged.
- Never infer `FTC won` from a single field.
- Keep legal result and transaction result separate.
- Every derived outcome must be traceable to primary evidence.
- Ambiguity goes to review; it is not guessed away.
- Do not build the SvelteKit/Cloudflare product until M0 passes.

## Status

Repository initialized. Source acquisition and field inspection are next.
