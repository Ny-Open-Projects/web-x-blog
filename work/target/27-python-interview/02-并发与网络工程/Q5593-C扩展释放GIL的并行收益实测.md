---
title: "[Q5593] C 扩展释放 GIL 的并行收益实测"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5593 · C 扩展释放 GIL 的并行收益实测

难度：P7 | 标签：原理深挖 | GIL | 多线程并行

**问**："Python 线程没用"是面试高频论断。hashlib/zlib/bz2 这类 C 扩展在做什么操作时会释放 GIL？如何实测一段 CPU 密集摘要计算的线程加速比？哪类操作释放、哪类不释放，判断依据是什么？

**答**：
结论：判断依据写在 C 源码里——凡是预计运行时间较长（毫秒级以上）的 C 调用都应包裹 `Py_BEGIN_ALLOW_THREADS ... Py_END_ALLOW_THREADS`。标准库中典型释放点：`hashlib` 对超过 2047 字节的 update/digest、`zlib`/`bz2`/`lzma` 的 compress/decompress（分块大小相关）、`socket.recv/send` 等 IO、`open().read()` 大文件读取、`sqlite3` 执行语句。**大块摘要计算是可并行的**：4 线程压 4 个独立数据块可接近 4 倍加速（核数允许时）；而小块数据（低于阈值）不释放 GIL，多线程退化为串行。
取舍：释放 GIL 的并行收益只在"输入可拆分、核数空闲"时成立；一旦共享了 Python 对象（合并结果 dict），串行段会吃掉收益。3.13 free-threading 解释器下这个前提整体变化，但 CPython 默认构建仍是 GIL 模型。
实战：把"并行摘要/压缩/解压"写成 ThreadPoolExecutor 作业是零依赖的 CPU 并行方案；容量推导用 `加速比 ≈ min(核数, 块数)` 再扣结果合并的串行占比（Amdahl）。

```python
import hashlib, time, os, sys
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def digest_blob(n_bytes):
    data = os.urandom(n_bytes)          # os.urandom 释放 GIL
    h = hashlib.sha256()
    h.update(data)                      # 大块 update 释放 GIL（阈值 2047B）
    return h.digest()

N = 16 << 20  # 16MB/块
NCPU = os.cpu_count() or 4
CHUNKS = max(NCPU, 4)

t0 = time.perf_counter()
for _ in range(CHUNKS):
    digest_blob(N)
t_seq = time.perf_counter() - t0

with ThreadPoolExecutor(max_workers=NCPU) as ex:
    t0 = time.perf_counter()
    list(ex.map(digest_blob, [N] * CHUNKS))
t_thr = time.perf_counter() - t0

print(f"核数={NCPU}, 块数={CHUNKS}, 每块 {N>>20} MB")
print(f"串行   {t_seq:.2f}s")
print(f"线程   {t_thr:.2f}s  加速比 ≈ {t_seq/t_thr:.2f}x  (GIL 在 C 段被释放)")

# 对照：小块不释放 GIL，线程无收益
small = 512
t0 = time.perf_counter()
for _ in range(CHUNKS):
    digest_blob(small)
s_seq = time.perf_counter() - t0
with ThreadPoolExecutor(max_workers=NCPU) as ex:
    t0 = time.perf_counter()
    list(ex.map(digest_blob, [small] * CHUNKS))
s_thr = time.perf_counter() - t0
print(f"512B 小块: 串行 {s_seq:.3f}s vs 线程 {s_thr:.3f}s (≈1x，GIL 全程持有)")

# 释放 GIL 的 IO 对照：并发 sleep/读盘线程也能并行
import urllib.request
print("释放点速查: hashlib(>2047B) / zlib / bz2 / lzma / socket / 大文件 read / sqlite3.execute")
```

**追问 1**：为什么 hashlib 设 2047 字节这个阈值？
- 追问 2 层：小于阈值的 update 一次几十微秒，线程切换（GIL 交接 5ms 粒度 + 上下文成本）开销大于收益，干脆持锁做完；大块则长到值得让出。
- 追问 3 层：这说明"是否释放"不是库的道德承诺而是成本权衡，同库不同参数行为不同，实测必须用生产块大小。

**追问 2**：结果合并的串行段怎么压下来？
- 追问 2 层：返回 bytes 而非 Python 大对象，合并用列表 append（GIL 下原子）或 `heapq.merge`；避免共享 dict 的锁竞争。
- 追问 3 层：串行占比超 ~10% 时 Amdahl 上限明显，改用分块写盘/分片存储，让合并发生在读取侧。

## 背诵要点
1. 释放 GIL 判据：C 源码里的 Py_BEGIN/END_ALLOW_THREADS；hashlib 大块(>2047B)、zlib/bz2/lzma、socket IO、sqlite3。
2. 大块 CPU 摘要可获近核数加速，小块不释放退化为串行——阈值是成本权衡，实测要用生产块大小。
3. 收益上限受结果合并串行段约束（Amdahl），接口设计让返回值小、合并顺路。

## 复盘追问
1. 为什么有的团队用线程并行 zlib 反而更慢？——块太小全在 GIL 内 + 线程切换税；先看块大小阈值再谈线程数。
2. 3.13 free-threading 下这套实测结论还成立吗？——成立的方向不变但上限不同：纯 Python 代码也开始并行，串行段占比重算。
