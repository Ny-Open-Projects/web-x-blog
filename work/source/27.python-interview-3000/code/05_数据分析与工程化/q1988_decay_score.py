"""时间衰减活跃分:指数半衰期加权,近期活跃权重更大"""

USERS = {
    "alice": [1, 2, 3, 10],      # 活跃发生在 N 天前
    "bob":   [30, 29, 28],
    "cindy": [2],
    "dave":  [1, 3, 5, 7, 9, 11],
}
HALF_LIFE = 7.0


def decay_score(active_days_ago, half_life):
    return sum(0.5 ** (d / half_life) for d in active_days_ago)


if __name__ == "__main__":
    print(f"半衰期 {HALF_LIFE:.0f} 天:7 天前的活跃权重 0.5,14 天前 0.25,21 天前 0.125")
    print(f"{'用户':<8}{'衰减分':>8}{'活跃天数':>8}")
    scored = sorted(USERS.items(), key=lambda kv: -decay_score(kv[1], HALF_LIFE))
    for u, days in scored:
        print(f"{u:<8}{decay_score(days, HALF_LIFE):>8.2f}{len(days):>8}")
    by_count = dict(sorted(((u, len(d)) for u, d in USERS.items()), key=lambda kv: -kv[1]))
    print("对照(按活跃天数):", by_count)
    print("要点:半衰期取业务周期(周活跃 7 天/月活跃 30 天),不是数学参数;衰减分用于分层与召回,不跨业务比较绝对值")
