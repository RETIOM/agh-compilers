from dataclasses import dataclass, field
from typing import Any

from src.language import Grammar
from src.tokens import Token


@dataclass(slots=True, repr=False)
class Scanner[S, ET]:
    grammar: Grammar[S, Any, ET]

    state: S = field(init=False)

    def __post_init__(self):
        self.state = self.grammar.start_state

    def _reset(self) -> None:
        self.state = self.grammar.start_state

    def _classify_char(self, char: str):
        return self.grammar.categorize(char)

    def _emit_token(self, tokens: list[Token[ET]], value: str, pos: int) -> None:
        token_type = self.grammar.resolve_token_type(self.state, value)
        if token_type is None:
            raise SyntaxError(f"Invalid token: '{value}' at position: {pos + 1}")
        tokens.append(Token(token_type, value))
        self._reset()

    def _advance(self, char: str, category, value: str) -> tuple[bool, str]:
        current_state = self.state
        new_state = self.grammar.transition(current_state, category)
        if new_state is None:
            return False, value

        self.state = new_state
        if self.grammar.should_append(current_state, category):
            value += char
        return True, value

    def _finalize(self, tokens: list[Token[ET]], value: str, pos: int) -> None:
        if not value:
            return
        self._emit_token(tokens, value, pos)

    def scan(self, text: str) -> list[Token[ET]]:
        tokens: list[Token[ET]] = []
        i = 0

        # Used for keeping track of last_accept values(i - beginning of current token)
        while i < len(text):
            self._reset()
            cur_value = ""
            last_accept_state: S | None = None
            last_accept_value = ""
            last_accept_pos = i
            j = i

            # Actual consumption loop(j - end of token)
            while j < len(text):
                char = text[j]
                category = self._classify_char(char)

                if category is None:
                    break

                if self.grammar.should_skip(self.state, category):
                    j += 1
                    i = j
                    continue

                advanced, cur_value = self._advance(char, category, cur_value)
                if not advanced:
                    break

                j += 1
                if self.grammar.get_token_type(self.state) is not None:
                    last_accept_state = self.state
                    last_accept_value = cur_value
                    last_accept_pos = j

            if j >= len(text) and last_accept_state is None:
                break

            if last_accept_state is None:
                offending = text[j] if j < len(text) else "<eof>"
                position = j + 1 if j < len(text) else j
                raise SyntaxError(f"Illegal token: {offending} at position: {position}")

            self.state = last_accept_state
            self._emit_token(tokens, last_accept_value, last_accept_pos - 1)
            i = last_accept_pos

        return tokens
