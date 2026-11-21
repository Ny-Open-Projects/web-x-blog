"""留存曲线两种口径:N 日留存(精确窗口)与滚动留存(累计回访即算)"""

try:
    import pandas as pd
except ImportError:
    pd = None

ACTIVE = {
    # user -> 活跃日偏移列表,0 为新增日
    "u1": [0, 1, 2, 3, 7],
    "u2": [0, 1, 3],
    "u3": [0, 7],
    "u4": [0, 1, 2],
    "u5": [0],
}


def nday_retention(offsets, day):
    """N 日留存:恰好第 N 天活跃 / 新增,窗口最严,同业对比用它"""
    new_users = [u for u, d in offsets.items() if 0 in d]
    hit = [u for u, d in offsets.items() if day in d]
    return len(hit) / len(new_users)


def rolling_retention(offsets, day):
    """滚动留存:第 N 天及以后任意一天回访都算,衡量粘性下限"""
    new_users = [u for u, d in offsets.items() if 0 in d]
    hit = [u for u, d in offsets.items() if any(x >= day for x in d)]
    return len(hit) / len(new_users)


if pd is None:
    print("天数   N日留存   滚动留存")
    for day in (1, 3, 7):
        print(f"{day:>3}   {nday_retention(ACTIVE, day):>8.0%}   {rolling_retention(ACTIVE, day):>7.0%}")
    print("要点:滚动留存恒 >= N 日留存;两口径差异大说明回访分散,报数必须标口径,跨团队对比前先对口径")
else:
    rows = [(u, d) for u, ds in ACTIVE.items() for d in ds]
    df = pd.DataFrame(rows, columns=["user", "day"])
    new_cnt = df[df["day"] == 0]["user"].nunique()
    for day in (1, 3, 7):
        nday = df[df["day"] == day]["user"].nunique() / new_cnt
        rolling = df[df["day"] >= day]["user"].nunique() / new_cnt
        print(f"day {day}: N日留存 {nday:.0%}, 滚动留存 {rolling:.0%}")
