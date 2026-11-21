from __future__ import annotations

from typing import Generic, List, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.children: List[Node[T]] = []   # 自引用:延迟求值

    def add(self, child: Node[T]) -> Node[T]:
        self.children.append(child)
        return child


def total(node: Node[int]) -> int:
    return node.value + sum(total(c) for c in node.children)


if __name__ == "__main__":
    root = Node(1)
    a = root.add(Node(2))
    root.add(Node(3))
    a.add(Node(4))
    print("sum:", total(root))
    print("isinstance 到参数化类是不允许的:", isinstance(root, Node))
