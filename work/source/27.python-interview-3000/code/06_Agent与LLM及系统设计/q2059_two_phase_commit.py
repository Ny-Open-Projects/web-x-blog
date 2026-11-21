"""两阶段提交概念模拟:prepare 收齐选票,全票才 commit,任一否决即全员 abort。"""


class Participant:
    def __init__(self, name, vote=True):
        self.name = name
        self.vote = vote
        self.staged = None
        self.value = None
        self.state = "init"

    def prepare(self, value):
        """第一阶段:只把写暂存起来,不对外可见。"""
        if self.vote:
            self.staged = value
            self.state = "prepared"
            return "yes"
        self.state = "aborted"
        return "no"

    def commit(self):
        if self.state == "prepared":
            self.state = "committed"
            self.value = self.staged

    def abort(self):
        if self.state == "prepared":
            self.staged = None
        self.state = "aborted"


class Coordinator:
    def __init__(self, participants):
        self.parts = participants
        self.decision = None

    def run(self, value):
        votes = [p.prepare(value) for p in self.parts]
        if all(v == "yes" for v in votes):
            self.decision = "commit"     # 现实里先写决策日志再广播
            for p in self.parts:
                p.commit()
            return "commit"
        self.decision = "abort"
        for p in self.parts:
            p.abort()
        return "abort"


if __name__ == "__main__":
    # 全票:全员提交,值可见
    parts = [Participant("db_a"), Participant("db_b"), Participant("db_c")]
    assert Coordinator(parts).run("new_value") == "commit"
    assert all(p.state == "committed" and p.value == "new_value" for p in parts)

    # 一票否决:全员回滚,暂存清干净,没有半提交
    parts2 = [Participant("db_a"), Participant("db_b", vote=False),
              Participant("db_c")]
    assert Coordinator(parts2).run("x") == "abort"
    assert all(p.state == "aborted" for p in parts2)
    assert all(p.value is None and p.staged is None for p in parts2), \
        "abort 后任何参与者不得留下可见的新值"

    # 超时按否决处理:宁可错杀不可悬挂出不一致
    class SlowParticipant(Participant):
        def prepare(self, value):
            return "no"                  # 超时视同投否决票

    parts3 = [Participant("db_a"), SlowParticipant("db_slow")]
    assert Coordinator(parts3).run("y") == "abort"
    assert parts3[0].state == "aborted" and parts3[0].value is None
    print("两阶段提交通过:全票提交 一票否决全员回滚,超时按否决不悬挂")
