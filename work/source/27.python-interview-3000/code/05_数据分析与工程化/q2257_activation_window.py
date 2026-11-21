"""激活口径: 关键行为窗口的天数选择如何改变结论"""

# 用户: 渠道, 注册到完成关键行为的天数, None 表示 14 天内未完成
USERS = [
    ("搜索", 0), ("搜索", 1), ("搜索", 2), ("搜索", None),
    ("信息流", 1), ("信息流", 3), ("信息流", 5), ("信息流", 6),
    ("信息流", None), ("信息流", None),
    ("自然量", 0), ("自然量", 2), ("自然量", 4), ("自然量", None),
]


def activation_rate(days, window):
    hit = sum(1 for d in days if d is not None and d <= window)
    return hit / len(days)


if __name__ == "__main__":
    chans = {}
    for ch, d in USERS:
        chans.setdefault(ch, []).append(d)
    print(f"{'渠道':<6}{'n':>3}{'1日激活':>9}{'3日激活':>9}{'7日激活':>9}")
    for ch, ds in chans.items():
        cells = [f"{activation_rate(ds, w):.0%}" for w in (1, 3, 7)]
        print(f"{ch:<6}{len(ds):>3}" + "".join(f"{c:>9}" for c in cells))
    print("要点: 窗口短于下一个决策周期; 窗口每放宽激活率必升, 跨期对比必须同窗口; 行为定义与窗口一起冻结")
