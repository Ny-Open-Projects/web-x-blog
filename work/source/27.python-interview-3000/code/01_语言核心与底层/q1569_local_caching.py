import timeit

EVENTS = [("click", 1), ("view", 2), ("click", 3)] * 50


class Collector:
    def __init__(self):
        self.bucket = []


def process_naive(col):
    out = []
    for ev in EVENTS:
        col.bucket.append(ev)          # 每次都走 LOAD_ATTR 与方法查找
    return out


def process_hoisted(col):
    out = []
    bucket = col.bucket                # 属性提升为局部
    append = out.append                # 绑定方法提升
    for ev in EVENTS:
        append(bucket, ev) if False else append((ev, bucket is col.bucket))
    return out


if __name__ == "__main__":
    a, b = Collector(), Collector()
    process_naive(a)
    process_hoisted(b)
    print("equivalent:", a.bucket == b.bucket)

    n = 300
    t_naive = timeit.timeit(lambda: process_naive(Collector()), number=n)
    t_hoist = timeit.timeit(lambda: process_hoisted(Collector()), number=n)
    print("naive  :", round(t_naive * 1000 / n, 3), "ms per run")
    print("hoisted:", round(t_hoist * 1000 / n, 3), "ms per run")

    # 全局查找 vs 局部:循环里反复调用全局函数
    global_fn = abs
    values = [-1, 2, -3, 4] * 25

    def use_global():
        total = 0
        for v in values:
            total += global_fn(v)
        return total

    def use_local():
        fn = global_fn
        total = 0
        for v in values:
            total += fn(v)
        return total

    print("results equal:", use_global() == use_local())
    t_g = timeit.timeit(use_global, number=2000)
    t_l = timeit.timeit(use_local, number=2000)
    print("global vs local lookup:", round(t_g * 1e6 / 2000, 2), "us vs",
          round(t_l * 1e6 / 2000, 2), "us")
