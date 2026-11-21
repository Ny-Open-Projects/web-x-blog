---
title: [Q5066] deque 与 list 双端操作的容量成本账
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5066 · deque 与 list 双端操作的容量成本账

> 难度:★★★☆ | 标签:容量规划, deque, list, 数据结构选型

**问**：滑动窗口要频繁在头部插入删除，同事把 list 换成 `collections.deque` 后 CPU 降了 30%。`list.pop(0)` 到底贵在哪？deque 的块状结构和 maxlen 有什么容量特性？什么场景下 deque 反而更慢？

**答**：结论：`list` 是连续指针数组（PyObject* 数组），`pop(0)`/`insert(0, x)` 必须**memmove 后面全部元素**——头部操作 O(n)，百万元素窗口每秒几千次就是每秒上亿次指针搬运；`deque` 是**块链表**（blockmap + 64 槽块，每块指针数组），两端 push/pop O(1)，只动端点块。容量特性：a) deque 支持 `maxlen=n`，满了自动从另一端丢元素，天然实现有界滑动窗口/最近 N 条去重队列，不用手写淘汰；b) list 有 over-allocation（见既有 Q1263），deque 按块分配，单块 512 字节级别，增量分配更平滑但随机访问要跨块解引用。**deque 更慢的场景**：a) 随机索引 `d[i]` O(n)（跨块寻址），list O(1) 连续内存还更缓存友好；b) 中间插删、切片语法（deque 不支持切片）；c) 纯尾部追加+迭代（append-only 流）list 同样 O(1) 且更省。选型口诀：**两端进出选 deque，随机读/切片选 list，栈用 list，队列用 deque 或 queue 模块**（线程安全版本另见并发类）。容量账：有界 deque `maxlen` 是把内存上限写进数据结构，比"事后裁剪 list"少一次 O(n) 拷贝和瞬时双倍峰值。

```python
# file: code/01_语言核心与底层/q5066_deque_vs_list.py
import time, collections

n = 200_000

# 1) 头部操作: list O(n) vs deque O(1)
head_list = list(range(n))
head_deque = collections.deque(range(n))

t0 = time.perf_counter()
for _ in range(2_000):
    head_list.pop(0); head_list.insert(0, -1)
t1 = time.perf_counter()
for _ in range(2_000):
    head_deque.pop(); head_deque.appendleft(-1)
t2 = time.perf_counter()
print(f"list 头部 2000 次: {(t1-t0)*1000:.1f} ms | deque 头部 2000 次: {(t2-t1)*1000:.2f} ms")

# 2) maxlen 有界窗口: 满了自动丢, 内存上限写进结构
win = collections.deque(maxlen=5)
for i in range(9):
    win.append(i)
print("滑动窗口(自动淘汰):", list(win))

# 3) 最近 N 条去重(经典 maxlen 用法)
seen = collections.deque(maxlen=3)
for ev in ["a", "b", "c", "a"]:
    if ev not in seen:
        print("新事件:", ev)
    seen.append(ev)
print("窗口内容:", list(seen))

# 4) deque 的弱项: 随机访问 O(n) 跨块
d = collections.deque(range(100_000))
t0 = time.perf_counter()
for i in range(0, 100_000, 1000):
    _ = d[i]
t1 = time.perf_counter()
lst = list(d)
t2 = time.perf_counter()
for i in range(0, 100_000, 1000):
    _ = lst[i]
t3 = time.perf_counter()
print(f"deque 随机读 100 次: {(t1-t0)*1e6:.0f} us | list 随机读: {(t3-t2)*1e6:.0f} us")
print("选型: 两端进出 deque / 随机读切片 list / 栈 list / 有界窗口 deque(maxlen)")
```

**追问**：1) deque 内部一个块多大、为什么是 64 槽？——CPython 实现 block 内含 64 个 PyObject*（更高层还有块映射表），这是内存局部性与再分配粒度的折中；扩容只追加块，两端操作不动已有数据。2) `queue.Queue` 与 deque 的关系？——Queue 内部就是 deque 加锁加条件变量，多线程消费必须用 Queue（或 3.13 的 queue.SimpleQueue 更轻），裸 deque 在多线程 append/pop 两端各自是原子的（GIL）但"判空再取"的复合操作有竞态。3) maxlen 满了丢元素能感知吗？——不能，静默丢弃；需要感知溢出就自己计数或换 `Queue(maxsize)` 的 full 信号/put_nowait 异常路径。

## 背诵要点
- `list.pop(0)/insert(0)` 是 memmove 全体元素 O(n)，deque 块状结构两端 O(1)；高频头部操作换 deque 直接省 CPU。
- `deque(maxlen=n)` 把内存上限与自动淘汰写进结构，免手写裁剪与双倍峰值；溢出静默丢弃无感知。
- deque 弱项：随机索引 O(n)、无切片；随机读/切片/append-only 选 list，多线程消费选 queue.Queue。

## 复盘追问
- 代码里还有没有在循环头部的 `pop(0)`/`insert(0)`/`del lst[0]`？（提示：grep 这些模式，估算 n 与频率的成本账，换 deque 或 maxlen）
- 有没有多线程直接共享裸 deque 的"判空再取"竞态？（提示：复合操作换 Queue 或加锁；对照本卡第 3 点演练）
