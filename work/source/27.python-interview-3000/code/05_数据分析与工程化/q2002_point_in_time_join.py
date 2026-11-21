"""时点对齐 join:事实按发生时刻匹配维表当时版本,防数据穿越"""

from bisect import bisect_right

# 用户等级维表拉链: key -> [(生效起, 失效止, 等级)]
DIM_LEVEL = {
    "u1": [("2026-01-01", "2026-05-31", "白银"),
           ("2026-06-01", "9999-12-31", "黄金")],
    "u2": [("2026-01-01", "9999-12-31", "白银")],
}
FACTS = [
    ("o1", "u1", "2026-04-10", 200),
    ("o2", "u1", "2026-06-05", 300),
    ("o3", "u2", "2026-03-01", 88),
    ("o4", "u1", "2026-07-01", 120),
]


def pit_join(fact, segments):
    """按事件时间二分定位生效区间,返回当时的维度值"""
    starts = [s[0] for s in segments]
    i = bisect_right(starts, fact[2]) - 1
    if i < 0:
        return None
    start, end, level = segments[i]
    return level if start <= fact[2] <= end else None


if __name__ == "__main__":
    for oid, uid, dt, amt in FACTS:
        pit = pit_join((oid, uid, dt, amt), DIM_LEVEL[uid])
        latest = DIM_LEVEL[uid][-1][2]
        flag = "" if pit == latest else "  <- 直接用最新版会错标"
        print(f"{oid} {uid} 下单于 {dt}: 时点等级 {pit}{flag}")
    print("要点:事实关联缓变维必须按事件时间取当时版本,直接取最新版是数据穿越,历史报表会被回写;拉链表加生效区间二分是标准解")
