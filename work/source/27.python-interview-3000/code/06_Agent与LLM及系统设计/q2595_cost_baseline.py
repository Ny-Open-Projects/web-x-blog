"""Q2595 成本告警的分位数基线:用历史同时段的 P95 做动态阈值。

固定阈值白天误报晚上漏报;按小时取历史同时段的 P95 当动态基线,
当前值超基线乘系数才告警,并带冷却窗口防连环轰炸。
业务高峰的基线天然高,夜间低谷的基线天然低。
"""
import random


def p95(xs):
    xs = sorted(xs)
    idx = min(len(xs) - 1, int(0.95 * (len(xs) - 1) + 0.5))
    return xs[idx]


def build_history(days=14, seed=7):
    rng = random.Random(seed)
    hist = {}
    for h in range(24):
        hist[h] = [50 + rng.randint(-5, 5) + (10 if 9 <= h <= 18 else 0)
                   for _ in range(days)]
    return hist


def detect(today, hist, factor=1.5, cooldown=2):
    alerts = []
    cool_until = -1
    for h, cost in enumerate(today):
        base = p95(hist[h])
        if cost > base * factor and h > cool_until:
            alerts.append((h, cost, base))
            cool_until = h + cooldown
    return alerts


def main():
    hist = build_history()
    rng = random.Random(99)
    normal_day = [55 + rng.randint(-4, 6) + (8 if 9 <= h <= 18 else 0) for h in range(24)]
    incident = list(normal_day)
    incident[14] = 200
    incident[15] = 190
    a1 = detect(normal_day, hist)
    a2 = detect(incident, hist)
    assert a1 == [], a1
    hits = [a[0] for a in a2]
    assert 14 in hits, a2
    assert 15 not in hits, a2          # 冷却窗口内不重复报
    assert p95(hist[14]) >= p95(hist[3])  # 白天基线高于凌晨
    print("正常日告警:", a1)
    print("异常日告警:", a2, "← 15 点在冷却窗口内被抑制")
    print("基线示例 14 点 P95:", p95(hist[14]), "凌晨 3 点 P95:", p95(hist[3]))


if __name__ == "__main__":
    main()
