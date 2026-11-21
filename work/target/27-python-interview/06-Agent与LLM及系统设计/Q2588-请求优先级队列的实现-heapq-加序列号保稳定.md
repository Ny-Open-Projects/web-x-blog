---
title: [Q2588] 请求优先级队列的实现:heapq 加序列号保稳定
date: 2026-11-17
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2588 · 请求优先级队列的实现:heapq 加序列号保稳定

> 难度:★★★☆ | 标签:LLM 运维, 队列, 数据结构

**问**:用 Python 实现一个请求优先级队列,有哪些一看就错的坑?

**答**:第一个坑是堆方向:heapq 是最小堆,数字越小越先出,约定优先级数字小者为高,写反了高优先级全沉底。第二个坑是稳定性:同优先级的元组比较会落到下一项,如果下一项是请求对象会直接报错,如果是字符串则按字典序出队——那是运气不是契约,必须显式塞一个单调递增 seq,同优先级严格按到达序出队。第三个坑是空队列:pop 要有可读的报错而不是裸 IndexError 泄栈。这三个点合起来就是 priority、seq、item 三元组的固定写法。优先级语义要写进类型注释和监控:队列里各级深度分别暴露,高优先级队列变深才是容量告警信号,总深度会掩盖结构性饥饿。

```python
# file: code/06_Agent与LLM及系统设计/q2588_priority_queue.py
"""Q2588 请求优先级队列的实现:heapq 加序列号保稳定。

优先级队列的核心实现细节:heapq 是最小堆,数字越小越先出;
同优先级时元组比较会落到第三项 item 上,顺序由字典序决定,
这是运气不是契约——必须补一个单调递增 seq 保证 FIFO 稳定。
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._h = []
        self._seq = 0

    def push(self, item, priority):
        heapq.heappush(self._h, (priority, self._seq, item))
        self._seq += 1

    def pop(self):
        if not self._h:
            raise IndexError("queue empty")
        _, _, item = heapq.heappop(self._h)
        return item

    def __len__(self):
        return len(self._h)


def main():
    q = PriorityQueue()
    q.push("low-1", 5)
    q.push("high-1", 1)
    q.push("low-2", 5)
    q.push("high-2", 1)
    out = [q.pop() for _ in range(4)]
    assert out == ["high-1", "high-2", "low-1", "low-2"], out
    # 对照:无 seq 的堆,同优先级按 item 字典序出队,语义不可控
    h = []
    for name, p in [("zz", 5), ("aa", 5)]:
        heapq.heappush(h, (p, name))
    assert heapq.heappop(h)[1] == "aa"   # 字典序,不是到达序
    try:
        q.pop()
        raise SystemExit(1)
    except IndexError as exc:
        print("空队列弹出被拒:", exc)
    print("带 seq 的出队序:", out, "← 同级按到达序,跨级按优先级")


if __name__ == "__main__":
    main()
```

**追问**:
- 追问一:优先级用什么字段?答:小整数等级加截止时刻组合,纯等级会丢 deadline 信息,纯 deadline 会饿低等级。
- 追问二:进程内队列挂了怎么办?答:堆本身无持久化,可靠场景外置到带持久化的队列,进程内堆只做调度缓冲。
