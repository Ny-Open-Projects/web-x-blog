"""迭代期间的字典变更限制:改值可以,改大小不行。"""


def safe_delete_snapshot(prices):
    deleted = []
    for key in list(prices):       # 先物化键快照再删
        if prices[key] <= 0:
            deleted.append(key)
            del prices[key]
    return deleted


def safe_delete_deferred(prices):
    doomed = [k for k, v in prices.items() if v <= 0]
    for k in doomed:               # 收集完再统一删
        del prices[k]
    return doomed


if __name__ == "__main__":
    prices = {"a": 10, "b": 0, "c": 5, "d": -1}
    try:
        for k in prices:
            if prices[k] <= 0:
                del prices[k]      # 迭代中改变大小
    except RuntimeError as e:
        print("迭代中删键:", e)

    prices = {"a": 10, "b": 0, "c": 5, "d": -1}
    for k in prices:
        prices[k] = 99             # 只覆盖值,大小不变
    print("迭代中改值:允许 ->", prices)

    p1 = {"a": 10, "b": 0, "c": 5, "d": -1}
    print("快照法:", safe_delete_snapshot(p1), "->", p1)
    p2 = {"a": 10, "b": 0, "c": 5, "d": -1}
    print("两步法:", safe_delete_deferred(p2), "->", p2)
