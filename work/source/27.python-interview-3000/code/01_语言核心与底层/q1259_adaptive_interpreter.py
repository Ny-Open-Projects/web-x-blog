import dis
import sys
import timeit


def hot(a, b):
    return a * b + 1


if __name__ == "__main__":
    print("python:", sys.version.split()[0])
    if sys.version_info >= (3, 11):
        for _ in range(200):          # 让计数器超阈值,触发 quickening
            hot(2, 3)
        print("3.11+ 特化后可见 BINARY_OP __mul__ 等专化形态:")
        dis.dis(hot, show_caches=False)
    else:
        ops = [i.opname for i in dis.get_instructions(hot)]
        print("当前版本无 PEP 659,始终通用执行,opnames:", ops)
    n = 200000
    print("call x%d: %.1f ms" % (n, timeit.timeit(lambda: hot(3, 4), number=n) * 1000))
