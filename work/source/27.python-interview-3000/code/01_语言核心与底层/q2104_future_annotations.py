"""from __future__ import annotations:注解延迟求值的收益与坑。"""
from __future__ import annotations

import typing


class Node:
    """自引用注解无需引号:注解只是字符串,定义时不求值。"""
    next_node: Node = None         # 没有该 import 时,这行必须写 "Node"

    def __init__(self, value):
        self.value = value
        self.next_node = None


def scale(x: int, factor: int = 2) -> int:
    return x * factor


if __name__ == "__main__":
    a, b = Node(1), Node(2)
    a.next_node = b
    print("自引用链:", a.next_node.value)

    print("类属性注解按 def 时为字符串:", Node.__annotations__)
    print("函数注解同样延迟:", scale.__annotations__)
    print("get_type_hints 显式解析:", typing.get_type_hints(scale))
    print("收益是前向引用免引号;代价是运行期读注解必须走 get_type_hints")
