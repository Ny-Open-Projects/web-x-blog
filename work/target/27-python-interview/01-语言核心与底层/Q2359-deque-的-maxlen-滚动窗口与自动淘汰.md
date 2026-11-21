---
title: [Q2359] deque 的 maxlen:滚动窗口与自动淘汰
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2359 · deque 的 maxlen:滚动窗口与自动淘汰

> 难度:★★☆☆☆ | 标签:deque, 滚动窗口, collections

**问**:deque(maxlen=N) 满了之后 append 会怎样?滑动平均怎么用一行实现?

**答**:构造时指定 maxlen,deque 就变成定长环形缓冲:append 超过容量时自动从对端淘汰最老元素,appendleft 淘汰右端,extend 一次塞超量则只保留最后 maxlen 个——淘汰是隐式的,没有任何异常或告警,这正是它适合「最近 N 条」语义的原因。两个典型用途:滚动窗口统计,窗口满后每步只有一次 O(1) 的 append 加一次 sum;日志/历史的「只留最近 N 条」存储,不需要手工裁剪。注意 maxlen 是只读属性,构造后不能改;要变长窗口只能重建。与手工 list 配合 del lst[0] 的方案相比,deque 两端操作 O(1) 且不会因头部删除引发整表搬移,数据流场景完胜。

```python
# file: code/01_语言核心与底层/q2359_deque_maxlen.py
"""deque 的 maxlen:自动淘汰的滚动窗口与滑动平均。"""
from collections import deque

if __name__ == "__main__":
    window = deque(maxlen=5)
    for i in range(8):
        window.append(i)
    print("只留最后 5 个:", list(window))

    w2 = deque([1, 2, 3], maxlen=3)
    w2.appendleft(0)
    print("appendleft 淘汰右端:", list(w2))

    w3 = deque(maxlen=3)
    w3.extend([10, 20, 30, 40, 50])
    print("extend 超量保留尾部:", list(w3))

    prices = [10, 11, 12, 13, 14, 15]
    ma = deque(maxlen=3)
    for p in prices:
        ma.append(p)
        print(f"price={p} window={list(ma)} avg={sum(ma) / len(ma):.2f}")
```

**追问**:1) 需要「最近 N 条」但 N 运行时可变怎么办?——deque 没法改 maxlen,封装一层:满时用 maxsize 判断手工 popleft,或按新 maxlen 重建 deque 并迁移数据。2) maxlen 的语义细节?——满员追加自动挤掉对端(静默丢旧);appendleft 挤掉右端;rotate 的窗口轮转;len ≤ maxlen 恒成立。3) 滚动窗口的应用?——滑动平均/最近事件/限流计数器;与 heapq 固定容量池互补(Q495);统计类窗口要保证「满了才开始」的语义一致。4) 生产陷阱?——静默淘汰旧数据被当 bug;重建 deque 的 O(n) 迁移在热路径;maxlen=0 的 deque 恒空边界。
