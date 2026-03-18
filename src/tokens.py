from dataclasses import dataclass, field


@dataclass(slots=True, frozen=True, repr=False)
class Token[ET]:
    type: ET
    value: str
    attributes: dict = field(default_factory=dict)

    def __repr__(self):
        return f"({self.type}, {self.value})"
