"""漏斗卡点时长分析:步骤间转化耗时的分位数,判断'慢转化'用户群"""

import statistics

SESSIONS = [
    # session, 各步骤时间戳秒:访问、加购、支付(None 表示未发生)
    ("s1", 0, 120, 600),
    ("s2", 0, 90, 3000),
    ("s3", 0, 600, 900),
    ("s4", 0, 300, None),
    ("s5", 0, 180, 1500),
    ("s6", 0, None, None),
]


def step_gaps(sessions):
    """相邻步骤的耗时列表,缺步的会话不进入该步统计"""
    gaps = {"browse_to_cart": [], "cart_to_pay": []}
    for _, t0, t1, t2 in sessions:
        if t1 is not None:
            gaps["browse_to_cart"].append(t1 - t0)
            if t2 is not None:
                gaps["cart_to_pay"].append(t2 - t1)
    return gaps


def describe(values):
    if not values:
        return "无样本"
    values = sorted(values)
    p90 = values[min(len(values) - 1, int(round(0.9 * len(values))) - 1)]
    return f"中位 {statistics.median(values):.0f}s  P90 {p90}s  均值 {statistics.mean(values):.0f}s"


if __name__ == "__main__":
    gaps = step_gaps(SESSIONS)
    for step, values in gaps.items():
        print(f"{step}: {describe(values)}")
    slow = [g for g in gaps["cart_to_pay"] if g > 1200]
    print(f"加购后超过 20 分钟才支付: {len(slow)} 人 -> 建议催付策略针对这一段")
