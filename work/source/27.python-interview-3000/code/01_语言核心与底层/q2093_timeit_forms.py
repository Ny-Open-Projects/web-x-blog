"""timeit 的两种喂法:statement 字符串与 callable 的开销差异。"""
import timeit


def target(n=1000):
    return sum(range(n))


ENV = {"target": target}


if __name__ == "__main__":
    n = 2000
    t_stmt = timeit.timeit("target()", globals=ENV, number=n)
    t_call = timeit.timeit(lambda: target(), number=n)
    print("字符串语句形式:", round(t_stmt, 4), "秒")
    print("callable 形式(多一层 lambda):", round(t_call, 4), "秒")
    print("差额是系统性包装开销:", round(t_call - t_stmt, 4), "秒")

    t_const = timeit.timeit("1 + 2", number=500000)
    t_names = timeit.timeit("a + b", setup="a, b = 1, 2", number=500000)
    print("常量折叠的假快:", round(t_const, 5), "| 变量加法真实成本:", round(t_names, 5))

    best = min(timeit.repeat("target()", globals=ENV, number=500, repeat=5))
    print("repeat 取最小值更抗干扰:", round(best, 4), "秒")
