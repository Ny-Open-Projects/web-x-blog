"""Q2569 Agent 间超时预算切分:给子 Agent 分时间要留回收余量。

父 Agent 剩余 T 秒要派 N 个子任务:先扣结果回收预留,再按预期
代价加权分配,设下限防饿死、上限防一家独大;子 Agent 拿到的是
自己的绝对截止时刻,超时自己负责,父端绝不被拖过自己的死线。
"""
import time


def split_budget(parent_remaining, weights, floor, cap, reserve):
    usable = parent_remaining - reserve
    assert usable > 0, "父预算扣掉回收预留后为负"
    total_w = sum(weights)
    raw = [usable * w / total_w for w in weights]
    clipped = [min(cap, max(floor, r)) for r in raw]
    if sum(clipped) > usable:  # 上限下限裁剪后若超支,按余量比例收回
        over = sum(clipped) - usable
        room = [c - floor for c in clipped]
        total_room = sum(room)
        if total_room > 0:
            clipped = [c - over * r / total_room for c, r in zip(clipped, room)]
    return [round(c, 3) for c in clipped]


def main():
    budgets = split_budget(parent_remaining=10.0, weights=[4, 3, 1],
                           floor=0.5, cap=6.0, reserve=1.5)
    usable = 8.5
    assert sum(budgets) <= usable + 1e-6, budgets
    assert all(b >= 0.5 for b in budgets), budgets
    assert all(b <= 6.0 for b in budgets), budgets
    now = time.monotonic()
    deadlines = [now + b for b in budgets]
    assert max(deadlines) <= now + 10.0
    extreme = split_budget(10.0, [9, 9, 1], floor=0.5, cap=3.0, reserve=1.5)
    assert all(b <= 3.0 for b in extreme) and sum(extreme) <= 8.5 + 1e-6
    print("常规切分:", budgets, "合计", round(sum(budgets), 3), "预留 1.5s 给回收")
    print("封顶切分:", extreme, "← cap=3 生效,无一家独大")


if __name__ == "__main__":
    main()
