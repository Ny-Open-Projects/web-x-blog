"""监控完整最小实现: 指标采集 -> 滑窗聚合 -> 阈值规则 -> 告警去重冷却"""
from collections import defaultdict, deque


class Monitor:
    def __init__(self, window=20):
        self.series = defaultdict(lambda: deque(maxlen=window))
        self.rules = []
        self.last_fired = {}   # 告警键 -> 上次触发时刻, 实现冷却去重
        self.alert_log = []

    def collect(self, metric, value):
        self.series[metric].append(value)

    def snapshot(self, metric):
        vals = sorted(self.series[metric])
        if not vals:
            return None
        n = len(vals)

        def pct(p):
            k = max(0, min(n - 1, int(round(p / 100.0 * (n - 1)))))
            return vals[k]
        return {"n": n, "avg": round(sum(vals) / n, 2),
                "p95": pct(95), "p99": pct(99), "max": vals[-1]}

    def add_rule(self, name, metric, agg, threshold, severity="P1", cooldown=60):
        self.rules.append({"name": name, "metric": metric, "agg": agg,
                           "threshold": threshold, "severity": severity, "cooldown": cooldown})

    def evaluate(self, now):
        """逐条规则求值: 命中且不在冷却期才发告警"""
        fired = []
        for r in self.rules:
            snap = self.snapshot(r["metric"])
            if snap is None:
                continue
            v = snap[r["agg"]]
            if v is None or v <= r["threshold"]:
                continue
            key = r["name"]
            if key in self.last_fired and now - self.last_fired[key] < r["cooldown"]:
                continue
            self.last_fired[key] = now
            alert = {"t": now, "name": r["name"], "severity": r["severity"],
                     "value": v, "window": snap}
            self.alert_log.append(alert)
            fired.append(alert)
        return fired


if __name__ == "__main__":
    m = Monitor(window=20)
    m.add_rule("接口延迟 p99 超标", "latency_ms", "p99", 200, severity="P1", cooldown=60)
    m.add_rule("错误率超标", "error_rate", "avg", 0.05, severity="P0", cooldown=60)

    # 第 0 秒: 正常流量
    for v in [80, 90, 95, 110, 100]:
        m.collect("latency_ms", v)
    for v in [0.01, 0.02, 0.01]:
        m.collect("error_rate", v)
    print("t=0 告警:", [a["name"] for a in m.evaluate(0)])

    # 第 10 秒: 流量劣化, 但都在冷却期内 -> 不重复告警
    for v in [150, 240, 320, 280, 300]:
        m.collect("latency_ms", v)
    for v in [0.12, 0.15, 0.11]:
        m.collect("error_rate", v)
    print("t=10 窗口:", m.snapshot("latency_ms"), m.snapshot("error_rate"))
    print("t=10 告警:", [a["name"] for a in m.evaluate(10)], "(冷却期内去重)")

    # 第 70 秒: 冷却期已过, 指标仍超标 -> 再次告警
    print("t=70 告警:", [a["name"] for a in m.evaluate(70)])

    print("告警流水:")
    for a in m.alert_log:
        print("  t=%d %s [%s] %s=%.2f" % (a["t"], a["name"], a["severity"],
                                          m.rules[0]["agg"] if a["name"].startswith("接口") else "avg",
                                          a["value"]))
    print("要点: 告警键级冷却防轰炸, 窗口聚合抗单点抖动, P0 与 P1 分级决定叫醒谁")
