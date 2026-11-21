"""复购周期:订单间隔分布、中位复购天数与 30 天复购率"""

from datetime import date

ORDERS = {
    "u1": [date(2025, 8, 1), date(2025, 8, 6), date(2025, 8, 20)],
    "u2": [date(2025, 8, 3), date(2025, 8, 25)],
    "u3": [date(2025, 8, 5)],
    "u4": [date(2025, 8, 2), date(2025, 8, 9), date(2025, 8, 12)],
    "u5": [date(2025, 8, 8), date(2025, 8, 10)],
}


def intervals(ds):
    ds = sorted(ds)
    return [(b - a).days for a, b in zip(ds, ds[1:])]


def median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


if __name__ == "__main__":
    all_iv = []
    for u, ds in ORDERS.items():
        iv = intervals(ds)
        all_iv += iv
        if iv:
            print(f"{u}: 订单 {len(ds)} 次,间隔 {iv}")
    buyers = [u for u, ds in ORDERS.items() if len(ds) >= 2]
    buckets = {"1-7天": 0, "8-30天": 0, "30天以上": 0}
    for v in all_iv:
        k = "1-7天" if v <= 7 else ("8-30天" if v <= 30 else "30天以上")
        buckets[k] += 1
    print(f"中位复购间隔 {median(all_iv)} 天,间隔分布 {buckets}")
    print(f"窗口内有复购的用户占比 {len(buyers) / len(ORDERS):.0%}")
    print("要点:复购率必须声明观察窗口;窗口尾部的新客还没来得及复购(右删失),按 cohort 对齐截止日比较才公平")
