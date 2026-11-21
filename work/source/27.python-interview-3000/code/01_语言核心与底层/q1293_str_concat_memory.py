import sys
import time
import tracemalloc


def run_concat(parts, keep_alias=False):
    tracemalloc.start()
    s = ""
    alias = s if keep_alias else None   # 别名破坏就地扩容条件
    for p in parts:
        s += p
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    assert alias is not None or not keep_alias
    return peak


def run_join(parts):
    tracemalloc.start()
    s = "".join(parts)
    peak = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    return s, peak


if __name__ == "__main__":
    parts = ["chunk%06d" % i for i in range(20000)]
    t0 = time.perf_counter()
    p1 = run_concat(parts)
    t1 = time.perf_counter()
    p2 = run_concat(parts, keep_alias=True)
    t2 = time.perf_counter()
    s, p3 = run_join(parts)
    t3 = time.perf_counter()
    print("+= unique  peak %.2f MB  %.1f ms" % (p1 / 1e6, (t1 - t0) * 1000))
    print("+= alias   peak %.2f MB  %.1f ms" % (p2 / 1e6, (t2 - t1) * 1000))
    print("join       peak %.2f MB  %.1f ms" % (p3 / 1e6, (t3 - t2) * 1000))
    print("result getsizeof:", sys.getsizeof(s))
