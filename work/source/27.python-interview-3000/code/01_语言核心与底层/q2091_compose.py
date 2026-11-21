"""函数组合:compose 与 pipeline 的极简实现。"""


def compose(*funcs):
    """从右向左:compose(f, g)(x) == f(g(x))。"""
    def composed(value):
        for func in reversed(funcs):
            value = func(value)
        return value
    return composed


def pipeline(*funcs):
    """从左向右:pipeline(f, g)(x) == g(f(x))。"""
    def piped(value):
        for func in funcs:
            value = func(value)
        return value
    return piped


def squash(s):
    return "-".join(s.split())


if __name__ == "__main__":
    clean = pipeline(str.strip, str.lower, squash)
    print("pipeline:", clean("  Hello  World  "))
    print("compose 同链:", compose(squash, str.lower, str.strip)("  Hello  World  "))

    import functools
    via_reduce = functools.reduce(lambda acc, f: f(acc), [str.strip, str.lower, squash],
                                  "  Hi  There  ")
    print("reduce 等价实现:", via_reduce)
