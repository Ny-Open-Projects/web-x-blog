"""发布后观察期报告:逐日对比发布前基线,超阈值标红"""

import statistics

BASELINE_7D = {"gmv": [1000, 1020, 990, 1010, 1030, 1005, 1015],
               "crash_rate": [0.001, 0.001, 0.002, 0.001, 0.001, 0.001, 0.002]}
AFTER_RELEASE = {
    "gmv": {"D1": 1010, "D2": 1002, "D3": 998},
    "crash_rate": {"D1": 0.0012, "D2": 0.0026, "D3": 0.0035},
}
WATCH_DAYS = 3
ALERT_RATIO = 1.2  # 相对基线均值偏离 20% 告警


def watch_report(baseline, after, days=WATCH_DAYS, alert=ALERT_RATIO):
    findings = []
    for metric, daily in after.items():
        base = statistics.mean(baseline[metric])
        for day, value in list(daily.items())[:days]:
            rel = value / base - 1
            exceeded = abs(rel) > (alert - 1)
            findings.append((metric, day, value, base, rel, exceeded))
    return findings


if __name__ == "__main__":
    rows = watch_report(BASELINE_7D, AFTER_RELEASE)
    for metric, day, value, base, rel, exceeded in rows:
        mark = " <-- 超阈值" if exceeded else ""
        print(f"{metric} {day}: {value} 基线均值 {base:.4g} 偏差 {rel:+.1%}{mark}")
    alerts = [f"{m} {d}" for m, d, *_rest in rows if _rest[-1]]
    print("\n超阈值项:", ", ".join(alerts) or "无")
    print("结论: crash_rate 连续上行,建议按预案升级排查而不是继续观察")
