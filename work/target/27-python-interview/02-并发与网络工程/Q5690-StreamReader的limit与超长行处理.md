---
title: "[Q5690] StreamReader 的 limit 与超长行：LimitOverrunError 处理"
date: 2026-11-23
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5690 · StreamReader 的 limit 与超长行：LimitOverrunError 处理

难度：P6 ｜ 标签：asyncio、StreamReader、limit、readuntil、协议设计

**问**：接一个上游服务，正常返回多行文本，偶尔某一行特别长（一条无换行的 JSON 日志），`readline()` 就抛 `ValueError: Separator is found, but chunk is longer than limit`，连接直接废掉。这个 limit 是什么、默认多大？为什么 `readuntil` 抛的是 `LimitOverrunError`，`readline` 抛的是 ValueError？线上该怎么处理才不丢数据？

**答**：
结论：`StreamReader` 有缓冲上限 `limit`（默认 64KiB），`readline()` / `readuntil()` 在缓冲里找不到分隔符且长度超过 limit 时就会抛错——这是保护机制，防止对端给一个永不换行的流把内存吃光。`readuntil()` 抛 `asyncio.LimitOverrunError`，异常带 `consumed`（已搜索到的位置），数据仍在内部缓冲、可以自己 `read()` 取走；`readline()` 把这层包成 `ValueError`（3.12 实测 `__cause__` 为 None），语义更模糊。

取舍：三条路——a) 建连接时显式给 `limit`（`asyncio.open_connection(limit=...)` / `start_server(limit=...)`），适合"协议最大帧长已知"；b) 用 `readuntil` 自己处理 `LimitOverrunError`（先取走已缓冲部分再续读），适合"偶发超长但要有界限"；c) 改协议：长度前缀或固定分块，从根上消灭"超长行"。最差的是 `readline()` + 宽泛 `except ValueError` 继续用同一个 reader——异常后内部状态不明确，容易读到半行。

实战：事故形态是"上游某次返回了一个 200KB 的堆栈当单行，客户端 readline 抛错后整个连接被丢弃，重试又遇到同一行 → 死循环重试打爆上游"。下面演示：超限 `readline` 报错、把 limit 调大后正常、`readuntil` 抛 `LimitOverrunError` 并给出 `consumed`。

```python
import asyncio


async def main():
    reader = asyncio.StreamReader(limit=16)   # 默认是 64 KiB
    reader.feed_data(b"x" * 64 + b"\n")
    try:
        await reader.readline()
    except ValueError as e:
        print("[1] 超长行 readline ->", type(e).__name__, "|", e)

    reader2 = asyncio.StreamReader(limit=1024)
    reader2.feed_data(b"y" * 64 + b"\n")
    print("[2] 把 limit 调大后:", (await reader2.readline())[:10], "...")

    reader3 = asyncio.StreamReader(limit=16)
    reader3.feed_data(b"short\n" + b"z" * 64 + b"\n")
    print("[3] 单行不超限时正常读:", await reader3.readline())
    try:
        await reader3.readuntil(b"\n")
    except asyncio.LimitOverrunError as e:
        print("[4] readuntil 抛 LimitOverrunError, consumed =", e.consumed)


asyncio.run(main())
```

**追问一**：`LimitOverrunError` 之后数据会被丢掉吗？—— 不会。异常带 `consumed`，告诉你"最多搜到第 N 字节还没找到分隔符"，数据仍在缓冲里，可以 `await reader.read(n)` 取走已到达的部分再继续。`readline()` 把它包成 ValueError 后这层信息就丢了，所以生产代码处理"可能超长"的协议时应该直接用 `readuntil`，把超限当成正常控制流。

**追问二**：把 limit 调到 10MB 有什么风险？—— limit 是**每个连接**的缓冲上限，内存风险 = 并发连接数 × limit。1 万个连接 × 1MB 就是 10GB 的潜在占用（实际按需增长，但攻击者可以同时喂满）。合理做法是按协议最大帧长设置（比如 64KiB 或 256KiB），再在应用层对"单条消息大小"做二次校验并拒绝超限，而不是靠调大 limit 掩盖协议问题。

## 背诵要点
- StreamReader 的 `limit` 默认 64KiB，超限时 `readuntil` 抛 `LimitOverrunError`（带 consumed）、`readline` 包成 `ValueError`。
- `LimitOverrunError` 不丢数据：可按 consumed 取走已缓冲部分再续读；`readline` 的 ValueError 语义模糊，别当控制流。
- 内存风险 = 连接数 × limit，按协议最大帧长设限，并在协议层拒绝超长消息。

## 复盘追问
- 上游偶发超长行导致连接被丢、重试打爆上游，如何用 limit/readuntil 正确处理？（超限当控制流、消费已缓冲数据、协议层限长）
- 为什么"把 limit 调大"不是根治？代价是什么？（每连接内存、协议设计、攻击面）
