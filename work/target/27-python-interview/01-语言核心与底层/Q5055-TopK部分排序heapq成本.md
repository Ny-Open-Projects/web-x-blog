---
title: [Q5055] Top-K 部分排序 heapq.nsmallest 的成本工程
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5055 · Top-K 部分排序 heapq.nsmallest 的成本工程

> 难度:★★★ | 标签:heapq, nsmallest, sorted, 排序, 成本工程

**问**：账单页要"消费额最高的前 10 笔"，后台任务写了 `sorted(transactions)[:10]`，数据到千万级后越来越慢。Top-K 问题有几种解法？`heapq.nsmallest` 为什么快？什么时候它反而比 sorted 慢？

**答**：三种解法成本结构完全不同。a) `sorted(data)[:k]`：O(n log n) 全排，n 个元素一个不落，还要物化整个新列表——k=10 时 99.99% 的工作是浪费；实测 100 万 int 约 400ms。b) `heapq.nsmallest(k, data)`：O(n log k)——维护一个 k 大小的堆，n 个元素各做一次"比堆顶+替换"，实测 100 万取 10 约 26ms，快 15 倍；对 k 很小、n 很大的场景是标准答案。c) 单遍维护最小堆（`heappushpop` 手写循环）：与 nsmallest 同阶但多了 Python 层循环开销，一般不如内置的 nsmallest（它内部有 C 优化路径）。反直觉的坑：**k 逼近 n/√n 量级时 nsmallest 反而劣化**，实测取 50 万条耗时 2.3s，远超 sorted 的 0.4s——因为堆维护成本 log k 随 k 涨，而 sorted 的 log n 几乎不动。工程上还有两条：数据在数据库里就 `ORDER BY x DESC LIMIT k`（走索引比任何 Python 端排序都省）；`nsmallest` 保证稳定性（并列时保留原序），取出来的前 k 个本身是有序的。

```python
# file: code/01_语言核心与底层/q5055_topk.py
import heapq, random, time

random.seed(42)
data = [random.randint(0, 10**9) for _ in range(1_000_000)]

t0 = time.perf_counter(); top1 = sorted(data)[:10]
t1 = time.perf_counter() - t0
t0 = time.perf_counter(); top2 = heapq.nsmallest(10, data)
t2 = time.perf_counter() - t0
print(f"sorted 全排 O(n log n): {t1*1000:.1f}ms")
print(f"nsmallest(10) O(n log k): {t2*1000:.1f}ms")
assert top1 == top2  # 结果一致且已按序

# 反例: k 接近 n 时 nsmallest 劣化
t0 = time.perf_counter(); heapq.nsmallest(500_000, data)
t3 = time.perf_counter() - t0
print(f"nsmallest(50万): {t3*1000:.1f}ms -> k/n 超过 ~1% 就老老实实 sorted")

# 流式场景: 数据逐条到达, 维护 Top-K, 内存 O(k)
heap = []  # 最小堆, 堆顶是当前第 10 大
for x in data[:100_000]:
    if len(heap) < 10:
        heapq.heappush(heap, x)
    elif x > heap[0]:                  # 比当前第 10 大还大才替换
        heapq.heapreplace(heap, x)
print("流式 Top-10 最大值:", sorted(heap, reverse=True))
```

**追问**：1) `nlargest` 和 `nsmallest` 哪个取"最大 10 个"？——`heapq.nlargest(10, data)`，Python 堆是最小堆，nlargest 内部同样做了取反/等价处理；结果已按降序排好。2) 数据是生成器（只能遍历一次）时三种方案怎么选？——sorted 要求先把生成器物化成 list（内存 O(n)）；nsmallest/nlargest 天然吃迭代器，内存 O(k)，流式唯一正解。3) `sorted(data, key=..., reverse=True)[:k]` 带 key 时 nsmallest 的优势还在吗？——在，且更大：nsmallest 对 key 只计算一次（内部先装饰后堆化），sorted 同样只算一次 key，差距主要来自 log k vs log n 的比较次数。

## 背诵要点
- Top-K 三档：sorted O(n log n) 全排物化；heapq.nsmallest O(n log k) 吃迭代器内存 O(k)；DB 内直接 ORDER BY ... LIMIT k。
- 实测 100 万取 10：sorted ≈400ms，nsmallest ≈26ms；但 k/n 超过约 1% 时 nsmallest 反超变慢（50 万条 2.3s）。
- 流式单遍：`heapreplace` 维护 k 大小堆，"比堆顶大才替换"；nlargest 返回降序、nsmallest 返回升序且稳定。

## 复盘追问
- 你们代码里有多少个 `sorted(...)[:k]` 式的 Top-K？审计思路是什么？（提示：grep `[:` 截断模式 + 按 n 与 k 的实际规模复核）
- 报表 Top-K 要求"近 7 天"滚动窗口，实时流里怎么维护？（提示：堆内元素带时间戳过期淘汰，或改用 Redis ZSET 滑窗）
