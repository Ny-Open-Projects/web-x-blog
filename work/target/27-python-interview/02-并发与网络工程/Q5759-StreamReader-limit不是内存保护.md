---
title: "[Q5759] StreamReader 的 limit 不是内存保护：超限异常后的缓冲状态与帧长上限"
date: 2026-11-25
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5759 · StreamReader 的 limit 不是内存保护：超限异常后的缓冲状态与帧长上限

难度：P7 ｜ 标签：asyncio、StreamReader、limit、LimitOverrunError、readuntil、readexactly、背压、OOM

**问**：一个 TCP 网关用 `asyncio.start_server` 收上游推送，按行 `readline()` 解析，设置了 `limit=64*1024`。某次上游发来一条 5MB 的无换行 JSON，进程没有报错退出，但 RSS 一路涨到 OOM；另一次抓到 `LimitOverrunError`，团队在 except 里直接重连，结果丢了一段数据。`limit` 到底限制什么？超限异常发生后，已经读进缓冲的数据去哪了？为什么调大 limit 不能解决 OOM？

**答**：

- **结论**：`StreamReader(limit=N)` 限制的是**单次 `readuntil`/`readline` 在缓冲区内搜索分隔符的范围**：当缓冲区里已有超过 N 字节仍找不到分隔符，就抛 `LimitOverrunError`（`readline` 会把它转换成 `ValueError`）。它**不限制** `_buffer` 的大小，也**不阻止** transport 继续从 socket 读数据：`data_received` 会不断 `feed_data`，如果应用一直不消费（或消费速度慢于到达速度），缓冲区可以无限增长——所以"limit=64KB"完全挡不住 5MB 的单帧，OOM 来自缓冲，不是来自 limit。超限时**数据不会被丢弃**：`LimitOverrunError.consumed` 告诉你在缓冲区里扫描了多少字节，`_buffer` 仍然保留着这些字节；正确的恢复是先用 `readexactly(e.consumed)`（或 `read`）把已缓冲的数据取走，再决定丢弃/解析/断开，而不是直接重连。真正要防 OOM，得在应用层加"最大帧长"并在缓冲超过阈值时 `transport.pause_reading()`（asyncio 的流默认不做读背压）。

- **取舍**：a) 按行协议：`limit` 设成"业务允许的最大行 + 余量"，超限即视为协议错误，读出 `consumed` 后丢弃该帧或断开，绝不能无限调大；b) 长度前缀协议：用 `readexactly(4)` 读长度、校验 `<= max_frame` 再 `readexactly(n)`，`readexactly` 不受 limit 约束，帧长上限由业务显式控制；c) 背压：`StreamReader` 不自动暂停读取，需要拿到 transport（`writer.transport` 或自定义 Protocol）在 `len(reader._buffer)` 超阈值时 `pause_reading()`、消费后再 `resume_reading()`；d) 不要用 `readline` 解析不可信输入：无换行的超大 payload 是天然的 DoS 向量，改用带长度上限的分帧器。

- **实战**：事故形态是"上游一条 5MB 无换行 JSON 打爆网关"——`limit=64KB` 只保证 `readline` 在 64KB 时抛错，但 transport 早已把更多数据喂进 `_buffer`；代码的 `except ValueError: reconnect()` 把缓冲里已经收到的字节连同连接一起丢掉，重连后上游重发，再次超限，形成"重连风暴 + 内存锯齿"。修复：①协议改成"4 字节长度前缀 + JSON"，先校验长度上限（如 1MB），超限直接回错误帧并关闭；②过渡期保留按行解析，但捕获 `LimitOverrunError` 后用 `readexactly(consumed)` 把数据取出、按"超长帧"计数并丢弃到下一个换行；③在 `data_received` 层加缓冲水位监控，超过 8MB 就 `pause_reading` 并告警。

