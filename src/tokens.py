from dataclasses import dataclass


@dataclass(slots=True, frozen=True, repr=False)
class Token[ET]:
    type: ET
    value: str
    attributes: dict | None = None

    def __repr__(self):
        if not self.attributes:
            return f"({self.type}, {self.value})"
        else:
            return f"({self.type}, {self.value}, {self.attributes})"
