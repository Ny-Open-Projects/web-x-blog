"""小样本抑制:格子样本量低于阈值不单独展示,合并到其他项并标注"""

CONVERSION = {
    # 渠道: (访问数, 下单数)
    "自然流量": (5200, 416),
    "信息流A": (3100, 217),
    "信息流B": (2900, 232),
    "搜索品牌": (1800, 162),
    "异业合作": (40, 5),
    "线下地推": (18, 2),
}
MIN_N = 100


def report(rows, min_n):
    big = {k: v for k, v in rows.items() if v[0] >= min_n}
    small = {k: v for k, v in rows.items() if v[0] < min_n}
    merged_n = sum(v[0] for v in small.values())
    merged_c = sum(v[1] for v in small.values())
    lines = []
    for k, (n, c) in sorted(big.items(), key=lambda x: -x[1][0]):
        lines.append(f"  {k:<8} 访问 {n:>5} 转化率 {c / n:.1%}")
    if small:
        lines.append(f"  其他(含 {len(small)} 个小样本渠道) 访问 {merged_n} 转化率 {merged_c / merged_n:.1%}")
    return lines, small


if __name__ == "__main__":
    lines, small = report(CONVERSION, MIN_N)
    print("渠道转化报表:")
    print("\n".join(lines))
    print(f"被抑制渠道: {sorted(small)} (访问数 < {MIN_N})")
    print("要点:小样本转化率天然大起大落,低于阈值要么合并要么置灰;阈值写进口径文档,'其他'桶的样本量也要展示")
