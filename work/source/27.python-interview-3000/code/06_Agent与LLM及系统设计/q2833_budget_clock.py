"""Q2833 Agent 步骤的预算时钟:时间片记账与收尾模式。

给整次运行一个时间预算,每步按预估领时间片、按实际耗时扣账;实际
超过预估的步骤记超支,剩余预算跌破水位线后运行进入收尾模式,后续
步骤自动换便宜路径,而不是被墙钟硬杀在半路留下一堆悬挂状态。
"""

WRAPUP_RATIO = 0.3


class BudgetClock:
    def __init__(self, total_ms):
        self.total = total_ms
        self.remaining = total_ms
        self.overruns = []
        self.mode = "normal"

    def charge(self, name, est_ms, actual_ms):
        """记账一步:先看模式,再按实际扣账,返回本步可用片。"""
        if self.mode == "normal" and self.remaining < self.total * WRAPUP_RATIO:
            self.mode = "wrap_up"
        self.remaining = max(0, self.remaining - actual_ms)
        if actual_ms > est_ms:
            self.overruns.append(name)
        return min(est_ms, self.remaining + actual_ms)


def pick_step_variant(clock, name):
    """收尾模式下选便宜路径:检索不重排、生成不展开。"""
    if clock.mode == "wrap_up":
        return name + ":lite"
    return name + ":full"


def main():
    clock = BudgetClock(1000)
    plan = [
        ("search", 150, 250),   # 超支
        ("read", 200, 300),     # 超支
        ("plan", 200, 200),
        ("draft", 300, 300),
    ]
    chosen = []
    for name, est, actual in plan:
        clock.charge(name, est, actual)
        chosen.append(pick_step_variant(clock, name))
    assert clock.overruns == ["search", "read"], clock.overruns
    assert chosen == ["search:full", "read:full", "plan:full", "draft:lite"], chosen
    assert clock.mode == "wrap_up", clock.mode
    assert clock.remaining == 0, clock.remaining
    print("各步实际选择:", chosen)
    print("超支步骤:", clock.overruns)
    print("最终模式:", clock.mode, "剩余预算:", clock.remaining)
    print("效果:预算快耗尽时自动转收尾,而不是中途被硬杀")


if __name__ == "__main__":
    main()
