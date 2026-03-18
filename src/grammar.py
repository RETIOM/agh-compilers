from abc import ABC, abstractmethod


class Grammar[S, C, ET](ABC):
    @property
    @abstractmethod
    def start_state(self) -> S: ...

    @abstractmethod
    def categorize(self, char: str) -> C | None: ...

    @abstractmethod
    def should_skip(self, state: S, category: C) -> bool: ...

    @abstractmethod
    def should_append(self, state: S, category: C) -> bool: ...

    @abstractmethod
    def transition(self, state: S, category: C) -> S | None: ...

    @abstractmethod
    def get_token_type(self, state: S) -> ET | None: ...
