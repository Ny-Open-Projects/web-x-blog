"""漏斗整体显著性:先端到端卡方检验,再逐级下钻并警惕多重比较"""

FUNNEL_STEPS = ["曝光", "点击", "加购", "支付"]

DATA = {
    "A": {"曝光": 10000, "点击": 1800, "加购": 620, "支付": 210},
    "B": {"曝光": 10000, "点击": 1950, "加购": 700, "支付": 268},
}
CHI2_CRITICAL_95 = 3.84  # 自由度 1 的 0.05 临界值


def chi2_2x2(a, b, c, d):
    """2x2 卡方统计量:两版本在转化/未转化上是否有差异"""
    n = a + b + c + d
    if min(a + b, c + d, a + c, b + d) == 0:
        return 0.0
    num = n * (a * d - b * c) ** 2
    den = (a + b) * (c + d) * (a + c) * (b + d)
    return num / den


if __name__ == "__main__":
    ra = DATA["A"]["支付"] / DATA["A"]["曝光"]
    rb = DATA["B"]["支付"] / DATA["B"]["曝光"]
    print(f"端到端转化率 A={ra:.2%} B={rb:.2%} 相对提升 {(rb - ra) / ra:+.1%}")
    a, b_ = DATA["A"]["支付"], DATA["A"]["曝光"] - DATA["A"]["支付"]
    c, d_ = DATA["B"]["支付"], DATA["B"]["曝光"] - DATA["B"]["支付"]
    x2 = chi2_2x2(a, b_, c, d_)
    print(f"端到端卡方 = {x2:.2f} -> {'显著,可下钻' if x2 > CHI2_CRITICAL_95 else '不显著,先别吹'}")
    print("-" * 48)
    for i in range(1, len(FUNNEL_STEPS)):
        prev, cur = FUNNEL_STEPS[i - 1], FUNNEL_STEPS[i]
        a, b_ = DATA["A"][cur], DATA["A"][prev] - DATA["A"][cur]
        c, d_ = DATA["B"][cur], DATA["B"][prev] - DATA["B"][cur]
        x = chi2_2x2(a, b_, c, d_)
        print(f"步骤 {prev}->{cur}: 卡方 {x:6.2f} {'显著' if x > CHI2_CRITICAL_95 else ''}")
    print("要点:先整体后局部;逐级检验做了 k 次就抬了假阳性,下钻结论按 Bonferroni 打折;报告写明检验口径")
