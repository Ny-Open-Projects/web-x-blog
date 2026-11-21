---
title: [Q821] APM 与 tracing 基础概念
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q821 · APM 与 tracing 基础概念

> 难度:★★★☆ | 标签:APM, tracing

**问**:APM 里的 trace 和 span 是什么?采样率怎么权衡?

**答**:**trace** 是一次请求的完整调用树,**span** 是树上一个计时节点(处理请求、查库、调下游),父子 span 组成时间线。观测价值:耗时分布一目了然——应用自身慢还是下游慢、哪个 SQL 慢;错误定位直接给出异常发生的精确位置。采样率控制开销:头部采样(入口决定整条 trace 是否记录)省资源但可能漏掉罕见错误;尾部采样(收集完再挑慢/错的)观测价值高但存储成本大。关键指标:应用耗时占比、下游耗时占比、错误 span 分布。

```python
# file: code/03_Web后端开发/q821_apm_span.py
from __future__ import annotations

import time
from typing import Optional

class Span:
    def __init__(self, name: str, parent_id: Optional[int] = None):
        self.name = name
        self.parent_id = parent_id
        self.t0 = time.perf_counter()

    def end(self):
        self.ms = round((time.perf_counter() - self.t0) * 1000, 1)

trace = []
root = Span("GET /orders")
trace.append(root)
child = Span("SELECT orders", parent_id=0)
trace.append(child)
time.sleep(0.01)
child.end()
root.end()
for s in trace:
    print(s.name, "parent:", s.parent_id, "ms:", s.ms)
```

**追问**:
- trace_id 和 request_id 什么关系?——request_id 是业务关联标识,trace_id 是链路追踪体系的标识,成熟的体系里 request_id 就用 trace_id。
- 不接 APM 能手工近似吗?——能,中间件计时 + 各依赖打点 + 日志聚合,就是手工版 span 树,规模化后必然要 APM。
