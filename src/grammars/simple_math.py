from enum import Enum

from src.grammar import Grammar


class SimpleMathToken(Enum):
    IDENTIFIER = 1  # [a-zA-Z][a-zA-Z0-9]*
    NUMBER = 2  # [0-9]+
    PLUS = 3  # \+
    MINUS = 4  # \-
    MULTIPLY = 5  # \*
    DIVIDE = 6  # \/
    LPAREN = 7  # \(
    RPAREN = 8  # \)


class SimpleMathCategory(Enum):
    ALPHA = 1
    DIGIT = 2
    PLUS = 3
    MINUS = 4
    MULTIPLY = 5
    DIVIDE = 6
    LPAREN = 7
    RPAREN = 8
    WHITESPACE = 9


class SimpleMathState(Enum):
    START = 0
    IDENTIFIER = 1
    NUMBER = 2
    PLUS = 3
    MINUS = 4
    MULTIPLY = 5
    DIVIDE = 6
    LPAREN = 7
    RPAREN = 8


class SimpleMathGrammar(Grammar):
    @property
    def start_state(self) -> SimpleMathState:
        return SimpleMathState.START

    def get_token_type(self, state: SimpleMathState) -> SimpleMathToken | None:
        match state:
            case SimpleMathState.IDENTIFIER:
                return SimpleMathToken.IDENTIFIER
            case SimpleMathState.NUMBER:
                return SimpleMathToken.NUMBER
            case SimpleMathState.PLUS:
                return SimpleMathToken.PLUS
            case SimpleMathState.MINUS:
                return SimpleMathToken.MINUS
            case SimpleMathState.MULTIPLY:
                return SimpleMathToken.MULTIPLY
            case SimpleMathState.DIVIDE:
                return SimpleMathToken.DIVIDE
            case SimpleMathState.LPAREN:
                return SimpleMathToken.LPAREN
            case SimpleMathState.RPAREN:
                return SimpleMathToken.RPAREN
            case _:
                return None

    def categorize(self, char: str) -> SimpleMathCategory | None:
        if char.isdigit():
            return SimpleMathCategory.DIGIT
        elif char.isalpha():
            return SimpleMathCategory.ALPHA
        elif char.isspace():
            return SimpleMathCategory.WHITESPACE
        elif char == "+":
            return SimpleMathCategory.PLUS
        elif char == "-":
            return SimpleMathCategory.MINUS
        elif char == "*":
            return SimpleMathCategory.MULTIPLY
        elif char == "/":
            return SimpleMathCategory.DIVIDE
        elif char == "(":
            return SimpleMathCategory.LPAREN
        elif char == ")":
            return SimpleMathCategory.RPAREN
        else:
            return None

    def transition(
        self, state: SimpleMathState, category: SimpleMathCategory
    ) -> SimpleMathState | None:
        match state:
            case SimpleMathState.START:
                match category:
                    case SimpleMathCategory.ALPHA:
                        return SimpleMathState.IDENTIFIER
                    case SimpleMathCategory.DIGIT:
                        return SimpleMathState.NUMBER
                    case SimpleMathCategory.PLUS:
                        return SimpleMathState.PLUS
                    case SimpleMathCategory.MINUS:
                        return SimpleMathState.MINUS
                    case SimpleMathCategory.MULTIPLY:
                        return SimpleMathState.MULTIPLY
                    case SimpleMathCategory.DIVIDE:
                        return SimpleMathState.DIVIDE
                    case SimpleMathCategory.LPAREN:
                        return SimpleMathState.LPAREN
                    case SimpleMathCategory.RPAREN:
                        return SimpleMathState.RPAREN
                    case _:
                        return None
            case SimpleMathState.IDENTIFIER:
                match category:
                    case SimpleMathCategory.ALPHA | SimpleMathCategory.DIGIT:
                        return SimpleMathState.IDENTIFIER
                    case _:
                        return None
            case SimpleMathState.NUMBER:
                match category:
                    case SimpleMathCategory.DIGIT:
                        return SimpleMathState.NUMBER
                    case _:
                        return None
            case _:
                return None

    def should_skip(self, state: SimpleMathState, category: SimpleMathCategory) -> bool:
        if category == SimpleMathCategory.WHITESPACE:
            return True
        else:
            return False

    def should_append(
        self, state: SimpleMathState, category: SimpleMathCategory
    ) -> bool:
        return True
