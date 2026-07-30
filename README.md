# Salsify Formula Writer

Create Salsify formulas by describing the business rule in plain language.

If you can explain the rule as an Excel formula - for example, "If Category is R/C Cars, return Y; otherwise return N" - you can use this skill. You do not need to know Salsify's formula syntax.

The skill works with Claude Code and OpenAI Codex.

## Install the skill

Ask Claude Code or Codex to install the skill globally from this repository. You only need to do this once.

### Claude Code

Paste this request into Claude Code:

```text
Install the salsify-formula-writer skill globally from this GitHub repository:
https://github.com/imontaine/salsify-formula-skill

The skill folder is:
skill-src/salsify-formula-writer
```

### Codex

Paste this request into Codex:

```text
$skill-installer Install the salsify-formula-writer skill globally from this GitHub repository:
https://github.com/imontaine/salsify-formula-skill

The skill folder is:
skill-src/salsify-formula-writer
```

## Ask for a formula

In Claude Code, begin your request with:

```text
/salsify-formula-writer
```

In Codex, begin your request with:

```text
$salsify-formula-writer
```

Then describe the rule as you would explain it to a coworker:

```text
/salsify-formula-writer Create a Computed Property formula.
If Brand is blank, return "Unknown". Otherwise, return Brand.
```

The full Claude command is `/salsify-formula-writer`, not `/salsify`. You can also ask naturally for a Salsify formula, but using the command makes the request explicit.

## Tell the skill where the formula will be used

This is the most important detail. The same business rule is written differently depending on where the formula goes.

| Where it will be used | What that means |
| --- | --- |
| Computed Property | A calculated field inside Salsify, similar to a calculated column in Excel. |
| Templated Export | A formula that fills a field in a retailer or customer export template. |
| Readiness Report | A check that shows whether product content is complete or ready. |
| In-app Bulk Edit | A formula used to update many products inside Salsify. |
| Digital Asset Renaming | A formula used to create delivery names for images and other assets. |

Salsify also refers to a calculated property as a **Computed Property**. Either phrase is fine.

## Computed Property vs. Templated Export

Here is one business rule used in two different places:

> For "Batteries Included?", return Y when Category is R/C Cars. Return N for every other category. Leave the result blank when Category is blank.

### Ask for a Computed Property

```text
/salsify-formula-writer Create a Computed Property formula for "Batteries Included?".

Use the "Category" property.
- If Category is "R/C Cars", return "Y".
- For every other category, return "N".
- If Category is blank, return null.
```

The skill returns a formula like this:

```text
IF(
  VALUE("Category"),
  IF(EQUAL(VALUE("Category"), "R/C Cars"), "Y", "N"),
  null
)
```

### Ask for a Templated Export

```text
/salsify-formula-writer Create a Templated Export formula for "Batteries Included?".

Use the "Category" property.
- If Category is "R/C Cars", return "Y".
- For every other category, return "N".
- If Category is blank, return null.

Give me a readable multiline version to review and a one-line version to paste into Salsify.
```

The skill first gives you a readable version:

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

It also gives you the one-line version required by the Templated Export formula box:

```text
SALSIFY_IF(SALSIFY_VALUE("Category"),SALSIFY_IF(SALSIFY_EQUAL(SALSIFY_VALUE("Category"),"R/C Cars"),"Y","N"),null)
```

You do not need to remember the `SALSIFY_` wording. The skill adds it when you say the formula is for a Templated Export.

## More examples

These examples are based on common Salsify formula use cases. Copy one and replace the property names or business rules with your own.

### Use a backup value when the first field is blank

```text
$salsify-formula-writer Create a Computed Property formula.
Use the first field that has a value: Brand, Manufacturer, or Supplier Name.
If all three are blank, return "Unknown".
```

### Add leading zeros to a UPC

```text
$salsify-formula-writer Create a Computed Property formula.
Add leading zeros to UPC until it is 12 characters long.
If UPC is blank, leave the result blank.
```

### Format a date for a retailer

```text
$salsify-formula-writer Create a Templated Export formula.
Format Launch Date as MM/DD/YYYY.
If Launch Date is blank, leave the result blank.
Give me the readable version and the one-line copy version.
```

### Convert inches to centimeters

```text
$salsify-formula-writer Create a Computed Property formula.
Convert Product Length from inches to centimeters by multiplying it by 2.54.
Round the result to two decimal places.
If Product Length is blank, leave the result blank.
```

### Check whether required content is complete

```text
$salsify-formula-writer Create a Readiness Report formula.
Return true when both Brand and Product Title have values.
Return false when either one is blank.
```

### Combine bullet points into one export field

```text
$salsify-formula-writer Create a Templated Export formula.
Combine all values from Bullet Points into one field.
Put " | " between each bullet point.
Give me the readable version and the one-line copy version.
```

### Clean up a product name

```text
$salsify-formula-writer Create a Computed Property formula.
Remove special characters from Product Name.
Keep letters, numbers, spaces, and hyphens.
If Product Name is blank, leave the result blank.
```

### Troubleshoot an existing formula

```text
$salsify-formula-writer Troubleshoot this Computed Property formula.
Explain the problem in plain language, correct it, and keep the same blank-value behavior:

PASTE FORMULA HERE
```

## A simple request template

You do not need to use technical terms. Include these five things when you can:

1. Where the formula will be used.
2. The Salsify property names.
3. The business rule.
4. What should happen when a value is blank.
5. One or two examples of the expected result.

Copy this template:

```text
Create a Salsify [Computed Property / Templated Export / Readiness Report] formula.

Use these properties:
- [PROPERTY NAME]
- [PROPERTY NAME]

Business rule:
- If [CONDITION], return [RESULT].
- Otherwise, return [RESULT].

When a value is blank:
- [LEAVE BLANK / USE A DEFAULT VALUE / OTHER RULE]

Examples:
- [EXAMPLE INPUT] should return [EXPECTED RESULT].
```

## What the skill handles for you

- Chooses the correct Salsify functions for the business rule.
- Checks that each function can be used in the requested formula area.
- Handles blank values and default values.
- Adds the required `SALSIFY_` wording for Templated Exports.
- Provides both a readable formula and a one-line copy formula for Templated Exports.
- Explains complicated formulas in plain language.
- Checks common problems such as missing parentheses or incorrect quotation marks.

The skill checks the formula against its included Salsify documentation. It cannot see your Salsify organization, so make sure the property names match your organization and preview the result in Salsify before using it for a production export.

## License

[MIT](LICENSE)
