"""指标突变检测:同时段基线 + 报警去重,避免告警风暴"""

import statistics
from datetime import datetime, timedelta

# 指标近14天同时段取值(按星期几对齐,减少周期干扰)
HISTORY = {
    "gmv": [820, 810, 830, 815, 825, 840, 818, 822, 809, 831, 817, 826, 833, 821],
    "dau": [52000, 51800, 52100, 51900, 52300, 52000, 51950, 52150, 51850,
            52200, 52050, 51900, 52350, 52080],
}
TODAY = {"gmv": 640, "dau": 51700}
ALARM_SIGMA = 3.0
COOLDOWN_MINUTES = 60


def detect(name, history, current, k=ALARM_SIGMA):
    mean = statistics.mean(history)
    std = statistics.pstdev(history)
    if std == 0:
        return None
    z = (current - mean) / std
    if abs(z) <= k:
        return None
    return {"metric": name, "value": current, "mean": round(mean, 1),
            "z": round(z, 2), "direction": "spike" if z > 0 else "drop"}


def dedup(alerts, last_sent, now):
    """同一指标同方向在冷却期内只报一次,防告警风暴"""
    sent = []
    for a in alerts:
        key = (a["metric"], a["direction"])
        if now - last_sent.get(key, datetime.min) >= timedelta(minutes=COOLDOWN_MINUTES):
            last_sent[key] = now
            sent.append(a)
    return sent


if __name__ == "__main__":
    now = datetime(2025, 6, 16, 10, 0)
    alerts = [a for a in (detect(k, v, TODAY[k]) for k, v in HISTORY.items()) if a]
    last_sent = {}
    print("第一轮告警:", dedup(alerts, last_sent, now))
    print("冷却期内重复告警:", dedup(alerts, last_sent, now + timedelta(minutes=10)), "-> 被抑制")
    print("冷却期后再次告警:", dedup(alerts, last_sent, now + timedelta(minutes=61)))
