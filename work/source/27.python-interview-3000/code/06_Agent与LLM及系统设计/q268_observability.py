"""轻量 tracer:记录每次 LLM 调用与工具调用的输入、输出、耗时,按 trace 聚合。"""
import time
import uuid


class Tracer:
    def __init__(self):
        self.spans: dict[str, list[dict]] = {}

    def span(self, trace_id: str, name: str, inputs, outputs, cost_ms: float):
        self.spans.setdefault(trace_id, []).append(
            {"name": name, "in": str(inputs)[:40], "out": str(outputs)[:40],
             "ms": round(cost_ms, 1)})

    def report(self, trace_id: str) -> str:
        spans = self.spans.get(trace_id, [])
        total = sum(s["ms"] for s in spans)
        lines = [f"  {s['name']:<12} {s['ms']:>6}ms  {s['in']} -> {s['out']}" for s in spans]
        return f"trace {trace_id} 共{len(spans)}步 总耗时{total:.0f}ms\n" + "\n".join(lines)


class TracedAgent:
    def __init__(self, tracer: Tracer):
        self.tracer = tracer

    def run(self, question: str) -> str:
        tid = uuid.uuid4().hex[:8]
        t0 = time.time()
        tool_out = "工具结果:北京 晴"          # 模拟工具
        time.sleep(0.01)
        self.tracer.span(tid, "tool_search", question, tool_out,
                         (time.time() - t0) * 1000)
        t1 = time.time()
        answer = f"根据[{tool_out}]回答:{question}"
        time.sleep(0.02)
        self.tracer.span(tid, "llm_generate", tool_out, answer,
                         (time.time() - t1) * 1000)
        print(self.tracer.report(tid))
        return answer


if __name__ == "__main__":
    TracedAgent(Tracer()).run("今天天气如何?")
