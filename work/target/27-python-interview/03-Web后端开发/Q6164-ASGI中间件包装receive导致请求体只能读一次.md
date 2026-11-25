---
title: "[Q6164] ASGI 中间件包装 receive 导致请求体只能读一次"
date: 2026-11-23
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6164 · ASGI 中间件包装 receive 导致请求体只能读一次

难度：P7 ｜ 标签：ASGI、中间件、receive、请求体、回放

**问**：纯 ASGI 中间件为了"记录请求体/做签名校验"包了一层 `receive`，先把 `http.request` 消息读完，再调用下游 app——为什么下游读到的 body 是空的？ASGI 的 `receive` 是"可重复消费的流"还是"一次性队列"？正确做法是什么——把读到的消息**回放**给下游，还是改用 `BaseHTTPMiddleware` 的 `.body()`？这和 Q6062/Q729 讲的"BaseHTTPMiddleware 任务泄漏与流式失效"是什么关系？

**答**：
结论：ASGI 的 `receive` 是**一次性消费的消息队列**（由服务器驱动，每次 `await receive()` 取一条并推进流），不是可反复读的 buffer。中间件先 `await receive()` 把 `http.request` 消息取走后，这些消息就从队列里消失了；下游 app 再 `await receive()` 只会拿到后续消息（通常是 `http.disconnect`）或空体——表现就是"日志里打印出了 body，但处理器里 `await request.body()` 是空的 / JSON 解析失败"。正确模式是**读一次 + 回放**：中间件把读到的消息存进列表，用一个生成器/迭代器封装成新的 `receive` 传给下游，下游读到的是同一批消息；注意回放要包含 `more_body` 标志与结束语义，且不能改变消息类型。

取舍：`BaseHTTPMiddleware` 提供 `.body()`/`Request` 对象看似方便，但它内部把请求体缓存到内存、用额外 task 桥接 receive/send，带来 Q6062/Q729 所述的"任务泄漏、流式响应失效、背压丢失"——在**请求体不大且不流式**时可用，性能敏感或流式场景应写纯 ASGI 中间件 + 手动回放。回放也有成本：整个 body 要驻留内存，所以要对大 body 设上限（超过就拒绝或只读前 N 字节），并避免把回放 buffer 做成另一个无界队列。

实战：事故形态是"加了一个 `X-Signature` 校验中间件后，所有 POST 接口报 'empty body' / 400"——根因就是中间件吞了 receive 没回放。排查看中间件里有没有"先读后不回放"的 `receive` 包装。下面用最小 ASGI 模拟三种情况：事故版（吞掉）、修复版（回放）、以及正常无中间件基线。

```python
import asyncio

async def downstream(scope, receive, send):
    body = b""
    while True:
        msg = await receive()
        body += msg.get("body", b"")
        if not msg.get("more_body", False):
            break
    await send({"type": "http.response.start", "status": 200, "headers": []})
    await send({"type": "http.response.body",
                "body": f"downstream got {body!r}".encode()})

def make_receive(payload):
    msgs = iter([{"type": "http.request", "body": payload, "more_body": False}])
    async def receive():
        return next(msgs, {"type": "http.disconnect"})
    return receive

async def run(mw):
    sent = []
    async def send(m): sent.append(m)
    await mw({"type": "http"}, make_receive(b'{"x":1}'), send)
    return sent[-1]["body"]

async def bad_mw(scope, receive, send):
    chunks = []
    while True:
        msg = await receive()
        chunks.append(msg)
        if not msg.get("more_body", False):
            break
    print("  middleware saw:", b"".join(c.get("body", b"") for c in chunks))
    # 事故：没有把 chunks 回放给下游
    return await downstream(scope, receive, send)

async def good_mw(scope, receive, send):
    chunks = []
    while True:
        msg = await receive()
        chunks.append(msg)
        if not msg.get("more_body", False):
            break
    it = iter(chunks)
    async def replay():
        return next(it, {"type": "http.disconnect"})
    return await downstream(scope, replay, send)

async def main():
    print("baseline :", await run(downstream))
    print("bad  mw  :", await run(bad_mw))
    print("good mw  :", await run(good_mw))

asyncio.run(main())
```

**追问一**：为什么回放 `receive` 时不能只回放 `body` 字节、必须回放完整消息（含 `more_body`）？——因为 `more_body` 是 ASGI 流控协议的一部分：下游靠它决定"是否继续 await 下一条"。若中间件把多条 `http.request` 消息合并成一条并丢掉 `more_body`，下游会**提前结束读取**，丢弃后续分块；反过来若错误地置 `more_body=True` 却没后续消息，下游会一直 await 到 `http.disconnect` 才结束，可能挂住。回放必须保真"消息序列"，不是"字节拼接"。

**追问二**：大文件上传场景，回放中间件的内存账怎么算？——回放要求把整个 body 驻留内存直到下游读完，所以内存 ≈ 请求体大小 × 并发数；一个 100MB 上传 × 10 并发就是 1GB。防线是设 `max_body_bytes` 上限（超过直接 413 或只做流式增量校验而不缓存全量），或对"只需要校验不需要读全量"的场景改在网关/代理层做。Q6062/Q729 提到的 `BaseHTTPMiddleware` 同样缓存 body，二者都不适合大文件——这正是"流式请求要在入口层处理，不进通用中间件"的原因。

## 背诵要点
- ASGI `receive` 是一次性消费队列，不是可重复 buffer；中间件先读会吞掉下游的 body。
- 修复：读一次 + 把完整消息序列（含 more_body）回放入新的 receive 传给下游。
- BaseHTTPMiddleware 缓存 body + 额外 task，有任务泄漏/流式失效（Q6062/Q729）；大 body 回放要设上限或改在入口层处理。

## 复盘追问
- 加了签名校验中间件后所有 POST 报 empty body，如何用"receive 一次性消费"定位并给出回放修复？（吞消息 vs 回放完整消息序列，讨论与 BaseHTTPMiddleware 的取舍）
- 为什么回放时只回放 body 字节会破坏 ASGI 协议？（more_body 决定下游读取终止，必须保真消息序列而非字节拼接）
