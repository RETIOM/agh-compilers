from dataclasses import dataclass
from enum import Enum

from src.language import ColorScheme, Grammar


class SimpleProgrammingToken(Enum):
    INVALID = -1
    IDENTIFIER = 1
    NUMBER = 2

    PLUS = 3
    MINUS = 4
    STAR = 5
    SLASH = 6
    PERCENT = 7
    PLUS_PLUS = 8
    MINUS_MINUS = 9

    ASSIGN = 10  # =
    PLUS_EQUALS = 11  # +=
    MINUS_EQUALS = 12  # -=
    STAR_EQUALS = 13  # *=
    SLASH_EQUALS = 14  # /=
    PERCENT_EQUALS = 15  # %=

    DOUBLE_EQUALS = 16  # ==
    NOT_EQUALS = 17  # !=
    LESS_THAN = 18  # <
    GREATER_THAN = 19  # >
    LESS_THAN_EQUALS = 20  # <=
    GREATER_THAN_EQUALS = 21  # >=

    LPAREN = 22
    RPAREN = 23
    LBRACE = 24
    RBRACE = 25
    DOT = 26
    SEMICOLON = 27
    LBRACKET = 31
    RBRACKET = 32

    LOGICAL_NOT = 28  # !
    LOGICAL_AND = 29  # &&
    LOGICAL_OR = 30  # ||
    KEYWORD = 40
    WHITESPACE = 1000
    COMMENT_SINGLE = 1001
    COMMENT_MULTI = 1002


class SimpleProgrammingCategory(Enum):
    INVALID = -1
    ALPHA = 1
    DIGIT = 2
    WHITESPACE = 3

    PLUS = 4
    MINUS = 5
    STAR = 6
    SLASH = 7
    PERCENT = 8
    EQUALS = 9
    LESS_THAN = 10
    GREATER_THAN = 11
    BANG = 12
    AMPERSAND = 13
    PIPE = 14

    LPAREN = 15
    RPAREN = 16
    LBRACE = 17
    RBRACE = 18
    DOT = 19
    SEMICOLON = 20
    NEWLINE = 21

    LBRACKET = 22
    RBRACKET = 23


class SimpleProgrammingState(Enum):
    INVALID = -1
    START = 0
    IDENTIFIER = 1
    NUMBER = 2

    PLUS = 3
    MINUS = 4
    STAR = 5
    SLASH = 6
    PERCENT = 7
    PLUS_PLUS = 8
    MINUS_MINUS = 9

    ASSIGN = 10
    PLUS_EQUALS = 11
    MINUS_EQUALS = 12
    STAR_EQUALS = 13
    SLASH_EQUALS = 14
    PERCENT_EQUALS = 15

    DOUBLE_EQUALS = 16
    NOT_EQUALS = 17
    LESS_THAN = 18
    GREATER_THAN = 19
    LESS_THAN_EQUALS = 20
    GREATER_THAN_EQUALS = 21

    LPAREN = 22
    RPAREN = 23
    LBRACE = 24
    RBRACE = 25
    DOT = 26
    SEMICOLON = 27

    LOGICAL_NOT = 28
    LOGICAL_AND = 29
    LOGICAL_OR = 30

    AMPERSAND = 31
    PIPE = 32

    LBRACKET = 33
    RBRACKET = 34

    WHITESPACE = 1000
    COMMENT_SINGLE = 1001
    COMMENT_MULTI = 1002
    COMMENT_MULTI_STAR = 1003
    COMMENT_MULTI_CLOSED = 1004


KEYWORDS = {
    "if": SimpleProgrammingToken.KEYWORD,
    "else": SimpleProgrammingToken.KEYWORD,
    "while": SimpleProgrammingToken.KEYWORD,
    "return": SimpleProgrammingToken.KEYWORD,
    "elif": SimpleProgrammingToken.KEYWORD,
}


