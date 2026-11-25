---
title: [Q5133] bytearray 的扩容策略与预分配容量账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5133 · bytearray 的扩容策略与预分配容量账

难度：P6 | 标签：bytearray、扩容、缓冲区复用、容量规划

**问**：写一个高频追加二进制帧的接收缓冲区，用 `bytes +=` 和 `bytearray +=` 差别有多大？bytearray 的内部扩容策略是什么，如何用预分配把百万次追加的成本压下来？

**答**：

**结论**：`bytes` 不可变，`+=` 每次都分配新对象并整体拷贝，n 次 append 总拷贝量是 O(n²)，这是粘包重组、日志缓冲等场景的经典性能坑。`bytearray` 可变，`+=` 是原地扩容（ amortized O(1)）：底层缓冲按几何倍数增长（约 1.125 倍 + 常数，不同于 list 的 ~1.125 倍策略细节），追加只写新尾部。预估大小时构造传参 `bytearray(size)` 或 `bytearray(b'') + 已知量` 一次到位，可完全消除 re alloc 抖动与峰值双倍内存。

**取舍**：bytearray 的代价是可变别名风险——把 bytearray 传给多个函数/协程，任何一处原地修改都影响所有持有者；`bytes(mv)`/`bytes(ba)` 转不可变需要一次 O(n) 拷贝。接收缓冲的常见模式是 bytearray + `del buf[:n]` 消费已处理前缀（memmove，前缀小时便宜），而非切片重建。

**实战**：容量账示例：单帧 4KB、峰值在途 128MB 缓冲，若用 bytes += 每来 4KB 拷贝整个缓冲一次，128MB 缓冲下每秒 1000 帧就是 ~128GB/s 的无效内存带宽，CPU 直接打满 memcpy；bytearray 原地追加后内存带宽降到真实数据量。用 `sys.getsizeof` 能直接看到扩容过程中的 capacity > len 现象。

```python
import sys, time

def bench_bytes(n, chunk):
    b = b""
    t = time.perf_counter()
    for _ in range(n):
        b = b + b"\x01" * chunk        # 每次整体拷贝
    return time.perf_counter() - t

def bench_ba(n, chunk):
    ba = bytearray()
    t = time.perf_counter()
    for _ in range(n):
        ba += b"\x01" * chunk          # 原地摊销扩容
    return time.perf_counter() - t

N, C = 4000, 1024
print(f"bytes     += {bench_bytes(N, C)*1000:8.2f} ms")
print(f"bytearray += {bench_ba(N, C)*1000:8.2f} ms")

# 扩容策略可见：capacity 系统性地大于 len
ba = bytearray()
sizes = []
for i in range(1, 40):
    ba += b"x"
    sizes.append(sys.getsizeof(ba))
print("sizeof 增长序列前 12 项:", sizes[:12])

# 预分配一次到位
ba2 = bytearray(1024 * 1024)           # 1MB 预分配
mv = memoryview(ba2)                   # 零拷贝写入视图
mv[:4] = b"\xde\xad\xbe\xef"
print("预分配 sizeof =", sys.getsizeof(ba2), "len =", len(ba2))
```

**追问 1**：`del buf[:n]` 消费前缀的成本是什么量级？
答：O(剩余长度) 的 memmove，把尾部数据搬到头部；若消费速率快、单次消费量小，频繁 del 会退化。大缓冲场景改成"读指针 + 定期 compaction"（记录 offset，超过阈值时一次性删除），把 O(n²) 摊平成 O(n)。

**追问 2**：bytearray 与 memoryview 配合有哪些坑？
答：memoryview 持有会锁住 bytearray 的 resize（导出协议禁止在有导出者时改变大小），追加时抛 `BufferError: Existing exports of data: object cannot be re-sized`——用完必须 `release()` 或用 with 块。

**追问 3**：为什么 bytearray += 比两个独立 bytearray 的 extend 快不了多少但比 bytes 快得多？
答：`+=` 和 `extend` 都走 `PyByteArray_OverAllocate` 同一条原地扩容路径；bytes 不可变导致每次必分配+拷贝，差距来自拷贝量而非调用开销。

## 背诵要点

- bytes += 是 O(n²) 整体拷贝，bytearray += 原地摊销扩容（约 1.125 倍增长），缓冲重组场景差几个数量级。
- `bytearray(size)` 预分配消除 realloc 抖动；memoryview 持有期间 bytearray 禁止 resize（BufferError）。
- 消费前缀 `del buf[:n]` 是 memmove，高频小消费改读指针 + 定期压缩。

## 复盘追问

- 如何在线上观测"缓冲区拷贝打满 CPU"？(提示：py-spy 热点落在 memcpy/_PyBytes_Join)
- bytearray 被多个协程共享修改，如何设计所有权协议避免竞态？(提示：单写者 + 队列交接)
