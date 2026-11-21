---
title: [Q1106] OpenTelemetry 概念与手动 span
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1106 · OpenTelemetry 概念与手动 span

> 难度:★★★★ | 标签:OpenTelemetry, tracing

**问**:讲讲 OpenTelemetry 的模型,手动埋一个 span 长什么样?

**答**:OTel 三件套:API(发起方埋点接口)、SDK(实现采样、处理、导出)、Exporter(把 span 送去 Jaeger/Tempo 等)。核心模型是 span:名字、起止时间、attributes、状态、父子引用,多个 span 构成一棵 trace 树,上下文经 context 传播(进程内 contextvars、跨进程 traceparent 头)。手动埋点即 `with tracer.start_as_current_span("db_query")`,块内任何子调用自动挂为子 span;块结束记录耗时并导出。规范价值:埋点一次,后端可换。

```python
# file: code/05_数据分析与工程化/q1106_manual_span.py
import itertools
import time

_ids = itertools.count(1)

class Span:
    def __init__(self, tracer, name, parent=None):
        self.id = next(_ids)
        self.name = name
        self.parent = parent
        self.tracer = tracer
        self.attrs = {}
        self.children = []
        self.dur_ms = None

    def __enter__(self):
        self.t0 = time.perf_counter()
        if self.parent:
            self.parent.children.append(self)
        return self

    def __exit__(self, *exc):
        self.dur_ms = (time.perf_counter() - self.t0) * 1000
        self.tracer.finished.append(self)

    def set_attr(self, k, v):
        self.attrs[k] = v

class Tracer:
    def __init__(self):
        self.finished = []

    def span(self, name, parent=None):
        return Span(self, name, parent)

    def render(self, span, depth=0):
        print("  " * depth + f"span {span.id} {span.name} {span.dur_ms:.1f}ms {span.attrs}")
        for c in span.children:
            self.render(c, depth + 1)

if __name__ == "__main__":
    tr = Tracer()
    with tr.span("http request") as root:
        root.set_attr("method", "GET")
        with tr.span("db query", parent=root) as s:
            s.set_attr("table", "orders")
        with tr.span("render", parent=root):
            pass
    tr.render(root)
    # 真实 OTel:with tracer.start_as_current_span("db_query") as span: span.set_attribute(...)
```

**追问**:
- 追问 1:traceparent 头里有什么?—— version-trace_id-span_id-flags,提取与注入即跨服务传播的全部秘密。
- 追问 2:采样策略有哪些?—— head sampling(入口决定整条是否记录)与 tail sampling(收集后按错误/延迟保留),成本与覆盖的权衡。
