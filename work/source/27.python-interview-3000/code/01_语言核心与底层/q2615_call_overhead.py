"""调用开销:Python 层函数与 C 内建函数的每次调用成本。"""
import timeit


def py_id(v):
    return v                       # 一个什么都不做的 Python 函数


if __name__ == "__main__":
    n = 500000
    t_py = timeit.timeit(lambda: py_id(7), number=n) / n * 1e9
    t_bi = timeit.timeit(lambda: abs(-7), number=n) / n * 1e9
    print(f"Python 层调用: {t_py:5.0f} ns/次")
    print(f"C 内建调用:   {t_bi:5.0f} ns/次")
    print(f"差距:          +{(t_py - t_bi) / t_bi * 100:.0f}%")
