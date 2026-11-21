"""长流程取消传播:协作式检查点 + 子任务快速退出 + 已完成步骤保留。"""


class CancellationToken:
    def __init__(self):
        self.cancelled = False
        self.reason = None

    def cancel(self, reason="user"):
        self.cancelled, self.reason = True, reason

    def check(self):
        if self.cancelled:
            raise InterruptedError(f"cancelled: {self.reason}")


class Pipeline:
    def __init__(self, steps, token):
        self.steps, self.token = steps, token
        self.done, self.progress_events = {}, []

    def run(self):
        try:
            for i, (name, fn) in enumerate(self.steps):
                self.token.check()                       # 步骤边界协作检查
                self.progress_events.append((i / len(self.steps), name, "running"))
                result = fn(self.token)
                self.done[name] = result
                self.progress_events.append(((i + 1) / len(self.steps), name, "done"))
        except InterruptedError as e:
            self.progress_events.append((None, "pipeline", "cancelled"))
            return {"status": "cancelled", "completed": self.done, "reason": str(e)}
        return {"status": "ok", "completed": self.done}


def step(name, fail_after=None):
    def fn(token):
        token.check()                                    # 子任务内部也检查
        return f"{name} result"
    return fn


if __name__ == "__main__":
    token = CancellationToken()
    steps = [(s, step(s)) for s in ["fetch", "analyze", "write", "notify"]]
    pipe = Pipeline(steps, token)

    # 模拟用户在 analyze 后取消:包装 analyze 完成时触发
    orig = dict(steps)
    def analyze_with_cancel(token):
        token.check()
        token.cancel("user")
        return "analyze partial"                          # 取消发生在子任务内
    steps[1] = ("analyze", analyze_with_cancel)

    out = pipe.run()
    print("状态:", out["status"], "已完成:", list(out["completed"]))
    assert out["status"] == "cancelled"
    assert "fetch" in out["completed"] and "write" not in out["completed"], "已完成保留,未开始不执行"
    assert any(ev[2] == "cancelled" for ev in pipe.progress_events)
    print("取消传播:步骤边界 + 子任务内双层检查,进度事件流完整")
