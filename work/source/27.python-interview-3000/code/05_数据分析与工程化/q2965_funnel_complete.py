"""用户行为漏斗完整实现: 有序去重匹配, 严格口径与可选步骤口径对照, 附下单耗时中位数"""
from datetime import datetime, timedelta
from statistics import median

STEPS = ["visit", "cart", "pay"]
OPTIONAL = {"cart"}   # 可跳步口径下允许直接跳过的中间步
T0 = datetime(2026, 3, 1, 10, 0)
# (user, step, ts) 原始事件, 含重复上报与先付后加购的乱序写入
RAW = [
    ("u1", "visit", T0), ("u1", "cart", T0 + timedelta(minutes=10)), ("u1", "pay", T0 + timedelta(minutes=30)),
    ("u2", "visit", T0), ("u2", "visit", T0 + timedelta(minutes=5)), ("u2", "cart", T0 + timedelta(minutes=20)),
    ("u3", "cart", T0 + timedelta(minutes=1)), ("u3", "pay", T0 + timedelta(minutes=2)),
    ("u4", "visit", T0), ("u4", "cart", T0 + timedelta(minutes=8)), ("u4", "pay", T0 + timedelta(minutes=9)),
    ("u5", "visit", T0), ("u5", "pay", T0 + timedelta(minutes=15)),
    ("u1", "pay", T0 + timedelta(minutes=1)),  # u1 加购前的支付事件, 有序匹配不应采纳
]


def build_user_events(events):
    """按用户聚合并按时间排序, 同一步骤天然支持多次上报"""
    per = {}
    for user, step, ts in events:
        per.setdefault(user, []).append((ts, step))
    for user in per:
        per[user].sort()
    return per


def match(per_user, strict):
    """有序首中匹配: 每步取上一步命中时刻之后的第一个事件.
    strict=True 逐步必达; False 时 OPTIONAL 中的步骤允许直接跳过"""
    matched = {}
    for user, evs in per_user.items():
        cursor, seq = None, []
        for step in STEPS:
            cands = [ts for ts, s in evs if s == step and (cursor is None or ts >= cursor)]
            if cands:
                seq.append((step, cands[0]))
                cursor = cands[0]
            elif not strict and step in OPTIONAL:
                continue
            else:
                break
        matched[user] = seq
    return matched


def funnel_report(matched):
    """按步骤名统计到达人数 -> 相邻步转化 -> 全程转化 -> 命中全程用户的首末步耗时中位数"""
    reach = {s: 0 for s in STEPS}
    for seq in matched.values():
        for step, _ in seq:
            reach[step] += 1
    reach_list = [reach[s] for s in STEPS]
    conv = [round(reach_list[i + 1] / reach_list[i] * 100, 1) if reach_list[i] else 0.0
            for i in range(len(STEPS) - 1)]
    overall = round(reach_list[-1] / reach_list[0] * 100, 1) if reach_list[0] else 0.0
    gaps = [(seq[-1][1] - seq[0][1]).total_seconds() / 60
            for seq in matched.values() if seq and seq[-1][0] == STEPS[-1]]
    med = round(median(gaps), 1) if gaps else None
    return reach_list, conv, overall, med


if __name__ == "__main__":
    per_user = build_user_events(RAW)
    for strict in (True, False):
        label = "严格口径" if strict else "可跳步口径"
        matched = match(per_user, strict=strict)
        reach, conv, overall, med = funnel_report(matched)
        print("%s: 到达 %s, 相邻步转化 %s, 全程 %.1f%%, 下单耗时中位数 %s 分钟"
              % (label, reach, conv, overall, med))
        if strict:
            for user in sorted(per_user):
                seq = matched[user]
                print("  %s -> %s" % (user, "未入漏斗" if not seq else
                                      "完整转化" if len(seq) == len(STEPS) else "停在 " + seq[-1][0]))
    print("口径说明: u3 无 visit 在任何口径下都不计入; u5 无加购, 仅可跳步口径到达 pay; u1 加购前的重复支付被有序匹配吸收")
    print("要点: 漏斗争议八成出在口径, 实现时把 严格/可选步/去重/有序 四个开关显式写进参数与报表脚注")
