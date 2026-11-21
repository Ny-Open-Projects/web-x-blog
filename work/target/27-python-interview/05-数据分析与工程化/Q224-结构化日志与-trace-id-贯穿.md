---
title: [Q224] 结构化日志与 trace id 贯穿
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q224 · 结构化日志与 trace id 贯穿

> 难度:★★★ | 标签:logging, contextvars, trace id

**问**:一个请求经过多个函数和线程,日志怎么自动带上同一个 trace id?

**答**:用 **contextvars.ContextVar** 保存请求级上下文(trace_id、user_id),它是协程与线程安全的(每个任务独立上下文),比全局变量和 thread-local 更适配 asyncio。做法:中间件生成 trace_id 写入 ContextVar;logging.Filter 在每条日志注入该字段;日志输出 JSON,采集系统按 trace_id 聚合。这样任何一层打的日志都能串回同一请求,排查时 `trace_id=xxx` 一搜全链路。坑:在线程池里跑同步任务时,context 会随 `asyncio.run_coroutine_threadsafe`/`loop.run_in_executor` 复制传递,显式传参更保险。

```python
# file: code/05_数据分析与工程化/q224_context_log.py
import contextvars
import logging
import json

trace_id_var: contextvars.ContextVar[str] = contextvars.ContextVar(
    "trace_id", default="-"
)


class TraceFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = trace_id_var.get()
        return True


def make_logger() -> logging.Logger:
    lg = logging.getLogger("trace.demo")
    lg.setLevel(logging.INFO)
    lg.addFilter(TraceFilter())
    return lg


def handle_request(lg, tid: str) -> None:
    trace_id_var.set(tid)
    lg.info("handling")


def test_trace_id_injected(caplog):
    lg = make_logger()
    handle_request(lg, "t-42")
    assert trace_id_var.get() == "t-42"
```

**追问**:
- ContextVar 在线程池里有什么坑?——`run_in_executor` 不会自动复制上下文,要用 `contextvars.copy_context().run` 包裹;否则线程池任务里 trace_id 丢失。
- logging.Filter 和 Formatter 怎么配合?——Filter 从 ContextVar 取值塞 record,Formatter 模板输出字段;只改 Formatter 拿不到运行时值。
- 采样控制日志量?——DEBUG 采样或按 trace 开关(错误链路全量、正常链路 1%);全量 DEBUG 是成本灾难。
