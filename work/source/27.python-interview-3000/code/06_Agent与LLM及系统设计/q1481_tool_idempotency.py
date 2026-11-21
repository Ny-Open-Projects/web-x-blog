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
