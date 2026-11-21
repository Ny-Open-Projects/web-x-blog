"""会话重建: 30 分钟不活跃切分与跨午夜归属"""

from datetime import datetime, timedelta

EVENTS = [
    ("u1", "2026-03-01 23:40", "home"), ("u1", "2026-03-01 23:50", "list"),
    ("u1", "2026-03-02 00:05", "detail"),          # 跨午夜但间隔 15 分钟, 同一会话
    ("u1", "2026-03-02 09:00", "home"),            # 新会话
    ("u2", "2026-03-02 10:00", "home"),
    ("u2", "2026-03-02 10:40", "detail"),          # 间隔 40 分钟, 新会话
    ("u3", "2026-03-02 11:00", "home"),            # 单事件会话, 弹出
]
GAP = timedelta(minutes=30)
FMT = "%Y-%m-%d %H:%M"


def build_sessions(events):
    sessions, cur = [], []
    prev_t = prev_u = None
    for user, ts, page in events:
        t = datetime.strptime(ts, FMT)
        if prev_u != user or (cur and t - prev_t > GAP):
            if cur:
                sessions.append(cur)
            cur = []
        cur.append((user, t, page))
        prev_t, prev_u = t, user
    if cur:
        sessions.append(cur)
    return sessions


if __name__ == "__main__":
    sessions = build_sessions(EVENTS)
    bounce = sum(1 for s in sessions if len(s) == 1)
    print(f"共 {len(sessions)} 个会话, 弹出会话 {bounce} 个, 弹出率 {bounce / len(sessions):.0%}")
    for s in sessions:
        start = s[0][1]
        dur = (s[-1][1] - start).total_seconds() / 60
        print(f"{s[0][0]} 会话起始 {start:%m-%d %H:%M} 归属日 {start.date()} 页面数 {len(s)} 时长 {dur:.0f} 分钟")
    print("要点: 会话归属首事件日期, 跨零点不断开; 时长是活跃下界; 阈值与归属规则进口径字典")
