"""名字查找阶梯:局部、闭包、全局、内建的耗时实测。"""
import timeit

N = 200000
x_global = 1234567


def use_local():
    x = x_global                   # 进入局部槽
    total = 0
    for _ in range(N):
        total = x                  # LOAD_FAST
    return total


def use_global():
    total = 0
    for _ in range(N):
        total = x_global           # LOAD_GLOBAL
    return total


def make_closure():
    y = 1234567

    def use_deref():
        total = 0
        for _ in range(N):
            total = y              # LOAD_DEREF
        return total
    return use_deref


def use_builtin():
    total = 0
    for _ in range(N):
        total = len                # LOAD_GLOBAL 未命中,回退 builtins
    return total


if __name__ == "__main__":
    for fn in (use_local, make_closure(), use_global, use_builtin):
        per_iter = timeit.timeit(fn, number=20) / 20 / N * 1e9
        print(f"{fn.__name__:12s} {per_iter:5.0f} ns/次")
