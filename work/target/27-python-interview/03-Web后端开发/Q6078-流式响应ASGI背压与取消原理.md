---
title: [Q6078] StreamingResponse 的 ASGI 背压与取消原理
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6078 · StreamingResponse 的 ASGI 消息流与背压原理

> 难度:★★★★ | 标签:原理深挖, ASGI, StreamingResponse, 背压

**问**：`StreamingResponse` 的生成器每个 chunk 是怎么变成 HTTP 字节的（ASGI `http.response.body` 消息流）？生成器产出快于客户端接收时背压在哪一层生效——`await send()` 什么时候会阻塞？客户端中途断开时生成器怎么被通知（GeneratorExit/CancelledError 走哪条路）？为什么流式接口里生成器抛异常会变成"半截响应"且状态码已无法更改？

**答**：结论：ASGI 的响应是一条消息序列：`http.response.start`（状态+头，只能发一次）之后跟随若干 `http.response.body(body=..., more_body=True)`，最后一条 `more_body=False` 收尾——`StreamingResponse` 内部把你的迭代器逐块 `await send(...)`。背压有两层：a) **ASGI 服务器层**（uvicorn）：`send()` 把字节写进 transport 写缓冲，缓冲超过高水位（Q5573 的 drain 机制）时 send 的 await 挂起——这是唯一真正的背压传导；b) 应用层没有内建背压：生成器是"被拉"的，每次 send 前取一块，若你 `send` 不阻塞（缓冲未满）且生成器无限产出，上游数据源（数据库游标）就持续被拉——**背压没传导到数据源时要自己加**（batch + sleep(0)/信号量）。断开路径：客户端断开 → uvicorn 停止读 socket → ASGI 服务器给 scope 发 `http.disconnect` 并**取消该请求的协程**（`await send()` 处抛 `CancelledError`）→ 取消沿 await 链传播进生成器的 await 点；纯同步生成器则靠 close() 触发 GeneratorExit——两条路径都要生成器有 try/finally 清理（游标关闭、临时文件删除，Q5062 同理）。"半截响应"原理：`http.response.start` 发出后状态码/头已上线路，之后生成器抛异常只能取消后续 body——客户端拿到 200 + 截断的内容（若无 Content-Length/chunked 完整性标记则难以察觉，Q1892 的 trailer 校验是补救之一）。实战：流式生成器必须 try/finally + 异常时记录"已发送字节数"，监控里把"流中断率"与"半截响应"单列指标。

```python
# file: code/03-Web后端开发/q6078_streaming_backpressure.py
import asyncio, sys, time

# 1) 极简 ASGI 流式响应: 消息流形态(start 只能一次 + more_body 链)
async def streaming_app(scope, receive, send):
    await send({"type": "http.response.start", "status": 200,
                "headers": [(b"content-type", b"text/plain")]})
    sent = 0
    try:
        for chunk in range(3):                    # 模拟数据源分块
            await send({"type": "http.response.body",
                        "body": f"chunk-{chunk}\n".encode(), "more_body": True})
            sent += 1
    except asyncio.CancelledError:                # 客户端断开 -> 协程被取消
        print("生成器被取消: 已发", sent, "块, finally 清理(关游标)")
        raise
    await send({"type": "http.response.body", "body": b"", "more_body": False})

# 2) 模拟慢客户端背压: send 到达写缓冲高水位时挂起(服务器层背压)
class SlowSend:
    def __init__(self, delay=0.05):
        self.delay = delay; self.n = 0
    async def __call__(self, msg):
        if msg["type"] == "http.response.body" and msg.get("more_body"):
            await asyncio.sleep(self.delay)       # 慢客户端: send 挂起 = 背压传导
            self.n += 1

async def main():
    slow = SlowSend()
    t0 = time.perf_counter()
    await streaming_app({}, lambda: asyncio.sleep(0), slow)
    print(f"慢客户端下 3 块流式发送耗时 {(time.perf_counter()-t0)*1000:.0f}ms "
          f"(每块被 send 的背压拖住, 数据源速度被限制)")

    # 3) 半截响应演示: start 已发, 生成器中途炸 -> 状态码无法更改
    async def broken_stream(scope, receive, send):
        await send({"type": "http.response.start", "status": 200,
                    "headers": [(b"content-type", b"text/plain")]})
        await send({"type": "http.response.body", "body": b"partial", "more_body": True})
        raise RuntimeError("数据源炸了")          # 此时状态码已上线, 无法改 500

    async def swallow_send(msg): await asyncio.sleep(0)
    try:
        await broken_stream({}, lambda: asyncio.sleep(0), swallow_send)
    except RuntimeError as e:
        print("半截响应:", e, "-> 客户端拿到 200 + 截断 body(须用 chunked/trailer 或内容自校验兜底)")

    # 4) 应用层背压: 数据源拉取与 send 解耦, 批次间让出
    async def paced_stream(send, batch=2):
        for i in range(0, 6, batch):
            body = b"".join(f"row-{j}\n".encode() for j in range(i, i + batch))
            await send({"type": "http.response.body", "body": body, "more_body": True})
            await asyncio.sleep(0)                # 让出: 防止无限产出堆满缓冲
        await send({"type": "http.response.body", "body": b"", "more_body": False})
    await paced_stream(swallow_send)
    print("批次化 + 让出 = 应用层背压(数据源拉取速度跟随客户端)")

asyncio.run(main())
print("python:", sys.version.split()[0])
```

**追问**：1) `http.disconnect` 消息与协程取消是什么关系？——ASGI 规范里服务器应在断开时把 disconnect 事件放入 receive 流，同时**服务器实现会取消请求协程**（uvicorn 两者都做）；如果应用不 await receive 就收不到 disconnect 消息，所以靠取消传播是主路径，靠 receive 轮询是补充（长任务里定期 `await receive()` 检查断开）。2) StreamingResponse 与 `Content-Length` 的互斥关系？——流式不知道总长所以不发 Content-Length（HTTP/1.1 用 chunked 或连接关闭标界），这带来两个后果：无法断点续传（Range 需要 Content-Length/Range 支持）、代理/客户端只能靠 chunked 完整性判断——需要精确长度时先算总长（一次性查询聚合）再流式。3) 大 CSV 导出的正确分块策略？——分页查游标（server-side cursor，Q6053 深分页账联动）+ 每批 1000-5000 行攒 buffer + 批间 await 让出 + 全程 try/finally 关游标；观测指标是"单批延迟"与"客户端接收速率"，客户端速率长期低于产出速率就是背压降速的正常形态。

## 背诵要点
- ASGI 响应=start 消息（仅一次）+ 若干 body 消息（more_body 链收尾）；StreamingResponse 逐块 await send。
- 背压在服务器层：send 写缓冲超水位挂起（Q5573 机制）传导到生成器；应用层要自己批次化+让出，防数据源被无限拉取。
- 断开=取消传播（CancelledError）或同步生成器 GeneratorExit，必须 try/finally 清理；start 发出后状态码不可改，中途异常=200 半截响应。

## 复盘追问
- 你们的大导出接口有没有"客户端断开后游标/临时文件泄漏"的迹象？（提示：监控打开的游标数与临时目录大小，grep 生成器确认 try/finally，见 Q5062 清理语义）
- 半截响应事故怎么让客户端"能发现"？目前靠什么保证完整性？（提示：加行计数尾行/内容哈希 trailer 或导出后生成校验文件，把完整性检查写进客户端协议，见 Q1892）
