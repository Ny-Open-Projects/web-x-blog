"""流失评分卡: 权重赋分 风险分层与 lift 校验"""

WEIGHTS = {
    "近7日未登录": 30,
    "客单价环比下降": 20,
    "未结客诉": 20,
    "距上次购买超1.5倍周期": 20,
    "新客未复购": 10,
}
USERS = [
    # id, 命中特征, 实际是否流失
    ("u1", ["近7日未登录", "客单价环比下降", "未结客诉", "距上次购买超1.5倍周期", "新客未复购"], True),
    ("u2", ["近7日未登录", "未结客诉"], True),
    ("u3", ["客单价环比下降", "新客未复购"], False),
    ("u4", ["距上次购买超1.5倍周期"], False),
    ("u5", ["近7日未登录", "距上次购买超1.5倍周期"], True),
    ("u6", ["近7日未登录", "客单价环比下降", "未结客诉"], True),
    ("u7", [], False),
    ("u8", ["新客未复购"], False),
]


def score(flags):
    return sum(WEIGHTS[f] for f in flags)


def band(s):
    if s >= 60:
        return "高危"
    return "中危" if s >= 40 else "低危"


if __name__ == "__main__":
    assert sum(WEIGHTS.values()) == 100, "权重必须配满 100 分"
    rows = []
    for uid, flags, churn in USERS:
        rows.append((uid, score(flags), band(score(flags)), churn))
    print("用户打分:")
    for uid, s, b, churn in rows:
        print(f"  {uid}: {s:3d} 分 {b} 实际流失={churn}")
    base = sum(c for *_, c in rows) / len(rows)
    print(f"整体流失率 {base:.1%}")
    for b in ["高危", "中危", "低危"]:
        grp = [c for _, _, bb, c in rows if bb == b]
        if not grp:
            continue
        rate = sum(grp) / len(grp)
        print(f"  {b}: n={len(grp)} 流失率 {rate:.0%} lift {rate / base:.2f}")
    hi = [c for _, _, bb, c in rows if bb == "高危"]
    assert sum(hi) / len(hi) > base, "高危组流失率必须显著高于整体"
    print("要点: 权重和恒为 100 便于解读, 分层阈值看 lift 定, 评分卡上线前必须用有标签样本回验")