```python
# StreamReader.limit 只约束 readuntil 的搜索范围, 缓冲区可以远超 limit
import asyncio

async def main():
    reader = asyncio.StreamReader(limit=64)

    # 1) feed_data 不受 limit 约束: 缓冲区直接涨到 1000 字节
    reader.feed_data(b"x" * 1000)
    print("→ 缓冲区:", len(reader._buffer), "字节, limit =", reader._limit)
    assert len(reader._buffer) == 1000
    assert len(reader._buffer) > reader._limit

    # 2) 超限异常不丢数据: consumed 表示扫描过的字节, 缓冲仍在
    over = None
    try:
        await reader.readuntil(b"\n")
    except asyncio.LimitOverrunError as e:
        over = e
        print("→ LimitOverrunError: consumed =", e.consumed, "| 缓冲还剩", len(reader._buffer))
    assert over is not None and over.consumed == 1000
    assert len(reader._buffer) == 1000

    # 3) 正确恢复: 先取走已缓冲的数据, 再决定丢弃或解析
    data = await reader.read(over.consumed)
    assert data == b"x" * 1000
    assert len(reader._buffer) == 0
    print("→ 用 consumed 取回完整数据:", len(data), "字节")

    # 4) read(n) 不受 limit 限制
    reader.feed_data(b"y" * 5000)
    chunk = await reader.read(5000)
    print("→ read(5000) 在 limit=64 下仍可读到:", len(chunk))
    assert len(chunk) == 5000

    # 5) 分隔符在 limit 内时正常返回(包含分隔符)
    reader.feed_data(b"ok\nrest")
    line = await reader.readuntil(b"\n")
    print("→ 正常 readuntil:", line)
    assert line == b"ok\n"

    # 6) 长度前缀协议: readexactly 不受 limit 约束, 帧长由业务校验
    reader.feed_data(b"z" * 10_000)
    body = await reader.readexactly(10_000)
    assert len(body) == 10_000
    print("→ readexactly 读取 10KB 帧:", len(body), "字节")

    # 7) limit 太小会把正常长行判成错误: 业务上限要匹配协议
    reader2 = asyncio.StreamReader(limit=8)
    reader2.feed_data(b"0123456789\n")
    msg = ""
    try:
        await reader2.readline()
    except ValueError as e:
        msg = str(e)
        print("→ readline 超限转成 ValueError:", e)
    assert "longer than limit" in msg

asyncio.run(main())
```

**追问一**：为什么 asyncio 的流不做读背压，而写方向有 `drain`？—— 写方向有明确的"应用产生数据"的入口：`write()` 把数据放进 transport 缓冲，`drain()` 在超过 high water 时挂起协程，形成背压。读方向的入口是内核：transport 收到 `data_received` 就必须尽快把内核缓冲搬走，否则内核窗口关闭、对端阻塞；标准库的 `StreamReaderProtocol` 选择"先收进用户态缓冲"，把"是否暂停"交给应用——但 `StreamReader` 没有暴露自动暂停策略，于是缓冲区成了无界队列。要背压只能自己拿 transport 调 `pause_reading()`/`resume_reading()`，或者用 `Protocol` 自己实现水位。结论：`limit` 是"解析安全阀"，不是"内存安全阀"，两者要分开设计。

**追问二**：`LimitOverrunError.consumed` 的确切含义是什么？为什么不能直接 `readline()` 重试？—— `consumed` 是"为了找分隔符，在缓冲区里已经扫描过的字节数"：如果分隔符在 limit 之外，扫描到 limit 就停下，此时 `consumed` 通常等于当前缓冲区长度（可能略小于，取决于实现的分块）；它告诉你"这 `consumed` 个字节属于当前这个超长帧"，可以先 `readexactly(consumed)` 取走，再继续找下一个分隔符。直接 `readline()` 重试没有意义：缓冲区还是那堆没有分隔符的数据，会再次超限；必须先消费或丢弃一段。另一个细节是 `readuntil` 在超限时**不会**把数据从缓冲里移除（它只是搜索失败），所以"异常后缓冲为空"的假设是错的，重连丢数据正是踩了这个假设。

## 背诵要点

- `limit` 只限制 `readuntil/readline` 的搜索范围，不限制 `_buffer`、不阻止 `feed_data`；OOM 来自无界缓冲，不是 limit。
- 超限抛 `LimitOverrunError`（`readline` 转 ValueError），`consumed` 是已扫描字节，数据仍在缓冲；先 `readexactly(consumed)` 再处理。
- `read(n)`/`readexactly(n)` 不受 limit 约束；防 OOM 要靠应用层最大帧长 + `pause_reading()` 读背压。

## 复盘追问

- 为什么把 limit 调到 10MB 仍然可能 OOM？（limit 只影响搜索失败点，transport 仍持续喂数据；缓冲上限要应用自己控制）
- 捕获 LimitOverrunError 后直接重连为什么会丢数据？（异常时数据还在 `_buffer` 里，重连把已收字节一起丢掉；应先按 `consumed` 取走）
