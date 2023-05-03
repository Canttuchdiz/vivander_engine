from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ChoiceData:
    id: int
    name: str
    text: str


@dataclass
class Node:
    data: ChoiceData
    children: List[Node]

    def find(self, data: ChoiceData, tree: Tree) -> Node:
        if tree.children:
            node = self.traverse(data.id, tree)
            return node

    def traverse(self, choice_id: int, node: Node) -> Node:
        if node.data.id == choice_id:
            return node
        if node.children:
            for child in node.children:
                result = self.traverse(choice_id, child)
                if result:
                    return result


class Tree(Node):
    pass
