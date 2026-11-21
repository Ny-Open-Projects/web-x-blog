
ALERTS = [
    {"name": "5xx 比例超 1% 持续 5 分钟", "severity": "P1", "action": "电话"},
    {"name": "p99 延迟超阈值 15 分钟", "severity": "P2", "action": "IM 通知"},
    {"name": "磁盘水位 80%", "severity": "P2", "action": "IM 通知"},
    {"name": "单实例重启一次", "severity": "P4", "action": "仅记录"},
]

p1 = [a["name"] for a in ALERTS if a["severity"] == "P1"]
print("电话级告警:", p1)
print("各分级数量:", {s: sum(1 for a in ALERTS if a["severity"] == s)
                     for s in {"P1", "P2", "P4"}})
