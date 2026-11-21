"""步骤级埋点与运行指标桩:结构化事件流 + 按工具聚合次数 耗时 失败率,输出慢步骤 top-k。"""
from collections import defaultdict


class StepTracer:
    """步骤埋点器:每次工具或 LLM 调用发一条事件,内存聚合成指标。"""

    def __init__(self):
        self.events = []

    def emit(self, run_id, step, kind, ms, tokens=0, ok=True):
        self.events.append({"run_id": run_id, "step": step, "kind": kind,
                            "ms": ms, "tokens": tokens, "ok": ok})

    def metrics(self):
        agg = defaultdict(lambda: {"count": 0, "ms": 0.0, "tokens": 0, "fail": 0})
        for e in self.events:
            a = agg[e["step"]]
            a["count"] += 1
            a["ms"] += e["ms"]
            a["tokens"] += e["tokens"]
            a["fail"] += 0 if e["ok"] else 1
        out = {}
        for step, a in agg.items():
            out[step] = {"count": a["count"], "total_ms": a["ms"],
                         "avg_ms": round(a["ms"] / a["count"], 1),
                         "tokens": a["tokens"], "fail_rate": round(a["fail"] / a["count"], 2)}
        return out

    def slowest(self, k=2):
        """按平均耗时给出 top-k 慢步骤,指导优化预算花在哪。"""
        m = self.metrics()
        return sorted(m.items(), key=lambda kv: -kv[1]["avg_ms"])[:k]

    def run_report(self, run_id):
        """按 run 汇总:总耗时 总 token 失败步骤清单。"""
        es = [e for e in self.events if e["run_id"] == run_id]
        return {"steps": len(es), "total_ms": sum(e["ms"] for e in es),
                "tokens": sum(e["tokens"] for e in es),
                "failed_steps": [e["step"] for e in es if not e["ok"]]}


if __name__ == "__main__":
    tr = StepTracer()
    tr.emit("run-1", "plan", "llm", ms=320, tokens=180)
    tr.emit("run-1", "search_web", "tool", ms=50)
    tr.emit("run-1", "search_web", "tool", ms=90, ok=False)
    tr.emit("run-1", "write_answer", "llm", ms=210, tokens=260)
    tr.emit("run-2", "search_web", "tool", ms=40)

    m = tr.metrics()
    assert m["search_web"] == {"count": 3, "total_ms": 180.0, "avg_ms": 60.0, "tokens": 0, "fail_rate": 0.33}
    assert m["plan"]["tokens"] == 180 and m["plan"]["fail_rate"] == 0.0

    slow = tr.slowest(k=2)
    assert [s[0] for s in slow] == ["plan", "write_answer"], "LLM 步骤最慢应排前"

    rep = tr.run_report("run-1")
    assert rep == {"steps": 4, "total_ms": 670, "tokens": 440, "failed_steps": ["search_web"]}
    assert tr.run_report("run-9")["steps"] == 0
    print("埋点指标通过:聚合 3 个步骤指标 失败率 0.33 慢步骤排序与 run 报告正确")
