---
title: [Q5634] 线程池 Future 结果积压的内存水位账
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5634 · 线程池 Future 结果积压的内存水位账

难度：P6 | 标签：ThreadPoolExecutor、Future、内存水位、容量规划

**问**：用 `ThreadPoolExecutor.submit` 批量派发 100 万个任务后逐个取结果，进程 RSS 涨了几个 GB 下不来。任务本身很小，内存去哪了？请推导"submit 快、消费慢"场景下的内存水位模型，并给出治理手段。

**答**：

**结论**：内存水位由三部分叠加：(1) `submit` 的每个任务都创建一个 `_WorkItem`（含 fn/args 包装 + Future 对象），排进**无界**的 `SimpleQueue` 工作队列——提交速率超过 max_workers 消化速率时队列长度线性增长；(2) 每个完成的 Future 持有 result 与 done-callbacks，**没人消费就一直活着**：`as_completed` 若先建全量 future 列表再迭代，已完成的 future 也全量驻留；(3) Future 内部还有线程安全锁与条件变量，单个开销虽小（百字节级），乘以百万级就是 GB 级水位。RSS 不回落是分配器（pymalloc arena 不还 OS）与引用未释放共同作用。

**取舍**：水位模型：稳态积压 ≈ (提交速率 − 消化速率) × 时间 × 单项成本；治理优先级——a) 分批派发（每批 in-flight ≤ k，k≈max_workers×2），用有界 in-flight 自然形成背压；b) 结果即取即用，避免"全派发完再收"；c) 大结果不进 Future，写文件/队列只回传引用；d) 进程内长期驻留列表改为生成器消费。

**实战**：监控点：队列长度（`executor._work_queue.qsize()`，内部属性仅诊断用）、未消费 future 计数（业务自建 in-flight gauge）、RSS。压测时务必让消费速率 ≥ 生产速率再测稳态，否则测到的是积压曲线不是吞吐水位。

```python
import sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed

def small_task(i):
    return i * 2

def unbounded_submit(n):
    """全量派发再统一收——积压模型演示（n 取小值避免真吃内存）。"""
    futs = [ex.submit(small_task, i) for i in range(n)]
    qsize = ex._work_queue.qsize()
    results = [f.result() for f in as_completed(futs)]
    return qsize, sum(results)

def bounded_inflight(n, k):
    """有界 in-flight：派发速率被消费速率卡住。"""
    it = iter(range(n))
    inflight = set()
    total = 0
    for i in it:
        inflight.add(ex.submit(small_task, i))
        while len(inflight) >= k:                 # 背压闸门
            done = next(as_completed(inflight))
            total += done.result()
            inflight.discard(done)
    while inflight:
        done = next(as_completed(inflight))
        total += done.result()
        inflight.discard(done)
    return total

if __name__ == "__main__":
    N, K = 2000, 64
    ex = ThreadPoolExecutor(max_workers=8)
    print("全量派发瞬时队列长度 =", unbounded_submit(N)[0])
    print("有界 in-flight 总和 =", bounded_inflight(N, K))
    f = ex.submit(small_task, 0)
    print("单个 Future 对象 sizeof =", sys.getsizeof(f), "字节（不含结果与回调）")
    print("单个结果值 sizeof =", sys.getsizeof(f.result()), "字节")
    ex.shutdown()
```

**追问 1**：如何测单个 Future + WorkItem 的真实成本？
答：`tracemalloc` 快照对比 submit 前后差值，或 `sys.getsizeof(future)` + 其内部字典/callbacks 合计；典型量级几百字节，百万任务即数百 MB 起，再叠加结果对象本体。

**追问 2**：`map` 与逐个 `submit` 在积压行为上的差异？
答：`Executor.map` 内部也是全量提交（一次性把所有任务塞进队列），不会因消费慢而节流；真正有界的方案只有自己控 in-flight 或换有界队列的自建池。

**追问 3**：为什么 worker 空闲后 RSS 不降回？
答：pymalloc 的 arena 按池管理，释放的对象内存留在进程内供复用；观测工具用 `tracemalloc` 看 Python 堆（应回落）与 RSS 的差值来判断是"真泄漏"还是"分配器保留"。

## 背诵要点

- 积压水位 ≈ (提交速率−消化速率)×时间×单项成本；submit 队列无界，Future 未消费则结果永久驻留。
- 治理靠有界 in-flight（k≈max_workers×2）形成背压；Executor.map 与全量 submit 同样不节流。
- RSS 不回落先分"分配器保留"与"真泄漏"：tracemalloc 看 Python 堆，RSS 看进程。

## 复盘追问

- 如何给"提交速率"自动限速以匹配下游消化能力？(提示：令牌桶 + 队列长度反馈)
- as_completed 全量列表版本与流式版本内存差如何用快照量化？(提示：tracemalloc 两个阶段 diff)
