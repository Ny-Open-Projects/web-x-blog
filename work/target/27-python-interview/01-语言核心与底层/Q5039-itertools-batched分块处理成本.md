---
title: [Q5039] itertools.batched（3.12 新增）：分块处理的成本账
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5039 · itertools.batched（3.12 新增）：分块处理的成本账

> 难度:★★★ | 标签:itertools, batched, 3.12, 版本演进, 流式处理

**问**：3.12 新增的 `itertools.batched` 解决了什么重复代码？它和手写切片、grouper 配方、生成器分块在内存与成本上差在哪？分块大小怎么定？

**答**：`batched(iterable, n)` 把任意可迭代对象切成 n 元组流——它把"分块循环"这个写错率最高的样板代码（最后一个不满块、哨兵、切片边界）标准化了。三个实现的成本差异：1) **batched**：惰性、O(1) 内存、每块一个 tuple，**不填充**（末块短于 n 是常态）；2) 手写 `islice` 循环：同样惰性但要自己处理末块与哨兵；3) 切片 `data[i:i+n]`：要求输入可索引（list 先整体入内存），大输入直接 OOM。成本要点：batched 对 list 输入是零拷贝的引用分块（元组只装指针），对生成器输入是纯拉取；**分块大小 n 的账**：n 是"批处理摊销 vs 单批故障半径"的杠杆——数据库批量插入常用 500-1000（锁窗口，Q1964/Q2478），API 批量调用按下游上限，批太大单批超时/重试代价指数上升。注意版本演进细节：3.12 的 batched 第二参数必须 ≥1（ValueError），3.13 起支持 `strict=True`（末块不足时报错，对标 zip 的 strict，Q517）。GC 细节：分块元组本身是短命对象，高吞吐下会影响 gen0 GC 频率（Q402），必要时调 threshold 而不是手写对象池。

```python
# file: code/01_语言核心与底层/q5039_batched_cost.py
import itertools
import sys
import time

# 1) 基本语义: 惰性、末块不填充、每块是 tuple
data = list(range(10))
batches = list(itertools.batched(data, 3))
print("batched(10,3):", batches, "| 末块长度:", len(batches[-1]))

# 2) 内存账: 对生成器输入保持 O(1) —— 不会先物化整个流
def gen():
    yield from range(10)

first = next(iter(itertools.batched(gen(), 4)))
print("生成器输入惰性取块:", first)

# 3) strict=True (3.13+): 末块不足即报错, 对齐 zip 的契约风格
def strict_demo():
    try:
        list(itertools.batched(data, 4, strict=True))   # 3.13+
        return "strict OK (末块恰好整除才通过)"
    except TypeError:
        return "本解释器 <3.13, 无 strict 参数 -> 需自行校验"
    except ValueError as e:
        return f"strict 命中不等长: {e}"

print("strict:", strict_demo())

# 4) 分块大小成本实验: 模拟"每批固定开销 + 每条线性开销"
def process(n_items: int, batch: int, per_batch_us: float = 500) -> float:
    n_batches = (n_items + batch - 1) // batch
    return n_batches * per_batch_us + n_items * 1.0   # 微秒

for batch in (10, 100, 500, 5000):
    cost = process(100_000, batch)
    blast = batch / 1000  # 单批故障半径(千条)
    print(f"batch={batch:5d} 总成本≈{cost/1000:.0f}ms 单批故障半径={blast:.0f}k条")

# 5) 与切片法的输入约束对比: 切片要求可索引(先物化), batched 接受任意迭代
try:
    it = iter(gen())
    list(itertools.batched(it, 3))
    print("迭代器输入 batched OK")
except TypeError as e:
    print("意外:", e)
```

**追问**：1) batched 为什么返回 tuple 而不是 list？——tuple 构造更快且不可变（下游误改风险为零），一次性物化语义与"批"的概念匹配；需要 list 时 `list(batch)` 自行转换。2) 3.12 与 3.13 的 batched 有什么演进差异？——3.13 加 `strict=True`（对齐 PEP 里 zip strict 的契约风格），并允许 n 为关键字参数；写跨版本代码时 strict 参数要 try/TypeError 兜底。3) 为什么不全用 batched(1) 逐条处理？——每批固定开销（网络往返/事务提交/锁获取）会被放大 n 倍，分块的本质是摊销固定成本；但批太大又放大故障半径与重试代价，账要两头算。

## 背诵要点
- batched：惰性 O(1) 内存、每块 tuple、末块不填充；3.13 加 strict=True 对齐 zip strict。
- 分块大小 = 固定开销摊销 vs 故障半径的杠杆，DB 批插常用 500-1000。
- 切片分块要求可索引输入（先物化），batched 接受任意迭代器。

## 复盘追问
- 你的批量写库把 batch 从 1000 调到 5000，耗时降了但偶发超时重试翻倍，怎么用成本模型定最优点？
- 高吞吐流水线里每秒产生十万级分块元组，GC 侧你会观察什么指标、怎么调？
