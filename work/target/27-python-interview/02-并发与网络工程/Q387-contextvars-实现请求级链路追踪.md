---
title: [Q387] contextvars 实现请求级链路追踪
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q387 · contextvars 实现请求级链路追踪

> 难度:★★★ | 标签:contextvars, 链路追踪, 并发

**问**:多线程/asyncio 服务里,怎么给每个请求一个 trace_id 并让全链路日志都带上?

**答**:全局变量会串请求,ThreadLocal 不适用于 asyncio。标准答案是 `contextvars.ContextVar`:每个任务/线程自动拥有独立上下文副本,`set()`/`get()` 即可,异步任务继承创建时的上下文。配合 logging 的 Filter 把 trace_id 注入每条日志,或注入日志格式串。这是 OpenTelemetry 等 APM 库的底层机制。

```python
# file: code/02_并发与网络工程/q387_contextvars_trace.py
"""contextvars + logging 实现请求级 trace_id。"""
import asyncio
import logging
import uuid
from contextvars import ContextVar

trace_id_var: ContextVar[str] = ContextVar("trace_id", default="-")


class TraceFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = trace_id_var.get()
        return True


log = logging.getLogger("svc")
log.setLevel(logging.INFO)
h = logging.StreamHandler()
h.setFormatter(logging.Formatter("[%(trace_id)s] %(message)s"))
h.addFilter(TraceFilter())
log.addHandler(h)


async def handle_request(tag: str):
    trace_id_var.set(uuid.uuid4().hex[:8])  # 每个请求设置自己的 trace_id
    log.info("%s 收到请求", tag)
    await asyncio.sleep(0.05)               # await 期间上下文不串
    log.info("%s 处理完成", tag)


async def main():
    # 两个并发请求,日志各自携带不同 trace_id
    await asyncio.gather(handle_request("req-A"), handle_request("req-B"))


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

**追问**:
- ContextVar 和 ThreadLocal 的区别?ThreadLocal 按线程隔离,同一协程任务切换会共享;ContextVar 按上下文隔离,asyncio 任务创建时自动拷贝上下文,线程中也各自独立,是统一方案。
- 如何把 trace_id 传给下游服务?放进 HTTP 头(如 W3C 的 traceparent),下游同样用 ContextVar 接住,形成跨服务链路。
