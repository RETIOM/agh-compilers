from enum import Enum
from dataclasses import dataclass, field


class SimpleMathToken(Enum):
    IDENTIFIER = 1  # [a-zA-Z][a-zA-Z0-9]*
    NUMBER = 2  # [0-9]+
    PLUS = 3  # \+
    MINUS = 4  # \-
    MULTIPLY = 5  # \*
    DIVIDE = 6  # \/
    LPAREN = 7  # \(
    RPAREN = 8  # \)


@dataclass(slots=True, frozen=True, repr=False)
class Token[ET]:
    type: ET
    value: str
    attributes: dict = field(default_factory=dict)

    def __repr__(self):
        return f"({self.type}, {self.value})"
