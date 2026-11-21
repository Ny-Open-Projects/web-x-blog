"""分群口径对齐检查:同一分群两种口径的人数差、差集样本与一致度"""

USERS_EVENTS = {
    "u1": {"pv": 12, "order": 1},
    "u2": {"pv": 3, "order": 0},
    "u3": {"pv": 0, "order": 2},
    "u4": {"pv": 0, "order": 0},   # 只有登录
    "u5": {"pv": 1, "order": 0},
    "u6": {"pv": 8, "order": 0},
    "u7": {"pv": 0, "order": 0},
}

DEF_A = {"name": "口径A 任意事件", "events": ("pv", "order")}
DEF_B = {"name": "口径B 关键事件", "events": ("order",)}


def segment(events, definition):
    return {u for u, ev in events.items()
            if any(ev.get(e, 0) > 0 for e in definition["events"])}


if __name__ == "__main__":
    seg_a, seg_b = segment(USERS_EVENTS, DEF_A), segment(USERS_EVENTS, DEF_B)
    print(f"{DEF_A['name']}: {len(seg_a)} 人 {sorted(seg_a)}")
    print(f"{DEF_B['name']}: {len(seg_b)} 人 {sorted(seg_b)}")
    print(f"仅 A 命中(有浏览无下单): {sorted(seg_a - seg_b)}")
    print(f"仅 B 命中: {sorted(seg_b - seg_a)}")
    jaccard = len(seg_a & seg_b) / len(seg_a | seg_b)
    print(f"Jaccard 一致度 = {jaccard:.2f},人数差 {len(seg_a) - len(seg_b)}")
    if jaccard < 0.9:
        print("结论:两张报表人数对不上是口径问题,先对齐事件清单再谈数据质量")
    print("要点:对齐检查输出差集样本和一致度,而不是只报两个总数;口径变更要留版本号")
