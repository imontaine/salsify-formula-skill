"""Convert Salsify's Common Formula Use Cases HTML fragment to Markdown."""

from __future__ import annotations

import argparse
import html
import re
from html.parser import HTMLParser
from pathlib import Path


TITLE_RE = re.compile(
    r'<span\b[^>]*class="slds-accordion__summary-content"[^>]*title="([^"]+)"',
    re.IGNORECASE,
)


def repair_mojibake(value: str) -> str:
    if not any(marker in value for marker in ("Ã", "â", "Â", "ð")):
        return value
    try:
        repaired = value.encode("cp1252").decode("utf-8")
    except (UnicodeEncodeError, UnicodeDecodeError):
        return value
    old_score = sum(value.count(marker) for marker in ("Ã", "â", "Â", "ð"))
    new_score = sum(repaired.count(marker) for marker in ("Ã", "â", "Â", "ð"))
    return repaired if new_score < old_score else value


def clean_text(value: str) -> str:
    value = repair_mojibake(html.unescape(value)).replace("\xa0", " ")
    value = value.replace("\r\n", "\n")
    value = re.sub(r"[ \t]+\n", "\n", value)
    value = re.sub(r"\n[ \t]+", "\n", value)
    value = re.sub(r"[ \t]{2,}", " ", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


class MarkdownConverter(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.suppressed_depth = 0
        self.in_pre = False
        self.in_code = False
        self.list_stack: list[tuple[str, int]] = []
        self.link_stack: list[str | None] = []

    def add(self, text: str) -> None:
        if self.suppressed_depth == 0:
            self.parts.append(text)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag in {"svg", "script", "style", "button", "img"}:
            self.suppressed_depth += 1
            return
        if self.suppressed_depth:
            return

        if tag == "pre":
            self.add("\n\n```text\n")
            self.in_pre = True
        elif tag == "code" and not self.in_pre:
            self.add("`")
            self.in_code = True
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            source_level = int(tag[1])
            level = min(6, source_level + 1)
            self.add("\n\n" + ("#" * level) + " ")
        elif tag == "p":
            self.add("\n\n")
        elif tag == "br":
            self.add("\n")
        elif tag in {"ul", "ol"}:
            start = int(attributes.get("start") or 1)
            self.list_stack.append((tag, start))
            self.add("\n")
        elif tag == "li":
            depth = max(0, len(self.list_stack) - 1)
            indent = "  " * depth
            if self.list_stack and self.list_stack[-1][0] == "ol":
                kind, number = self.list_stack[-1]
                self.list_stack[-1] = (kind, number + 1)
                marker = f"{number}."
            else:
                marker = "-"
            self.add(f"\n{indent}{marker} ")
        elif tag == "strong":
            self.add("**")
        elif tag == "em":
            self.add("*")
        elif tag == "a":
            href = attributes.get("href")
            self.link_stack.append(href)
            if href and not self.in_pre and not self.in_code:
                self.add("[")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"svg", "script", "style", "button", "img"}:
            if self.suppressed_depth:
                self.suppressed_depth -= 1
            return
        if self.suppressed_depth:
            return

        if tag == "pre":
            self.add("\n```\n")
            self.in_pre = False
        elif tag == "code" and not self.in_pre and self.in_code:
            self.add("`")
            self.in_code = False
        elif tag in {"p", "h1", "h2", "h3", "h4", "h5", "h6"}:
            self.add("\n")
        elif tag in {"ul", "ol"}:
            if self.list_stack:
                self.list_stack.pop()
            self.add("\n")
        elif tag == "strong":
            self.add("**")
        elif tag == "em":
            self.add("*")
        elif tag == "a":
            href = self.link_stack.pop() if self.link_stack else None
            if href and not self.in_pre and not self.in_code:
                self.add(f"]({href})")

    def handle_data(self, data: str) -> None:
        if self.suppressed_depth:
            return
        if self.in_pre:
            self.add(data)
        else:
            self.add(re.sub(r"\s+", " ", data))

    def markdown(self) -> str:
        value = clean_text("".join(self.parts))
        value = re.sub(r"\n +", "\n", value)
        value = re.sub(r" +\n", "\n", value)
        value = re.sub(r"\n{3,}", "\n\n", value)
        return value.strip()


def load_function_names(reference_path: Path) -> list[str]:
    source = reference_path.read_text(encoding="utf-8")
    return re.findall(r"^### ([A-Z][A-Z0-9_.]*)(?: .*)?$", source, re.MULTILINE)


def function_anchor(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def used_functions(section_html: str, function_names: list[str]) -> list[str]:
    found: list[str] = []
    for name in function_names:
        pattern = rf"(?<![A-Z0-9_]){re.escape(name)}\s*\("
        if re.search(pattern, section_html, re.IGNORECASE):
            found.append(name)
    return found


def parse_sections(source: str) -> list[tuple[str, str]]:
    matches = list(TITLE_RE.finditer(source))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
        title = repair_mojibake(html.unescape(match.group(1))).strip()
        sections.append((title, source[match.end() : end]))
    return sections


def render(
    sections: list[tuple[str, str]], function_names: list[str]
) -> tuple[str, int]:
    lines = [
        "# Salsify Common Formula Use Cases",
        "",
        "Source: Salsify “Common Formula Use Cases — Examples & Explanations”",
        "Source last modified: April 27, 2026",
        "Extracted: July 30, 2026",
        "",
        "This guide preserves Salsify’s documented explanations and formulas. "
        "Function links point to the companion function reference.",
        "",
        "## Quick index",
        "",
    ]
    for title, _ in sections:
        anchor = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
        lines.append(f"- [{title}](#{anchor})")

    formula_blocks = 0
    lines.extend(["", "## Use cases", ""])
    for title, section_html in sections:
        converter = MarkdownConverter()
        converter.feed(section_html)
        body = converter.markdown()
        functions = used_functions(section_html, function_names)
        formula_blocks += len(re.findall(r"<pre\b", section_html, re.IGNORECASE))

        lines.extend([f"## {title}", ""])
        if functions:
            links = [
                f"[`{name}`](salsify-functions.md#{function_anchor(name)})"
                for name in functions
            ]
            lines.extend(["**Functions used:** " + ", ".join(links), ""])
        lines.extend([body, ""])

    return "\n".join(lines).rstrip() + "\n", formula_blocks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("function_reference", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    source = args.source.read_text(encoding="utf-8")
    sections = parse_sections(source)
    if len(sections) != 23:
        raise ValueError(f"Expected 23 use cases, found {len(sections)}")

    function_names = load_function_names(args.function_reference)
    markdown, formula_blocks = render(sections, function_names)
    args.output.write_text(markdown, encoding="utf-8")
    print(
        f"Wrote {len(sections)} use cases with {formula_blocks} formula blocks "
        f"to {args.output}"
    )


if __name__ == "__main__":
    main()
