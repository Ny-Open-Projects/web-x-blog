---
title: [Q5056] memoryview 零拷贝与 bytes 拼接的成本工程
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5056 · memoryview 零拷贝与 bytes/bytearray 拼接的成本工程

> 难度:★★★★ | 标签:memoryview, bytearray, bytes, 拷贝, 成本工程

**问**：二进制协议解析模块把收到的包逐个 `data = data + chunk` 拼接，吞吐上不去。bytes 拼接的真实成本是什么？bytearray、join、memoryview 各适合什么场景？"零拷贝"省的到底是哪一次拷贝？

**答**：bytes 是不可变对象，`a = a + b` 会**新分配一个 len(a)+len(b) 的缓冲区并把两边全量拷贝**——循环拼接是 O(n²) 总拷贝量，n 越大税越重。三条正路：a) 一次性已知所有分片用 `b"".join(chunks)`：join 先算总长、一次分配、精确拷贝一遍，实测与 `bytearray +=` 同档（约 0.5ms/2MB）；b) 流式追加用 `bytearray += chunk`（amortized O(1) 尾部追加，内部预留超额容量）；c) **不搬数据**用 `memoryview`：`mv = memoryview(buf)` 后 `mv[a:b]` 切片共享底层内存不复制，适合"解析头部后把 payload 原地转交"的协议处理。零拷贝省的是"用户态里从源缓冲复制到新缓冲"这一次——syscalls 层面（如 socket recv）的那次内核到用户态拷贝依然存在，要省它得 recv_into/sendfile。陷阱：持有 memoryview 期间原 bytearray **不能 resize**（会抛 `BufferError: Existing exports of data: object cannot be re-sized`），所以解析完要 `del mv` 释放导出才能继续追加；memoryview 跨线程共享时要自己管生命周期，这是零拷贝的代价。

```python
# file: code/01_语言核心与底层/q5056_memoryview.py
import time

chunks = [bytes(1024) for _ in range(2000)]   # 2000 个 1KB 分片, 共 2MB

# 1) 反例: bytes 循环 + -> O(n^2) 全量拷贝
t0 = time.perf_counter()
buf = b""
for c in chunks:
    buf = buf + c
t1 = time.perf_counter() - t0
print(f"bytes 循环 + : {t1*1000:.1f}ms (每次都全量拷贝)")

# 2) join: 一次分配精确拷贝
t0 = time.perf_counter()
out = b"".join(chunks)
t2 = time.perf_counter() - t0
print(f"b''.join     : {t2*1000:.1f}ms")

# 3) bytearray += : 流式追加 amortized O(1)
t0 = time.perf_counter()
ba = bytearray()
for c in chunks:
    ba += c
t3 = time.perf_counter() - t0
print(f"bytearray += : {t3*1000:.1f}ms")

# 4) memoryview: 切片零拷贝, 解析协议头不搬 payload
mv = memoryview(out)
header = mv[0:16]          # 不复制
payload = mv[16:1024]      # 不复制
print("切片共享原缓冲:", payload.obj is out, "| payload 长度:", len(payload))
del mv, header, payload    # 释放导出后才能 resize 原缓冲

# 5) 陷阱验证: 有活跃 view 时 bytearray 禁止 resize
mv = memoryview(ba)
try:
    ba += b"x"
except BufferError as e:
    print("持有 view 时追加 ->", e)
del mv
ba += b"x"
print("del view 后正常追加, 长度:", len(ba))
```

**追问**：1) `bytearray +=` 为什么是 amortized O(1) 而不像 list 拼接那样每次 O(n)？——bytearray 内部维护超额预留容量（类似 list 的 over-allocation），追加只写入预留区；真正扩容时才 realloc。2) `recv_into`/`memoryview` 组合如何做到"一次拷贝都不多"？——recv_into 把内核数据直接写进你预分配的缓冲（省掉"临时 bytes 对象"那次），解析用 memoryview 切片（省掉协议层拷贝），全链路只剩内核→用户态一次。3) C 扩展（如 numpy）拿走 memoryview 后 Python 侧怎么保证安全？——靠 buffer 协议的导出计数与 `BufferError` 拦截 resize；跨边界的缓冲所有者要显式约定生命周期，必要时 `.cast()`/`.release()`。

## 背诵要点
- bytes `a=a+b` 每次全量拷贝 O(n²)；`b"".join` 一次分配精确拷贝；流式追加用 `bytearray +=`（amortized O(1)）。
- `memoryview` 切片零拷贝共享底层缓冲，解析协议头/payload 原地转交；持有期间原 bytearray 禁止 resize（BufferError）。
- 零拷贝省的是用户态复制；内核→用户态那次要靠 `recv_into`/`sendfile` 才能省。

## 复盘追问
- 你们协议解析/文件处理代码里还有几处 `bytes +` 循环？怎么从 profile 定位？（提示：cProfile 看 bytes.__add__ 累计时间，或 tracemalloc 看瞬时双倍分配）
- 大文件上传改用分块 + memoryview 后，哪些隐性拷贝仍然存在？（提示：框架层 request body 缓冲、TLS 记录层加解密、日志副本）
