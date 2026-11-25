---
title: "[Q5768] Transport.abort 与 close：写缓冲是丢弃还是排空"
date: 2026-11-25
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5768 · Transport.abort 与 close：写缓冲是丢弃还是排空

难度：P7 ｜ 标签：asyncio、Transport、abort、close、背压、优雅关闭

基线：CPython 3.12.2，纯标准库；用"服务端不读、客户端写 3MB"构造写缓冲积压，对比 `close()` 与 `abort()` 后的 `get_write_buffer_size()`。

**问**：一个流式导出服务向客户端推 20MB CSV，客户端网络很慢。停机时对所有连接调 `transport.close()` 想"优雅收尾"，结果 2000 个连接各自积压 3～4MB 用户态写缓冲，进程 RSS 涨到 14GB 被 OOM Kill；另一次为了快速释放内存改成全部 `abort()`，正常完成的下载却出现"文件少了最后 200KB"，客户端校验失败。`close()` 和 `abort()` 到底对写缓冲做了什么？`is_closing()` 为什么两者都返回 True？什么时候该用哪个？

**答**：

- **结论**：`transport.close()` 是**优雅关闭**：停止接收新写入，把 `_buffer` 里已有的数据继续写给内核，发完后再发 FIN（半关闭/关闭）；在数据排空之前，`get_write_buffer_size()` 仍然是积压的字节数，内存不会立刻释放。`transport.abort()` 是**立即中止**：丢弃用户态写缓冲，直接关闭底层 socket（通常触发 RST），`get_write_buffer_size()` 立刻变 0，`connection_lost()` 可能带 `ConnectionResetError`；对端可能收到截断的数据。两者都会让 `is_closing()` 返回 `True`，所以不能靠它区分"还在排空"和"已经丢弃"，要看 `get_write_buffer_size()`、`connection_lost` 的异常，以及业务上是否允许截断。
- **取舍**：正常业务完成必须用 `close()`（或 `write_eof()` 后等 `wait_closed()`），否则响应会被截断；只有"对端已经不可救药/我们要抢内存/安全中断"时才用 `abort()`。停机策略应该分层：先停止接新请求 → 给每个连接一个排空预算（如 5 秒）→ 预算内 `close()` 并等待 → 超时后 `abort()` 强制回收；不要一刀切。另一个取舍是背压：如果应用从不 `await drain()`，写缓冲会无限涨，`close()` 只是在"慢慢漏"，`abort()` 才是止血；根治要靠 `drain()` 或 `set_write_buffer_limits` + 应用层限速。
- **实战**：导出服务在 `finally` 里统一 `close()`，没有超时；慢客户端把缓冲撑爆。修复：① 每个连接记录 `created_at` 与 `get_write_buffer_size()`，停机时先 `close()`，用 `asyncio.wait_for(writer.wait_closed(), 5)` 等排空；② 超时后 `transport.abort()` 并计数 `force_aborted`；③ 正常运行中 `await writer.drain()` 做背压，写缓冲超过 8MB 就主动断开慢客户端。RSS 峰值从 14GB 降到 1.2GB，正常下载的截断归零。

下面用"服务端不读"稳定制造积压，验证：`abort()` 立即清空缓冲；`close()` 后缓冲原样保留（仍在排空）；再次 `abort()` 才清零。

```python
# Transport.abort 丢弃写缓冲; close 保留缓冲等待排空
import asyncio


async def main():
    release = asyncio.Event()

    async def handler(reader, writer):
        await release.wait()               # 故意不读, 让客户端写缓冲积压
        writer.close()

    server = await asyncio.start_server(handler, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    payload = b"x" * 3_000_000

    # 1) abort: 立即丢弃
    reader1, writer1 = await asyncio.open_connection("127.0.0.1", port)
    tr1 = writer1.transport
    tr1.set_write_buffer_limits(high=1024, low=512)
    tr1.write(payload)
    await asyncio.sleep(0.05)
    before_abort = tr1.get_write_buffer_size()
    print("[1] abort 前缓冲:", before_abort)
    assert before_abort > 0

    tr1.abort()
    await asyncio.sleep(0.05)
    print("[2] abort 后缓冲:", tr1.get_write_buffer_size(), "is_closing:", tr1.is_closing())
    assert tr1.get_write_buffer_size() == 0
    assert tr1.is_closing() is True

    # 2) close: 缓冲保留, 等待排空
    reader2, writer2 = await asyncio.open_connection("127.0.0.1", port)
    tr2 = writer2.transport
    tr2.set_write_buffer_limits(high=1024, low=512)
    tr2.write(payload)
    await asyncio.sleep(0.05)
    before_close = tr2.get_write_buffer_size()
    print("[3] close 前缓冲:", before_close)
    assert before_close > 0

    tr2.close()
    just_closed = tr2.get_write_buffer_size()
    await asyncio.sleep(0.05)
    after_wait = tr2.get_write_buffer_size()
    print("[4] close 后立即/50ms:", just_closed, after_wait, "is_closing:", tr2.is_closing())
    assert just_closed == before_close, "close 不丢缓冲"
    assert after_wait > 0, "对端不读时, 缓冲仍在排空"
    assert tr2.is_closing() is True

    # 3) 超时后强制 abort 回收
    tr2.abort()
    await asyncio.sleep(0.05)
    print("[5] 再次 abort 后:", tr2.get_write_buffer_size())
    assert tr2.get_write_buffer_size() == 0

    release.set()
    server.close()
    await asyncio.sleep(0.1)
    print("[6] 完成: 正常完成用 close, 超时/抢内存用 abort")


asyncio.run(main())
```

**追问一**：`close()` 之后还能 `write()` 吗？—— 不能可靠写入。`close()` 会把 transport 标记为 closing，后续 `write()` 通常被静默丢弃并打一条 warning（不同版本行为略有差异），`drain()` 可能抛 `ConnectionResetError`。正确顺序是"所有业务数据 `write` + `await drain` 完成 → `write_eof()`（可选）→ `close()` → `await wait_closed()`"，不要在 `close()` 后补数据。

**追问二**：为什么 `close()` 不立刻释放内存，而 `abort()` 可以？—— 因为 `close()` 的语义是"保证已接受的数据尽量送达"，用户态 `_buffer` 必须保留到内核可写；`abort()` 的语义是"放弃未发送数据"，可以直接清空 `_buffer` 并重置连接。前者是可靠性优先，后者是资源/时延优先。设计停机流程时，先算"最坏排空时间 = 缓冲字节 / 对端可接受速率"，超过预算就 abort，不要把 `close()` 当成"立即关闭"。

## 背诵要点

- `close()` 保留写缓冲并排空，`get_write_buffer_size()` 仍 >0；`abort()` 立即清空并强制关闭。
- 两者 `is_closing()` 都为 True，区分要看缓冲大小、`connection_lost` 异常和业务是否允许截断。
- 正常完成用 `close()` + `wait_closed()`；停机加排空预算，超时 `abort()` 止血；根治靠 `drain()` 背压。

## 复盘追问

- 为什么 2000 个慢连接会让 `close()` 把 RSS 撑爆？（每个连接的用户态缓冲都要保留到排空，close 不释放）
- `abort()` 后对端看到的是什么？（连接重置/截断，已发出的部分可能收到，但剩余数据丢失，客户端校验会失败）
