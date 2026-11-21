"""管道看门狗: 错过心跳的分级处置阶梯"""

SOFT_SECONDS = 300   # 超过 5 分钟无心跳 -> 告警观察
HARD_SECONDS = 900   # 超过 15 分钟无心跳 -> 判定僵尸并处置


def watchdog_check(heartbeat, now):
    """heartbeat 为空表示从未上报, 返回级别与处置动作"""
    if heartbeat is None:
        return "ACT", ["登记无心跳任务", "查询调度记录", "人工确认后重新拉起"]
    age = now - heartbeat["ts"]
    if age <= SOFT_SECONDS:
        return "OK", [f"心跳正常, 进度 {heartbeat['progress']}"]
    if age <= HARD_SECONDS:
        return "WARN", [
            f"心跳停滞 {age}s, 进度停在 {heartbeat['progress']}",
            "查询任务日志尾部与宿主机负载",
            "通知属主观察, 不动手杀进程",
        ]
    return "ACT", [
        f"心跳停滞 {age}s 超过硬阈值",
        "保全现场: 归档最后心跳与日志片段",
        "标记僵尸实例并终止",
        "任务回队重跑, 幂等键保证不重放已产出",
    ]


if __name__ == "__main__":
    cases = [
        ("健康", {"ts": 1000, "progress": "3/10"}, 1060),
        ("软超时", {"ts": 1000, "progress": "3/10"}, 1400),
        ("硬超时", {"ts": 1000, "progress": "3/10"}, 2200),
        ("无心跳", None, 2200),
    ]
    ladder = {"OK": 0, "WARN": 1, "ACT": 2}
    results = []
    for name, hb, now in cases:
        level, actions = watchdog_check(hb, now)
        results.append(level)
        print(f"[{name}] -> {level}")
        for a in actions:
            print(f"    - {a}")
    assert results == ["OK", "WARN", "ACT", "ACT"], "四级场景应命中三个级别"
    assert ladder["OK"] < ladder["WARN"] < ladder["ACT"], "处置阶梯必须单调升级"
    assert len(watchdog_check({"ts": 1000, "progress": "3/10"}, 2200)[1]) >= 4, "硬超时要保全现场再处置"
    print("要点: 看门狗的价值在'阶梯'而非'一刀切', 软超时先观察, 硬超时先留证再杀, 杀完必须能幂等重跑")
