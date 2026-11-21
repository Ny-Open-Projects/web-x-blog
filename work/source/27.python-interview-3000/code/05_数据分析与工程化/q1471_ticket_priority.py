"""工单优先级算法:影响面 x 紧急度矩阵,输出 P0-P3 与 SLA 时限"""

TICKETS = [
    # 工单, 受影响用户数, 是否阻断生产, 承诺时限剩余小时, 提出方层级
    ("T1 核心报表白屏", 2000, True, 1, "高管"),
    ("T2 某个指标口径疑问", 1, False, 72, "运营"),
    ("T3 看板加载慢", 300, False, 24, "普通用户"),
    ("T4 数据不一致工单", 500, True, 8, "销售"),
]


def priority(affected, blocking, hours_left, escalation):
    """影响(广度 x 深度)与紧急(时限 x 升级)双维打分,矩阵映射到 P0-P3"""
    impact = 2 if affected >= 1000 else 1 if affected >= 100 else 0
    if blocking:
        impact = max(impact, 2)
    urgency = 2 if hours_left <= 4 else 1 if hours_left <= 24 else 0
    if escalation == "高管":
        urgency = max(urgency, 1)
    score = impact * 2 + urgency
    if score >= 4:
        return "P0"
    if score == 3:
        return "P1"
    if score == 2:
        return "P2"
    return "P3"


SLA_HOURS = {"P0": 1, "P1": 4, "P2": 24, "P3": 72}


if __name__ == "__main__":
    ranked = sorted(TICKETS,
                    key=lambda t: ["P0", "P1", "P2", "P3"].index(priority(*t[1:])))
    for name, affected, blocking, hours, esc in ranked:
        p = priority(affected, blocking, hours, esc)
        print(f"{p} (响应 {SLA_HOURS[p]}h 内) {name}")
    print("要点:优先级算法要写进制度,同一输入必须得到同一优先级,避免吵架")
