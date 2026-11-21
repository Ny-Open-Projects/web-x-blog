import sys
from collections import deque
from itertools import islice, tee


def pairwise(iterable):
    """3.9 兼容实现,3.10+ 可直接用 itertools.pairwise。"""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def sliding_window(iterable, width):
    it = iter(iterable)
    window = deque(islice(it, width), maxlen=width)
    if len(window) == width:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def deltas(seq):
    return [b - a for a, b in pairwise(seq)]


if __name__ == "__main__":
    if sys.version_info >= (3, 10):
        from itertools import pairwise as std_pairwise
        print("stdlib pairwise:", list(std_pairwise([1, 2, 3, 4])))
    else:
        print("python", sys.version_info[:3], "uses the recipe above")

    print("pairwise:", list(pairwise([1, 2, 3, 4])))
    print("deltas  :", deltas([10, 12, 9, 15, 15]))

    print("window 3:", list(sliding_window(range(5), 3)))
    print("window 1:", list(sliding_window("abc", 1)))

    # 相邻重复检测:监控指标连续相等要合并
    readings = [42, 42, 42, 43, 43, 44]
    repeats = sorted({a for a, b in pairwise(readings) if a == b})
    print("consecutive equal:", repeats)
