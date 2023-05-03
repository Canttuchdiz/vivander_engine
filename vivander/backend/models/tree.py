from vivander.backend.models.node import Node, ChoiceData
from vivander.backend.types.errors import InvalidNodeID
from typing import List

class Tree:
    def __init__(self, root: Node) -> None:
        self.root = root

    def descend_tree(self) -> List[ChoiceData]:
        current_node = self.root
        choices = []
        while current_node.children:
            id_prompt = current_node.request_Input()
            try:
                current_node = self.next_branch(id_prompt, current_node)
                choices.append(current_node.data)
            except AttributeError as e:
                raise InvalidNodeID("ID provided does not match a provided node.")
        return choices

    def next_branch(self, choice_id: int, node: Node) -> Node:
        for child in node.children:
            if child.data.id == choice_id:
                return child
