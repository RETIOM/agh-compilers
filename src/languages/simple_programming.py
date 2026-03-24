from dataclasses import dataclass
from enum import Enum

from src.language import ColorScheme, Grammar


class SimpleProgrammingToken(Enum):
    INVALID = -1
    IDENTIFIER = 1  # [_a-zA-Z][_a-zA-Z0-9]\*
    NUMBER = 2  # [0-9]\+
    MATH_OP = 3  # +, -, *, /, %, ++, --
    COMPARE_OP = 4  # ==, !=, <, >, <=, >=
    ASSIGN_OP = 5  # =, +=, -=, *=, /=, %=
    LPAREN = 6  # (
    RPAREN = 7  # )
    LBRACE = 8  # {
    RBRACE = 9  # }
    DOT = 10  # .
    SEMICOLON = 11  # ;
    LOGICAL_OP = 12 # !, &&, ||
    KEYWORD = 20  # Look at the KEYWORDS dict
    WHITESPACE = 1000  # {SPACE} and \n


class SimpleProgrammingCategory(Enum):
    INVALID = -1
    ALPHA = 1
    DIGIT = 2
    MATH = 3  # +, -, *, /, %
    EQUALS = 4  # =
    ANGLE = 5  # <, >
    BANG = 6  # !
    LPAREN = 7
    RPAREN = 8
    LBRACE = 9
    RBRACE = 10
    DOT = 11
    SEMICOLON = 12
    WHITESPACE = 13
    AMPERSAND = 14 # &
    PIPE = 15 # |


