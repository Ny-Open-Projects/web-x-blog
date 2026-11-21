"""退款冲销: 净收入桥与归属口径的抉择"""

GROSS = {"1月": 100, "2月": 110, "3月": 105}     # 千元
# 退款事件: 原销售月, 退款发生月, 金额
REFUNDS = [("1月", "3月", 5), ("2月", "2月", 3), ("3月", "3月", 2)]
MONTHS = ["1月", "2月", "3月"]


def net_by_refund_month():
    """政策A: 退款记在退款发生月, 历史不动"""
    net = dict(GROSS)
    for _, refund_m, amt in REFUNDS:
        net[refund_m] -= amt
    return net


def net_by_sale_month():
    """政策B: 退款冲回原销售月, 历史月份需重述"""
    net = dict(GROSS)
    for sale_m, _, amt in REFUNDS:
        net[sale_m] -= amt
    return net


def mom(net):
    return {m: (net[m] / net[p] - 1) * 100 for p, m in zip(MONTHS, MONTHS[1:])}


if __name__ == "__main__":
    a, b = net_by_refund_month(), net_by_sale_month()
    print("政策A 按退款月: " + ", ".join(f"{m} 净收入 {a[m]}" for m in MONTHS))
    print("政策B 归原销售月: " + ", ".join(f"{m} 净收入 {b[m]}" for m in MONTHS))
    assert a["3月"] != b["3月"], "两种政策对 3 月应给出不同的净收入"
    print(f"政策A 环比: 2月 {mom(a)['2月']:+.1f}%, 3月 {mom(a)['3月']:+.1f}%"
          " <- 3月大跌其实是 1 月的旧账退款砸下来的")
    print(f"政策B 环比: 2月 {mom(b)['2月']:+.1f}%, 3月 {mom(b)['3月']:+.1f}%"
          " <- 平滑, 但 1 月是重述数, 报表必须脚注标 restated")
    assert a["1月"] == 100 and b["1月"] == 95, "政策B 重述 1 月"
    print("要点: 归属口径一经选用必须冻结, 换口径等于换指标; 跨月退款永远会制造 A 口径的假波动")
