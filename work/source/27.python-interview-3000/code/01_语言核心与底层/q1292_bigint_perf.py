import sys
import time


def bench(label, fn, repeat=3):
    best = min(_time_once(fn) for _ in range(repeat))
    print("%-24s %8.2f ms" % (label, best * 1000))


def _time_once(fn):
    t0 = time.perf_counter()
    fn()
    return time.perf_counter() - t0


if __name__ == "__main__":
    a = (1 << 100000) - 1               # 10 万位二进制
    b = (1 << 50000) - 1
    bench("square 100k-bit", lambda: a * a)
    bench("square 50k-bit ", lambda: b * b)
    bench("add 100k-bit   ", lambda: a + a)
    bench("modpow 2^1e8   ", lambda: pow(2, 10 ** 8, 1000000007))
    print("bit_length:", a.bit_length())
    if hasattr(sys, "get_int_max_str_digits"):
        print("int<->str digit limit:", sys.get_int_max_str_digits())
    else:
        print("no int<->str limit before 3.11")
