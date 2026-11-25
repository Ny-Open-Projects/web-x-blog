---
title: "[Q6260] ASGI lifespan 关闭顺序：连接排空、依赖逆序释放与关闭超时"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6260 · ASGI lifespan 关闭顺序：连接排空、依赖逆序释放与关闭超时

难度：P7 ｜ 标签：ASGI、lifespan、优雅关闭、连接排空、逆序释放、SIGTERM、uvicorn、超时

基线：库知识卡，代码用标准库模拟 lifespan shutdown 的"停收 → 排空 → 逆序释放"编排。

**问**：一个 FastAPI 服务用 lifespan 管理 DB 连接池、Redis 客户端和 OTel exporter，`shutdown` 里按 db → redis → otel 的顺序 `close()`。滚动发布时偶发"新 Pod 起来了，旧 Pod 卡在 Terminating 30 秒后被 SIGKILL"，日志里只有 `waiting for connections to drain`，没有任何 close 日志；另一次提前 close 了 DB，结果排空中的请求在收尾时写审计表失败。lifespan.shutdown 到底在什么时机执行？关闭顺序应该怎么排？为什么要给每一步加超时？

**答**：

- **结论**：ASGI server 的关闭流程是：收到 SIGTERM → **停止 accept 新连接** → 等待在途请求结束（uvicorn 的 `timeout_graceful_shutdown`，默认 None 表示一直等）→ 发送 `lifespan.shutdown` → 应用执行清理 → 进程退出。关键推论：①`lifespan.shutdown` 在**连接排空之后**才执行，所以在这里 close 连接池是安全的——前提是排空真的能结束；②只要还有长连接（SSE、WebSocket、挂起的流式响应），排空就永远不结束，`lifespan.shutdown` **永远不会执行**，依赖不会被释放，最后 K8s 到 `terminationGracePeriodSeconds` 直接 SIGKILL；③清理顺序应该是**启动顺序的逆序**：先停后台消费者（不再拉新消息）、再关"生产者"（DB/Redis 写连接），最后关"观测/上报"（OTel），否则会出现"用已关闭的 DB 写审计日志"；④每一步都要有超时与独立 try/except，一个依赖卡住不能拖死后面的释放。

- **取舍**：a) 默认无限等排空：对 HTTP 短请求最优雅，但对长连接是灾难；必须设置 `timeout_graceful_shutdown`（小于 `terminationGracePeriodSeconds`），超时后强制断开；b) 先 close 依赖再排空：能让请求快速失败，但正在收尾的请求会报错（审计丢失、响应截断），不推荐；c) 逆序释放 + 每步超时：实现稍复杂，但能保证"即使 DB close 卡住，OTel 也能 flush"；d) 后台消费者要先停：否则 shutdown 期间还在拉消息，消息处理到一半连接被关，产生"已 ack 未完成"的丢消息。

- **实战**：事故形态是"滚动发布必卡 30 秒"——服务有一个 SSE 端点，客户端断线重连逻辑很激进，旧 Pod 停止 accept 后仍有几十条 SSE 连接挂着，uvicorn 无限等排空，`lifespan.shutdown` 不执行，OTel 的缓冲没 flush、DB 连接被内核断开，监控上出现"发布期间追踪缺失 + 连接错误尖刺"。修复：①设置 `timeout_graceful_shutdown=10`（小于 K8s 的 30s），超时强制关闭；②应用层在收到关闭信号时先给 SSE 客户端发 `event: close` 并主动结束流；③shutdown 按"停消费者 → 排空（带超时）→ 逆序关依赖（每步 5s 超时）"执行，每步打日志；④把 `terminationGracePeriodSeconds` 设为"排空 + 释放"的总预算再加余量。

