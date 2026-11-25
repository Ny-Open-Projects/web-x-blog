---
title: "[Q5734] executor.map 的全量提交语义：立即入队、乱序结果与迭代点异常"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5734 · executor.map 的全量提交语义：立即入队、乱序结果与迭代点异常

难度：P6 ｜ 标签：executor.map、立即提交、无背压、迭代点异常、结果有序、submit 对比、map 立即物化

**问**：`ThreadPoolExecutor.map(fn, items)` 是懒执行还是立即提交？传进去的 items 是生成器时，map 会不会立即把它全部物化？异常在什么时候抛出——submit 时还是迭代结果时？`map` 返回顺序与完成顺序什么关系？什么时候必须用 submit 循环替代 map？

**答**：
结论：`map` 的三个关键语义：①**立即全量提交**——`executor.map(fn, iterable)` 在调用时就消费整个 iterable，把**所有**任务一次性入队（哪怕工作线程数只有 2，1 万个任务也全部进入无界队列），传生成器不会带来"边产边提交"的背压；②**结果有序**——返回的迭代器按输入顺序 yield，先完成的任务也要等前面的任务先出队（`as_completed`（Q070）才是完成序）；③**异常在迭代点抛出**——submit 阶段零异常（除了 fn 本身不可调用），任务执行中的异常被存进对应 Future，**迭代到那个位置才重新抛出**——前面位置的正常结果已产出，后面位置的还没被取。三个坑：①"map 懒惰"错觉导致大生成器被全量物化、队列瞬间膨胀（Q5634 积压家族）；②一个任务的异常让 `for r in executor.map(...)` 整条循环中断，**剩余结果全部丢弃**，而已执行的副作用无法回滚；③想要"边提交边限流"必须手写 submit + 信号量/分批。修补姿势：分块提交（chunked submit）、或用 `submit` 循环拿到 Future 句柄做自定义限流与异常收集。

取舍：a) 输入量可控（几十个任务）+ 全要结果：`map` 最简洁，异常在迭代点集中处理也自然；b) 输入是海量生成器：**绝不直接 map**——分块物化（itertools.islice 轮次）或 submit+信号量限流，把背压显式化；c) 需要"失败的继续跑完、收集全部异常"：submit 循环 + 逐个 `future.result()` + try 收集（Q2661 部分失败回传家族）；d) 需要完成序驱动的主循环：`as_completed` 而不是 map；e) 与 multiprocessing.Pool.map 的差异：Pool.map 的 chunksize 会把输入切块下发（Q5590），而 TPE.map 没有切块概念——两代 API 的"map"不是一个语义，跨池迁移代码要重新核对行为。

实战：事故形态是"对账脚本用 `executor.map(check, gen_10w_rows())`，一晚把 10 万任务全量入队，Future 对象与闭包占满数 GB 内存 OOM；同时某行数据异常让 map 迭代点抛错，主循环退出，剩下 8 万行检查结果（含已写入的副作用）状态不明——修复为 1000 行分块提交 + 每块内异常收集落盘，内存水位与失败可见性都恢复"。下面实测 map 的立即提交、有序返回与迭代点异常。

