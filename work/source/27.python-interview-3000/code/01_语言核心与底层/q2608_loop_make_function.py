"""循环内定义函数:MAKE_FUNCTION 的开销与 code 对象共享。"""
import dis
import timeit


def build_in_loop():
    out = []
    for i in range(200):
        def f(i=i):                # 每次迭代 MAKE_FUNCTION 一次
            return i
        out.append(f)
    return out


def build_predef():
    out = []
    def f(i):                      # 只 MAKE_FUNCTION 一次
        return i
    for i in range(200):
        out.append(f)              # 复用同一函数对象
    return out


if __name__ == "__main__":
    fns = build_in_loop()
    print("code 对象共享:", fns[0].__code__ is fns[1].__code__)   # True
    print("函数对象不同:  ", fns[0] is fns[1])                     # False
    print("默认参固化生效:", [f() for f in fns[:3]])               # [0, 1, 2]

    n = 2000
    t_loop = timeit.timeit(build_in_loop, number=n) / n / 200 * 1e9
    t_pre = timeit.timeit(build_predef, number=n) / n / 200 * 1e9
    print(f"循环内定义: {t_loop:.0f} ns/次, 复用外部函数: {t_pre:.0f} ns/次")

    print("\n循环体的字节码:MAKE_FUNCTION 在 FOR_ITER 之内")
    dis.dis(build_in_loop)
