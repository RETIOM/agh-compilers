# TODO:
# Implement the colorizer
# For now it shall return an HTML with colors from the languages color_scheme
from dataclasses import dataclass

from src.language import ColorScheme
from src.tokens import Token


@dataclass(slots=True, frozen=True)
class Colorizer[ET]:
    color_scheme: ColorScheme

    def colorize(self, tokens: list[Token[ET]]) -> str:
        return ""