@dataclass(slots=True)
class SimpleProgrammingColorScheme(ColorScheme):
    paren_depth: int = 0
    brace_depth: int = 0
    bracket_depth: int = 0

    RAINBOW_COLORS = (
        "color:#ffd700;",  # 0: Gold
        "color:#da70d6;",  # 1: Pink
        "color:#87cefa;",  # 2: Light blue
    )

    def get_color(self, token: SimpleProgrammingToken) -> str:
        match token:
            case SimpleProgrammingToken.LPAREN:
                color = self.RAINBOW_COLORS[self.paren_depth % len(self.RAINBOW_COLORS)]
                self.paren_depth += 1
                return color

            case SimpleProgrammingToken.RPAREN:
                self.paren_depth = max(0, self.paren_depth - 1)
                return self.RAINBOW_COLORS[self.paren_depth % len(self.RAINBOW_COLORS)]

            case SimpleProgrammingToken.LBRACE:
                color = self.RAINBOW_COLORS[self.brace_depth % len(self.RAINBOW_COLORS)]
                self.brace_depth += 1
                return color

            case SimpleProgrammingToken.RBRACE:
                self.brace_depth = max(0, self.brace_depth - 1)
                return self.RAINBOW_COLORS[self.brace_depth % len(self.RAINBOW_COLORS)]

            case SimpleProgrammingToken.LBRACKET:
                color = self.RAINBOW_COLORS[
                    self.bracket_depth % len(self.RAINBOW_COLORS)
                ]
                self.bracket_depth += 1
                return color

            case SimpleProgrammingToken.RBRACKET:
                self.bracket_depth = max(0, self.bracket_depth - 1)
                return self.RAINBOW_COLORS[
                    self.bracket_depth % len(self.RAINBOW_COLORS)
                ]

            case SimpleProgrammingToken.KEYWORD:
                return "color:#9467bd; font-weight:bold;"
            case SimpleProgrammingToken.IDENTIFIER:
                return "color:#1f77b4;"
            case SimpleProgrammingToken.NUMBER:
                return "color:#d62728;"

            case (
                SimpleProgrammingToken.PLUS
                | SimpleProgrammingToken.MINUS
                | SimpleProgrammingToken.STAR
                | SimpleProgrammingToken.SLASH
                | SimpleProgrammingToken.PERCENT
                | SimpleProgrammingToken.PLUS_PLUS
                | SimpleProgrammingToken.MINUS_MINUS
            ):
                return "color:#2ca02c;"

            case (
                SimpleProgrammingToken.DOUBLE_EQUALS
                | SimpleProgrammingToken.NOT_EQUALS
                | SimpleProgrammingToken.LESS_THAN
                | SimpleProgrammingToken.GREATER_THAN
                | SimpleProgrammingToken.LESS_THAN_EQUALS
                | SimpleProgrammingToken.GREATER_THAN_EQUALS
            ):
                return "color:#e377c2;"

            case (
                SimpleProgrammingToken.ASSIGN
                | SimpleProgrammingToken.PLUS_EQUALS
                | SimpleProgrammingToken.MINUS_EQUALS
                | SimpleProgrammingToken.STAR_EQUALS
                | SimpleProgrammingToken.SLASH_EQUALS
                | SimpleProgrammingToken.PERCENT_EQUALS
            ):
                return "color:#8c564b;"

            case (
                SimpleProgrammingToken.LOGICAL_NOT
                | SimpleProgrammingToken.LOGICAL_AND
                | SimpleProgrammingToken.LOGICAL_OR
            ):
                return "color:#ff7f0e;"

            case SimpleProgrammingToken.DOT | SimpleProgrammingToken.SEMICOLON:
                return "color:#7f7f7f;"
            case (
                SimpleProgrammingToken.COMMENT_SINGLE
                | SimpleProgrammingToken.COMMENT_MULTI
            ):
                return "color:#008000; font-style:italic;"
            case SimpleProgrammingToken.WHITESPACE:
                return ""

            case SimpleProgrammingToken.INVALID:
                return "text-decoration: underline wavy red;"

            case _:
                return "color:#000000;"

    def reset(self) -> None:
        self.paren_depth = 0
        self.brace_depth = 0
        self.bracket_depth


