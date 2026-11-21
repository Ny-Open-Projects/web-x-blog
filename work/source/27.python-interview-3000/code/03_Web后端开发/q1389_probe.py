"""拨测结果评估:可用性、SLO 与连续失败告警(纯标准库)。"""

PROBES = [(True, 0.12), (True, 0.10), (False, 0.0), (False, 0.0),
          (False, 0.0), (True, 0.15), (True, 0.11)]


def evaluate(probes, slo=0.99, alert_after=3):
    ok = sum(1 for ok, _ in probes if ok)
    availability = ok / len(probes)
    streak = worst = 0
    for ok, _ in probes:
        streak = 0 if ok else streak + 1
        worst = max(worst, streak)
    lat = sorted(p[1] for p in probes if p[0])
    return {"availability": round(availability, 3), "meet_slo": availability >= slo,
            "max_consecutive_fail": worst, "alert": worst >= alert_after,
            "ok_p95_s": round(lat[min(int(len(lat) * 0.95), len(lat) - 1)], 2)}


print("故障窗口:", evaluate(PROBES))
print("健康窗口:", evaluate([(True, 0.1)] * 100))
