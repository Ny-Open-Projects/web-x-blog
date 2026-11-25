---
title: "[Q5694] Server.wait_closed 在 3.12 变成等所有连接断开"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5694 · Server.wait_closed 在 3.12 变成等所有连接断开

难度：P7 ｜ 标签：asyncio、start_server、wait_closed、优雅停机、3.12 行为变更

**问**：优雅停机代码是 `server.close()` 然后 `await server.wait_closed()`，3.11 上秒过，升到 3.12 后停机卡满 30s 被 K8s `SIGKILL`，连接被硬切。`close()` 和 `wait_closed()` 各自等什么？3.12 改了什么？为什么"等连接自己结束"不能当作优雅停机？正确顺序是什么？

**答**：
结论：`server.close()` 只做一件事——停止监听、不再 accept 新连接，**已有的连接继续服务**。`wait_closed()` 的语义在 3.12 变了：早期版本只等"监听 socket 关闭完成"，3.12 改为等 server 关闭**并且所有活动连接都结束**（`asyncio.Server` 开始跟踪连接）。于是"close 之后立刻 wait_closed"会一直挂到每个长连接（keep-alive、SSE、WebSocket）自己断开，而这些连接往往在等客户端主动关，双方互等 → 停机超时 → 被 `SIGKILL`。

取舍：a) 停机要分两步：先 `close()` 停止接入，再对连接发"该走了"的信号（HTTP 响应加 `Connection: close`、WebSocket 发 close 帧），并设一个**短于编排系统 grace period** 的等待上限；b) 用 `asyncio.wait_for(server.wait_closed(), timeout)` 兜底，超时后主动取消所有连接任务（自己维护 Task 集合，或 `loop.shutdown_asyncgens` 之外再遍历）；c) 不要用 `wait_closed()` 当"等连接排空"的唯一手段，它没有超时参数，也不区分"空闲长连接"和"正在传输的连接"。

实战：事故形态是"发版时 Pod 进入 Terminating，preStop 睡 5s，应用 close 后 wait_closed 卡住，30s 后 SIGKILL，长轮询客户端全部报错重连，形成重连风暴"。下面演示 3.12 下 `wait_closed` 被活动连接挂住、客户端断开后才返回，以及带超时的兜底写法。

```python
import asyncio
import time


async def handle(reader, writer):
    try:
        await reader.read(1)          # 等客户端发数据或断开
    finally:
        writer.close()


async def main():
    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    reader, writer = await asyncio.open_connection("127.0.0.1", port)

    server.close()                     # 只停止 accept，不断已有连接
    t0 = time.monotonic()
    try:
        await asyncio.wait_for(server.wait_closed(), 0.2)
        print("[1] wait_closed 立即返回")
    except TimeoutError:
        print("[1] 3.12：被活动连接挂住 %.2fs" % (time.monotonic() - t0))

    writer.close()
    await writer.wait_closed()          # 客户端先走
    await asyncio.wait_for(server.wait_closed(), 1)
    print("[2] 连接清空后 wait_closed 返回")

    # 兜底写法：无论连接是否排空，停机都有上限
    server2 = await asyncio.start_server(handle, "127.0.0.1", 0)
    port2 = server2.sockets[0].getsockname()[1]
    r2, w2 = await asyncio.open_connection("127.0.0.1", port2)
    server2.close()
    try:
        await asyncio.wait_for(server2.wait_closed(), 0.1)
    except TimeoutError:
        print("[3] 超时兜底：主动断开剩余连接")
        w2.close()
        await w2.wait_closed()
    await asyncio.wait_for(server2.wait_closed(), 1)
    print("[4] 兜底后正常退出")


asyncio.run(main())
```

**追问一**：`server.close()` 之后新连接会怎样？—— 监听 socket 关闭，内核拒绝新连接（客户端看到 `ConnectionRefused` 或 SYN 超时）。已经完成三次握手、还在 accept 队列里的连接也会被丢弃。所以"先 close 再等"会有一小段"客户端以为连上了、实际被重置"的窗口；严格的优雅停机要在 close 前先把实例从负载均衡摘除（K8s 的 readiness 探针失败 + preStop 延迟），让流量先停。

**追问二**：为什么 `wait_closed()` 没有 timeout 参数？—— 它的设计定位是"资源释放完成的通知"，不是"连接排空策略"。asyncio 把"何时强制断开"留给应用决定，因为不同协议（HTTP keep-alive、WebSocket、gRPC 流）的"优雅"定义不同。实际工程里几乎总要包一层 `wait_for`，并把"超时后如何取消连接任务"写清楚，否则 3.12 的行为变更会把老代码的隐藏假设直接暴露成线上故障。

## 背诵要点
- `close()` 只停 accept，已有连接继续；3.12 的 `wait_closed()` 会等所有活动连接结束。
- 长连接（keep-alive/SSE/WS）互等会让停机卡到编排系统的 grace period，最后被 SIGKILL。
- 优雅停机 = 先摘流量 + close + 通知连接关闭 + `wait_for(wait_closed, 短超时)` + 强制取消兜底。

## 复盘追问
- 3.11 停机秒过、3.12 卡 30s，行为差异在哪？（wait_closed 跟踪活动连接）
- 如何设计一个"有上限、可观测、不丢在途请求"的 asyncio 停机流程？（摘流量、drain、超时、强制取消）
