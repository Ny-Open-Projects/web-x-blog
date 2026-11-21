---
title: [Q1204] 长流程 Agent 的进度与取消传播
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1204 · 长流程 Agent 的进度与取消传播

> 难度:★★★☆ | 标签:多 Agent, 可靠性

**问**:一个跑 20 步的多 Agent 流程,用户中途取消,取消信号怎么传播到位?

**答**:取消要设计成"协作式":全局取消标志(或 context token),每个步骤边界检查;取消传播到子 Agent 时,子 Agent 要在工具调用间检查标志并快速退出,不能等长任务自然结束。取消后状态处理三选:全回滚(适合事务性)、保留已完成(检查点语义,常见)、标记取消但后台跑完(写操作收尾)。进度上报用步骤号 + 百分比 + 当前阶段描述,UI 靠它渲染;进度与取消共用同一事件通道,保证顺序一致。

```python
# file: code/06_Agent与LLM及系统设计/q1204_progress_cancel.py
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
```

**追问**:
- 已提交给外部 API 的调用怎么取消?答:外部副作用尽量幂等 + 补偿(发撤销请求),不可撤销的标记为"取消后仍将完成",通知层要能说明这一点。
- 取消和暂停语义怎么分?答:暂停保留全部状态可恢复(审批场景),取消是终态只保留已完成产物;UI 上两个按钮背后必须是两种状态机路径。
