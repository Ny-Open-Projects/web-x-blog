"""截止时间传播:每次下发绝对时刻 调用链越深剩余越少,子步骤按剩余预算自裁。"""
class FakeClock:
    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t

    def advance(self, ms):
        self.t += ms


class Deadline:
    def __init__(self, clock, total_ms):
        self.clock = clock
        self.deadline = clock() + total_ms

    def remain_ms(self):
        return self.deadline - self.clock()

    def child(self):
        d = object.__new__(Deadline)
        d.clock = self.clock
        d.deadline = self.deadline
        return d


def call_downstream(deadline, cost_ms, name):
    if deadline.remain_ms() <= cost_ms:
        return {"name": name, "ok": False,
                "reason": "剩余 %dms 不足 %dms" % (deadline.remain_ms(), cost_ms)}
    deadline.clock.advance(cost_ms)
    return {"name": name, "ok": True}


if __name__ == "__main__":
    clock = FakeClock()
    root = Deadline(clock, total_ms=100)
    r1 = call_downstream(root, 60, "llm-call")
    assert r1["ok"]
    assert root.remain_ms() == 40, "根预算被真实扣减"
    sub = root.child()
    assert sub.deadline == root.deadline, "子调用继承同一绝对时刻 不是新预算"
    r2 = call_downstream(sub, 50, "tool-call")
    assert not r2["ok"] and "不足" in r2["reason"], "剩余不够快速失败 不启动注定超时的工作"
    r3 = call_downstream(sub, 30, "cache-read")
    assert r3["ok"]
    r4 = call_downstream(root, 15, "last-mile")
    assert not r4["ok"], "根与子共享预算 最后一跳感知耗尽"
    assert root.remain_ms() == 10
    print("截止时间传播通过:绝对时刻下传 剩余自裁 穷途快速失败")
