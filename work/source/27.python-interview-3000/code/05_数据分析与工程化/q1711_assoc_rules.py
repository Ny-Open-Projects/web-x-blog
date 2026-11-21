"""关联规则三指标:support、confidence、lift,lift>1 才说明正关联"""

BASKETS = [
    {"面包", "牛奶", "鸡蛋"},
    {"牛奶", "咖啡"},
    {"面包", "牛奶"},
    {"咖啡", "牛奶", "饼干"},
    {"面包", "鸡蛋"},
    {"牛奶", "鸡蛋", "饼干"},
]


def support(itemset, baskets):
    n = len(baskets)
    return sum(1 for b in baskets if itemset <= b) / n


def rules(baskets, min_support=0.2):
    """从二项集生成双向规则,输出三指标并按 lift 降序"""
    items = sorted({i for b in baskets for i in b})
    out = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            x, y = {items[i]}, {items[j]}
            s_xy = support(x | y, baskets)
            if s_xy < min_support:
                continue
            s_x, s_y = support(x, baskets), support(y, baskets)
            out.append((f"{items[i]}->{items[j]}", s_xy, s_xy / s_x, s_xy / (s_x * s_y)))
            out.append((f"{items[j]}->{items[i]}", s_xy, s_xy / s_y, s_xy / (s_x * s_y)))
    return sorted(out, key=lambda r: -r[3])


if __name__ == "__main__":
    print(f"{'规则':<12}{'support':>9}{'confidence':>11}{'lift':>7}")
    for name, s, c, l in rules(BASKETS):
        tag = " 正关联" if l > 1.0001 else (" 独立" if abs(l - 1) <= 1e-9 else " 负关联")
        print(f"{name:<12}{s:>9.2%}{c:>11.2%}{l:>7.2f}{tag}")
    print("要点:support 看普遍性,confidence 看方向强度,lift=观测共现/独立时期望共现;热门商品天然共现高,必须用 lift 校正")
