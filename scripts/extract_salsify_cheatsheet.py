"""Extract Salsify formula documentation from a saved cheat-sheet HTML fragment."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


WRAPPER_RE = re.compile(
    r'<div\b[^>]*class="wrapper"[^>]*data-idshort="(?P<slug>[^"]+)"[^>]*>',
    re.IGNORECASE,
)
TITLE_RE = re.compile(
    r'<span\b[^>]*class="slds-accordion__summary-content"[^>]*title="([^"]+)"',
    re.IGNORECASE,
)
DESCRIPTION_RE = re.compile(
    r'<div\b[^>]*class="accordion-info-box article-description-box"[^>]*>'
    r"(.*?)</div>",
    re.IGNORECASE | re.DOTALL,
)
COMPATIBILITY_RE = re.compile(
    r'<div\b[^>]*class="accordion-info-box compatibity-box"[^>]*>'
    r"(.*?)</ul>",
    re.IGNORECASE | re.DOTALL,
)
COMPATIBILITY_ITEM_RE = re.compile(
    r'<li\b[^>]*class="(compatible-with|not-compatible-with)"[^>]*>'
    r"(.*?)</li>",
    re.IGNORECASE | re.DOTALL,
)
SYNTAX_RE = re.compile(
    r'class="syntax-usage-header"[^>]*>.*?</div>\s*'
    r"<code\b[^>]*>(.*?)</code>",
    re.IGNORECASE | re.DOTALL,
)
PRE_RE = re.compile(r"<pre\b[^>]*>(.*?)</pre>", re.IGNORECASE | re.DOTALL)
OUTPUT_RE = re.compile(
    r"<strong\b[^>]*>\s*Output(?:\s+[^:<]*)?:?\s*</strong>(.*?)(?=</p>)",
    re.IGNORECASE | re.DOTALL,
)
BUTTON_RE = re.compile(r"<button\b.*?</button>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>", re.DOTALL)
BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)


def repair_mojibake(value: str) -> str:
    """Repair common UTF-8-as-Windows-1252 artifacts without changing clean text."""
    if not any(marker in value for marker in ("Ã", "â", "Â", "ð")):
        return value
    try:
        repaired = value.encode("cp1252").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return value
    old_markers = sum(value.count(marker) for marker in ("Ã", "â", "Â", "ð"))
    new_markers = sum(repaired.count(marker) for marker in ("Ã", "â", "Â", "ð"))
    return repaired if new_markers < old_markers else value


def clean_inline(fragment: str) -> str:
    fragment = BUTTON_RE.sub("", fragment)
    fragment = BR_RE.sub("\n", fragment)
    fragment = TAG_RE.sub("", fragment)
    value = html.unescape(fragment).replace("\xa0", " ")
    value = repair_mojibake(value)
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r" *\n *", "\n", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def clean_code(fragment: str) -> str:
    fragment = BUTTON_RE.sub("", fragment)
    fragment = BR_RE.sub("\n", fragment)
    fragment = TAG_RE.sub("", fragment)
    value = html.unescape(fragment).replace("\xa0", " ")
    value = repair_mojibake(value)
    lines = [line.rstrip() for line in value.replace("\r\n", "\n").split("\n")]
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return "\n".join(lines).strip()


def fence_for(code: str) -> str:
    longest = max((len(match.group(0)) for match in re.finditer(r"`+", code)), default=0)
    return "`" * max(3, longest + 1)


def parse_entries(source: str) -> list[dict[str, object]]:
    matches = list(WRAPPER_RE.finditer(source))
    entries: list[dict[str, object]] = []

    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
        section = source[match.start() : end]

        title_match = TITLE_RE.search(section)
        if not title_match:
            raise ValueError(f"Missing title for entry slug {match.group('slug')!r}")

        description_match = DESCRIPTION_RE.search(section)
        compatibility_match = COMPATIBILITY_RE.search(section)
        syntax_match = SYNTAX_RE.search(section)
        formulas = [clean_code(block) for block in PRE_RE.findall(section)]
        formulas = [formula for formula in formulas if formula]
        outputs = [clean_inline(block) for block in OUTPUT_RE.findall(section)]
        outputs = [output for output in outputs if output]
        compatible_with: list[str] = []
        not_compatible_with: list[str] = []
        if compatibility_match:
            for status, body in COMPATIBILITY_ITEM_RE.findall(
                compatibility_match.group(1)
            ):
                destination = (
                    compatible_with
                    if status.lower() == "compatible-with"
                    else not_compatible_with
                )
                destination.append(clean_inline(body))

        entries.append(
            {
                "name": html.unescape(title_match.group(1)).strip(),
                "slug": match.group("slug"),
                "description": (
                    clean_inline(description_match.group(1)) if description_match else ""
                ),
                "compatible_with": compatible_with,
                "not_compatible_with": not_compatible_with,
                "syntax": clean_code(syntax_match.group(1)) if syntax_match else "",
                "formulas": formulas,
                "outputs": outputs,
            }
        )

    return entries


def render_markdown(entries: list[dict[str, object]]) -> str:
    callable_count = sum(entry["name"] != "LET...IN" for entry in entries)
    lines = [
        "# Salsify Formula Function Reference",
        "",
        "Source: Salsify “Formulas Cheat Sheet”",
        "Source last modified: June 3, 2026",
        "Extracted: July 30, 2026",
        "",
        "## Summary",
        "",
        f"- {len(entries)} documented formula-language entries",
        f"- {callable_count} callable functions",
        "- 1 language construct: `LET...IN`",
        "",
        (
            "Names, syntax, descriptions, example formulas, and outputs below were "
            "extracted from the Salsify source page. Property IDs and sample values "
            "are Salsify’s examples."
        ),
        "",
        "## Quick index",
        "",
    ]

    for entry in entries:
        anchor = re.sub(r"[^a-z0-9]+", "-", str(entry["name"]).lower()).strip("-")
        lines.append(f"- [`{entry['name']}`](#{anchor})")

    lines.extend(["", "## Function details", ""])

    for entry in entries:
        name = str(entry["name"])
        description = str(entry["description"])
        compatible_with = list(entry["compatible_with"])
        not_compatible_with = list(entry["not_compatible_with"])
        syntax = str(entry["syntax"])
        formulas = list(entry["formulas"])
        outputs = list(entry["outputs"])

        heading_suffix = " (language construct)" if name == "LET...IN" else ""
        lines.extend([f"### {name}{heading_suffix}", ""])

        lines.extend(
            [
                "**Compatible with:** "
                + ("; ".join(compatible_with) if compatible_with else "None"),
                "",
                "**Not compatible with:** "
                + (
                    "; ".join(not_compatible_with)
                    if not_compatible_with
                    else "None"
                ),
                "",
            ]
        )

        if description:
            lines.extend([description, ""])

        if syntax:
            fence = fence_for(syntax)
            lines.extend(["**Syntax**", "", f"{fence}text", syntax, fence, ""])

        if formulas:
            for formula_index, formula in enumerate(formulas):
                label = (
                    "**Official example**"
                    if len(formulas) == 1
                    else f"**Official example {formula_index + 1}**"
                )
                fence = fence_for(formula)
                lines.extend([label, "", f"{fence}text", formula, fence, ""])
                if formula_index < len(outputs):
                    lines.extend(
                        ["**Output**", "", f"`{outputs[formula_index]}`", ""]
                    )

            if len(outputs) > len(formulas):
                lines.extend(["**Additional documented outputs**", ""])
                for output in outputs[len(formulas) :]:
                    lines.append(f"- `{output}`")
                lines.append("")
        elif outputs:
            lines.extend(["**Documented outputs**", ""])
            for output in outputs:
                lines.append(f"- `{output}`")
            lines.append("")
        else:
            lines.extend(
                [
                    "_The extracted Salsify entry does not include an example formula._",
                    "",
                ]
            )

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    source = args.source.read_text(encoding="utf-8")
    entries = parse_entries(source)
    if len(entries) != 128:
        raise ValueError(f"Expected 128 entries, found {len(entries)}")

    names = [str(entry["name"]) for entry in entries]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate function titles found")
    incomplete_compatibility = [
        str(entry["name"])
        for entry in entries
        if len(entry["compatible_with"]) + len(entry["not_compatible_with"]) < 6
    ]
    if incomplete_compatibility:
        raise ValueError(
            "Incomplete compatibility metadata for: "
            + ", ".join(incomplete_compatibility)
        )

    args.output.write_text(render_markdown(entries), encoding="utf-8")
    example_count = sum(len(list(entry["formulas"])) for entry in entries)
    output_count = sum(len(list(entry["outputs"])) for entry in entries)
    print(
        f"Wrote {len(entries)} entries with {example_count} example formulas "
        f"and {output_count} documented outputs to {args.output}"
    )


if __name__ == "__main__":
    main()
