from itertools import groupby
from operator import itemgetter

EVENTS = [
    ("web", 1), ("db", 1), ("web", 2), ("db", 2), ("web", 3),
]


def count_by_key_naive(events):
    """未排序直接分组:web 与 db 被切碎,组数虚高。"""
    return [(k, len(list(g))) for k, g in groupby(events, key=itemgetter(0))]


def count_by_key_sorted(events):
    """先按同一把 key 排序,再分组聚合。"""
    ordered = sorted(events, key=itemgetter(0))
    return {k: sum(1 for _ in g) for k, g in groupby(ordered, key=itemgetter(0))}


def run_length(seq):
    """不排序的合法用法:连续段编码。"""
    return [(k, len(list(g))) for k, g in groupby(seq)]


if __name__ == "__main__":
    print("naive :", count_by_key_naive(EVENTS))
    print("sorted:", count_by_key_sorted(EVENTS))

    print("runs of aabbbc:", run_length("aabbbc"))

    # 分组聚合:按分数段统计(先分箱再分组)
    scores = [88, 92, 79, 61, 55, 73, 95, 67]

    def band(s):
        return "pass" if s >= 60 else "fail"

    ordered = sorted(scores, key=band)
    summary = {}
    for k, g in groupby(ordered, key=band):
        items = list(g)
        summary[k] = {"count": len(items), "min": min(items), "max": max(items)}
    print("bands:", summary)