```python
# 模拟 ASGI lifespan shutdown: 停收 -> 停消费者 -> 排空(带超时) -> 逆序释放
import asyncio

ACQUIRED = ["db", "cache", "otel"]      # 启动时的获取顺序

async def drain(delay):
    await asyncio.sleep(delay)

async def shutdown(log, drain_delay, drain_timeout=0.2, close_timeout=0.1):
    log.append("stop_accept")           # 1) 不再接新连接

    log.append("stop_consumer")         # 2) 后台消费者先停, 不再拉新消息
    try:
        await asyncio.wait_for(drain(drain_delay), drain_timeout)
        log.append("drained")
    except asyncio.TimeoutError:
        log.append("drain_timeout")     # 3) 排空超时: 强制继续, 不能卡死

    for dep in reversed(ACQUIRED):      # 4) 逆序释放
        try:
            await asyncio.wait_for(asyncio.sleep(0), close_timeout)
            log.append(f"close:{dep}")
        except asyncio.TimeoutError:
            log.append(f"close_timeout:{dep}")

async def main():
    log = []
    await shutdown(log, drain_delay=0.01)
    print("→ 正常关闭顺序:", log)
    assert log == [
        "stop_accept", "stop_consumer", "drained",
        "close:otel", "close:cache", "close:db",
    ]

    # 排空超时: 仍然要继续释放依赖
    log2 = []
    await shutdown(log2, drain_delay=1.0, drain_timeout=0.05)
    print("→ 排空超时后的顺序:", log2)
    assert log2[:3] == ["stop_accept", "stop_consumer", "drain_timeout"]
    assert log2[-3:] == ["close:otel", "close:cache", "close:db"]

    # 反例: 没有超时, 排空卡住 -> shutdown 永远到不了 close
    log3 = []
    async def bad_shutdown():
        log3.append("stop_accept")
        await drain(10)                 # 没有 wait_for
        log3.append("close:db")

    try:
        await asyncio.wait_for(bad_shutdown(), 0.05)
    except asyncio.TimeoutError:
        pass
    print("→ 无超时被 SIGKILL 前的日志:", log3)
    assert log3 == ["stop_accept"]      # 依赖一个都没释放

    # 关闭顺序依赖: cache 的 flush 需要 db, 所以 db 必须最后关
    order = [x.split(":")[1] for x in log if x.startswith("close:")]
    assert order.index("db") > order.index("cache") > order.index("otel")
    print("→ 释放顺序满足依赖: otel -> cache -> db")

asyncio.run(main())
```

**追问一**：为什么 `lifespan.shutdown` 在排空之后，而不是在收到 SIGTERM 时立刻执行？—— 因为 lifespan 的语义是"应用生命周期的结束"，server 希望先把"应用还在服务"的阶段收尾（让在途请求完成），再进入"应用要销毁"的阶段；如果先 shutdown，连接池已关，正在处理的请求会立刻失败，等于强制中断。这个设计对短请求很优雅，但对长连接不友好：server 不知道你的 SSE 什么时候结束，只能无限等或按 `timeout_graceful_shutdown` 强制断。所以应用必须自己参与：收到关闭信号时主动结束长连接，或者把长连接迁到独立的 server/端口，避免它们阻塞整个进程的优雅关闭。

**追问二**：逆序释放为什么重要？如果某个依赖的 `close()` 卡住，应该怎么办？—— 逆序是因为依赖关系通常是"后获取的依赖前面那个"：OTel exporter 可能用 HTTP 连接池，cache 客户端可能用 DB 做持久化，DB 是底座；先关底座会让上层的 flush/清理失败（本卡开头的"审计写不进去"就是先关了 DB）。每一步 `close()` 都要包 `wait_for`：卡住时记录 `close_timeout:dep`、继续关下一个，最后进程仍能退出；否则一个不响应 close 的客户端就能把整个 Pod 拖到 SIGKILL。实现上可以用 `AsyncExitStack`（它按注册的逆序回调，但默认不设超时），或者自己维护"资源栈 + 每步超时"；无论哪种，都要在日志里留下"哪一步超时"，否则下次排查仍然只能看到"卡在 Terminating"。

## 背诵要点

- 关闭顺序：停 accept → 停后台消费者 → 排空在途请求（带超时）→ 逆序释放依赖 → 退出；lifespan.shutdown 在排空之后才执行。
- 长连接（SSE/WebSocket）会让排空永不结束，shutdown 永不执行；必须设 `timeout_graceful_shutdown` 并主动结束长连接。
- 依赖按启动逆序释放（otel → cache → db），每步独立超时 + 日志；一个 close 卡住不能拖死后续释放。

## 复盘追问

- 为什么滚动发布时旧 Pod 卡在 Terminating、没有任何 close 日志？（长连接让排空不结束，lifespan.shutdown 没执行；需要 graceful timeout + 主动断流）
- 为什么不能先关 DB 再排空？（在途请求收尾还要写库，先关会导致审计/响应失败；应排空后再逆序释放）
