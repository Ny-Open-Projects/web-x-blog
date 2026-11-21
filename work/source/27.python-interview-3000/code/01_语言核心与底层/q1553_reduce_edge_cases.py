import math
from functools import reduce


def compose(*funcs):
    """函数组合:reduce 真正的舒适区——非交换合并。"""
    return lambda x: reduce(lambda acc, f: f(acc), reversed(funcs), x)


if __name__ == "__main__":
    print("sum via reduce :", reduce(lambda a, b: a + b, [1, 2, 3, 4]))
    print("with initial   :", reduce(lambda a, b: a + b, [], 100))

    try:
        reduce(lambda a, b: a + b, [])
    except TypeError as err:
        print("empty no init  :", err)

    print("product        :", reduce(lambda a, b: a * b, [2, 3, 4], 1))
    print("wrong identity :", reduce(lambda a, b: a * b, [2, 3, 4], 0))

    process = compose(str.strip, str.title, lambda s: s.replace(" ", "_"))
    print("composed:", process("  hello world  "))

    # 嵌套 dict 构建:非交换,顺序敏感
    path = ("config", "db", "host")
    nested = reduce(lambda acc, key: {key: acc}, reversed(path), "localhost")
    print("nested:", nested)

    # 有名字的特化优先:sum、math.prod、''.join、any、all
    print("math.prod:", math.prod([2, 3, 4]))
