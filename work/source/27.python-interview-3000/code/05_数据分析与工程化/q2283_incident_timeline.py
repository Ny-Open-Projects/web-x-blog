"""事故时间线自动汇总: 多源事件归并与相位锚点"""

from datetime import datetime

RAW = [
    ("2026-03-01 20:12", "deploy", "v2.3.1 上线 pay-service"),
    ("2026-03-01 20:31", "alert", "错误率 3.2% 超阈值"),
    ("2026-03-01 20:31", "alert", "错误率 3.2% 超阈值"),      # 重复投递折叠
    ("2026-03-01 20:34", "chat", "值班认领"),
    ("2026-03-01 20:41", "action", "执行回滚 v2.3.0"),
    ("2026-03-01 20:52", "alert", "错误率回落 0.3%"),
    ("2026-03-01 20:55", "chat", "确认恢复"),
]
FMT = "%Y-%m-%d %H:%M"


def build_timeline(raw):
    events, seen = [], set()
    for ts, kind, msg in raw:
        key = (ts, kind, msg)
        if key in seen:
            continue
        seen.add(key)
        events.append((datetime.strptime(ts, FMT), kind, msg))
    events.sort(key=lambda e: e[0])
    dep = next((e for e in events if e[1] == "deploy"), None)
    alert = next((e for e in events if e[1] == "alert"), None)
    act = next((e for e in events if e[1] == "action"), None)
    rec = next((e for e in reversed(events) if e[1] == "alert" and "回落" in e[2]), None)
    return events, dep, alert, act, rec


if __name__ == "__main__":
    events, dep, alert, act, rec = build_timeline(RAW)
    for t, kind, msg in events:
        print(f"{t:%H:%M} [{kind:<7}] {msg}")
    if dep and alert:
        print(f"\nMTTD {alert[0] and (alert[0] - dep[0]).total_seconds() / 60:.0f} 分钟 (部署->首告警)")
    if alert and rec:
        print(f"MTTR {(rec[0] - alert[0]).total_seconds() / 60:.0f} 分钟 (首告警->指标回落)")
    print("要点: 多源归并去重; 四个相位锚点全团队统一; 关键决策靠人工注解, 时间线落库成组织资产")
