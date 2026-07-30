# Salsify Formula Writer Skill

An Agent Skill for creating, explaining, validating, troubleshooting, and optimizing formulas in the Salsify ProductXM formula language.

The same skill package works with both OpenAI Codex and Anthropic Claude Code because it follows the [Agent Skills open standard](https://agentskills.io/specification): a `SKILL.md` file with bundled references and scripts.

## What it provides

- A catalog of 128 Salsify functions with syntax, examples, and formula-area compatibility.
- Guidance for Computed Properties, Readiness Reports, Templated Exports, In-app Bulk Edits, Salsibot Product Edits, and Digital Asset Renaming.
- Specialized references for common use cases, arrays, variables, time zones, and Templated Export formulas.
- A deterministic formula linter that checks syntax structure, function names, context compatibility, smart quotes, placeholders, and Templated Export prefixes.
- For Templated Exports, both a readable multiline verification formula and an equivalent one-line formula for the Salsify formula box.

The linter performs local lexical checks. It does not execute formulas or validate property IDs against a Salsify organization.

## Repository layout

```text
skill-src/
└── salsify-formula-writer/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    └── scripts/
        └── lint_formula.py
```

Install the entire `skill-src/salsify-formula-writer` directory. The `agents/openai.yaml` file provides optional Codex UI metadata and does not affect Claude Code.

## Installation

Clone the repository:

```bash
git clone https://github.com/imontaine/salsify-formula-skill.git
cd salsify-formula-skill
```

### Codex

Codex discovers personal skills in `~/.agents/skills` and project skills in `.agents/skills`.

Personal installation:

```bash
mkdir -p ~/.agents/skills
cp -R skill-src/salsify-formula-writer ~/.agents/skills/
```

Project installation:

```bash
mkdir -p .agents/skills
cp -R skill-src/salsify-formula-writer .agents/skills/
```

PowerShell personal installation:

```powershell
New-Item -ItemType Directory -Path "$HOME\.agents\skills" -Force
Copy-Item -Recurse -Force "skill-src\salsify-formula-writer" "$HOME\.agents\skills\"
```

Codex detects skill changes automatically. Restart Codex if the skill does not appear.

### Claude Code

Claude Code discovers personal skills in `~/.claude/skills` and project skills in `.claude/skills`.

Personal installation:

```bash
mkdir -p ~/.claude/skills
cp -R skill-src/salsify-formula-writer ~/.claude/skills/
```

Project installation:

```bash
mkdir -p .claude/skills
cp -R skill-src/salsify-formula-writer .claude/skills/
```

PowerShell personal installation:

```powershell
New-Item -ItemType Directory -Path "$HOME\.claude\skills" -Force
Copy-Item -Recurse -Force "skill-src\salsify-formula-writer" "$HOME\.claude\skills\"
```

Claude Code normally detects changes inside an existing skills directory immediately. Restart it if the top-level skills directory was created after the session started.

## Using the skill

State the formula area whenever possible because Salsify function compatibility and syntax can vary by context.

Useful request details include:

- Formula area, such as Computed Property or Templated Export
- Exact property IDs
- Example stored values
- Required output
- Behavior for null, blank, or unmatched values
- Whether the result must be a scalar or an array

### Codex

Invoke it explicitly with `$salsify-formula-writer`:

```text
$salsify-formula-writer Create a Computed Property formula that returns 10 when iq_department is Skincare and 3 otherwise.
```

```text
$salsify-formula-writer Create a Templated Export formula that returns 1 when calc_max_sale_qty is greater than 0 and 0 otherwise.
```

Codex may also activate the skill automatically when a request matches its description.

### Claude Code

Invoke it explicitly with `/salsify-formula-writer`:

```text
/salsify-formula-writer Create a Computed Property formula that returns 10 when iq_department is Skincare and 3 otherwise.
```

```text
/salsify-formula-writer Create a Templated Export formula that returns 1 when calc_max_sale_qty is greater than 0 and 0 otherwise.
```

Claude Code may also activate the skill automatically when a request matches its description.

## General request examples

These prompts work with either client. Add `$salsify-formula-writer` in Codex or `/salsify-formula-writer` in Claude Code when you want to invoke the skill explicitly.

### Simple fallback

```text
Create a Computed Property formula that returns the value of "Brand" when it exists and "Unknown" when it is blank.
```

### Conditional department mapping

```text
Create a Computed Property formula using "iq_department". Return 10 for Skincare, Makeup, Fragrances, Hair Care, Bath & Body, and Tools & Brushes. Return 3 for any other populated department and null when the property is blank.
```

### Readiness check

```text
Create a Readiness Report formula that returns true only when both "Brand" and "Product Title" have values. Return false otherwise.
```

### Join a multi-value property

```text
Create a Templated Export formula that joins every value from "Bullet Points" with a pipe surrounded by spaces: " | ". Include the multiline verification version and the one-line copy version.
```

### Clean and normalize text

```text
Create a Computed Property formula that removes HTML from "Description", trims unnecessary whitespace, and returns null when Description is blank.
```

### Convert measurements

```text
Create a Computed Property formula that converts "Product Length" from inches to centimeters by multiplying by 2.54. Round the result to two decimal places and preserve null when Product Length is blank.
```

### In-app bulk edit

```text
Create an In-app Bulk Edit formula that converts "Brand" to proper case only when Brand has a value. Leave products with no Brand unchanged.
```

### Templated Export threshold

```text
Create a Templated Export formula that returns 1 when "calc_max_sale_qty" is greater than 0 and returns 0 otherwise.
```

### Digital asset renaming

```text
Create a Digital Asset Renaming formula that names each asset using the product's "SKU", a hyphen, and an alphabetical asset index. Preserve the original file extension.
```

### Debug an existing formula

```text
Troubleshoot this Salsify Computed Property formula. Explain the defect, correct it, preserve its current null behavior, and validate every function used:

PASTE_FORMULA_HERE
```

### Explain and document a formula

```text
Explain this Salsify formula line by line. List every function, its purpose, compatible formula areas, expected null behavior, and a sample result:

PASTE_FORMULA_HERE
```

### Optimize a complex formula

```text
Rewrite this Computed Property formula to make it easier to maintain. Use variables when they reduce repetition, preserve the exact output behavior, and explain each change:

PASTE_FORMULA_HERE
```

### Reusable request template

```text
Create a [FORMULA AREA] formula.

Property IDs:
- [PROPERTY_ID]: [DESCRIPTION OR SAMPLE VALUE]

Rules:
1. [FIRST CONDITION AND OUTPUT]
2. [SECOND CONDITION AND OUTPUT]
3. [DEFAULT OR UNMATCHED BEHAVIOR]

Blank/null behavior:
- [DESCRIBE REQUIRED RESULT]

Output:
- [TEXT, NUMBER, BOOLEAN, ARRAY, OR DELIMITED STRING]

Examples:
- [INPUT] -> [EXPECTED OUTPUT]
```

## Templated Export output

Templated Export functions receive the `SALSIFY_` prefix. The skill returns two equivalent forms.

Verification form:

```text
SALSIFY_IF(
  SALSIFY_GT(
    SALSIFY_VALUE("calc_max_sale_qty"),
    "0"
  ),
  "1",
  "0"
)
```

Copy-ready form:

```text
SALSIFY_IF(SALSIFY_GT(SALSIFY_VALUE("calc_max_sale_qty"),"0"),"1","0")
```

## Formula validation

The linter requires Python 3.10 or newer and has no third-party dependencies.

Validate a general formula:

```bash
python skill-src/salsify-formula-writer/scripts/lint_formula.py formula.txt
```

Validate a Templated Export formula:

```bash
python skill-src/salsify-formula-writer/scripts/lint_formula.py --context templated-export formula.txt
```

Require the Templated Export formula to be one line and comment-free:

```bash
python skill-src/salsify-formula-writer/scripts/lint_formula.py --context templated-export --require-one-line formula.txt
```

Supported context values:

- `computed-property`
- `in-app-bulk-edit`
- `salsibot-product-edit`
- `digital-asset-renaming`
- `templated-export`
- `readiness-report`

## Updating the skill

The normalized source references are stored at the repository root. Extraction utilities are in `scripts/`, and the installable package is in `skill-src/salsify-formula-writer`.

After updating formulas or references:

1. Synchronize the changed files into `skill-src/salsify-formula-writer`.
2. Run the formula linter against representative formulas.
3. Validate `skill-src/salsify-formula-writer/SKILL.md` against the Agent Skills specification.
4. Test one in-app formula and one Templated Export formula in the relevant Salsify environment.

## Documentation

- [Agent Skills specification](https://agentskills.io/specification)
- [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code skill documentation](https://code.claude.com/docs/en/skills)

## License

[MIT](LICENSE)
