"""Q2998 故障切换的多供应商编排:熔断+半开探测+优先级恢复。

多供应商容错不是简单的 try 下一家:每家要有独立熔断器(连续失败
开闸,冷却后半开放一个探测请求),探测成功才恢复正席;恢复后按
优先级回到主供应商,而不是永远黏在备胎上。编排器对上层只暴露一个
调用入口,把「此刻谁该接单」的决策全部收进去。
"""


class Circuit:
    CLOSED, OPEN, HALF_OPEN = "closed", "open", "half_open"

    def __init__(self, fail_threshold=2, cooldown=8.0):
        self.fail_threshold = fail_threshold
        self.cooldown = cooldown
        self.fail_streak = 0
        self.state = self.CLOSED
        self.opened_at = None

    def can_try(self, now):
        if self.state == self.CLOSED:
            return True
        if self.state == self.OPEN and now - self.opened_at >= self.cooldown:
            self.state = self.HALF_OPEN          # 放一个探测请求
            return True
        return False

    def on_result(self, ok, now):
        if ok:
            self.fail_streak = 0
            self.state = self.CLOSED             # 探测成功恢复正席
        else:
            self.fail_streak += 1
            if self.state == self.HALF_OPEN or \
               self.fail_streak >= self.fail_threshold:
                self.state = self.OPEN
                self.opened_at = now
                self.fail_streak = self.fail_threshold


class Provider:
    def __init__(self, name, priority, breaker=None):
        self.name = name
        self.priority = priority
        self.breaker = breaker or Circuit()

    def call(self, request):
        raise NotImplementedError                # 由测试桩覆写


class FailoverOrchestrator:
    def __init__(self, providers, clock):
        self.providers = sorted(providers, key=lambda p: p.priority)
        self.clock = clock
        self.trace = []

    def execute(self, request):
        now = self.clock()
        for p in self.providers:
            if not p.breaker.can_try(now):
                self.trace.append(p.name + ":skip")
                continue
            try:
                result = p.call(request)
            except Exception as exc:
                p.breaker.on_result(False, now)
                self.trace.append(p.name + ":fail(" + str(exc) + ")")
                continue
            p.breaker.on_result(True, now)
            self.trace.append(p.name + ":ok")
            return result, p.name
        raise RuntimeError("全部供应商不可用")


def main():
    now = [0.0]

    def make(name, fail_times):
        """桩:前 fail_times 次调用抛错,之后成功。"""
        state = {"n": 0}

        def call(request):
            state["n"] += 1
            if state["n"] <= fail_times:
                raise ConnectionError("down")
            return name + " 说:好的"

        p = Provider(name, priority=0)
        p.call = call                      # 覆写实例方法作为桩
        return p

    primary = make("primary", 99)                # 一直挂
    backup = make("backup", 1)                   # 首次失败随后恢复
    orch = FailoverOrchestrator([primary, backup], clock=lambda: now[0])

    # 第 1 次:primary 失败 -> backup 也失败 -> 整体失败
    try:
        orch.execute("q")
        raise AssertionError("应当整体失败")
    except RuntimeError as exc:
        assert "全部供应商" in str(exc)

    # 第 2 次:primary 还没熔断再试一次,失败后熔断;backup 成功
    out, who = orch.execute("q")
    assert who == "backup" and out == "backup 说:好的", (out, who)

    # 冷却期内 primary 被跳过,backup 直接接单
    now[0] = 3.0
    out2, who2 = orch.execute("q")
    assert who2 == "backup", who2

    # 冷却结束:primary 半开放探测,仍然失败,继续熔断
    now[0] = 12.0
    out3, who3 = orch.execute("q")
    assert who3 == "backup", who3                # 探测失败降级

    # 再冷却+探测成功:primary 恢复正席,按优先级回到主位
    now[0] = 25.0
    primary.call = lambda r: "primary 康复了"    # 探测时已恢复
    out4, who4 = orch.execute("q")
    assert who4 == "primary" and out4 == "primary 康复了", (out4, who4)
    assert primary.breaker.state == Circuit.CLOSED

    events = [t.split(":")[1].split("(")[0] for t in orch.trace]
    assert "fail" in events and "skip" in events and "ok" in events
    print("故障切换轨迹:", " | ".join(orch.trace))
    print("恢复后主供应商:", who4)


if __name__ == "__main__":
    main()
