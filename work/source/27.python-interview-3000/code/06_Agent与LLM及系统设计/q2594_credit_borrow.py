"""Q2594 fair-share 的借还机制:闲时攒券,忙时爆量,封顶防抖。

纯 fair-share 对突发不友好;给租户发可积累的信用券,闲置期
攒券、突发期一次性消耗,封顶限制最大借用量,防长期闲置者
瞬间打满全场,防抖且可解释。
"""


def simulate(demand, cap, regen=1):
    credit = 0
    timeline = []
    served_total = 0
    for r, want in enumerate(demand):
        credit = min(cap, credit + regen)   # 闲置攒券,封顶
        use = min(want, credit)
        credit -= use
        served_total += use
        timeline.append((r, want, use, credit))
    return timeline, served_total


def main():
    demand = [0] * 10 + [8] + [0] * 3
    timeline, total = simulate(demand, cap=6)
    assert timeline[9] == (9, 0, 0, 6), timeline[9]     # 攒券封顶在 6
    assert timeline[10] == (10, 8, 6, 0), timeline[10]  # 突发 8 只放 6
    assert total == 6
    uncapped, total2 = simulate(demand, cap=100)
    assert uncapped[9] == (9, 0, 0, 10), uncapped[9]    # 无封顶攒到 10
    assert uncapped[10] == (10, 8, 8, 3), uncapped[10]  # 突发 8 全放,余 3 券
    print("时间线 轮 需求 放行 余券(封顶 6):")
    for row in timeline[8:11]:
        print("  ", row)
    print("封顶:突发只放 6;无封顶对照:一次放 8,余券 2 还能继续透支")


if __name__ == "__main__":
    main()
