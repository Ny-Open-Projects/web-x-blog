---
title: [Q5604] shared_memory 环形缓冲容量推导
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5604 · shared_memory 环形缓冲的容量推导

> 难度:★★★★☆ | 标签:容量规划, 共享内存, 多进程

**问**:多进程流水线想用 `multiprocessing.shared_memory` 搭一个零拷贝环形缓冲，容量与水位怎么定？和 Pipe/Queue 比账差在哪？

**答**:结论：环形缓冲容量 = 最大单条消息 × 并发在途条数 + 元数据（头尾指针、每条槽的定长头）。两个硬约束：① shared_memory 的段大小创建后**不可扩**，容量必须按峰值预留（Q5509 讲过生命周期坑）；② 环形槽位要么定长（简单、零碎片），要么存变长块（要额外管理空洞）。与 Queue 的账差：Queue 走 pickle+管道，每条消息有序列化 CPU 税且缓冲不可控（Q5543/Q5598）；共享内存把"序列化税"换成"自管协议税"——头尾指针要用共享 Value/锁保证原子推进，读空/写满语义自己实现。容量推导示范：单条 1MB、在途 64 条 → 段 66MB 起步；上游峰值速率 × 消费延迟 > 在途条数时会丢/阻塞，阻塞策略要显式选（背压等待 or 覆盖旧帧）。

```python
from multiprocessing import shared_memory, Value, Lock
import struct

SLOT = 1024 * 1024        # 单条 1MB（定长槽）
SLOTS = 8                 # 演示缩小，生产按峰值×1.5 预留
HEAD_BYTES = 8            # 每槽定长头：len + seq

shm = shared_memory.SharedMemory(create=True, size=SLOTS * SLOT)
print(f"段容量 {SLOTS * SLOT / 2**20:.0f}MB, 在途上限 {SLOTS - 1}（留一槽区分空/满）")

head, tail, lock = Value("L", 0), Value("L", 0), Lock()

def push(data: bytes) -> bool:
    with lock:
        if (head.value + 1) % SLOTS == tail.value:
            return False                 # 满：生产端背压（或选择覆盖旧帧）
        off = head.value * SLOT
        shm.buf[off:off + HEAD_BYTES] = struct.pack("<II", len(data), head.value)
        shm.buf[off + HEAD_BYTES:off + HEAD_BYTES + len(data)] = data
        head.value = (head.value + 1) % SLOTS
        return True

def pop() -> bytes:
    with lock:
        if tail.value == head.value:
            return b""                   # 空
        off = tail.value * SLOT
        n, _ = struct.unpack("<II", shm.buf[off:off + HEAD_BYTES])
        out = bytes(shm.buf[off + HEAD_BYTES:off + HEAD_BYTES + n])
        tail.value = (tail.value + 1) % SLOTS
        return out

print(push(b"frame-1"), pop())
shm.close(); shm.unlink()                # 声明周期纪律：生产者/消费者约定后统一清理（Q5509）
```

**追问一层**:为什么留一槽区分空/满？还有哪些空满判别方案（计数器法）？
**追二层**:头尾指针用 Value+锁推进，相比每槽自旋标志的取舍是什么？多消费者场景还能这样吗？

**背诵要点**
- 容量=单条×在途数+元数据；段创建后不可扩，按峰值×1.5 预留。
- 环形缓冲换掉序列化税，换来自管协议（指针原子性、空满语义）。
- 满/空策略（阻塞、覆盖）必须显式选，丢帧要有观测。

**复盘追问**
- 消费者崩溃时在途槽如何回收？提示：租约/seq 校验与超时重置。
- 单条消息超过槽容量怎么处理？提示：分片协议或退回 Queue。
