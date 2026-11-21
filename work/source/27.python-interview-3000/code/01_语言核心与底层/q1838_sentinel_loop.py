"""哨兵循环实测:for、while True 与 iter 双参的性价比。"""
import timeit

N = 20000


def make_stream():
    it = iter(range(N))
    return lambda: next(it, None)     # 耗尽后永远返回 None 作为哨兵


def by_for():
    for v in range(N):
        pass
    return "done"


def by_iter_sentinel():
    stream = make_stream()
    for v in iter(stream, None):      # 双参 iter:每轮调 stream,等于 None 即停
        pass
    return "done"


def by_while_true():
    stream = make_stream()
    while True:
        if stream() is None:
            break
    return "done"


def bench(fn, number=100):
    return round(min(timeit.repeat(fn, number=number, repeat=3)), 4)


if __name__ == "__main__":
    for name, fn in [("for", by_for),
                     ("iter 双参", by_iter_sentinel),
                     ("while True + is None", by_while_true)]:
        print(name, ":", bench(fn), "s / 100 x 20000 次")
