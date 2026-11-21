---
title: [Q268] LLM 应用的可观测性怎么做
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q268 · LLM 应用的可观测性怎么做

> 难度:★★★★ | 标签:Agent, 可观测性

**问**:Agent 应用要追踪哪些指标和轨迹?和普通服务监控有什么不同?

**答**:三类数据:1) Trace——一次请求的完整链路:每次 LLM 调用的完整 messages、工具调用与结果、每步耗时,这是排查"为什么模型这么答"的唯一手段;2) Metrics——TTFT/总延迟、token 用量与成本、工具成功率、检索命中率、任务完成率;3) Feedback——用户点踩、人工抽检。与普通服务的差别:输入输出是长文本且非确定,必须保留完整 prompt 快照而非只记状态码;且要能按 session 聚合多轮调用。业界常用 Langfuse/LangSmith/OTel 落地。

```python
# file: code/06_Agent与LLM及系统设计/q268_observability.py
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
```

**追问**:
- trace 里必须存什么?——每次 LLM 调用的完整 messages(含 system 版本)、工具调用与结果、耗时与 token;只有状态码的监控对 LLM 排查毫无用处。
- prompt 里的 PII 怎么处理?——入库前脱敏或脱敏展示(保留调试能力),访问权限按角色收;trace 泄露 PII 是合规事故。
- 按 session 聚合为什么重要?——多轮会话中每轮独立调用,只有按 session 串起来才能还原「模型为什么这么答」。
