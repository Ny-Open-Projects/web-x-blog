---
title: [Q1285] deadline 传播:超时在调用链上的正确携带
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1285 · deadline 传播:超时在调用链上的正确携带

> 难度:★★★★☆ | 标签:超时, 工程实践, 可靠性

**问**:整个请求预算 300ms,下游三层调用各自 sleep,超时怎么在调用链上生效?子操作的超时和父操作是什么关系?

**答**:deadline(绝对时间点)而非 timeout(相对时长)才是可传播的:入口创建 `Deadline(total)`,每层操作取 `parent.remaining()` 与自己的预算取 min 构造子 deadline——这样子操作不会「借」到父级已经花掉的时间,整条链共享同一个截止时刻。执行点在每个可能阻塞的操作前后 `check()`:剩余时间 ≤0 就抛 DeadlineExceeded,把超时从「各层各自为政的 sleep」变成「全局预算的硬约束」。与 socket timeout/asyncio wait_for 的关系:deadline 是策略层(决定预算分配),单操作超时是机制层(真正打断 IO),两者配合——check 把预算切成段,IO 超时保证单段可打断。数学上注意 perf_counter(Q505)单调时钟,绝不拿 time.time 算 deadline(墙钟会跳)。

```python
# file: code/01_语言核心与底层/q1285_deadline.py
import time


class DeadlineExceeded(Exception):
    pass


class Deadline:
    def __init__(self, seconds=None, parent=None):
        if parent is not None:
            left = parent.remaining()
            seconds = left if seconds is None else min(seconds, left)
        self._at = None if seconds is None else time.perf_counter() + seconds

    def remaining(self):
        if self._at is None:
            return None
        return self._at - time.perf_counter()

    def check(self, point=""):
        left = self.remaining()
        if left is not None and left <= 0:
            raise DeadlineExceeded("deadline exceeded at " + point)


def do_step(deadline, name, cost):
    deadline.check(name)
    time.sleep(cost)
    deadline.check(name + " after")


if __name__ == "__main__":
    dl = Deadline(0.15)
    do_step(dl, "step1", 0.05)
    print("step1 ok, remaining: %.2fs" % dl.remaining())
    try:
        do_step(dl, "step2", 0.2)          # 超出整体预算
    except DeadlineExceeded as e:
        print("stopped ->", e)
    child = Deadline(parent=dl, seconds=10)
    print("child inherits tighter parent: %.2fs" % child.remaining())
```

**追问**:1) 为什么不用「剩余毫秒数」层层传递?——相对时长每层都要自己减去已耗时间,一旦有人忘记就放大预算;绝对时间点天然合并,min 即语义,没有可忘的步骤。2) 传播的完整模型?——入口用 monotonic 时钟算绝对 deadline,每层 deadline=min(传入, 自身预算);重试循环每次检查剩余时间,预算耗尽即失败——总预算恒定。3) 与框架的对接?——asyncio.wait_for 是相对超时,内部换算 loop.time();HTTP 层是 request deadline header;gRPC 的 deadline propagation 同构。4) 生产陷阱?——每层都「新起一个 30s 超时」,链路总耗时无界;中间层吞掉 deadline;重试不检查剩余预算,超时后还在打下游。
