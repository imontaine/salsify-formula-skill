# Templated Export Formulas

Use these rules whenever the requested formula context is a Templated Export.

## Required response and paste format

Templated Export formula boxes accept one-line formulas. For every Templated Export request, return both forms in this order:

1. **Verification - multiline:** Indented and readable so function nesting, arguments, and closing delimiters can be checked. Comments may be included when useful.
2. **Copy into formula box - one line:** The exact equivalent formula on one physical line, with no comments.

Preserve all spaces and delimiters inside quoted strings while converting to one line. Do not change function order, arguments, literals, property IDs, or empty-value behavior. Validate the multiline form with `--context templated-export`, then validate the copy-ready form with both `--context templated-export` and `--require-one-line`.

Example:

```text
# Verification - multiline
SALSIFY_IF(
  SALSIFY_VALUE("calc_max_sale_qty"),
  SALSIFY_VALUE("calc_max_sale_qty"),
  "NULL__VALUE"
)

# Copy into formula box - one line
SALSIFY_IF(SALSIFY_VALUE("calc_max_sale_qty"),SALSIFY_VALUE("calc_max_sale_qty"),"NULL__VALUE")
```

## Prefix rules

- Prefix every Salsify function call with `SALSIFY_`.
- Prefix nested function calls individually.
- Do not prefix property IDs, string literals, numeric arguments, `null`, arrays, or comments.
- In in-app Computed Property and Readiness Report formulas, use the normal unprefixed function names.
- Check each base function's `Compatible with` field in `salsify-functions.md` before adding the prefix. The prefix does not make an incompatible function compatible.

Example:

```text
# In-app
IF(EQUAL(VALUE("Category"), "R/C Cars"), "Y", "N")

# Templated Export
SALSIFY_IF(
  SALSIFY_EQUAL(SALSIFY_VALUE("Category"), "R/C Cars"),
  "Y",
  "N"
)
```

The one-branch form returns no value when the condition is false:

```text
SALSIFY_IF(
  SALSIFY_EQUAL(SALSIFY_VALUE("Category"), "R/C Cars"),
  "Y"
)
```

## Current-name discrepancy

An older article uses `EQUALS` and `SALSIFY_EQUALS`. The canonical June 2026 cheat sheet documents `EQUAL`; therefore use:

- In-app: `EQUAL(...)`
- Templated Export: `SALSIFY_EQUAL(...)`

Preserve the older spelling only when repairing an organization-specific formula already proven to require it, and state the discrepancy.

## Values and multiple values

Return the first value:

```text
# In-app
VALUE("Bullet Points")

# Templated Export
SALSIFY_VALUE("Bullet Points")
```

Return the second value:

```text
SALSIFY_VALUE("Bullet Points", 2)
```

Join all values with a comma and space:

```text
SALSIFY_JOIN_VALUES("Bullet Points", ", ")
```

With stored values `Soft and Delicate` and `Warm and Cozy`, the joined output is:

```text
Soft and Delicate, Warm and Cozy
```

## Variables

The June 2026 compatibility matrix lists `LET...IN` as compatible with Templated Export Formulas. Keep the language keywords `let` and `in` unprefixed, but prefix every function call inside the expression:

```text
let category = SALSIFY_VALUE("Category") in

SALSIFY_IF(
  SALSIFY_EQUAL(category, "R/C Cars"),
  "Y",
  "N"
)
```

This supersedes the older May 2025 note that variables were unavailable in templated exports. State the source-version discrepancy if variable support affects the answer.

## Comments and formatting

- Start a formula comment with `#`; everything after it on the same line is ignored.
- Use comments for instructions, context, or temporarily disabling a line.
- Use straight ASCII quotes.
- Blank lines and indentation may be used for readability.

```text
# Removes HTML formatting from Description
# Last edited 2022-04-02 by Richard M.
SALSIFY_STRIP_HTML(
  SALSIFY_VALUE("Description")
)
```

## Function groups mentioned in the guide

- Numbers: `ADD`, `SUBTRACT`, `ROUND`, `LENGTH`
- Combining and transforming values: `CONCATENATE`, `COALESCE`, `LOWER`, `UPPER`, `PROPER`
- Conditionals: `IF`, `AND`, `OR`, `EQUAL`, `NOT`
- Category hierarchies
- Digital asset URLs and metadata
- Digital asset renaming

Do not assume every function in a group works in a Templated Export. Verify each function's compatibility entry, then apply `SALSIFY_`.
