"""用户分群动态更新:T+1 规则重算、迁移清单与快照留痕"""

USERS = [
    # user_id, 昨日分群, 近7天消费, 近7天活跃天数
    ("u1", "high", 1200, 6),
    ("u2", "high", 100, 1),
    ("u3", "mid", 280, 4),
    ("u4", "low", 900, 7),
    ("u5", None, 260, 5),
]


def classify(consume_7d, active_days):
    """业务规则:高价值=消费>=1000 且活跃>=5;成长群=消费>=200;其余为低价值"""
    if consume_7d >= 1000 and active_days >= 5:
        return "high"
    if consume_7d >= 200:
        return "mid"
    return "low"


def refresh(rows):
    """重算分群并区分三类变化:迁移、保持、新用户入群"""
    moved, stayed, joined = [], [], []
    for uid, old_seg, consume, days in rows:
        seg = classify(consume, days)
        if old_seg is None:
            joined.append((uid, seg))
        elif seg != old_seg:
            moved.append((uid, old_seg, seg))
        else:
            stayed.append(uid)
    return moved, stayed, joined


if __name__ == "__main__":
    moved, stayed, joined = refresh(USERS)
    print("分群迁移:", moved)
    print("保持不变:", stayed)
    print("新用户入群:", joined)
    print("工程要点:分群结果按日期 append 快照,不做原地 update,便于回溯与迁移率监控")
