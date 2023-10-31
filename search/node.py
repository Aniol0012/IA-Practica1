from __future__ import annotations
from typing import Any, List


class Node():

    def __init__(self, state: Any, action: Any = None, cost: int = 0, parent: Node = None) -> None:
        self.state = state;
        self.action = action;
        self.cost = cost;
        self.parent = parent;

    def get_actions_from_root(self) -> List[Any]:
        """ Get sequence of actions from root to 'self.
        
        Returns:
            Sequence of actions sorted from root to 'self'.
        """
        actions = []

        node = self
        while node.parent:
            actions.append(node.action)
            node = node.parent

        actions.reverse()
        return actions
