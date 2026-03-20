import argparse

from src.colorizer import Colorizer
from src.consts import HTML_BODY
from src.language import Language
from src.languages.simple_math import SimpleMathColorScheme, SimpleMathGrammar
from src.scanner import Scanner


def parse_args():
    parser = argparse.ArgumentParser(description="A simple scanner")
    parser.add_argument("text", type=str, help="Scanner input")
    parser.add_argument(
        "-g",
        "--grammar",
        type=str,
        required=False,
        choices=["SimpleMath"],
        default="SimpleMath",
    )
    return parser.parse_args()


def build_language(grammar_type: str) -> Language | None:
    match grammar_type:
        case "SimpleMath":
            grammar = SimpleMathGrammar()
            color_scheme = SimpleMathColorScheme()
            language = Language(grammar=grammar, color_scheme=color_scheme)
            return language
        case _:
            return None


def main():
    args = parse_args()
    language = build_language(args.grammar)
    if language is None:
        raise ValueError("Language can't be None!")

    scanner = Scanner(language.grammar)
    colorizer = Colorizer(language.color_scheme)

    out = scanner.scan(args.text)
    html = colorizer.colorize(out)

    with open("index.html", "w") as f:
        f.write(
            HTML_BODY.format(title=language.color_scheme.__class__.__name__, body=html)
        )

    for token in out:
        print(token)


if __name__ == "__main__":
    main()
