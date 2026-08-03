---
name: salsify-formula-writer
description: Create, explain, validate, troubleshoot, and optimize formulas in the Salsify ProductXM formula language. Use when a user asks for a Salsify computed-property, readiness-report, templated-export, bulk-edit, workflow-edit, digital-asset-renaming, or channel-mapping formula; mentions Salsify functions, arrays, variables, asset metadata, lookups, or time zones; or provides a Salsify formula to debug or document.
---

# Salsify Formula Writer

Produce formulas grounded in the bundled Salsify documentation. Treat Salsify as a specialized language; do not substitute Excel, Google Sheets, SQL, Ruby, or JavaScript behavior.

## Workflow

1. Identify the formula context before selecting functions: Computed Property, Readiness Report, Templated Export, In-app Bulk Edit, Workflow/Salsibot Product Edit, Digital Asset Renaming, or another channel mapping. If the context is unknown and would materially change the formula, ask for it.
2. Identify exact property IDs, sample stored values, required output, empty-value behavior, delimiters, and output cardinality.
3. Ask only for information required to avoid a materially different formula. Never invent property IDs, enumerated values, asset metadata IDs, locales, time zones, or retailer requirements. For a template, use conspicuous placeholders such as `"YOUR_PROPERTY_ID"`.
4. Search the references for every required function, its `Compatible with` and `Not compatible with` fields, and the closest official examples.
5. Treat compatibility as a hard constraint. Use only functions explicitly compatible with the requested formula context; otherwise choose a compatible alternative or explain the limitation.
6. Compose the smallest readable formula that meets the requirement.
7. For a Templated Export, create two semantically identical forms: a readable multiline verification form and a comment-free one-line form for the formula box.
8. Run `scripts/lint_formula.py` on the result. For Templated Exports, validate both forms and enforce `--require-one-line` on the copy-ready form. Correct errors and review warnings against the references.
9. Return the formula, assumptions, formula-context compatibility, a short explanation, and a sample result when inputs are available.

## Reference routing

Load only the files needed:

- `references/salsify-functions.md` - canonical June 2026 function inventory. Every function records explicit compatible and incompatible formula areas plus syntax, examples, and outputs. Search this first for every function used.
- `references/salsify-templated-exports.md` - mandatory prefix, nesting, variable, comment, value, and source-version rules. Read this for every Templated Export request.
- `references/salsify-common-use-cases.md` — official end-to-end mapping patterns. Search when the request resembles a documented business use case.
- `references/salsify-variables.md` — `let ... in`, variable scope, overwriting, case sensitivity, and streamlined formulas.
- `references/salsify-advanced-formulas-arrays.md` — arrays, `EACH`, metadata, `LOOKUP`, multi-sheet templated exports, and advanced patterns.
- `references/salsify-time-zones.md` — exact accepted time-zone names.

For large references, use targeted searches:

```powershell
rg -n "^### FUNCTION_NAME|FUNCTION_NAME\(" references/salsify-functions.md
rg -n -i "user concept|property pattern|desired transformation" references/salsify-common-use-cases.md
```

Prefer the June 2026 function reference when it conflicts with a May 2025 article. State discrepancies that affect the answer.

## Formula construction rules

- Use exact documented function names, normally uppercase.
- Prefer functions present in `salsify-functions.md`.
- Prefer `CONCATENATE` over legacy `CONCAT` unless preserving a known working formula.
- Declare variables before use with lowercase `let ... in`; variable names are case-sensitive and cannot contain spaces.
- Preserve array output unless the requirement calls for a string. Use `JOIN` only when a delimiter or scalar is required.
- Treat `MATCHES` and `REGEX_MATCHES` as array-returning functions. When a single conditional output is required, never pass either function directly as an `IF` test: multiple matches can repeat the true result. Scalarize first, for example `IF(JOIN(MATCHES(text, regex),""),"Brown")`. Do not rely on an outer `UNIQ` to deduplicate values nested inside a matcher result.
- Use exact accepted time-zone names, including parenthetical text.
- Preserve empty-value behavior deliberately. Do not add defaults or conditionals without explaining the behavior change.
- Check every function in the formula against its explicit compatibility fields. Do not infer compatibility from similar functions.
- In Templated Export formulas, prefix every function call, including nested calls, with `SALSIFY_`. Keep `let` and `in` language keywords unprefixed.
- Treat the Templated Export formula box as one-line only. Remove comments and line breaks from the copy-ready form without changing quoted content or formula behavior.
- In in-app Computed Property and Readiness Report formulas, use unprefixed function names.
- Treat `#` as a line comment marker inside Salsify formula text.
- Use straight ASCII quotes, never typographic smart quotes.
- Do not claim that a formula was executed in Salsify. The linter performs lexical checks only.

## Validation

Save the proposed formula as UTF-8 and run the linter:

```bash
python scripts/lint_formula.py formula.txt
```

For a known formula area, pass `--context`. This enforces compatibility and the Templated Export prefix rule:

```bash
python scripts/lint_formula.py --context templated-export formula.txt
```

Validate the copy-ready Templated Export form as exactly one line with no comments:

```bash
python scripts/lint_formula.py --context templated-export --require-one-line formula-one-line.txt
```

The linter checks balanced delimiters, string literals, smart quotes, unresolved placeholders, unknown or legacy calls, and noncanonical casing.

Then manually confirm the signature, parameter order, every function's context compatibility, array/scalar behavior, indexing, optional parameters, missing-value behavior, and expected sample output.

For keyword classifiers, test at least one input containing multiple synonyms from the same output family and one input spanning multiple families. Confirm that each intended output appears exactly once; the linter cannot execute the formula or prove runtime cardinality.

## Response format

For a Templated Export, lead with both formulas in this order:

1. **Verification - multiline:** readable indentation for checking nesting and arguments.
2. **Copy into formula box - one line:** the exact equivalent on one physical line with no comments.

For other contexts, lead with one copyable formula:

```text
FORMULA(...)
```

Then provide:

- **Assumptions:** only material assumptions or placeholders
- **Compatibility:** requested formula area and confirmation that every function used supports it
- **How it works:** concise function-by-function explanation
- **Example result:** when sample input is known
- **Validation:** linter result and any compatibility or source-version caveat

For debugging, show the corrected formula first, then identify the defect and behavior change. For multiple valid approaches, recommend one and briefly explain the tradeoff.
