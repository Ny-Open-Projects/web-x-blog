"""慢请求分级超时:按请求等级分配总预算,并按比例切给各阶段,阶段超限即时失败。"""

TIERS = {"interactive": 1.0, "batch": 3.0, "background": 10.0}
STAGE_SHARES = {"retrieve": 0.3, "generate": 0.6, "reserve": 0.1}


class TimeoutPolicy:
    def __init__(self, clock):
        self.clock = clock                       # 可注入假时钟:返回当前秒

    def plan(self, tier):
        assert tier in TIERS, "未知请求等级"
        total = TIERS[tier]
        return {"tier": tier, "total": total,
                "stages": {k: total * v for k, v in STAGE_SHARES.items()}}

    def run_stage(self, budget, stage_fn):
        start = self.clock()
        result = stage_fn()
        if self.clock() - start > budget:
            raise TimeoutError("stage exceeded %.2fs budget" % budget)
        return result


if __name__ == "__main__":
    t = [0.0]
    clock = lambda: t[0]
    policy = TimeoutPolicy(clock)

    plan = policy.plan("interactive")
    assert abs(plan["stages"]["generate"] - 0.6) < 1e-9, "generate 占总预算六成"
    assert plan["stages"]["retrieve"] < plan["stages"]["generate"] < plan["total"]
    assert policy.plan("background")["total"] > policy.plan("batch")["total"]

    def fast_stage():
        t[0] += 0.2
        return "ok"
    assert policy.run_stage(plan["stages"]["retrieve"], fast_stage) == "ok"

    def slow_stage():
        t[0] += 0.5                              # 预算 0.3,直接冲到超限
        return "slow result"
    blew = False
    try:
        policy.run_stage(plan["stages"]["retrieve"], slow_stage)
    except TimeoutError:
        blew = True
    assert blew, "阶段超预算必须抛 TimeoutError 而不是拖着整条请求"
    print("分级超时通过:三级预算切分阶段,阶段超限即时失败,假时钟可测")
