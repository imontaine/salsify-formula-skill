"""Perform lexical checks on a Salsify ProductXM formula.

This does not execute formulas or validate them against a Salsify organization.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


SMART_QUOTES = {
    "\u2018": "left single quotation mark",
    "\u2019": "right single quotation mark",
    "\u201c": "left double quotation mark",
    "\u201d": "right double quotation mark",
}
LEGACY_OR_UNDOCUMENTED = {"CONCAT", "LEFT", "RIGHT"}
HEADING_RE = re.compile(r"^### ([A-Z][A-Z0-9_.]*)(?: .*)?$", re.MULTILINE)
CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")
ARRAY_MATCHER_IF_RE = re.compile(
    r"\b(?:SALSIFY_)?IF\s*\(\s*(?:SALSIFY_)?(MATCHES|REGEX_MATCHES)\s*\(",
    re.IGNORECASE,
)
SALSIFY_PREFIX = "SALSIFY_"
CONTEXTS = {
    "computed-property": "Computed Property Formulas",
    "in-app-bulk-edit": "In-app Bulk Edit Formulas",
    "salsibot-product-edit": "Salsibot Product Edit via Formulas",
    "digital-asset-renaming": "Digital Asset Renaming Formulas",
    "templated-export": "Templated Export Formulas",
    "readiness-report": "Readiness Report Formulas",
}


def load_functions(reference: Path) -> dict[str, tuple[str, set[str]]]:
    text = reference.read_text(encoding="utf-8")
    matches = list(HEADING_RE.finditer(text))
    functions: dict[str, tuple[str, set[str]]] = {}
    for index, match in enumerate(matches):
        name = match.group(1)
        if name == "LET...IN":
            continue
        section_end = (
            matches[index + 1].start() if index + 1 < len(matches) else len(text)
        )
        section = text[match.end() : section_end]
        compatible_match = re.search(
            r"^\*\*Compatible with:\*\*\s*(.+)$", section, re.MULTILINE
        )
        compatible = (
            {
                item.strip()
                for item in compatible_match.group(1).split(";")
                if item.strip() and item.strip() != "None"
            }
            if compatible_match
            else set()
        )
        functions[name.upper()] = (name, compatible)
    return functions


def mask_strings_and_comments(formula: str) -> tuple[str, list[str]]:
    masked = list(formula)
    errors: list[str] = []
    quote: str | None = None
    escaped = False
    index = 0

    while index < len(formula):
        char = formula[index]
        if quote:
            masked[index] = " "
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
            index += 1
            continue

        if char in {"'", '"'}:
            quote = char
            masked[index] = " "
            index += 1
            continue

        if char == "#":
            while index < len(formula) and formula[index] not in "\r\n":
                masked[index] = " "
                index += 1
            continue

        index += 1

    if quote:
        errors.append(f"Unclosed {quote} string literal.")
    return "".join(masked), errors


def contains_comment(formula: str) -> bool:
    quote: str | None = None
    escaped = False
    for char in formula:
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
        elif char in {"'", '"'}:
            quote = char
        elif char == "#":
            return True
    return False


def delimiter_errors(masked: str) -> list[str]:
    errors: list[str] = []
    stack: list[tuple[str, int]] = []
    pairs = {")": "(", "]": "["}
    for index, char in enumerate(masked):
        if char in {"(", "["}:
            stack.append((char, index))
        elif char in pairs:
            if not stack or stack[-1][0] != pairs[char]:
                errors.append(f"Unexpected {char!r} at character {index + 1}.")
            else:
                stack.pop()
    for char, index in stack:
        errors.append(f"Unclosed {char!r} opened at character {index + 1}.")
    return errors


def lint(
    formula: str,
    reference: Path,
    context: str | None = None,
    require_one_line: bool = False,
) -> tuple[list[str], list[str]]:
    documented = load_functions(reference)
    errors: list[str] = []
    warnings: list[str] = []
    context_label = CONTEXTS.get(context) if context else None

    if require_one_line:
        formula_body = formula.rstrip("\r\n")
        if "\n" in formula_body or "\r" in formula_body:
            errors.append("Copy-ready formula must be exactly one line.")
        if contains_comment(formula):
            errors.append("Copy-ready one-line formula must not contain comments.")

    for quote, label in SMART_QUOTES.items():
        if quote in formula:
            errors.append(f"Replace {label} {quote!r} with a straight ASCII quote.")

    masked, string_errors = mask_strings_and_comments(formula)
    errors.extend(string_errors)
    errors.extend(delimiter_errors(masked))

    if re.search(r"\{\{[^{}]+\}\}", formula):
        warnings.append("Formula contains unresolved {{placeholders}}.")

    direct_matcher_tests = {
        match.group(1).upper() for match in ARRAY_MATCHER_IF_RE.finditer(masked)
    }
    for matcher in sorted(direct_matcher_tests):
        warnings.append(
            f"{matcher} returns an array when used directly as an IF test and can "
            "repeat the true output once per match. Scalarize it first, for example "
            f'IF(JOIN({matcher}(...),""),"result").'
        )

    seen_calls: set[str] = set()
    for match in CALL_RE.finditer(masked):
        called = match.group(1)
        upper = called.upper()
        if upper in seen_calls:
            continue
        seen_calls.add(upper)
        prefixed = upper.startswith(SALSIFY_PREFIX)
        base_upper = upper[len(SALSIFY_PREFIX) :] if prefixed else upper
        if base_upper in documented:
            canonical, compatible = documented[base_upper]
            expected_call = f"{SALSIFY_PREFIX}{canonical}" if prefixed else canonical
            if called != expected_call:
                warnings.append(
                    f"Use canonical function casing {expected_call} instead of {called}."
                )
            if context == "templated-export" and not prefixed:
                errors.append(
                    f"Templated Export function {called} must use the "
                    f"{SALSIFY_PREFIX} prefix: {SALSIFY_PREFIX}{canonical}."
                )
            elif context and context != "templated-export" and prefixed:
                warnings.append(
                    f"{called} uses the Templated Export {SALSIFY_PREFIX} prefix "
                    f"in the {context_label} context."
                )
            if context_label and compatible and context_label not in compatible:
                errors.append(
                    f"{expected_call} is not compatible with {context_label}."
                )
        elif base_upper in LEGACY_OR_UNDOCUMENTED | {"EQUALS"}:
            display_name = f"{SALSIFY_PREFIX}{base_upper}" if prefixed else base_upper
            warnings.append(
                f"{display_name} appears in older Salsify articles but has no "
                "standalone entry in the June 2026 function reference."
            )
        else:
            warnings.append(
                f"Unknown function call {called}; confirm it in the current "
                "Salsify formula editor."
            )

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "formula_file",
        nargs="?",
        type=Path,
        help="UTF-8 formula file. Reads stdin when omitted.",
    )
    parser.add_argument(
        "--reference",
        type=Path,
        default=Path(__file__).resolve().parent.parent
        / "references"
        / "salsify-functions.md",
    )
    parser.add_argument(
        "--context",
        choices=sorted(CONTEXTS),
        help=(
            "Formula area. Enables compatibility checks and enforces SALSIFY_ "
            "prefixes for templated-export."
        ),
    )
    parser.add_argument(
        "--require-one-line",
        action="store_true",
        help="Reject line breaks and comments in a copy-ready formula.",
    )
    args = parser.parse_args()

    formula = (
        args.formula_file.read_text(encoding="utf-8")
        if args.formula_file
        else sys.stdin.read()
    )
    if not formula.strip():
        print("ERROR: No formula provided.")
        return 1

    errors, warnings = lint(
        formula, args.reference, args.context, args.require_one_line
    )
    for message in errors:
        print(f"ERROR: {message}")
    for message in warnings:
        print(f"WARNING: {message}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s).")
        return 1
    print(f"PASS: 0 errors, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
