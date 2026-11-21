import sys
from functools import lru_cache


class TreeNode:
    def __init__(self, value, children=()):
        self.value = value
        self.children = list(children)


def sum_recursive(node):
    return node.value + sum(sum_recursive(c) for c in node.children)


def sum_iterative(root):
    """显式栈:把递归调用换成待处理栈,深度不再受递归限制。"""
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        total += node.value
        stack.extend(node.children)
    return total


def deep_chain(depth):
    node = TreeNode(0)
    for i in range(1, depth):
        node = TreeNode(i, (node,))
    return node


@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    tree = TreeNode(1, (TreeNode(2, (TreeNode(3),)), TreeNode(4)))
    print("sum recursive:", sum_recursive(tree))
    print("sum iterative:", sum_iterative(tree))

    depth = 5000
    deep = deep_chain(depth)
    print("iterative deep chain:", sum_iterative(deep))
    limit = sys.getrecursionlimit()
    try:
        sys.setrecursionlimit(200)
        try:
            sum_recursive(deep)
            print("recursive: unexpectedly survived")
        except RecursionError:
            print("recursive: RecursionError as expected at low limit")
    finally:
        sys.setrecursionlimit(limit)

    print("fib(60) memo:", fib(60))
    a, b = 0, 1                    # 状态对推进:斐波那契根本不需要栈
    for _ in range(60):
        a, b = b, a + b
    print("fib(60) pair :", a)
