from collections import defaultdict
from datetime import datetime, timedelta

events = [
    ("u1", "2026-01-01 10:00", "view"),
    ("u1", "2026-01-01 10:05", "cart"),
    ("u1", "2026-01-01 10:30", "pay"),
    ("u2", "2026-01-01 11:00", "view"),
    ("u2", "2026-01-01 12:10", "cart"),
    ("u3", "2026-01-01 09:00", "cart"),
]
steps = ["view", "cart", "pay"]
window = timedelta(hours=1)

by_user = defaultdict(list)
for user, ts, ev in events:
    by_user[user].append((datetime.fromisoformat(ts), ev))

counts = [0] * len(steps)
for evs in by_user.values():
    evs.sort()
    i, anchor = 0, None
    for ts, ev in evs:
        if ev == steps[i] and (i == 0 or ts - anchor <= window):
            if i == 0:
                anchor = ts
            i += 1
            if i == len(steps):
                break
    for j in range(i):
        counts[j] += 1

for s, c in zip(steps, counts):
    print(s, c)
print("逐步转化率:", [f"{counts[i+1]/counts[i]:.0%}" for i in range(len(steps) - 1)])
print("u2 的 cart 超过 1 小时窗口,不计入")
