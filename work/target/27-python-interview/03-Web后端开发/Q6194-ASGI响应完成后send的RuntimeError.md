---
title: "[Q6194] ASGI 响应结束后的 send：后台任务把连接写崩"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6194 · ASGI 响应结束后的 send：后台任务把连接写崩

难度：P7 ｜ 标签：ASGI、send、more_body、RuntimeError、后台任务、双写

**问**：流式接口里 `yield` 结束后又启动了一个任务往里 `send`，日志出现 `RuntimeError: Unexpected ASGI message 'http.response.body', after response already completed`，连接被重置。ASGI 的 `send` 有什么状态机？`more_body` 为什么要显式写？为什么"发完还能再发"的假设会让整个请求 500？

**答**：
结论：ASGI 的响应是**单向状态机**：`http.response.start`（一次）→ 若干 `http.response.body`，最后一条必须 `more_body=False`；服务端收到"最后一条 body"（或 `Content-Length` 凑满）就认为响应完成，此后任何 `send` 都是协议错误，Starlette/Uvicorn 会抛 `RuntimeError` 并关闭连接。`more_body` 的默认值是 `False`——**漏写就等于声明"这是最后一块"**，后续再 `send` 全部非法。这也是流式生成器必须每块都写 `more_body=True`、最后一块写 `False` 的原因。

取舍：a) 想"响应后再干活"用 `BackgroundTasks` 或 `response.background`，它们跑在响应完成**之后**，不会再碰 `send`；b) 想在响应过程中推送，必须保持 `more_body=True` 直到真正结束，并且由同一个任务/生成器负责发；c) 双写场景（SSE 转 WebSocket、代理转发）只能有一个"owner"持有 `send`，其他协程通过队列交给 owner 发，避免并发 send 交错；d) 客户端提前断开时 `send` 会抛异常或成为空操作，必须捕获并停止生产，否则后台任务会继续烧 CPU。

实战：事故形态是"导出接口用 StreamingResponse 边查边写，查询结束后一个 `finally` 里又补发了一条'统计信息' body，导致偶发 500；只有在慢查询时触发，测试环境很快所以复现不了"。下面用一个最小的 ASGI 状态机演示 `more_body` 漏写、完成后 send、以及用队列串行化的正确写法。

```python
import asyncio


class ASGISend:
    def __init__(self):
        self.started = False
        self.done = False
        self.messages = []

    async def __call__(self, message):
        t = message["type"]
        if self.done:
            raise RuntimeError(
                f"Unexpected ASGI message {t!r}, after response already completed"
            )
        if t == "http.response.start":
            if self.started:
                raise RuntimeError("response already started")
            self.started = True
        elif t == "http.response.body":
            self.messages.append(message.get("body", b""))
            if not message.get("more_body", False):   # 默认 False = 最后一块
                self.done = True
        else:
            raise RuntimeError(f"unknown message {t!r}")


async def bad_stream(send):
    await send({"type": "http.response.start", "status": 200})
    await send({"type": "http.response.body", "body": b"part1"})   # 漏 more_body
    await send({"type": "http.response.body", "body": b"part2"})   # 已完成后又发


async def main():
    send = ASGISend()
    try:
        await bad_stream(send)
    except RuntimeError as e:
        print("[1]", e)
    print("[2] 已发出的 body:", send.messages, "done:", send.done)

    # 正确：每块 more_body=True，最后一块 False
    send2 = ASGISend()
    await send2({"type": "http.response.start", "status": 200})
    for chunk in (b"part1", b"part2"):
        await send2({"type": "http.response.body", "body": chunk, "more_body": True})
    await send2({"type": "http.response.body", "body": b"", "more_body": False})
    print("[3] 正确流式:", send2.messages, "done:", send2.done)

    # 多生产者：用队列把 send 串行化，只有一个 owner
    send3 = ASGISend()
    queue = asyncio.Queue()

    async def owner():
        await send3({"type": "http.response.start", "status": 200})
        while True:
            chunk = await queue.get()
            if chunk is None:
                await send3({"type": "http.response.body", "body": b"", "more_body": False})
                return
            await send3({"type": "http.response.body", "body": chunk, "more_body": True})

    async def producer(name):
        for i in range(2):
            await queue.put(f"{name}{i}".encode())

    task = asyncio.create_task(owner())
    await asyncio.gather(producer("a"), producer("b"))
    await queue.put(None)
    await task
    print("[4] 队列串行化:", send3.messages, "done:", send3.done)


asyncio.run(main())
```

**追问一**：`more_body` 漏写为什么不会立刻报错？—— 因为它默认 `False`，服务端看到"最后一块"就把响应标记完成，连接进入 keep-alive 或关闭；后续 `send` 才触发错误。也就是说**错误点在下一次写**，而不是漏写的那次，日志栈指向"无辜"的后续调用，排查时容易被误导。写流式代码时把 `more_body=True` 当成显式契约，每块都写，别依赖默认值。

**追问二**：客户端提前断开时 `send` 会怎样？—— 取决于服务器实现：Uvicorn 在连接关闭后 `send` 可能抛 `RuntimeError`/`ConnectionResetError`，也可能静默丢弃；Starlette 不会主动取消你的生成器（3.x 的行为），所以生产者必须自己检测 `await request.is_disconnected()` 或捕获发送异常来停止。否则一个已经没人看的 SSE 流会继续查库、继续算，把 worker 拖死。

## 背诵要点
- ASGI 响应是单向状态机：start 一次、body 若干，最后一条必须 `more_body=False`（默认就是 False）。
- 完成后任何 `send` 都是 `RuntimeError`；错误点在下一次写，容易误判。
- 只有一个 owner 持有 `send`；多生产者用队列串行化；响应后干活用 BackgroundTasks。

## 复盘追问
- 流式接口偶发 `Unexpected ASGI message ... after response already completed`，如何定位？（漏 more_body / 完成后补发）
- 多个协程都想往同一个响应写，怎么保证不交错？（单 owner + 队列）
