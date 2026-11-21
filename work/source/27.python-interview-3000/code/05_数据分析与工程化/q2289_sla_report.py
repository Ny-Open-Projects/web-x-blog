"""SLA 月报: 可用率, 错误预算与 MTTA MTTR 分位"""

from statistics import quantiles

MONTH_MINUTES = 30 * 24 * 60
INCIDENTS = [
    # id, 起止(同日内简化), 确认耗时分钟
    ("I1", "03-04 02:10", "03-04 02:55", 8),
    ("I2", "03-11 14:00", "03-11 15:40", 22),
    ("I3", "03-19 09:30", "03-19 09:48", 5),
    ("I4", "03-27 21:00", "03-27 23:30", 35),
]
BUDGET_MIN = 43.2   # 99.9% SLO 的月度错误预算


def minutes_of(hhmm):
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m


if __name__ == "__main__":
    downtime, acks, repairs = 0.0, [], []
    for inc_id, start, end, acked in INCIDENTS:
        mins = minutes_of(end.split(" ")[1]) - minutes_of(start.split(" ")[1])
        downtime += mins
        acks.append(acked)
        repairs.append(mins)
    avail = 1 - downtime / MONTH_MINUTES
    q_ack = quantiles(acks, n=10, method="inclusive")
    q_rep = quantiles(repairs, n=10, method="inclusive")
    print(f"月可用率 {avail:.3%} (SLO 99.9%, 预算 {BUDGET_MIN} 分钟)")
    print(f"停机 {downtime:.0f} 分钟, 错误预算消耗 {downtime / BUDGET_MIN:.0%}")
    print(f"MTTA 中位 {q_ack[4]:.1f} 分钟, P90 {q_ack[8]:.1f} 分钟")
    print(f"MTTR 中位 {q_rep[4]:.1f} 分钟, P90 {q_rep[8]:.1f} 分钟")
    print("要点: 停机按用户影响折算; 预算击穿触发冻结发布; 分位数不平均, 小样本注明方法")
