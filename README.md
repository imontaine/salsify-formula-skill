# Salsify Formula Writer

A reusable AI skill for creating, explaining, validating, and troubleshooting formulas in the Salsify ProductXM formula language.

It works with both Claude Code and OpenAI Codex and includes the Salsify function cheat sheet, examples, compatibility rules, arrays, variables, time zones, and Templated Export requirements.

## Install it globally

You do not need to copy files manually. Ask your AI coding agent to install the skill from this repository.

### Claude Code

Paste this into Claude Code:

```text
Install the salsify-formula-writer skill globally from this GitHub repository:
https://github.com/imontaine/salsify-formula-skill

The skill folder in the repository is:
skill-src/salsify-formula-writer
```

### Codex

Paste this into Codex:

```text
$skill-installer Install the salsify-formula-writer skill globally from this GitHub repository:
https://github.com/imontaine/salsify-formula-skill

The skill folder in the repository is:
skill-src/salsify-formula-writer
```

## Use the skill

### Claude Code

Type `/salsify-formula-writer`, followed by your request:

```text
/salsify-formula-writer Create a Salsify Computed Property formula that returns "Unknown" when Brand is blank and otherwise returns Brand.
```

### Codex

Type `$salsify-formula-writer`, followed by your request:

```text
$salsify-formula-writer Create a Salsify Computed Property formula that returns "Unknown" when Brand is blank and otherwise returns Brand.
```

Both clients can also activate the skill automatically when you ask for a Salsify formula. Explicitly invoking it makes sure the specialized references and validator are used.

> The default Claude command is `/salsify-formula-writer`, not `/salsify`, because the command comes from the installed skill directory name.

## Always name the formula area

This is the most important part of the request. Salsify syntax and function compatibility change depending on where the formula will be used.

| Formula area | How to ask | Important behavior |
| --- | --- | --- |
| Computed Property | "Create a Salsify Computed Property formula..." | Uses normal function names such as `IF` and `VALUE`. |
| Templated Export | "Create a Salsify Templated Export formula..." | Every function needs the `SALSIFY_` prefix. The final formula must be one line. |
| Readiness Report | "Create a Salsify Readiness Report formula..." | Uses normal unprefixed function names. |
| In-app Bulk Edit | "Create a Salsify In-app Bulk Edit formula..." | The skill checks every function for Bulk Edit compatibility. |
| Digital Asset Renaming | "Create a Salsify Digital Asset Renaming formula..." | Only asset-renaming-compatible functions may be used. |

Salsify calls a calculated property a **Computed Property**. The skill understands either phrase, but using "Computed Property" is clearest.

## Computed Property vs. Templated Export

Here is the same business rule requested in the two different contexts.

### Ask for a Computed Property

```text
Create a Salsify Computed Property formula for the property "Category".
Return "Y" when Category is "R/C Cars" and return "N" for every other category.
Return null when Category is blank.
```

The generated functions are unprefixed:

```text
IF(
  VALUE("Category"),
  IF(EQUAL(VALUE("Category"), "R/C Cars"), "Y", "N"),
  null
)
```

### Ask for a Templated Export

```text
Create a Salsify Templated Export formula for the property "Category".
Return "Y" when Category is "R/C Cars" and return "N" for every other category.
Return null when Category is blank.
Give me a readable multiline version for verification and a one-line version to paste into the formula box.
```

The verification version uses `SALSIFY_` on every function:

```text
SALSIFY_IF(
  SALSIFY_VALUE("Category"),
  SALSIFY_IF(
    SALSIFY_EQUAL(SALSIFY_VALUE("Category"), "R/C Cars"),
    "Y",
    "N"
  ),
  null
)
```

The skill also returns the required one-line version:

```text
SALSIFY_IF(SALSIFY_VALUE("Category"),SALSIFY_IF(SALSIFY_EQUAL(SALSIFY_VALUE("Category"),"R/C Cars"),"Y","N"),null)
```

## Examples from the Salsify cheat sheet

### Return a default value

```text
Create a Salsify Computed Property formula that returns the first populated value from "Brand", "Manufacturer", or "Supplier Name". Return "Unknown" when all three properties are blank.
```

### Add leading zeros

```text
Create a Salsify Computed Property formula that pads "UPC" with leading zeros until it contains 12 characters. Preserve null when UPC is blank.
```

### Change date formatting

```text
Create a Salsify Templated Export formula that formats "Launch Date" as MM/DD/YYYY. Include the multiline verification formula and the one-line copy formula.
```

### Convert inches to centimeters

```text
Create a Salsify Computed Property formula that converts "Product Length" from inches to centimeters by multiplying by 2.54. Round to two decimal places and return null when Product Length is blank.
```

### Create a true/false readiness check

```text
Create a Salsify Readiness Report formula that returns true when both "Brand" and "Product Title" contain values. Return false otherwise.
```

### Join multiple values

```text
Create a Salsify Templated Export formula that joins every value from "Bullet Points" using a pipe with spaces around it: " | ".
```

### Remove unwanted characters

```text
Create a Salsify Computed Property formula that removes special characters and symbols from "Product Name" while keeping letters, numbers, spaces, and hyphens.
```

### Rename digital assets

```text
Create a Salsify Digital Asset Renaming formula that uses "SKU", a hyphen, and an alphabetical asset index. Preserve the original file extension.
```

### Troubleshoot a formula

```text
Troubleshoot this Salsify Computed Property formula.
Explain the problem, correct it, preserve its current null behavior, and validate every function used:

PASTE_FORMULA_HERE
```

## A good request includes

- The formula area: Computed Property, Templated Export, Readiness Report, Bulk Edit, or Asset Renaming
- Exact property IDs
- A few example stored values
- The expected output
- What should happen for blank, null, or unmatched values
- Whether the output should be text, a number, a boolean, an array, or a delimited string

Copy this template:

```text
Create a Salsify [FORMULA AREA] formula.

Property IDs:
- [PROPERTY_ID]: [DESCRIPTION OR SAMPLE VALUE]

Rules:
1. [CONDITION] -> [OUTPUT]
2. [CONDITION] -> [OUTPUT]
3. Default -> [OUTPUT]

Blank/null behavior:
- [REQUIRED RESULT]

Example:
- [INPUT] -> [EXPECTED OUTPUT]
```

## What the skill checks

- Function names and argument structure
- Compatibility with the requested Salsify formula area
- Templated Export `SALSIFY_` prefixes
- One-line Templated Export output
- Balanced parentheses and brackets
- Straight quotes instead of smart quotes
- Null and default behavior

The bundled linter performs local syntax and compatibility checks. It does not execute formulas or verify property IDs inside your Salsify organization.

## Documentation

- [Agent Skills specification](https://agentskills.io/specification)
- [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skill documentation](https://code.claude.com/docs/en/skills)

## License

[MIT](LICENSE)
