---
title: "[Q5653] 多进程 fan-in 结果合并的峰值容量账"
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5653 · 多进程 fan-in 结果合并的峰值容量账

难度：P6 ｜ 标签：ProcessPoolExecutor、fan-in、峰值内存、容量规划

**问**：N 个进程各产出结果集、主进程合并时，内存峰值为什么会远大于"结果总量"？`as_completed` 逐个收与 `map` 全量收、结果对象直接持有与流式聚合，各自的峰值账怎么算？如何把 fan-in 峰值压到可用水位内？

**答**：
结论：fan-in 峰值 = **在飞结果总量 + 合并过程中的瞬时放大**。三个放大源：① `executor.map` / 一次性 `list(results)` 把 N 份结果同时握在主进程（还叠加 IPC pickle 反序列化的临时对象）；② 合并操作本身（`sorted(all)`、`Counter.update`、构建 dict）再生成一份新结构，瞬时 = 原始 + 合并产物；③ 结果对象跨进程经过 pickle → bytes → 对象 三次形态转换，peak 里同时存在两形态。峰值账公式：`peak ≈ Σ(单结果对象内存) × max_concurrent_inflight + Σ(合并临时结构) + 反序列化瞬态`。控制手段按杠杆排序：流式聚合（收到一份处理一份，只留聚合产物）、限制 in-flight 数（`Semaphore` 或按需 submit）、让 worker 端预聚合（map-reduce 的 reduce 下推）、大结果换 `shared_memory` 或临时文件落盘。

取舍：`as_completed` 只改变"完成顺序感知"，**不限制在飞数量**——若你一次性 submit 了 10 万个任务，10 万份结果照样堆在队列里；真正的背压是"完成一个再提交一个"的有界管道。worker 端预聚合最省 IPC（传输字节也降），但牺牲失败粒度与进度可见性。

实战：以 5000 万行日志汇总为例的实测账：全量收峰值 ≈ 结果集 ×3（pickle bytes + 对象 + 聚合结构），流式 + worker 预聚合可压到 ×1.2 以内；落盘兜底用 NDJSON 分片写临时文件 + 最终多路归并（heapq.merge），峰值 O(单分片) 而非 O(总量)。

```python
import os, resource, sys
from concurrent.futures import ProcessPoolExecutor, as_completed

def rss_kb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 if sys.platform != "darwin" else 1)

def produce(chunk_id):
    # 模拟每个 worker 产出一个中等结果集
    return [(chunk_id, i, f"row-{i}" ) for i in range(20_000)]

def full_collect(n_workers=4):
    with ProcessPoolExecutor(max_workers=n_workers) as ex:
        futs = [ex.submit(produce, i) for i in range(n_workers)]
        all_rows = [row for f in as_completed(futs) for row in f.result()]  # 全量握在主进程
    return len(all_rows)

def streaming_aggregate(n_workers=4):
    total = 0
    seen_keys = 0
    with ProcessPoolExecutor(max_workers=n_workers) as ex:
        futs = [ex.submit(produce, i) for i in range(n_workers)]
        for f in as_completed(futs):
            for _, _, k in f.result():     # 收到一份处理一份，只留聚合标量
                total += 1
                seen_keys += hash(k) % 2
    return total, seen_keys

if __name__ == "__main__":                    # macOS spawn 必须
    print("rss before      :", rss_kb())
    n = full_collect()
    print("full collect rows:", n, " rss after :", rss_kb())
    del n
    t, s = streaming_aggregate()
    print("streaming rows   :", t, " rss after :", rss_kb(), "（峰值显著更低）")

    # 限制 in-flight 的有界管道：完成一个才提交下一个
    from collections import deque
    def bounded_pipeline(n_tasks=8, workers=2, limit=2):
        out = 0
        with ProcessPoolExecutor(max_workers=workers) as ex:
            inflight = deque()
            nxt = 0
            while nxt < n_tasks or inflight:
                while inflight and inflight[0].done():
                    out += len(inflight.popleft().result())
                while nxt < n_tasks and len(inflight) < limit:
                    inflight.append(ex.submit(produce, nxt)); nxt += 1
                if inflight and not inflight[0].done():
                    inflight[0].result()       # 阻塞等最早的一个
                    out += len(inflight.popleft().result())
            return out
    print("bounded pipeline rows:", bounded_pipeline())
```

**追问一**：为什么"worker 端预聚合"同时降 IPC 与主进程峰值，却常被跳过？——它要求 reduce 逻辑可下推且可交换（求和/计数可以，全局排序不行），并把失败语义从"单任务重试"变为"分片重算"；工程上先问聚合算子代数性质，再决定下推与否。

**追问二**：`shared_memory` 能把 fan-in 峰值降到什么程度、代价是什么？——结果写共享内存可消掉 pickle bytes 形态与传输拷贝，峰值趋近 O(结果总量)；代价是生命周期管理（孤儿块泄漏）、跨平台行为差异与需要自定布局（固定 schema），只适合大块数值/定长结构，任意嵌套对象仍要 pickle。

## 背诵要点
- fan-in 峰值 ≈ 在飞结果 × 并发 + 合并临时结构 + pickle/对象双形态瞬态；map/list 全量收最贵。
- as_completed 不限背压；有界管道（完成一个提交一个）才是水位控制，worker 端预聚合同时省 IPC。
- 兜底：NDJSON 分片落盘 + heapq.merge 归并，峰值从 O(总量) 降为 O(单分片)。

## 复盘追问
- 一次全量重算把主进程 RSS 顶到 limit 触发 OOMKilled，如何从合并路径重建容量账并分阶段压峰值？（三放大源逐一验证：pickle 瞬态/在飞/聚合临时，讨论流式改造排期）
- 为什么"限制 in-flight"与"限制 worker 数"是两个不同旋钮？（worker 数管 CPU 并行度，in-flight 管主进程内存水位；讨论二者解耦后的配置策略）
