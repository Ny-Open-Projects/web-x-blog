---
title: [Q5608] asyncore 退役与 asyncio 迁移演进
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5608 · asyncore 退役与 asyncio 迁移演进

> 难度:★★★★☆ | 标签:版本演进, asyncore, asyncio

**问**:标准库的 asyncore/asynchat 被移除了，老代码怎么办？迁移到 asyncio 的对应关系是什么？

**答**:结论：asyncore/asynchat（源自 1996 年的 medusa）是回调式多路复用框架，PEP 594 将其退役，3.12 起从标准库移除。迁移映射三件套：① `asyncore.dispatcher.handle_read/write` → asyncio 的 `StreamReader/Writer`（Q5573）或 `loop.add_reader` 低层 API；② `asynchat.async_chat` 的终止符协议 → `StreamReader.readline` / `readuntil(b"\r\n\r\n")`；③ `handle_accept` → `asyncio.start_server`（每连接回调）。典型坑：asyncore 时代的代码混用阻塞调用（DNS、文件）——迁移到 asyncio 后这些会直接阻塞 loop，要顺路换 `to_thread`/线程池；`log()` 覆写等隐式约定也要显式化。对老代码的三选一：完整改写为 asyncio（长投入）、用 `loop.add_reader` 做最小语义对齐（渐进）、第三方 backport `pyasyncore`/`pyasynchat`（临时续命，不解决根本问题）。这与 Q5045 的"退役电池升级"同属一条治理线，但本卡聚焦**网络框架**的迁移路径。

```python
# 老代码形态（3.12 已移除，仅示意，不可运行）：
#   import asyncore, asynchat
#   class Echo(asynchat.async_chat): collect_incoming_data / found_terminator ...
#
# 迁移目标：等价 echo server，对照表如下
import asyncio

async def handle(reader, writer):                     # ← handle_accept+handle_read
    while True:
        line = await reader.readline()                # ← asynchat 的 set_terminator(b"\n")
        if not line:
            break
        writer.write(line)                            # ← push()
        await writer.drain()                          # ← 背压（老框架没有）
    writer.close()
    await writer.wait_closed()                        # ← handle_close

async def main():
    server = await asyncio.start_server(handle, "127.0.0.1", 0)
    print("迁移后 echo server:", server.sockets[0].getsockname())
    r, w = await asyncio.open_connection(*server.sockets[0].getsockname()[:2])
    w.write(b"hi\n"); await w.drain()
    print("echo:", await r.readline())
    w.close(); await w.wait_closed()
    server.close(); await server.wait_closed()

asyncio.run(main())
```

**追问一层**:`loop.add_reader(fd, cb)` 与 `start_server` 的分层关系？什么场景退回低层 API？
**追二维**:老 asyncore 代码里"DNS 解析阻塞 accept 线程"这类问题，迁移后应落在哪层解决？

**背诵要点**
- PEP 594 退役、3.12 移除 asyncore/asynchat；老代码走改写/低层 API/backport 三选一。
- 映射：dispatcher→add_reader 或 Stream，asynchat 终止符→readuntil/readline。
- 迁移必须顺路清理隐式阻塞调用，否则事件循环背同样的锅。

**复盘追问**
- backport 方案的冻结风险（不再修漏洞）如何评估？提示：CVE 跟踪与边界隔离。
- 大存量 handler 如何渐进迁移？提示：阻塞 handler 包 to_thread，逐步内化。
