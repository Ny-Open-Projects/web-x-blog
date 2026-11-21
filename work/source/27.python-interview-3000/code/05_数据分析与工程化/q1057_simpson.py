
data = {
    "ios":     {"A": (80, 100), "B": (225, 300)},   # 成功数, 总数
    "android": {"A": (260, 400), "B": (60, 100)},
}
agg = {"A": [0, 0], "B": [0, 0]}
for dev, arms in data.items():
    for arm, (c, n) in arms.items():
        agg[arm][0] += c
        agg[arm][1] += n
        print(f"{dev:8} {arm}: {c}/{n} = {c/n:.1%}")
for arm, (c, n) in agg.items():
    print(f"合计  {arm}: {c}/{n} = {c/n:.1%}")
print("每个分群 A 更好,聚合后 B 更好 -> 辛普森悖论,根因是分群流量结构不同")
