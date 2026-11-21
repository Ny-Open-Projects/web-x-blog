"""上游延迟的容忍表: 分源分时的等待与放行决策"""

TOLERANCE = {
    # 数据源: 核心时段容忍分钟, 平峰容忍分钟, 硬上限分钟
    "pay_core":  {"peak": 10, "off": 30, "hard": 120},
    "user_tags": {"peak": 45, "off": 90, "hard": 300},
    "log_sink":  {"peak": 120, "off": 240, "hard": 720},
}


def is_peak(hour):
    return 10 <= hour < 22


def decide(source, hour, delay_minutes):
    if source not in TOLERANCE:
        return "ESCALATE", "未知数据源, 无容忍策略"
    tol = TOLERANCE[source]
    limit = tol["peak"] if is_peak(hour) else tol["off"]
    if delay_minutes <= limit:
        return "WAIT_OK", f"延迟 {delay_minutes} 分钟在容忍线 {limit} 内, 继续等待"
    if delay_minutes <= tol["hard"]:
        return "PROCEED_DEGRADED", f"延迟 {delay_minutes} 分钟超出容忍线 {limit} 但未破硬顶 {tol['hard']}, 放行旧分区并标注新鲜度"
    return "ESCALATE", f"延迟 {delay_minutes} 分钟击穿硬顶 {tol['hard']}, 升级 oncall"


if __name__ == "__main__":
    cases = [
        ("pay_core", 14, 8), ("pay_core", 14, 45), ("pay_core", 3, 25),
        ("pay_core", 14, 200), ("user_tags", 11, 40), ("log_sink", 23, 300),
        ("unknown_src", 12, 5),
    ]
    for source, hour, delay in cases:
        action, why = decide(source, hour, delay)
        tag = "核心时段" if is_peak(hour) else "平峰"
        print(f"{source:<11} {hour:02d}时[{tag}] 延迟 {delay:>3} 分钟 -> {action:<17} {why}")
    assert decide("pay_core", 14, 8)[0] == "WAIT_OK"
    assert decide("pay_core", 14, 45)[0] == "PROCEED_DEGRADED"
    assert decide("pay_core", 3, 25)[0] == "WAIT_OK", "凌晨 25 分钟在平峰容忍线内"
    assert decide("pay_core", 14, 200)[0] == "ESCALATE"
    assert decide("unknown_src", 12, 5)[0] == "ESCALATE"
    print("要点: 容忍表把'等多久'从吵架变成查表, 核心时段收紧, 平峰放宽, 硬顶之外一律升级")
