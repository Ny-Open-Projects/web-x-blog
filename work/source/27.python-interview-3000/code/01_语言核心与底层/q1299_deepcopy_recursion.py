import copy
import sys


def build_nested(depth):
    node = []
    for _ in range(depth):
        node = [node]
    return node


def depth_of(node):
    d = 0
    while isinstance(node, list) and node:
        node = node[0]
        d += 1
    return d


def iterative_copy(root):
    # 针对本结构(每层恰一个孩子, 最内层为空)的迭代重建:从叶子逐层向外
    depth = depth_of(root)
    cur = []
    for _ in range(depth):
        cur = [cur]
    return cur


if __name__ == "__main__":
    print("recursionlimit:", sys.getrecursionlimit())
    shallow = build_nested(300)
    copied = copy.deepcopy(shallow)
    print("deepcopy depth 300 ok:", depth_of(copied) == 300,
          "<- 每层约耗 2 个栈帧, 500 层已贴着默认限制")
    deep = build_nested(5000)
    try:
        copy.deepcopy(deep)
    except RecursionError as e:
        print("depth 5000 ->", type(e).__name__)
    fixed = iterative_copy(deep)
    print("iterative copy depth:", depth_of(fixed))