@dataclass(slots=True, frozen=True, init=False)
class SimpleProgrammingGrammar(Grammar):
    @property
    def start_state(self) -> SimpleProgrammingState:
        return SimpleProgrammingState.START

    def get_token_type(
        self, state: SimpleProgrammingState
    ) -> SimpleProgrammingToken | None:
        match state:
            case SimpleProgrammingState.IDENTIFIER:
                return SimpleProgrammingToken.IDENTIFIER
            case SimpleProgrammingState.NUMBER:
                return SimpleProgrammingToken.NUMBER

            case SimpleProgrammingState.PLUS:
                return SimpleProgrammingToken.PLUS
            case SimpleProgrammingState.MINUS:
                return SimpleProgrammingToken.MINUS
            case SimpleProgrammingState.STAR:
                return SimpleProgrammingToken.STAR
            case SimpleProgrammingState.SLASH:
                return SimpleProgrammingToken.SLASH
            case SimpleProgrammingState.PERCENT:
                return SimpleProgrammingToken.PERCENT
            case SimpleProgrammingState.PLUS_PLUS:
                return SimpleProgrammingToken.PLUS_PLUS
            case SimpleProgrammingState.MINUS_MINUS:
                return SimpleProgrammingToken.MINUS_MINUS

            case SimpleProgrammingState.ASSIGN:
                return SimpleProgrammingToken.ASSIGN
            case SimpleProgrammingState.PLUS_EQUALS:
                return SimpleProgrammingToken.PLUS_EQUALS
            case SimpleProgrammingState.MINUS_EQUALS:
                return SimpleProgrammingToken.MINUS_EQUALS
            case SimpleProgrammingState.STAR_EQUALS:
                return SimpleProgrammingToken.STAR_EQUALS
            case SimpleProgrammingState.SLASH_EQUALS:
                return SimpleProgrammingToken.SLASH_EQUALS
            case SimpleProgrammingState.PERCENT_EQUALS:
                return SimpleProgrammingToken.PERCENT_EQUALS

            case SimpleProgrammingState.DOUBLE_EQUALS:
                return SimpleProgrammingToken.DOUBLE_EQUALS
            case SimpleProgrammingState.NOT_EQUALS:
                return SimpleProgrammingToken.NOT_EQUALS
            case SimpleProgrammingState.LESS_THAN:
                return SimpleProgrammingToken.LESS_THAN
            case SimpleProgrammingState.GREATER_THAN:
                return SimpleProgrammingToken.GREATER_THAN
            case SimpleProgrammingState.LESS_THAN_EQUALS:
                return SimpleProgrammingToken.LESS_THAN_EQUALS
            case SimpleProgrammingState.GREATER_THAN_EQUALS:
                return SimpleProgrammingToken.GREATER_THAN_EQUALS

            case SimpleProgrammingState.LPAREN:
                return SimpleProgrammingToken.LPAREN
            case SimpleProgrammingState.RPAREN:
                return SimpleProgrammingToken.RPAREN
            case SimpleProgrammingState.LBRACE:
                return SimpleProgrammingToken.LBRACE
            case SimpleProgrammingState.RBRACE:
                return SimpleProgrammingToken.RBRACE
            case SimpleProgrammingState.LBRACKET:
                return SimpleProgrammingToken.LBRACKET
            case SimpleProgrammingState.RBRACKET:
                return SimpleProgrammingToken.RBRACKET
            case SimpleProgrammingState.DOT:
                return SimpleProgrammingToken.DOT
            case SimpleProgrammingState.SEMICOLON:
                return SimpleProgrammingToken.SEMICOLON

            case SimpleProgrammingState.LOGICAL_NOT:
                return SimpleProgrammingToken.LOGICAL_NOT
            case SimpleProgrammingState.LOGICAL_AND:
                return SimpleProgrammingToken.LOGICAL_AND
            case SimpleProgrammingState.LOGICAL_OR:
                return SimpleProgrammingToken.LOGICAL_OR

            case SimpleProgrammingState.WHITESPACE:
                return SimpleProgrammingToken.WHITESPACE
            case SimpleProgrammingState.COMMENT_SINGLE:
                return SimpleProgrammingToken.COMMENT_SINGLE
            case SimpleProgrammingState.COMMENT_MULTI:
                return SimpleProgrammingToken.COMMENT_MULTI
            case SimpleProgrammingState.COMMENT_MULTI_STAR:
                return SimpleProgrammingToken.COMMENT_MULTI
            case SimpleProgrammingState.COMMENT_MULTI_CLOSED:
                return SimpleProgrammingToken.COMMENT_MULTI

            case SimpleProgrammingState.AMPERSAND:
                return SimpleProgrammingToken.INVALID
            case SimpleProgrammingState.PIPE:
                return SimpleProgrammingToken.INVALID

            case SimpleProgrammingState.INVALID:
                return SimpleProgrammingToken.INVALID
            case _:
                return None

    def resolve_token_type(
        self,
        state: SimpleProgrammingState,
        value: str,
    ) -> SimpleProgrammingToken | None:
        token_type = self.get_token_type(state)
        if token_type == SimpleProgrammingToken.IDENTIFIER:
            return KEYWORDS.get(value, SimpleProgrammingToken.IDENTIFIER)

        return token_type

    def categorize(self, char: str) -> SimpleProgrammingCategory | None:
        if char == "\n":
            return SimpleProgrammingCategory.NEWLINE
        if char.isalpha() or char == "_":
            return SimpleProgrammingCategory.ALPHA
        if char.isdigit():
            return SimpleProgrammingCategory.DIGIT
        if char.isspace():
            return SimpleProgrammingCategory.WHITESPACE
        if char == "+":
            return SimpleProgrammingCategory.PLUS
        if char == "-":
            return SimpleProgrammingCategory.MINUS
        if char == "*":
            return SimpleProgrammingCategory.STAR
        if char == "/":
            return SimpleProgrammingCategory.SLASH
        if char == "%":
            return SimpleProgrammingCategory.PERCENT
        if char == "=":
            return SimpleProgrammingCategory.EQUALS
        if char == "<":
            return SimpleProgrammingCategory.LESS_THAN
        if char == ">":
            return SimpleProgrammingCategory.GREATER_THAN
        if char == "!":
            return SimpleProgrammingCategory.BANG
        if char == "(":
            return SimpleProgrammingCategory.LPAREN
        if char == ")":
            return SimpleProgrammingCategory.RPAREN
        if char == "{":
            return SimpleProgrammingCategory.LBRACE
        if char == "}":
            return SimpleProgrammingCategory.RBRACE
        if char == "[":
            return SimpleProgrammingCategory.LBRACKET
        if char == "]":
            return SimpleProgrammingCategory.RBRACKET
        if char == ".":
            return SimpleProgrammingCategory.DOT
        if char == ";":
            return SimpleProgrammingCategory.SEMICOLON
        if char == "&":
            return SimpleProgrammingCategory.AMPERSAND
        if char == "|":
            return SimpleProgrammingCategory.PIPE
        return SimpleProgrammingCategory.INVALID

    def transition(
        self,
        state: SimpleProgrammingState,
        category: SimpleProgrammingCategory,
    ) -> SimpleProgrammingState | None:
        match state:
            case SimpleProgrammingState.START:
                match category:
                    case SimpleProgrammingCategory.ALPHA:
                        return SimpleProgrammingState.IDENTIFIER
                    case SimpleProgrammingCategory.DIGIT:
                        return SimpleProgrammingState.NUMBER
                    case SimpleProgrammingCategory.WHITESPACE:
                        return SimpleProgrammingState.WHITESPACE
                    case SimpleProgrammingCategory.NEWLINE:
                        return SimpleProgrammingState.WHITESPACE
                    case SimpleProgrammingCategory.PLUS:
                        return SimpleProgrammingState.PLUS
                    case SimpleProgrammingCategory.MINUS:
                        return SimpleProgrammingState.MINUS
                    case SimpleProgrammingCategory.STAR:
                        return SimpleProgrammingState.STAR
                    case SimpleProgrammingCategory.SLASH:
                        return SimpleProgrammingState.SLASH
                    case SimpleProgrammingCategory.PERCENT:
                        return SimpleProgrammingState.PERCENT
                    case SimpleProgrammingCategory.EQUALS:
                        return SimpleProgrammingState.ASSIGN
                    case SimpleProgrammingCategory.LESS_THAN:
                        return SimpleProgrammingState.LESS_THAN
                    case SimpleProgrammingCategory.GREATER_THAN:
                        return SimpleProgrammingState.GREATER_THAN
                    case SimpleProgrammingCategory.BANG:
                        return SimpleProgrammingState.LOGICAL_NOT
                    case SimpleProgrammingCategory.AMPERSAND:
                        return SimpleProgrammingState.AMPERSAND
                    case SimpleProgrammingCategory.PIPE:
                        return SimpleProgrammingState.PIPE
                    case SimpleProgrammingCategory.LPAREN:
                        return SimpleProgrammingState.LPAREN
                    case SimpleProgrammingCategory.RPAREN:
                        return SimpleProgrammingState.RPAREN
                    case SimpleProgrammingCategory.LBRACE:
                        return SimpleProgrammingState.LBRACE
                    case SimpleProgrammingCategory.RBRACE:
                        return SimpleProgrammingState.RBRACE
                    case SimpleProgrammingCategory.LBRACKET:
                        return SimpleProgrammingState.LBRACKET
                    case SimpleProgrammingCategory.RBRACKET:
                        return SimpleProgrammingState.RBRACKET
                    case SimpleProgrammingCategory.DOT:
                        return SimpleProgrammingState.DOT
                    case SimpleProgrammingCategory.SEMICOLON:
                        return SimpleProgrammingState.SEMICOLON
                    case SimpleProgrammingCategory.INVALID:
                        return SimpleProgrammingState.INVALID
                    case _:
                        return None

            case SimpleProgrammingState.IDENTIFIER:
                if category in (
                    SimpleProgrammingCategory.ALPHA,
                    SimpleProgrammingCategory.DIGIT,
                ):
                    return SimpleProgrammingState.IDENTIFIER
                return None

            case SimpleProgrammingState.NUMBER:
                if category == SimpleProgrammingCategory.DIGIT:
                    return SimpleProgrammingState.NUMBER
                return None

            case SimpleProgrammingState.WHITESPACE:
                if category in (
                    SimpleProgrammingCategory.WHITESPACE,
                    SimpleProgrammingCategory.NEWLINE,
                ):
                    return SimpleProgrammingState.WHITESPACE
                return None

            case SimpleProgrammingState.PLUS:
                if category == SimpleProgrammingCategory.PLUS:
                    return SimpleProgrammingState.PLUS_PLUS
                if category == SimpleProgrammingCategory.EQUALS:
                    return SimpleProgrammingState.PLUS_EQUALS
                return None

            case SimpleProgrammingState.MINUS:
                if category == SimpleProgrammingCategory.MINUS:
                    return SimpleProgrammingState.MINUS_MINUS
                if category == SimpleProgrammingCategory.EQUALS:
                    return SimpleProgrammingState.MINUS_EQUALS
                return None

            case SimpleProgrammingState.STAR:
                if category == SimpleProgrammingCategory.EQUALS:
                    return SimpleProgrammingState.STAR_EQUALS
                return None

            case SimpleProgrammingState.SLASH:
                if category == SimpleProgrammingCategory.EQUALS:
                    return SimpleProgrammingState.SLASH_EQUALS
                if category == SimpleProgrammingCategory.SLASH:
                    return SimpleProgrammingState.COMMENT_SINGLE
                if category == SimpleProgrammingCategory.STAR:
                    return SimpleProgrammingState.COMMENT_MULTI
                return None

            case SimpleProgrammingState.COMMENT_SINGLE:
                if category == SimpleProgrammingCategory.NEWLINE:
                    return None
                return SimpleProgrammingState.COMMENT_SINGLE

            case SimpleProgrammingState.COMMENT_MULTI:
                if category == SimpleProgrammingCategory.STAR:
                    return SimpleProgrammingState.COMMENT_MULTI_STAR
                return SimpleProgrammingState.COMMENT_MULTI

            case SimpleProgrammingState.COMMENT_MULTI_STAR:
                if category == SimpleProgrammingCategory.SLASH:
                    return SimpleProgrammingState.COMMENT_MULTI_CLOSED
                if category == SimpleProgrammingCategory.STAR:
                    return SimpleProgrammingState.COMMENT_MULTI_STAR
                return SimpleProgrammingState.COMMENT_MULTI

            case SimpleProgrammingState.COMMENT_MULTI_CLOSED:
                return None

            case SimpleProgrammingState.PERCENT:
                if category == SimpleProgrammingCategory.EQUALS:
                    return SimpleProgrammingState.PERCENT_EQUALS
                return None

            case SimpleProgrammingState.ASSIGN:
                if category == SimpleProgrammingCategory.EQUALS:
                    return SimpleProgrammingState.DOUBLE_EQUALS
                return None

            case SimpleProgrammingState.LESS_THAN:
                if category == SimpleProgrammingCategory.EQUALS:
                    return SimpleProgrammingState.LESS_THAN_EQUALS
                return None

            case SimpleProgrammingState.GREATER_THAN:
                if category == SimpleProgrammingCategory.EQUALS:
                    return SimpleProgrammingState.GREATER_THAN_EQUALS
                return None

            case SimpleProgrammingState.LOGICAL_NOT:
                if category == SimpleProgrammingCategory.EQUALS:
                    return SimpleProgrammingState.NOT_EQUALS
                return None

            case SimpleProgrammingState.AMPERSAND:
                if category == SimpleProgrammingCategory.AMPERSAND:
                    return SimpleProgrammingState.LOGICAL_AND
                return None

            case SimpleProgrammingState.PIPE:
                if category == SimpleProgrammingCategory.PIPE:
                    return SimpleProgrammingState.LOGICAL_OR
                return None

            case _:
                return None

    def should_skip(
        self, state: SimpleProgrammingState, category: SimpleProgrammingCategory
    ) -> bool:
        return False

    def should_append(
        self, state: SimpleProgrammingState, category: SimpleProgrammingCategory
    ) -> bool:
        return True
