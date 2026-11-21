"""2PC 协调者故障:prepare 后崩溃,参与者凭决策日志恢复,全局结果不许分叉。"""


class Participant:
    def __init__(self, name):
        self.name = name
        self.staged = None
        self.value = None
        self.state = "init"

    def prepare(self, value):
        self.staged = value
        self.state = "prepared"
        return "yes"

    def commit(self):
        if self.state == "prepared":
            self.state = "committed"
            self.value = self.staged

    def abort(self):
        self.state = "aborted"
        self.staged = None


class Coordinator:
    def __init__(self):
        self.intent_log = []         # 现实里这是协调者的持久决策日志

    def run(self, parts, value, crash_after_prepare=False):
        votes = [p.prepare(value) for p in parts]
        all_yes = all(v == "yes" for v in votes)
        # 决策先落日志再广播:崩在何时都能凭日志恢复出唯一决议
        self.intent_log.append("will_commit" if all_yes else "will_abort")
        if crash_after_prepare:
            return None
        decision = "commit" if all_yes else "abort"
        for p in parts:
            (p.commit if decision == "commit" else p.abort)()
        return decision

    def recover(self, parts):
        """恢复:读决策日志补广播;日志为空视为未开始,按 abort 收场。"""
        if not self.intent_log:
            for p in parts:
                p.abort()
            return "abort"
        decision = "commit" if self.intent_log[-1] == "will_commit" else "abort"
        for p in parts:
            (p.commit if decision == "commit" else p.abort)()
        return decision


def assert_uniform(parts, decision):
    states = [p.state for p in parts]
    if decision == "commit":
        assert states == ["committed"] * len(parts), states
    else:
        assert all(s == "aborted" for s in states), states


if __name__ == "__main__":
    # 崩在 prepare 之后:参与者停在 prepared,恢复后统一提交
    c1 = Coordinator()
    parts1 = [Participant("a"), Participant("b")]
    assert c1.run(parts1, "v1", crash_after_prepare=True) is None
    assert all(p.state == "prepared" for p in parts1)
    # 参与者单方面不能拍板提交:等恢复而不是自作主张
    assert c1.recover(parts1) == "commit"
    assert_uniform(parts1, "commit")

    # 崩在一票否决场景:恢复后统一放弃
    class No(Participant):
        def prepare(self, value):
            self.state = "aborted"
            return "no"

    c2 = Coordinator()
    parts2 = [Participant("a"), No("b")]
    assert c2.run(parts2, "v2", crash_after_prepare=True) is None
    assert c2.recover(parts2) == "abort"
    assert_uniform(parts2, "abort")

    # 无决策日志的冷恢复:全部 abort,绝不猜一个 commit
    c3 = Coordinator()
    parts3 = [Participant("a")]
    assert c3.recover(parts3) == "abort"
    assert_uniform(parts3, "abort")
    print("2PC 恢复通过:决策日志先行,崩溃后恢复决议唯一,参与者永不单方面提交")
