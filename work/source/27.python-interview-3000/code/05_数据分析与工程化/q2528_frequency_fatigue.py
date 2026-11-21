"""曝光频次分布与疲劳信号: CTR 随频次衰减的实测"""

USERS = [
    # 用户在活动期的总曝光次数与总点击数
    (1, 0), (2, 0), (3, 1), (4, 1), (5, 2),
    (6, 2), (7, 1), (8, 1), (9, 1), (12, 1), (15, 0),
]
BUCKETS = [("1", 1, 1), ("2", 2, 2), ("3-5", 3, 5), ("6-10", 6, 10), ("11+", 11, 10 ** 9)]


def bucket_of(n):
    for name, lo, hi in BUCKETS:
        if lo <= n <= hi:
            return name
    raise ValueError(n)


if __name__ == "__main__":
    agg = {name: [0, 0] for name, _, _ in BUCKETS}
    for imp, click in USERS:
        b = bucket_of(imp)
        agg[b][0] += imp
        agg[b][1] += click
    print(f"{'频次档':<6} 曝光 点击 CTR")
    ctrs = {}
    for name, _, _ in BUCKETS:
        imp, click = agg[name]
        if imp == 0:
            continue
        ctr = click / imp
        ctrs[name] = ctr
        print(f"{name:<6} {imp:4d} {click:4d} {ctr:6.1%}")
    peak = max(ctrs, key=ctrs.get)
    last = [b for b in ("6-10", "11+") if b in ctrs][-1]
    print(f"峰值在 {peak} 档({ctrs[peak]:.1%}), 高频档 {last} 跌到 {ctrs[last]:.1%}, 疲劳明显")
    assert ctrs[peak] > ctrs[last] * 5, "高频档应显著衰减"
    print("要点: 频次超 6 后每多投一次的边际 CTR 急跌, 与其加频次不如换素材或直接封顶")
