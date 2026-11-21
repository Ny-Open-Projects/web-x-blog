"""Agent 并发隔离子会话:每个子任务独立上下文与预算,失败不污染主会话。"""


class SubSession:
    """子会话:独立 messages、独立预算、独立失败标记,主会话只接收摘要。"""

    def __init__(self, sid, task, budget=100):
        self.sid, self.task, self.budget = sid, task, budget
        self.messages, self.spent, self.failed = [], 0, False
        self.result = None

    def run(self, tool, args, max_attempts=10):
        """子任务循环:结果不完整就重试,预算耗尽即自熔断,异常向上抛给管理器。"""
        for _ in range(max_attempts):
            if self.spent + 10 > self.budget:
                self.failed = True
                return None
            self.spent += 10
            out = tool(args)
            if out is not None:
                self.messages.append(("tool", tool.__name__, str(out)[:30]))
                return out
        self.failed = True
        return None


class SubSessionManager:
    """管理器:派发子任务、隔离异常、聚合结果;主会话上下文永不接触子会话内部消息。"""

    def __init__(self, budget_each=100):
        self.budget_each = budget_each
        self.sessions = []

    def dispatch(self, task, tool, args_list):
        results = []
        for i, args in enumerate(args_list):
            ss = SubSession(f"{task}#{i}", task, self.budget_each)
            self.sessions.append(ss)
            try:
                out = ss.run(tool, args)
            except Exception as exc:         # 子会话异常被边界截住 记为该项失败
                ss.failed = True
                results.append({"sid": ss.sid, "error": str(exc)})
                continue
            results.append({"sid": ss.sid, "result": out})
        return results

    def aggregate(self, results):
        """聚合规则:错误折叠为一行,不携带子会话上下文;成功项保留。"""
        ok = [r["result"] for r in results if "result" in r and r["result"] is not None]
        bad = [r["sid"] for r in results if "error" in r or r.get("result") is None]
        return {"ok": ok, "failed_sids": bad}


if __name__ == "__main__":
    def fetch(args):
        if args.get("id") == 2:
            raise ValueError("源站 2 拒绝访问")
        return "doc-" + str(args["id"])

    def spam(args):                      # 无限重试型任务:预算会先耗尽
        return None

    mgr = SubSessionManager(budget_each=50)
    res = mgr.dispatch("fetch_docs", fetch, [{"id": 1}, {"id": 2}, {"id": 3}])
    agg = mgr.aggregate(res)
    assert agg["ok"] == ["doc-1", "doc-3"]
    assert agg["failed_sids"] == ["fetch_docs#1"], "异常子会话被隔离为失败项"

    blast = [s for s in mgr.sessions if s.failed]
    assert len(blast) == 1 and blast[0].sid == "fetch_docs#1"
    assert all(s.spent <= 50 for s in mgr.sessions), "子会话预算各自独立"

    mgr2 = SubSessionManager(budget_each=20)
    res2 = mgr2.dispatch("spam_task", spam, [{"x": 1}])
    agg2 = mgr2.aggregate(res2)
    assert agg2["ok"] == [] and agg2["failed_sids"] == ["spam_task#0"]
    assert mgr2.sessions[0].failed and mgr2.sessions[0].spent <= 20
    print("子会话隔离通过:异常与预算耗尽均被限制在子会话内,主会话只拿到聚合结果")
