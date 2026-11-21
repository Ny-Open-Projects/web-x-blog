---
title: [Q2095] heapq 的稳定性陷阱与平局裁决
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2095 · heapq 的稳定性陷阱与平局裁决

> 难度:★★★★☆ | 标签:heapq, 稳定性, 优先队列

**问**:heapq 是稳定排序吗?相等优先级的任务怎么保证先入先出?

**答**:heap 不是排序而是堆结构,对相等优先级**没有任何稳定性承诺**——出堆顺序由堆的交换路径决定,与入队顺序无关,demo 里 z、y、x、w 同优先级入堆,裸堆弹出顺序是 w、x、y、z,恰好倒序。标准解法是三元组 (priority, index, item):index 用 itertools.count() 生成全局递增序号,平局时先比 index,同优先级就恢复先入先出;序号还顺带解决另一个陷阱——优先级相同时堆会比较第二元素,元素本身不可比(比如 dict、自定义对象)就 TypeError,序号充当了平局裁决的可比替身。记住这条铁律:往堆里放业务对象,永远带上序号位。

```python
# file: code/01_语言核心与底层/q2095_heapq_stability.py
"""heapq 没有稳定性:相等键的出堆顺序不可依赖。"""
import heapq


letters = [("z", 1), ("y", 1), ("x", 1), ("w", 1)]


if __name__ == "__main__":
    plain = []
    for name, priority in letters:
        heapq.heappush(plain, (priority, name))
    print("入堆顺序:", [n for n, _ in letters])
    print("裸堆出队:", [name for _, name in [heapq.heappop(plain) for _ in range(4)]])

    indexed = []
    for idx, (name, priority) in enumerate(letters):
        heapq.heappush(indexed, (priority, idx, name))
    print("带序号出队:", [name for _, _, name in [heapq.heappop(indexed) for _ in range(4)]])

    class Task:
        pass

    heap3 = [(1, 0, "a"), (1, 1, "b")]
    heapq.heapify(heap3)
    try:
        heapq.heappush(heap3, (1, Task()))     # 漏掉序号:平局时比较对象本身
    except TypeError as e:
        print("同优先级缺序号:", str(e)[:48])
```

**追问**:1) 序号为什么常用 itertools.count?——全局递增永不重复,天然表达入队先后;heappushpop 与先 push 再 pop 差别?——前者一次 sift 更快且堆满时可能原样返回新元素,适合固定容量池(参考 Q495)。2) 平局裁决的必要性?——Python 比较只到第二个元素,优先级相同时比较第三个——对象不可比就 TypeError;(priority, count, item) 的 count 兜底还保证 FIFO 稳定。3) 固定容量池的语义?——heappushpop 先比较再入堆:新元素更差时直接返回它,堆不动;nsmallest/nlargest 内部同思路。4) 生产陷阱?——对象直接进堆不可比;平局顺序不稳定(没加 count);heappushpop 与 push+pop 语义差(满堆时)被误解。
