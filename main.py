import argparse
from src.grammar import Grammar
from src.grammars.simple_math import SimpleMathGrammar
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


def build_grammar(grammar_type: str) -> Grammar | None:
    match grammar_type:
        case "SimpleMath":
            return SimpleMathGrammar()
        case _:
            return None


def main():
    args = parse_args()
    grammar = build_grammar(args.grammar)
    if grammar is None:
        raise ValueError(f"Grammar can't be None!") 
    scanner = Scanner(grammar)

    out = scanner.scan(args.text)

    for token in out:
        print(token)


if __name__ == "__main__":
    main()
