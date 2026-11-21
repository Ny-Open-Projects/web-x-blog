"""简化 LTV:月留存曲线 x 月均贡献,误差全部来自留存尾部外推"""

MONTH_RETENTION = [1.0, 0.55, 0.38, 0.30, 0.26, 0.22]  # M0..M5 观测期留存
ARPU_MONTH = 45.0


def ltv_observed(retention, arpu):
    """观测期 LTV:各月存活率 x ARPU 求和,只报有数据支撑的部分"""
    return sum(r * arpu for r in retention)


def ltv_with_tail(retention, arpu, decay=0.85, cap_months=24):
    """尾部外推:末段留存按固定月衰减,并封顶避免无限累加"""
    total = sum(r * arpu for r in retention)
    r = retention[-1]
    for _ in range(len(retention), cap_months):
        r *= decay
        total += r * arpu
    return total


if __name__ == "__main__":
    l1 = ltv_observed(MONTH_RETENTION, ARPU_MONTH)
    l2 = ltv_with_tail(MONTH_RETENTION, ARPU_MONTH)
    naive = ARPU_MONTH * len(MONTH_RETENTION)
    print(f"观测期 6 个月 LTV: {l1:.0f} 元(天真口径 {naive:.0f} 元,默认月月留存 100%,高估)")
    print(f"含尾部外推 24 个月 LTV: {l2:.0f} 元")
    print("要点:LTV 的不确定部分全在尾部,衰减率与封顶假设要写进口径;CAC 回本判断必须用同一外推口径,不能两套混比")
