"""积压估算:Little 定律与清空时间,容量规划的最小工具"""

import math

SCENARIOS = [
    # 场景, 到达速率 行/秒, 处理速率 行/秒, 当前积压 行
    ("稳态", 800, 1000, 0),
    ("积压增长", 1200, 1000, 0),
    ("故障后追赶", 800, 1000, 600000),
]


def estimate(in_rate, out_rate, backlog):
    growth = in_rate - out_rate
    if growth <= 0 and backlog == 0:
        return {"state": "稳态", "drain_hours": 0.0, "backlog_1h": 0}
    backlog_1h = max(0, backlog + growth * 3600)
    if growth < 0:
        drain_hours = backlog / (-growth) / 3600
        return {"state": "清空中", "drain_hours": round(drain_hours, 2),
                "backlog_1h": backlog_1h}
    return {"state": "持续积压", "drain_hours": math.inf,
            "backlog_1h": backlog_1h}


def required_out_rate(in_rate, backlog, deadline_hours):
    """给定清理时限反推需要的处理速率"""
    return in_rate + backlog / (deadline_hours * 3600)


if __name__ == "__main__":
    for name, r_in, r_out, backlog in SCENARIOS:
        r = estimate(r_in, r_out, backlog)
        print(f"{name}: {r}")
    need = required_out_rate(800, 600000, 2)
    print(f"2 小时内清完 60 万积压需要处理速率 {need:.0f} 行/秒")
    print("要点:容量规划就是 Lambda/W 的算术,先算清楚再谈扩容")
