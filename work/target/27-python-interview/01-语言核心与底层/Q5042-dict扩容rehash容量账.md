---
title: [Q5042] dict 扩容与 rehash 的容量账
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5042 · dict 扩容与 rehash 的容量账

> 难度:★★★ | 标签:dict, rehash, 容量规划, p99

**问**：给一个高吞吐服务做容量规划，热点 dict 会涨到千万级 key。dict 的扩容（rehash）机制是什么？扩容瞬间会发生什么（延迟毛刺、内存翻倍）？如何预估一个千万 key dict 的实际内存并做容量预算？

**答**：CPython dict 用紧凑结构（dk_indices + dk_entries）。负载因子超阈值（`usable*3 >= size*2`，即约 2/3 满）触发扩容：新表容量按 `used*3` 对齐到 2 的幂（小表翻倍、大表 `used*3` 取整），然后**一次性把所有 entry 重新插入新表**——O(n) 停顿，且新旧两表短暂共存使瞬时内存接近翻倍。容量账三步：1) **内存**：`sys.getsizeof(d)` 给出表结构大小，加上 key/value 对象本体（Q556 是浅大小）；千万级 `str→int` dict 实测量级约数百 MB，可用 `getsizeof` + 抽样 key 对象大小推算；2) **毛刺**：rehash 是同步的，写入线程在扩容瞬间出现毫秒级停顿（千万 key 实测可达几十 ms 量级，取决于 key 类型与缓存命中率），对 p99 敏感的服务要把"扩容点"当作已知毛刺源；3) **预算**：预知规模时**一次性建满**（先插入再使用，或 `dict.fromkeys` 预置），让扩容发生在启动期而非流量高峰；或改分片（多个小 dict，扩容粒度变小）。与 list 的渐进式 over-allocation（Q1263）不同，dict 扩容无"渐进"选项，这是设计上要记住的差异。

```python
# file: code/01_语言核心与底层/q5042_dict_rehash.py
import sys
import time
import tracemalloc

d = {}
prev_size = sys.getsizeof(d)
print("初始表大小:", prev_size, "bytes")

# 观测扩容点: getsizeof 跳变 = rehash 发生
resizes = []
for i in range(20000):
    d[f"key-{i}"] = i
    s = sys.getsizeof(d)
    if s != prev_size:
        resizes.append((len(d), prev_size, s))
        prev_size = s
for n, before, after in resizes[:6]:
    print(f"len={n:>6} 时扩容: {before:>7} -> {after:>7} bytes")
print("前 2 万 key 共扩容", len(resizes), "次")

# rehash 停顿实测: 从 50 万 key 再涨一批, 对比稳态插入与扩容点插入
big = {f"k{i}": i for i in range(500_000)}
t0 = time.perf_counter()
for i in range(50_000):
    big[f"x{i}"] = i
steady = (time.perf_counter() - t0) * 1000
# 一次性建满同样的 55 万, 观测整体成本(含全部扩容)
t0 = time.perf_counter()
full = {f"j{i}": i for i in range(550_000)}
build = (time.perf_counter() - t0) * 1000
print(f"稳态批量插入 5 万: {steady:.0f} ms | 含扩容建满 55 万: {build:.0f} ms")

# 容量预估: 表结构 + 抽样 key/value 本体
n = len(big)
sample = 2000
ks = sum(sys.getsizeof(k) for k in list(big.keys())[:sample]) / sample
vs = sys.getsizeof(0)  # 小 int 共享, 真实业务对象要抽样自己的 value
est = sys.getsizeof(big) + n * (ks + vs)
tracemalloc.start()
mark = {f"k{i}": i for i in range(100_000)}
cur, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"getsizeof 估算 55 万 key ≈ {est/1e6:.0f} MB(不含共享 int 复用)")
print(f"tracemalloc 实测 10 万 key: {cur/1e6:.1f} MB -> 推算 55 万 ≈ {cur/1e6*5.5:.0f} MB")
```

**追问**：1) dict 删除大量元素后内存会归还吗？——dict **从不收缩**（删除只标记 DKIX_DUMMY 占位，insert 复用空洞），千万 key 删剩 1 万后 `getsizeof` 不变；要释放只能重建 dict。这是容量规划里"内存只涨不降"的关键假设（对比 Q6029 RSS 不降问题在 allocator 层的叠加）。2) 为什么 3.7+ 保证 dict 有序，扩容会不会打乱顺序？——顺序由 dk_entries 的插入序保证，rehash 只重建 dk_indices 索引表、entries 顺序不变，所以扩容与有序性正交。3) key 全是 int 时有什么优化？——小整数有共享池（Q006）且 int key 的 hash 是自身，rehash 缓存友好；容量估算时 value 若是小 int 别按每对象 28 bytes 重复计入。

## 背诵要点
- dict 约 2/3 满触发扩容：一次性 O(n) rehash + 新旧表共存内存近翻倍，是 p99 毛刺源。
- 预知规模就在启动期一次建满；高基数场景用分片降低单次扩容粒度。
- dict 删除不收缩内存；估算 = getsizeof(表) + 抽样的 key/value 对象本体。

## 复盘追问
- 你的服务 p99 每天固定时刻出现毛刺，如何验证/排除"dict 扩容点"这个假设？（提示：对齐 key 数量增长曲线与毛刺时间点，py-spy 看栈是否落在 dict insert）
- 千万 key 的 dict 改分片时，怎么选分片函数和分片数？（提示：hash 前缀取模 vs 一致性哈希，Q1341，扩容迁移成本与数据倾斜）
