"""辛普森悖论复现: 分层全胜却在聚合层翻车, 加权标准化还原真相"""

# 变体 -> 来源层 -> (访客数, 转化数); 每层 A 的转化率都更高
DATA = {
    "A": {"搜索": (200, 18), "直访": (300, 15), "推送": (500, 15)},
    "B": {"搜索": (700, 56), "直访": (250, 10), "推送": (50, 1)},
}


def rate(cell):
    visits, conv = cell
    return conv / visits


if __name__ == "__main__":
    total = sum(v for var in DATA.values() for v, _ in var.values())
    weights = {}
    for src in DATA["A"]:
        n = sum(DATA[var][src][0] for var in DATA)
        weights[src] = n / total
    print("分层转化率(A 应全胜):")
    for src in DATA["A"]:
        ra, rb = rate(DATA["A"][src]), rate(DATA["B"][src])
        assert ra > rb, f"{src} 层 A 应更高"
        print(f"  {src}: A {ra:.1%} > B {rb:.1%}, 该层流量权重 {weights[src]:.0%}")
    agg = {}
    for var, strata in DATA.items():
        v = sum(x for x, _ in strata.values())
        c = sum(y for _, y in strata.values())
        agg[var] = c / v
    print(f"聚合转化率: A {agg['A']:.1%} vs B {agg['B']:.1%}"
          f" -> {'B 胜' if agg['B'] > agg['A'] else 'A 胜'}, 悖论出现")
    assert agg["B"] > agg["A"], "聚合层应出现方向翻转"
    std = {}
    for var, strata in DATA.items():
        std[var] = sum(weights[src] * rate(cell) for src, cell in strata.items())
    print(f"按统一流量结构标准化: A {std['A']:.1%} vs B {std['B']:.1%}"
          f" -> {'A 胜' if std['A'] > std['B'] else 'B 胜'}, 与分层一致")
    assert std["A"] > std["B"], "标准化后应与分层方向一致"
    print("根因: B 把流量堆进高转化层, 聚合率混合了'层内能力'与'结构差异'两个因素")
