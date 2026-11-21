"""监控自身的监控:采集器心跳登记,断流与滞后分级检测"""

COLLECTORS = {
    # 采集器: 最近心跳距今秒数
    "node_exporter": 5,
    "app_metrics": 40,
    "log_shipper": 900,
}
STALE_AFTER = 30      # 超过 30s 没心跳算滞后
DEAD_AFTER = 300      # 超过 300s 算断流
ESCALATE = {"log_shipper": "P2", "app_metrics": "P3", "node_exporter": "P3"}


def classify(age):
    if age is None:
        return "never", "从未上报,检查采集器是否启动"
    if age > DEAD_AFTER:
        return "dead", "断流,数据缺口已产生,评估从备份补点"
    if age > STALE_AFTER:
        return "stale", "滞后,先看采集器资源与网络"
    return "fresh", "正常"


if __name__ == "__main__":
    alarms = []
    for name, age in COLLECTORS.items():
        state, advice = classify(age)
        line = f"{name:<14} 距上次心跳 {age:>4}s [{state}] {advice}"
        print(line)
        if state != "fresh":
            alarms.append((name, state, ESCALATE.get(name, "P3")))
    print("告警升级:", alarms if alarms else "无")
    print("要点:元监控与业务监控分开部署,告警走独立通道,避免监控挂了没人知道;断流比指标异常更严重,因为缺口永远补不回来")
