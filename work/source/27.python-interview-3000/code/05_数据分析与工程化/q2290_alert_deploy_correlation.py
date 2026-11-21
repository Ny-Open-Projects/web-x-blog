"""告警与发布的关联: 时间窗匹配回答是不是发版搞的"""

from datetime import datetime, timedelta

DEPLOYS = [
    ("2026-03-01 18:40", "pay-service v2.3.1"),
    ("2026-03-02 10:05", "search v1.9.0"),
    ("2026-03-02 11:30", "web v4.2.0"),
]
ALERTS = [
    ("2026-03-01 19:05", "pay 错误率超阈值"),
    ("2026-03-01 19:40", "pay 错误率超阈值"),
    ("2026-03-02 10:20", "search 查询超时"),
    ("2026-03-02 16:00", "磁盘使用率高"),
]
FMT = "%Y-%m-%d %H:%M"
WINDOW = timedelta(minutes=120)

if __name__ == "__main__":
    deploys = [(datetime.strptime(t, FMT), name) for t, name in DEPLOYS]
    linked, unlinked = [], []
    for t, msg in ALERTS:
        t = datetime.strptime(t, FMT)
        candidates = [(dt, name) for dt, name in deploys if timedelta(0) <= t - dt <= WINDOW]
        if candidates:
            dt, name = candidates[0]   # 窗口内最近一次发布
            gap = (t - dt).total_seconds() / 60
            linked.append((msg, name))
            print(f"{t:%m-%d %H:%M} {msg} <-> 疑似 {name} (间隔 {gap:.0f} 分钟)")
        else:
            unlinked.append(msg)
            print(f"{t:%m-%d %H:%M} {msg} <-> 窗口内无发布, 按环境问题处理")
    suspects = sorted(set(n for _, n in linked))
    print(f"关联率 {len(linked)}/{len(ALERTS)}, 疑似肇事发布: {suspects}")
    print("要点: 关联不是因果, 回滚验证或拐点对齐确认; 窗口按告警延迟分布定; 发布记录必须结构化可查")
