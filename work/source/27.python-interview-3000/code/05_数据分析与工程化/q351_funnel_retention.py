from collections import defaultdict
from datetime import date, timedelta

def funnel(events, steps):
    """events: user -> 有序列表 of (date, step)。按序且窗口内才算。"""
    counts = [0] * len(steps)
    for user, evs in events.items():
        idx = 0
        step_dates = []
        for d, s in sorted(evs):
            if idx < len(steps) and s == steps[idx]:
                step_dates.append(d)
                idx += 1
        if len(step_dates) == len(steps):
            counts = [c + 1 for c in counts]
        else:
            for i in range(len(step_dates)):
                counts[i] += 1
    return {steps[i]: counts[i] for i in range(len(steps))}

def next_day_retention(first_login, active_days):
    """first_login: user -> date; active_days: user -> set of dates"""
    buckets = defaultdict(lambda: [0, 0])   # cohort -> [new_users, retained]
    for u, d0 in first_login.items():
        key = d0
        buckets[key][0] += 1
        if (d0 + timedelta(days=1)) in active_days.get(u, set()):
            buckets[key][1] += 1
    return {k: round(v[1] / v[0], 3) for k, v in buckets.items()}

if __name__ == "__main__":
    d1, d2 = date(2026, 11, 1), date(2026, 11, 2)
    events = {"u1": [(d1, "browse"), (d1, "cart"), (d1, "pay")],
              "u2": [(d1, "browse"), (d1, "pay")]}   # 跳过 cart,漏斗断裂
    print(funnel(events, ["browse", "cart", "pay"]))
    print(next_day_retention(
        {"u1": d1, "u2": d1},
        {"u1": {d1, d2}, "u2": {d1}}))
