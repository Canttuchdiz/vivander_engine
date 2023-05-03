from __future__ import annotations
from dataclasses import dataclass
from vivander.backend.types.data import ChoiceData
from typing import List

@dataclass
class Node:
    data: ChoiceData
    children: List[Node]

    def request_Input(self) -> int:
        ids = [str(child.data.id) for child in self.children]
        request = int(input(f"Choices {ids}\nEnter an id: "))
        return request