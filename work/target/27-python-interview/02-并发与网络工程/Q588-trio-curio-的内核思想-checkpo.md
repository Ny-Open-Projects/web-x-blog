---
title: [Q588] trio/curio 的内核思想:checkpoint 与显式调度
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q588 · trio/curio 的内核思想:checkpoint 与显式调度

> 难度:★★★★ | 标签:trio, curio, 调度

**问**:curio/trio 这类"新一代"异步库和 asyncio 最本质的设计差异是什么?

**答**:两点。第一,取消必须显式配合:trio 的取消只在 checkpoint(如 `await sleep(0)`)处发生,库作者能明确指出"这里可中断",避免 asyncio 里"任意 await 都可能被取消"的隐式炸弹;第二,内核极简:curio 坚持调度器只做调度,所有 IO/同步原语都是显式 trap,性能开销更可预测。结构化并发(nursery)就诞生于 trio。下面实现一个 curio 风格的迷你内核:任务用生成器 yield trap,内核统一处理 sleep 与唤醒,展示"调度权完全在内核"的模型。

```python
# file: code/02_并发与网络工程/q588_curio_kernel.py
import heapq
import time
from collections import deque


class Kernel:
    """curio 风格内核: 任务是生成器, yield trap 请求内核服务。"""

    def __init__(self) -> None:
        self._ready: deque = deque()
        self._sleeping = []  # (deadline, seq, task)
        self._seq = 0
        self._results = {}

    def add(self, tid: int, gen) -> None:
        self._ready.append((tid, gen))

    def run(self) -> dict:
        current_time = time.monotonic
        while self._ready or self._sleeping:
            # 1. 唤醒到期任务
            now = current_time()
            while self._sleeping and self._sleeping[0][0] <= now:
                _, _, (tid, gen) = heapq.heappop(self._sleeping)
                self._ready.append((tid, gen))
            # 2. 跑一个就绪任务直到它 yield trap
            if not self._ready:
                if self._sleeping:
                    delay = max(0.0, self._sleeping[0][0] - current_time())
                    time.sleep(min(delay, 0.01))  # 真实内核会 epoll 等待
                continue
            tid, gen = self._ready.popleft()
            try:
                trap = gen.send(None)
            except StopIteration as e:
                self._results[tid] = e.value
                continue
            # 3. 内核裁决 trap
            if trap[0] == "sleep":
                self._seq += 1
                heapq.heappush(
                    self._sleeping, (current_time() + trap[1], self._seq, (tid, gen))
                )
            elif trap[0] == "checkpoint":
                self._ready.append((tid, gen))  # 立即重新排队
        return self._results


def task_a(kernel: Kernel) -> int:
    for i in range(3):
        yield ("sleep", 0.03)
        print(f"task_a 步骤 {i}")
    return "a-done"


def task_b(kernel: Kernel) -> str:
    for i in range(2):
        yield ("checkpoint",)  # 显式可取消点: 换其他任务跑
        print(f"task_b 步骤 {i}")
    return "b-done"


if __name__ == "__main__":
    k = Kernel()
    k.add(1, task_a(k))
    k.add(2, task_b(k))
    t0 = time.perf_counter()
    results = k.run()
    print("结果:", results, f"耗时 {time.perf_counter() - t0:.2f}s")
```

**追问**:1) trio 为什么坚持"取消必须到达 checkpoint"?——它把"哪里可能被打断"变成代码里可见的事实,审查者只需检查 checkpoint 分布,而不是推理任意 await 点的状态一致性。2) checkpoint 与 asyncio 的差异?——asyncio 任意 await 都可能取消;trio 要求显式 checkpoint(或裸 await 点);内核级保护结构(nursery/cancel scope)让取消可组合。3) 显式调度的收益?——可读性与可审计性(取消语义字面可见);shield 的显式变体(Protect);与结构化并发完全自洽(Q589)。4) 生产陷阱?——长 CPU 段无 checkpoint(取消饿死);把 checkpoint 当性能税删掉;混用 asyncio 心智写 trio 代码。

---
