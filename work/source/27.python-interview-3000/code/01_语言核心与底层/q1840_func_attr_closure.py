"""函数属性 vs 闭包变量:持久状态的两种载体实测。"""
import timeit


def make_with_attr():
    def counter():
        counter.n += 1          # 状态挂在函数对象上,全局名查找
        return counter.n
    counter.n = 0               # 外部可见、可重置、可内省
    return counter


def make_with_closure():
    n = 0

    def counter():
        nonlocal n              # 状态藏在 cell,快速局部访问
        n += 1
        return n
    return counter


def bench(fn, number=100000):
    return round(timeit.timeit(fn, number=number), 4)


if __name__ == "__main__":
    a, b = make_with_attr(), make_with_closure()
    print("attr 递增:", a(), a(), a())
    print("closure 递增:", b(), b(), b())
    a.n = 0                     # 函数属性:外部可直接重置
    print("重置 attr 后:", a())
    print("闭包状态不可直视:", not hasattr(b, "n"))
    print("attr 版耗时:", bench(a), "| closure 版耗时:", bench(b))
