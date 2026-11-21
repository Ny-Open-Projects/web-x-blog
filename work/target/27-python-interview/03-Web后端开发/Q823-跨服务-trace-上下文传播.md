---
title: [Q823] 跨服务 trace 上下文传播
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q823 · 跨服务 trace 上下文传播

> 难度:★★★☆ | 标签:tracing, W3C

**问**:调用下游服务时,链路信息怎么传过去?为什么不该自造私有追踪头?

**答**:标准是 **W3C Trace Context** 的 `traceparent` 头:`00-{trace_id}-{span_id}-{flags}`,版本-链路-当前 span-采样标记。服务端解析后:trace_id 沿用实现全链路串联,自己的 span_id 生成新值,调用再下游时把 header 换成自己 span。不自造头的原因:APM/网关/多语言生态都认标准头,自造的私有协议每接一个服务都要写一次适配,最终必然收敛回标准。

```python
# file: code/03_Web后端开发/q823_trace_context.py

def make_traceparent(trace_id: str, span_id: str, sampled: bool = True) -> str:
    flags = "01" if sampled else "00"
    return f"00-{trace_id}-{span_id}-{flags}"

def parse_traceparent(header: str) -> dict:
    _, trace_id, span_id, flags = header.split("-")
    return {"trace_id": trace_id, "span_id": span_id, "sampled": flags == "01"}

tp = make_traceparent("4bf92f3577b34da6a3ce929d0e0e4736", "00f067aa0ba902b7")
print(tp)
print(parse_traceparent(tp))
```

**追问**:
- flags 里的采样标记有什么用?——下游据此决定是否记录自己的 span,保证同一条 trace 的采样决策一致。
- 消息队列场景怎么传播?——把 traceparent 放进消息属性/头,消费端解析后接续链路。
