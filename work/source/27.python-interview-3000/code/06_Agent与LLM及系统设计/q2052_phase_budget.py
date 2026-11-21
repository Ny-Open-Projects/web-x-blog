"""请求超时的分段预算:总预算切成连接 排队 生成三段,逐段记账 超支挤占后段。"""


class PhaseBudget:
    SHARES = (("connect", 0.2), ("queue", 0.3), ("generate", 0.5))

    def __init__(self, total_ms):
        self.total = total_ms
        self.spent = {name: 0 for name, _ in self.SHARES}
        self.left = total_ms
        self.finished = False

    def share_ms(self, phase):
        share = dict(self.SHARES)[phase]
        return int(self.total * share)

    def enter(self, phase):
        """进入段:可用量取计划份额与剩余总额的较小者,前段超支自动挤压后段。"""
        if self.finished or self.left <= 0:
            raise TimeoutError("总预算已耗尽,拒绝进入 " + phase)
        return min(self.share_ms(phase), self.left)

    def exit(self, phase, used_ms):
        self.spent[phase] += used_ms
        self.left -= used_ms
        if self.left <= 0:
            self.left = 0
            self.finished = True
            raise TimeoutError("总预算耗尽于 " + phase)


if __name__ == "__main__":
    b = PhaseBudget(2000)
    assert b.enter("connect") == 400
    b.exit("connect", 380)
    assert b.enter("queue") == 600
    b.exit("queue", 700)                       # 排队超支 100
    assert b.left == 920
    assert b.enter("generate") == 920, "生成段计划 1000 但只剩 920"
    b.exit("generate", 900)
    assert b.left == 20 and not b.finished

    # 超支传染:前两段吃光预算,排队段退出即熔断,生成段进不去
    b2 = PhaseBudget(2000)
    b2.exit("connect", 400)
    try:
        b2.exit("queue", 1600)
        raise AssertionError("排队段吃光预算必须熔断")
    except TimeoutError as e:
        assert "queue" in str(e) and b2.finished
    try:
        b2.enter("generate")
        raise AssertionError("预算耗尽必须拒绝进入")
    except TimeoutError as e:
        assert "耗尽" in str(e)

    # 生成段中途耗尽也要熔断
    b3 = PhaseBudget(2000)
    b3.exit("connect", 400)
    b3.exit("queue", 600)
    try:
        b3.exit("generate", 1200)
        raise AssertionError("生成段超支必须熔断")
    except TimeoutError as e:
        assert "generate" in str(e)
        assert b3.left == 0 and b3.finished
    print("分段预算通过:三段记账,前段超支挤压后段,耗尽即熔断留段名")
