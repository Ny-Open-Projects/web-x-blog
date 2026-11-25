---
title: "[Q6203] StreamingResponse：客户端断开后生成器怎么收尾"
date: 2026-11-24
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6203 · StreamingResponse：客户端断开后生成器怎么收尾

难度：P7 ｜ 标签：FastAPI、StreamingResponse、ClientDisconnect、GeneratorExit、资源清理

**问**：SSE/大文件下载用 `StreamingResponse` 包一个异步生成器，用户关掉页面后，后台仍在查数据库、往一个没人读的 socket 写，连接和游标泄漏。框架怎么感知断开？生成器收到的是 `GeneratorExit` 还是 `CancelledError`？`request.is_disconnected()` 能主动查吗？为什么在生成器里 `except Exception` 兜不住？

**答**：
结论：ASGI 服务器在客户端断开时会投递 `http.disconnect`；Starlette 的 `StreamingResponse` 用 anyio task group 并发跑"监听断开"和"发送数据"，一旦收到断开，就取消发送任务，异步生成器在挂起点收到 `CancelledError`（同步生成器则是 `GeneratorExit`），`finally`/`aclose()` 负责释放资源。`GeneratorExit`/`CancelledError` 都继承 `BaseException`，`except Exception` 捕获不到；如果生成器吞掉它们继续 `yield`，框架会报 "async generator ignored GeneratorExit" 或直接断开异常。

取舍：a) 长流式接口在每轮循环检查 `await request.is_disconnected()`，主动退出，别等发送失败；b) 资源释放放 `finally`，用 `async with`/`contextlib.aclosing` 保证 `aclose` 被调用；c) 发送端捕获 `ClientDisconnect`/`BrokenPipeError` 只做"停止生产"，不要转成 500 再写响应（响应头已发）；d) 不要在生成器里做不可中断的同步阻塞，取消只能发生在 await 点；e) 上游数据库游标要显式关闭，别依赖 GC。

实战：事故形态是"日志导出接口用 StreamingResponse 边查边发，用户取消后生成器卡在 `await cursor.fetchmany()` 的同步驱动里，游标一直占着连接，几次之后连接池耗尽；改成 `async for` + `is_disconnected` 检查 + `finally: await cursor.close()` 后恢复"。下面演示消费者提前退出时生成器的 `finally` 与 `aclose`。

```python
import asyncio


class ClientGone(Exception):
    pass


async def stream_body(n):
    try:
        for i in range(n):
            await asyncio.sleep(0.01)
            yield f"chunk-{i}"
    finally:
        print("[gen] finally 执行，释放游标/连接")


async def send_all(disconnect_after):
    sent = 0
    gen = stream_body(100)
    try:
        async for chunk in gen:
            if sent >= disconnect_after:
                raise ClientGone
            sent += 1
            print("[send]", chunk)
    except ClientGone:
        print("[1] 检测到客户端断开，停止发送")
    finally:
        await gen.aclose()
        print("[2] 已显式关闭生成器")


asyncio.run(send_all(3))
```

**追问一**：`request.is_disconnected()` 为什么不能随便调？—— 它内部会 `receive()` 一条消息；如果当前有其他组件（比如读取请求体）也在等 `receive`，两者会抢同一个 ASGI 消息队列，可能导致请求体读取卡住或消息丢失。StreamingResponse 场景下响应已开始、请求体通常已读完，主动查相对安全；但要在应用层确保没有并发 `receive`，否则用框架的断开监听更稳。

**追问二**：为什么断开后不要继续 `yield`？—— 连接已经不可写，继续 `send` 会抛 `ClientDisconnect`/`BrokenPipeError`，框架可能把它记成 500 或 "ASGI callable returned without completing response"；更糟的是生成器吞掉取消后继续跑，占用 worker 和数据库资源。正确姿势是收到取消/断开就退出循环，`finally` 清理，让异常自然结束。

## 背诵要点
- 客户端断开 → ASGI `http.disconnect` → 框架取消发送任务；异步生成器收到 `CancelledError`，同步是 `GeneratorExit`。
- 两者都是 `BaseException`，`except Exception` 拦不住；吞掉会导致生成器无法关闭。
- 清理放 `finally` + `aclose`；长流主动 `is_disconnected()`；别在断开后继续 yield。

## 复盘追问
- 用户关页面后数据库游标为什么没释放？（生成器未被关闭/取消点被阻塞）
- 流式响应里捕获 `BrokenPipeError` 后还能返回 500 吗？（响应头已发，只能停止生产并记录）
