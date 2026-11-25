---
title: "[Q5198] heapq 里塞字典：优先级相同的瞬间 TypeError"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5198 · heapq 里塞字典：优先级相同的瞬间 TypeError

难度：P6 ｜ 标签：heapq、元组比较、TypeError、tiebreaker、任务调度

**问**：优先队列用 `heapq.heappush(heap, (priority, task))`，单个任务运行正常，压测时偶发 `TypeError: '<' not supported between instances of 'dict' and 'dict'`。为什么单条不报、并发才报？堆什么时候会比较第二个元素？怎么在保持"同优先级先进先出"的同时避免比较业务对象？

**答**：
结论：`heapq` 只保证"父节点不大于子节点"，元组按字典序比较——先比 `priority`，相等时**接着比第二个元素**。只有发生"插入位置上浮"或"弹出后下沉"时才需要比较；插入第一条时没有父节点可比，所以永远不报，直到出现两个相同优先级，才会去比较 `task` 这个字典。字典没有定义 `<`，于是抛 `TypeError`。这不是偶发，而是"同优先级首次出现"的确定性事件，只是时机取决于数据。

取舍：a) 加单调递增计数器做 tiebreaker：`(priority, seq, task)`，`seq` 唯一，永远不会比到 `task`，还顺带获得同优先级 FIFO 的稳定性；b) 用 `dataclass(order=True)`，把 `task` 标成 `compare=False`，`__lt__` 只看前几个字段；c) 包一层 `__lt__` 只比 `priority` 的小类（相等返回 False），语义上不是全序，但 `heapq` 只要求"不矛盾"的偏序，实践可用。要警惕的是"给 dict 加 `__lt__`"——内置 dict 改不了，子类化会带来性能与语义问题。

实战：事故形态是"延迟任务调度器把 `(execute_at, payload)` 压堆，单机测试没触发同毫秒任务，上线后同一秒批量创建的定时任务直接把 worker 打挂"。下面演示单条不报、同优先级报错、计数器兜底与 `order=True` 两种修法。

```python
import heapq
import itertools
from dataclasses import dataclass, field

heap = []
heapq.heappush(heap, (1, {"id": "a"}))
print("[1] 只有一条时不比较第二元素:", heap[0][1])

try:
    heapq.heappush(heap, (1, {"id": "b"}))
except TypeError as e:
    print("[2] 同优先级插入:", type(e).__name__, "|", e)

seq = itertools.count()
heap2 = []
for name in ("a", "b", "c"):
    heapq.heappush(heap2, (1, next(seq), {"id": name}))
print("[3] 计数器兜底，同优先级 FIFO:",
      [heapq.heappop(heap2)[2]["id"] for _ in range(3)])


@dataclass(order=True)
class Job:
    priority: int
    payload: dict = field(compare=False)   # 不参与比较
    seq: int = field(default=0, compare=False)


h3 = [Job(1, {"id": "a"}), Job(1, {"id": "b"})]
heapq.heapify(h3)
print("[4] dataclass compare=False:", [heapq.heappop(h3).payload["id"] for _ in range(2)])

# 反例：只给 priority 的偏序
class Task:
    def __init__(self, p, name):
        self.p, self.name = p, name

    def __lt__(self, other):
        return self.p < other.p      # 相等返回 False，不比较业务字段


h4 = [Task(2, "x"), Task(2, "y"), Task(1, "z")]
heapq.heapify(h4)
print("[5] 偏序 __lt__:", [heapq.heappop(h4).name for _ in range(3)])
```

**追问一**：为什么"只比 priority 的 `__lt__`"在 `heapq` 里是安全的？—— `heapq` 的算法只依赖"父不大于子"的偏序判断，不要求全序；相等时返回 False 会让元素停在原位，堆性质依然成立。但它不保证同优先级 FIFO（顺序取决于上浮/下沉路径），要稳定就得加 `seq`。另外，三条路径混合（`Job` 与 `Task`）时 Python 会尝试反向比较，`__lt__` 类型不匹配又会炸，队列里只放一种类型。

**追问二**：`heapq` 的 `key` 参数（3.5+）能解决吗？—— `heapq.nlargest/nsmallest` 有 `key`，但 `heappush/heappop/heapify` 没有 `key`，所以不能靠它绕开比较；`heapq.heapify` 也不接受 `key`。要按优先级组织复杂对象，必须让对象自身可比较（`__lt__`/dataclass order）或把可比较的元组压进堆。这也是"用 `PriorityQueue` 时同样要处理"的问题，`queue.PriorityQueue` 内部就是 `heapq`。

## 背诵要点
- `heapq` 元组按字典序比较，优先级相等时比较第二元素；单条插入不触发比较，同优先级才炸。
- 修法：`(priority, seq, payload)` 计数器（同时得到稳定 FIFO）或 `dataclass(order=True, compare=False)`。
- `heappush/heappop/heapify` 没有 `key` 参数，`PriorityQueue` 同样受此约束。

## 复盘追问
- 压测偶发 `dict < dict` 的 TypeError，为何单测复现不了？（比较发生在上浮/下沉，需同优先级两条）
- 既要优先级又要同优先级 FIFO，怎么设计键？（`(priority, seq)` 单调计数器）
