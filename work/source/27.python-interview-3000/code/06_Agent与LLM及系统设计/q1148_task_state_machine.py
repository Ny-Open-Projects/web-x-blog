"""任务状态机:转换表校验 + 审计日志 + 按状态定义恢复语义。"""


TRANSITIONS = {
    "PENDING": {"RUNNING", "CANCELLED"},
    "RUNNING": {"PAUSED", "SUCCEEDED", "FAILED", "CANCELLED"},
    "PAUSED": {"RUNNING", "CANCELLED"},
    "FAILED": {"PENDING", "CANCELLED"},      # 重试 = 回到 PENDING
    "SUCCEEDED": set(),
    "CANCELLED": set(),
}


class Task:
    def __init__(self, tid):
        self.tid, self.state, self.log = tid, "PENDING", []

    def transition(self, to, reason=""):
        if to not in TRANSITIONS[self.state]:
            raise ValueError(f"非法转换 {self.state} -> {to}")
        self.log.append((self.state, to, reason))
        self.state = to

    def recover(self):
        """崩溃恢复:按当前状态决定动作。"""
        if self.state == "RUNNING":
            self.transition("FAILED", "crash_recovery")
            self.transition("PENDING", "auto_retry")
        return self.state


if __name__ == "__main__":
    t = Task("job-1")
    t.transition("RUNNING", "start")
    print("运行中崩溃,恢复 ->", t.recover())
    assert t.state == "PENDING"
    t.transition("RUNNING", "retry")
    t.transition("SUCCEEDED", "done")
    print("最终状态:", t.state)
    try:
        t.transition("RUNNING", "幽灵重启")
    except ValueError as e:
        print("非法转换被拦截:", e)
    for a, b, r in t.log:
        print(f"  {a} -> {b}  ({r})")
    assert len(t.log) == 5
