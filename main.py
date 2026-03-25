import argparse
import sys
from pathlib import Path

from src.colorizer import Colorizer
from src.consts import HTML_BODY
from src.language import ColorScheme, Grammar, Language
from src.languages.simple_math import SimpleMathColorScheme, SimpleMathGrammar
from src.languages.simple_programming import (
    SimpleProgrammingColorScheme,
    SimpleProgrammingGrammar,
)
from src.scanner import Scanner


def parse_args():
    parser = argparse.ArgumentParser(description="A simple scanner")
    group_input = parser.add_mutually_exclusive_group(required=True)
    group_input.add_argument("text", type=str, nargs="?", help="Scanner input")
    group_input.add_argument(
        "-f", "--file", type=Path, help="Path to the file with input"
    )
    parser.add_argument(
        "-g",
        "--grammar",
        type=str,
        required=False,
        choices=["SimpleMath", "SimpleProgramming"],
        default="SimpleMath",
    )
    return parser.parse_args()


def build_language(grammar_type: str) -> Language | None:
    grammar: Grammar
    color_scheme: ColorScheme
    match grammar_type:
        case "SimpleMath":
            grammar = SimpleMathGrammar()
            color_scheme = SimpleMathColorScheme()
        case "SimpleProgramming":
            grammar = SimpleProgrammingGrammar()
            color_scheme = SimpleProgrammingColorScheme()
        case _:
            return None

    language = Language(grammar=grammar, color_scheme=color_scheme)
    return language


def main():
    args = parse_args()
    language = build_language(args.grammar)
    if language is None:
        raise ValueError("Language can't be None!")

    scanner = Scanner(language.grammar)
    colorizer = Colorizer(language.color_scheme)

    if args.file is not None:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                scanner_input = f.read()
        except FileNotFoundError:
            print(f"File not found: '{args.file}'")
            sys.exit(1)
    else:
        scanner_input = args.text
    out = scanner.scan(scanner_input)
    html = colorizer.colorize(out)

    with open("index.html", "w") as f:
        f.write(
            HTML_BODY.format(title=language.color_scheme.__class__.__name__, body=html)
        )

    for token in out:
        print(token)


if __name__ == "__main__":
    main()