class SimpleProgrammingState(Enum):
    INVALID = -1
    START = 0
    IDENTIFIER = 1
    NUMBER = 2
    MATH_OP = 3
    MATH_OP_DOUBLE = 31   
    ASSIGN_OP = 4  
    COMPARE_OP = 5 
    BANG = 6  # !
    LPAREN = 7
    RPAREN = 8
    LBRACE = 9
    RBRACE = 10
    DOT = 11
    SEMICOLON = 12
    WHITESPACE = 30
    AMPERSAND = 14
    PIPE = 15
    LOGICAL_OP = 16
    ANGLE = 17


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

            case SimpleProgrammingToken.KEYWORD:
                return "color:#9467bd; font-weight:bold;"  
            case SimpleProgrammingToken.IDENTIFIER:
                return "color:#1f77b4;" 
            case SimpleProgrammingToken.NUMBER:
                return "color:#d62728;"  

            case SimpleProgrammingToken.MATH_OP:
                return "color:#2ca02c;"  
            case SimpleProgrammingToken.COMPARE_OP:
                return "color:#e377c2;" 
            case SimpleProgrammingToken.ASSIGN_OP:
                return "color:#8c564b;"  
            case SimpleProgrammingToken.LOGICAL_OP: 
                return "color:#ff7f0e;"  

            case SimpleProgrammingToken.DOT | SimpleProgrammingToken.SEMICOLON:
                return "color:#7f7f7f;"  
            case SimpleProgrammingToken.WHITESPACE:
                return "" 

            case SimpleProgrammingToken.INVALID:
                return "text-decoration: underline wavy red;"

            case _:
                return "color:#000000;" 

    def reset(self) -> None:
        self.paren_depth = 0
        self.brace_depth = 0


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
            case SimpleProgrammingState.MATH_OP:
                return SimpleProgrammingToken.MATH_OP
            case SimpleProgrammingState.MATH_OP_DOUBLE:
                return SimpleProgrammingToken.MATH_OP
            case SimpleProgrammingState.COMPARE_OP:
                return SimpleProgrammingToken.COMPARE_OP
            case SimpleProgrammingState.ASSIGN_OP:
                return SimpleProgrammingToken.ASSIGN_OP
            case SimpleProgrammingState.LPAREN:
                return SimpleProgrammingToken.LPAREN
            case SimpleProgrammingState.RPAREN:
                return SimpleProgrammingToken.RPAREN
            case SimpleProgrammingState.LBRACE:
                return SimpleProgrammingToken.LBRACE
            case SimpleProgrammingState.RBRACE:
                return SimpleProgrammingToken.RBRACE
            case SimpleProgrammingState.DOT:
                return SimpleProgrammingToken.DOT
            case SimpleProgrammingState.SEMICOLON:
                return SimpleProgrammingToken.SEMICOLON
            case SimpleProgrammingState.WHITESPACE:
                return SimpleProgrammingToken.WHITESPACE
            case SimpleProgrammingState.BANG:
                return SimpleProgrammingToken.LOGICAL_OP
            case SimpleProgrammingState.LOGICAL_OP:
                return SimpleProgrammingToken.LOGICAL_OP
            case SimpleProgrammingState.AMPERSAND:
                return SimpleProgrammingToken.INVALID
            case SimpleProgrammingState.PIPE:
                return SimpleProgrammingToken.INVALID
            case SimpleProgrammingState.INVALID:
                return SimpleProgrammingToken.INVALID
            case SimpleProgrammingState.ANGLE:
                return SimpleProgrammingToken.COMPARE_OP
            case _:
                return None

    def categorize(self, char: str) -> SimpleProgrammingCategory | None:
        if char.isalpha() or char == '_':
            return SimpleProgrammingCategory.ALPHA
        elif char.isdigit():
            return SimpleProgrammingCategory.DIGIT
        elif char.isspace():
            return SimpleProgrammingCategory.WHITESPACE
        elif char in "+-*/%":
            return SimpleProgrammingCategory.MATH
        elif char == "=":
            return SimpleProgrammingCategory.EQUALS
        elif char in "<>":
            return SimpleProgrammingCategory.ANGLE
        elif char == "!":
            return SimpleProgrammingCategory.BANG
        elif char == "(":
            return SimpleProgrammingCategory.LPAREN
        elif char == ")":
            return SimpleProgrammingCategory.RPAREN
        elif char == "{":
            return SimpleProgrammingCategory.LBRACE
        elif char == "}":
            return SimpleProgrammingCategory.RBRACE
        elif char == ".":
            return SimpleProgrammingCategory.DOT
        elif char == ";":
            return SimpleProgrammingCategory.SEMICOLON
        elif char == "&":
            return SimpleProgrammingCategory.AMPERSAND
        elif char == "|":
            return SimpleProgrammingCategory.PIPE
        else:
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
                    case SimpleProgrammingCategory.MATH:
                        return SimpleProgrammingState.MATH_OP
                    case SimpleProgrammingCategory.EQUALS:
                        return SimpleProgrammingState.ASSIGN_OP
                    case SimpleProgrammingCategory.BANG:
                        return SimpleProgrammingState.BANG
                    case SimpleProgrammingCategory.LPAREN:
                        return SimpleProgrammingState.LPAREN
                    case SimpleProgrammingCategory.RPAREN:
                        return SimpleProgrammingState.RPAREN
                    case SimpleProgrammingCategory.LBRACE:
                        return SimpleProgrammingState.LBRACE
                    case SimpleProgrammingCategory.RBRACE:
                        return SimpleProgrammingState.RBRACE
                    case SimpleProgrammingCategory.DOT:
                        return SimpleProgrammingState.DOT
                    case SimpleProgrammingCategory.SEMICOLON:
                        return SimpleProgrammingState.SEMICOLON
                    case SimpleProgrammingCategory.INVALID:
                        return SimpleProgrammingState.INVALID
                    case SimpleProgrammingCategory.AMPERSAND:
                        return SimpleProgrammingState.AMPERSAND
                    case SimpleProgrammingCategory.PIPE:
                        return SimpleProgrammingState.PIPE
                    case SimpleProgrammingCategory.ANGLE:
                        return SimpleProgrammingState.ANGLE
                    case _:
                        return None

            case SimpleProgrammingState.IDENTIFIER:
                match category:
                    case (
                        SimpleProgrammingCategory.ALPHA
                        | SimpleProgrammingCategory.DIGIT
                    ):
                        return SimpleProgrammingState.IDENTIFIER
                    case _:
                        return None

            case SimpleProgrammingState.NUMBER:
                match category:
                    case SimpleProgrammingCategory.DIGIT:
                        return SimpleProgrammingState.NUMBER
                    case _:
                        return None

            case SimpleProgrammingState.WHITESPACE:
                match category:
                    case SimpleProgrammingCategory.WHITESPACE:
                        return SimpleProgrammingState.WHITESPACE
                    case _:
                        return None

            case SimpleProgrammingState.ASSIGN_OP:
                match category:
                    case SimpleProgrammingCategory.EQUALS:
                        return (
                            SimpleProgrammingState.COMPARE_OP
                        )  
                    case _:
                        return None

            case SimpleProgrammingState.COMPARE_OP:
                return None

            case SimpleProgrammingState.BANG:
                match category:
                    case SimpleProgrammingCategory.EQUALS:
                        return (
                            SimpleProgrammingState.COMPARE_OP
                        ) 
                    case _:
                        return None

            case SimpleProgrammingState.MATH_OP:
                match category:
                    case SimpleProgrammingCategory.EQUALS:
                        return SimpleProgrammingState.ASSIGN_OP  
                    case SimpleProgrammingCategory.MATH:
                        return (
                            SimpleProgrammingState.MATH_OP_DOUBLE
                        ) 
                    case _:
                        return None

            case SimpleProgrammingState.MATH_OP_DOUBLE:
                return None
            
            case SimpleProgrammingState.AMPERSAND:
                match category:
                    case SimpleProgrammingCategory.AMPERSAND:
                        return SimpleProgrammingState.LOGICAL_OP
                    case _:
                        return None
                        
            case SimpleProgrammingState.PIPE:
                match category:
                    case SimpleProgrammingCategory.PIPE:
                        return SimpleProgrammingState.LOGICAL_OP
                    case _:
                        return None
                    
            case SimpleProgrammingState.ANGLE:
                match category:
                    case SimpleProgrammingCategory.EQUALS:
                        return SimpleProgrammingState.COMPARE_OP 
                    case _:
                        return None

            case SimpleProgrammingState.LOGICAL_OP:
                return None 

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

        if token_type == SimpleProgrammingToken.MATH_OP and len(value) == 2:
            if value not in ("++", "--"):
                return SimpleProgrammingToken.INVALID

        return token_type

    def should_skip(
        self, state: SimpleProgrammingState, category: SimpleProgrammingCategory
    ) -> bool:
        return False

    def should_append(
        self, state: SimpleProgrammingState, category: SimpleProgrammingCategory
    ) -> bool:
        return True
