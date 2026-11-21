"""递归深度控制:限制的真实含义与显式栈转换。"""
import sys


def sum_tree(node):
    """递归版:深链式结构会撞上限。"""
    if node is None:
        return 0
    return node["v"] + sum_tree(node["left"]) + sum_tree(node["right"])


def sum_tree_iter(node):
    """显式栈版:深度只受堆内存限制。"""
    total = 0
    stack = [node]
    while stack:
        cur = stack.pop()
        if cur is None:
            continue
        total += cur["v"]
        stack.append(cur["left"])
        stack.append(cur["right"])
    return total


def make_chain(depth):
    node = None
    for v in range(depth):
        node = {"v": v, "left": None, "right": node}
    return node


if __name__ == "__main__":
    print("当前递归上限:", sys.getrecursionlimit())
    chain = make_chain(1500)
    print("显式栈版处理 1500 深:", sum_tree_iter(chain))
    try:
        sum_tree(chain)
    except RecursionError:
        print("递归版: RecursionError")

    old = sys.getrecursionlimit()
    sys.setrecursionlimit(10000)
    try:
        print("调大上限后递归版:", sum_tree(chain))
    finally:
        sys.setrecursionlimit(old)
