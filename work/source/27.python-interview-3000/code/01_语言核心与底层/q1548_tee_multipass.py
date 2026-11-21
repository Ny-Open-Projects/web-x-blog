from itertools import tee


def stats_stream(values):
    """单遍产流,三路消费:max、min、count。"""
    s1, s2, s3 = tee(values, 3)
    maximum = max(s1, default=None)
    minimum = min(s2, default=None)
    count = sum(1 for _ in s3)
    return maximum, minimum, count


def lag_demo(values, lag):
    """快分支先跑:落后 lag 个元素的部分滞留缓冲,慢分支仍能看到全量。"""
    fast, slow = tee(values, 2)
    head = list(zip(range(lag), fast))   # fast 先消费 lag 个
    tail = list(slow)                    # slow 从缓冲补齐,一个不少
    return head, len(tail)


if __name__ == "__main__":
    data = [5, 3, 9, 1, 7, 4]
    print("stats:", stats_stream(data))
    print("stats empty:", stats_stream(iter([])))

    head, tail_len = lag_demo(range(10), 3)
    print("fast consumed:", head)
    print("slow still sees all:", tail_len, "items")

    # tee 副本共享底层流:任一副本的 next 都推进同一进度
    a, b = tee(iter([1, 2, 3, 4]), 2)
    print("a first:", next(a))
    print("b first:", next(b), " 从缓冲补齐,不是下一个元素")
    print("a rest  :", list(a), "| b rest:", list(b))
