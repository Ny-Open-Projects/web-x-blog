---
title: [Q1481] 工具调用幂等框架:step_id 幂等表与结果重放
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1481 · 工具调用幂等框架:step_id 幂等表与结果重放

> 难度:★★★☆ | 标签:Agent, 幂等, 可靠性

**问**:模型重试或网络重发导致同一个工具步骤被调两次,怎么保证副作用只发生一次?

**答**:核心是给每个 Agent 步骤分配全局唯一的 step_id,执行前先查幂等表:状态是 done 就直接重放历史结果,状态是 pending 说明上次执行中断,绝不能盲目重发,要走工具自身的业务幂等键兜底。执行采用两阶段记录:先落 pending 再调用工具,成功后把结果原子地写成 done;调用抛异常则回滚为 failed,让重试路径可以安全重新进入。这样同一 step_id 无论重复请求多少次,工具的真实副作用计数都是 1,而调用方始终拿到一致的结果,只需用一个 replayed 标记区分新执行与重放。

```python
# file: code/06_Agent与LLM及系统设计/q1481_tool_idempotency.py
"""工具调用幂等框架:step_id 幂等表 + 结果重放,重复请求绝不二次执行副作用。"""
import json
import hashlib


class ToolRegistry:
    """真实工具集合,带副作用计数用于验证只执行一次。"""

    def __init__(self):
        self.side_effects = []

    def book_ticket(self, args):
        self.side_effects.append(("book", json.dumps(args, sort_keys=True)))
        return {"ticket_id": "T-" + hashlib.md5(json.dumps(args, sort_keys=True).encode()).hexdigest()[:6]}

    def refund(self, args):
        self.side_effects.append(("refund", json.dumps(args, sort_keys=True)))
        return {"refunded": args.get("order_id")}


TOOLS = {"book_ticket": lambda a: None, "refund": lambda a: None}


class IdempotentRunner:
    """幂等执行器:同一 step_id 只放行一次;中断在 pending 的请求可被安全恢复。"""

    def __init__(self, store, tools):
        self.store = store          # 持久层桩:step_id -> {"state", "result"}
        self.tools = tools
        self.executed = 0           # 实际执行计数,用于验证幂等

    def run(self, step_id, tool, args):
        rec = self.store.get(step_id)
        if rec and rec["state"] == "done":
            return dict(rec["result"], replayed=True)      # 重放历史结果
        if rec and rec["state"] == "pending":
            # 上次执行中断:副作用可能已发生,交由工具自身幂等键兜底
            return dict(rec.get("result") or {"error": "pending_recover"}, replayed=False)
        self.store[step_id] = {"state": "pending", "tool": tool}
        try:
            result = self._call(tool, args)
        except Exception as exc:                            # 失败回滚到未执行
            self.store[step_id] = {"state": "failed", "error": str(exc)}
            raise
        self.store[step_id] = {"state": "done", "result": result}
        return dict(result, replayed=False)

    def _call(self, tool, args):
        self.executed += 1
        fn = getattr(self.tools, tool)
        return fn(args)


if __name__ == "__main__":
    tools = ToolRegistry()
    store = {}
    runner = IdempotentRunner(store, tools)
    args = {"flight": "CA185", "seat": "A1"}

    first = runner.run("step-1", "book_ticket", args)
    again = runner.run("step-1", "book_ticket", args)       # 模型重试,同 step_id
    third = runner.run("step-1", "book_ticket", args)       # 网络层再重试一次

    assert first["replayed"] is False
    assert again["replayed"] is True and third["replayed"] is True
    assert again["ticket_id"] == first["ticket_id"]
    assert runner.executed == 1, "副作用必须只发生一次"
    assert len(tools.side_effects) == 1

    failed = 0
    try:
        runner.run("step-2", "no_such_tool", {})
    except AttributeError:
        failed = 1
    assert failed == 1 and store["step-2"]["state"] == "failed"
    assert runner.run("step-1", "book_ticket", args)["ticket_id"] == first["ticket_id"]
    print("幂等框架通过:3 次同 step_id 调用只执行 1 次副作用,失败步骤被记录为 failed")
```

**追问**:
- 幂等表的存储放哪里? 答:必须放在工具副作用真正发生之前的持久层,比如数据库唯一键或 Redis SETNX,放内存里进程一崩就失效;
- 工具本身不支持幂等怎么办? 答:在执行器里为它包一层业务键,如订单号加操作类型做唯一约束,把非幂等工具改造成可重试的。
