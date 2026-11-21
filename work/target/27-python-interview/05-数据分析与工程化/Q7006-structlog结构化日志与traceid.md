---
title: [Q7006] 结构化日志:structlog 上下文绑定与 trace_id 贯穿
date: 2026-11-18
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7006 · 结构化日志:structlog 上下文绑定与 trace_id 贯穿

> 难度:★★★ | 标签:日志, 可观测性, structlog

**问**：微服务排障要在五六个服务的日志里人工串 trace_id，还经常串不上。用 structlog 做结构化日志，上下文（trace_id/user_id）怎么做到贯穿异步任务和线程池而不串号？和 logging 原生方案比，工程收益在哪？

**答**：结论：trace_id 贯穿的难点是**上下文在跨执行域（asyncio task、线程池、进程池）时的传递与隔离**。structlog 的解法是 contextvars（`structlog.contextvars.bind_contextvars`）——contextvars 在 asyncio task 创建时自动拷贝、在线程池里需显式透传（`contextvars.copy_context()`），并配合中间件在入口绑定、出口解绑。日志工程收益不在"JSON 格式"本身，而在**查询效率（字段可索引）、采样与分级（ERROR 全收、INFO 采样）、与 trace/metrics 的关联（日志带 trace_id 即可跳转到链路）**。

原理与实战：
- contextvars 与 threading.local 的本质区别：contextvar 值随 asyncio task 上下文隔离，`asyncio.create_task` 自动继承当前 context，天然支持并发请求不串号；线程池（`loop.run_in_executor`）不自动继承，要么传参要么 `copy_context().run(fn)`。这就是"串号"事故的根因：老代码用全局变量绑 trace_id。
- 事故复盘：网关并发 100 请求时日志 trace_id 大量错配，根因是 middleware 里 `logger.info` 用了模块级 logger 并把 trace_id 存在模块级 dict（key 是线程 id，协程共用线程）。修复：`bind_contextvars(trace_id=...)` 进 contextvar，`clear_contextvars()` 在请求边界清理；线程池路径用 `ctx = contextvars.copy_context(); loop.run_in_executor(pool, ctx.run, fn)`。
- 落地三件套：中间件入口绑定（从 headers 提取 `traceparent`，无则生成）、`add_log_level`+JSON renderer 输出、异常时 `logger.exception` 自动带 stack。跨服务贯穿还要求**入口识别上游 trace 头**（W3C traceparent），否则每服务自造 id 链路必断。

```python
# 基线:Python 3.9+ 标准库(contextvars);structlog 仅注释示意,核心可运行
import contextvars, asyncio
from concurrent.futures import ThreadPoolExecutor

_request_ctx = contextvars.ContextVar("req", default=None)

def bind(trace_id: str) -> None:
    _request_ctx.set(trace_id)                    # structlog.contextvars.bind_contextvars 等价

def log(msg: str) -> dict:
    return {"msg": msg, "trace_id": _request_ctx.get()}

async def handler(tid: str, pool: ThreadPoolExecutor) -> dict:
    bind(tid)
    ctx = contextvars.copy_context()              # 关键:线程池显式透传上下文
    loop = asyncio.get_running_loop()
    side = await loop.run_in_executor(pool, ctx.run, lambda: log("io-task"))
    return log("handler-done") | {"side": side["trace_id"]}

async def main() -> None:
    pool = ThreadPoolExecutor(max_workers=2)
    r1, r2 = await asyncio.gather(handler("T1", pool), handler("T2", pool))
    print(r1["trace_id"], r1["side"])             # T1 T1 ——不串号
    print(r2["trace_id"], r2["side"])             # T2 T2
    pool.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
```

**追问**：
- 一层追问：为什么不用 MDC/NDC（logging 的 ThreadLocal 方案）？——threading.local 在 asyncio 下同一线程跑多个请求，天然串号；contextvars 是为协程设计的隔离原语，logging 生态现在也有 `logging.config`+contextvars 的适配（`ContextVarFilter`），但 structlog 的链式处理器在绑定/渲染上更顺手。
- 二层追问：日志采样怎么做才不丢关键信息？——分级采样：ERROR/WARN 全收；INFO 按流量哈希采样（同 trace 同决策，保证一条链路要么全收要么全丢，可整链还原）；慢请求/5xx 自动升采样。关键是"按 trace 采样"而不是"按条采样"。
- 三层追问：结构化日志上线后查询还是慢，瓶颈在哪？——通常在日志管道：JSON 日志要经采集→Kafka→ES，字段设计（高基数字段别做索引、消息体别进正排）决定查询性能；trace_id 必须是 keyword 不是 text，这个字段类型错误是最常见的"串得上但查不动"。