```python
# executor.map 的全量提交语义
import threading
import time
from concurrent.futures import ThreadPoolExecutor

submitted = []
lock = threading.Lock()

def record(tag: str) -> str:
    with lock:
        submitted.append(tag)
    if tag == "boom":
        raise ValueError(f"task {tag} failed")
    time.sleep(0.02)
    return f"done-{tag}"

pool = ThreadPoolExecutor(max_workers=2, thread_name_prefix="map")

print("[1] map 调用即全量提交: 生成器被立即物化, 全部任务进入无界队列")
def gen_items(n: int):
    for i in range(n):
        yield f"t{i}"
items = gen_items(5)
futures_iter = pool.map(record, items)               # <- 此刻 items 已被消费光, 5 个任务全部入队
print("    map 调用返回后, 已提交任务数 =", len(submitted), "(生成器 items 已耗尽)")
print("    map 是否懒惰?", len(submitted) == 5, "并立即全量提交")

print("[2] 返回有序: 先完成也要按输入顺序 yield")
t0 = time.perf_counter()
results = list(pool.map(lambda x: time.sleep(0.1) or x, [0, 1, 2]))
print("    结果顺序 =", results, "(严格输入序, 耗时约 3*0.1s = 串行无意义等待时的浪费)")

print("[3] 异常在迭代点抛出: submit 阶段零异常, 迭代到坏位置才炸")
work = ["a", "boom", "c", "d"]
collected, raised = [], None
try:
    for r in pool.map(record, work):
        collected.append(r)
except ValueError as e:
    raised = e
print("    'a' 正常产出:", collected, "-> 迭代到 boom 抛:", type(raised).__name__, "-", raised)
print("    异常后剩余结果 (y 的 Future) 仍会执行, 但结果被丢弃 -> 副作用不可回滚")
print("[4] 修补姿势: 分块提交 + submit 循环, 背压与异常收集显式化")
print("    for chunk in batches(items, 100): futures = [pool.submit(...) ...]")
pool.shutdown(wait=True)
```

**追问一**：`map` 为什么选择"立即全量物化"而不是惰性拉取？这个设计的历史与实现原因是什么？—— 实现层面：CPython 的 `Executor.map` 是**普通函数不是生成器**——它在调用时就 `list(iterable)`、逐个 submit、收集 Future 列表，返回的是这组 Future 上的结果迭代器（`_ResultIterator`）。历史/语义原因：①结果必须**按输入序**返回，而"按序"要求所有 Future 在结果迭代器创建时就已经确定——惰性拉取会让"顺序"依赖提交进度，语义复杂化；②与内建 map 的直觉对齐：`map` 在 Py3 之前就是立即求值的（Py2 的 map 返回列表），Py3 内建 map 改为惰性迭代器，但 Executor.map 没跟着改——这是两代 API 语义漂移的著名案例（与 Pool.map 的 chunksize 漂移叠加，成为跨池迁移的经典坑）。工程启示：**API 名字相同不等于语义相同**，并发族 API（map/as_completed/wait）每个的求值时机都要单独核对文档与源码，不能凭内建函数直觉迁移。

**追问二**：要"海量输入 + 背压 + 异常不中断"的正确模板长什么样？分块大小怎么定？—— 标准模板三段式：①**分块物化**：`for chunk in iter(lambda: list(itertools.islice(gen, N)), [])`——每批只物化 N 条，内存水位 = N 个 Future 而不是全量；②**批内 submit + 逐个收**：`futures = [pool.submit(fn, x) for x in chunk]`，然后 `for x, f in zip(chunk, futures): try: f.result() except Exception: 记录继续`——异常收集不中断（Q2661 家族）；③**批间限流**：批结束等待 `as_completed` 全部落定再进下一批，天然形成"提交速度 ≤ 消费速度"的背压——不需要额外信号量。分块大小 N 的定法：与池大小同量级（2-4 倍 max_workers），太小则批间空转多、太大则单批内存与异常放大面回涨；异常比例高时再收紧。若单任务粒度差异巨大，退到"信号量 + 无界生产"的逐条限流版本——把背压从"批粒度"下放到"任务粒度"。

## 背诵要点
- Executor.map 调用即全量物化提交（生成器也被吃光），队列为无界；结果按输入序 yield，异常在迭代点才抛。
- 异常中断循环 → 剩余结果丢弃、副作用不可回滚；海量输入用 islice 分块 + submit 循环 + 异常收集。
- TPE.map 与 Pool.map（chunksize）语义不同；Executor.map 不是生成器——API 同名不等于语义相同。

## 复盘追问
- map 传 10 万条生成器为什么 OOM？（立即全量物化提交，Future+闭包进无界队列；改分块提交显式背压）
- map 的异常行为和 submit 循环差在哪？（map 迭代点抛错中断循环丢剩余结果；submit 逐个 result 可收集继续）
