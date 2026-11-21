"""购物篮共现矩阵:商品对共现次数与条件概率,pandas 交叉表与标准库双实现"""

try:
    import pandas as pd
except ImportError:
    pd = None

BASKETS = [
    ["面包", "牛奶", "鸡蛋"],
    ["牛奶", "咖啡"],
    ["面包", "牛奶"],
    ["咖啡", "牛奶", "饼干"],
    ["面包", "鸡蛋"],
    ["牛奶", "鸡蛋", "饼干"],
]


def cooccurrence(baskets):
    items = sorted({i for b in baskets for i in b})
    count = {a: {b: 0 for b in items} for a in items}
    for b in baskets:
        uniq = sorted(set(b))
        for a in uniq:
            for c in uniq:
                if a != c:
                    count[a][c] += 1
    item_cnt = {i: sum(1 for b in baskets if i in b) for i in items}
    return items, count, item_cnt


if pd is None:
    items, count, item_cnt = cooccurrence(BASKETS)
    print("共现次数矩阵(行=已买 列=同时买):")
    print("      " + " ".join(f"{b:>4}" for b in items))
    for a in items:
        print(f"{a:>5} " + " ".join(f"{count[a][b]:>4}" for b in items))
    print("\n条件概率 P(同时买列 | 已买行):")
    for a in items:
        others = [b for b in items if b != a]
        row = [f"{b}:{count[a][b] / item_cnt[a]:.0%}" for b in others]
        print(f"  {a} -> " + ", ".join(row))
    print("要点:共现矩阵对称,对角线即商品自身篮数;它是关联规则和捆绑销售的原料")
else:
    from itertools import combinations
    rows = []
    for b in BASKETS:
        for a, c in combinations(sorted(set(b)), 2):
            rows.append((a, c))
            rows.append((c, a))
    df = pd.DataFrame(rows, columns=["a", "c"])
    print(pd.crosstab(df["a"], df["c"]))
