"""漏斗的分步时间窗: 每步独立时限, 而非一条总窗口"""
from datetime import datetime, timedelta

STEPS = ["曝光", "点击", "加购", "支付"]
# 每步相对上一步命中事件的最大允许间隔, 单位分钟
WINDOWS = {"点击": 30, "加购": 24 * 60, "支付": 72 * 60}

E = datetime(2026, 3, 1, 10, 0)
EVENTS = [
    ("u1", "曝光", E), ("u1", "点击", E + timedelta(minutes=5)),
    ("u1", "加购", E + timedelta(hours=2)), ("u1", "支付", E + timedelta(hours=20)),
    ("u2", "曝光", E), ("u2", "点击", E + timedelta(minutes=40)),
    ("u2", "加购", E + timedelta(hours=3)), ("u2", "支付", E + timedelta(hours=30)),
    ("u3", "曝光", E), ("u3", "点击", E + timedelta(minutes=2)),
    ("u3", "加购", E + timedelta(days=2)), ("u3", "支付", E + timedelta(days=4)),
    ("u4", "曝光", E), ("u4", "点击", E + timedelta(minutes=3)),
    ("u5", "曝光", E + timedelta(minutes=1)), ("u5", "点击", E + timedelta(minutes=4)),
    ("u5", "加购", E + timedelta(hours=10)), ("u5", "支付", E + timedelta(hours=60)),
    ("u6", "支付", E + timedelta(minutes=1)),
]


def build_index(events):
    idx = {}
    for user, step, ts in events:
        idx.setdefault(user, {}).setdefault(step, []).append(ts)
    for per in idx.values():
        for step in per:
            per[step].sort()
    return idx


def funnel_step_window(idx, user):
    """有序匹配, 且每步必须落在相对上一步的独立时限内"""
    cur, path = None, []
    for step in STEPS:
        cands = idx.get(user, {}).get(step, [])
        if cur is not None:
            cands = [ts for ts in cands if cur <= ts <= cur + timedelta(minutes=WINDOWS[step])]
        if not cands:
            return path, "中断于" + step
        cur = cands[0]
        path.append(step)
    return path, "完整"


def funnel_overall(idx, user, overall_minutes):
    """对照口径: 有序匹配但只约束首尾总跨度"""
    cur, first = None, None
    for step in STEPS:
        cands = [ts for ts in idx.get(user, {}).get(step, []) if cur is None or ts >= cur]
        if not cands:
            return False
        cur = cands[0]
        if first is None:
            first = cur
    return (cur - first) <= timedelta(minutes=overall_minutes)


if __name__ == "__main__":
    idx = build_index(EVENTS)
    users = sorted(idx)
    for u in users:
        path, why = funnel_step_window(idx, u)
        print(f"{u}: {' -> '.join(path) if path else '无有效起点'}  [{why}]")
    counts = {s: 0 for s in STEPS}
    for u in users:
        for s in funnel_step_window(idx, u)[0]:
            counts[s] += 1
    print("分步窗漏斗:", " -> ".join(f"{s} {counts[s]}" for s in STEPS))
    strict_pay = counts["支付"]
    loose_pay = sum(1 for u in users if funnel_overall(idx, u, 72 * 60))
    print(f"对照口径: 72h 总窗口宽松口径支付 {loose_pay} 人, 分步窗口径 {strict_pay} 人")
    assert loose_pay > strict_pay, "分步窗口径应更严格, 转化数更少"
    assert "u2" not in [u for u in users if len(funnel_step_window(idx, u)[0]) == 4], "u2 点击超 30 分钟应被剔除"
    print("要点: 每步独立时限把'转化'定义得可解释, 总窗口口径会把超窗点击也算进漏斗")
