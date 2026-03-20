import html
from dataclasses import dataclass

from src.consts import SPAN
from src.language import ColorScheme
from src.tokens import Token


@dataclass(slots=True, frozen=True)
class Colorizer[ET]:
    color_scheme: ColorScheme

    def _color_token(self, token_value: str, color: str):
        return SPAN.format(color=color, token=html.escape(token_value))

    def colorize(self, tokens: list[Token[ET]]) -> str:
        output = ""
        for token in tokens:
            color = self.color_scheme.get_color(token.type)
            if not color:
                color = "#000000"
            output += self._color_token(token.value, color)

        return output
