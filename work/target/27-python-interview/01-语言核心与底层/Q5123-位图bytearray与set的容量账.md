---
title: [Q5123] 大规模 ID 集合的位图容量账：bytearray vs set
date: 2026-11-21
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5123 · 大规模 ID 集合的位图容量账：bytearray vs set

> 难度:★★★☆☆ | 标签:容量规划, 位图, bytearray

**问**:要判断"1 亿个用户 ID（0 ≤ id < 1e8）里哪些出现过"，面试者都答 set，但内存撑不住。用 `bytearray` 做位图要多少内存？set 撑到多大？什么条件下位图不划算？

**答**:结论：先算账。**set 存 int**：每个 int 对象约 28 字节 + set 槽位（load factor 约 0.6，每元素摊约 8-16 字节表空间），1 亿个去重 int ≈ 3.6-4.5 GB，还没算转 int 本身的解析成本。**位图 bytearray**：每 ID 只占 1 bit，1e8/8 = 12.5 MB——差 300 倍。实现上用 `bytearray(N // 8 + 1)`，置位 `buf[id >> 3] |= 1 << (id & 7)`，查询同掩码。取舍：位图只在**ID 值域紧凑**时划算；若 ID 是稀疏雪花号（值域 1e18），位图要按 max(id) 开空间，直接爆——此时改用 Roaring 风格的"分块位图"（高位分桶 + 桶内位图/有序数组混合）或干脆放 Redis bitmap。实战延伸：a) `int.from_bytes`/`memoryview` 可把位图当不可变载体序列化传输；b) 多线程置位同字节有竞态（`|=` 非原子），要么按 ID 分片加锁，要么用 numpy/ctypes 原子写；c) 计数场景别把"判重位图"误当"计数器"——那是 8 倍空间的 bitmap-counter 或 HyperLogLog 的活。

```python
import sys, random

def bitmap_ops(nbits: int):
    buf = bytearray(nbits // 8 + 1)
    def add(i): buf[i >> 3] |= 1 << (i & 7)
    def has(i): return bool(buf[i >> 3] >> (i & 7) & 1)
    return buf, add, has

N = 1_000_000
random.seed(7)
ids = [random.randrange(0, N) for _ in range(N // 10)]   # 10 万个 ID，值域 1e6

# ---- 方案一：set ----
s = set(ids)
set_mem = sys.getsizeof(s) + sum(sys.getsizeof(i) for i in s) * 0 + sys.getsizeof(0) * len(s)
print(f"set: {len(s)} 个去重 int，粗账 {set_mem/1e6:.1f} MB（不含表开销）")

# ---- 方案二：位图 bytearray ----
buf, add, has = bitmap_ops(N)
for i in ids:
    add(i)
print(f"bytearray 位图: {sys.getsizeof(buf)/1e6:.2f} MB（值域 1e6 -> 约 0.125 MB 量级）")
print("抽查命中:", has(ids[0]), "| 未命中:", has(N - 1) if ids[0] != N - 1 else "-")

# ---- 稀疏值域的反例：雪花号位图不可行 ----
snow_id = 723_100_000_000_000_123
print(f"稀疏雪花号位图需 {snow_id/8/1e9:.1f} GB —— 必须换分块位图或外部结构")

# ---- 置位吞吐（位运算 O(1)，瓶颈在 Python 层循环） ----
import timeit
b2, add2, _ = bitmap_ops(N)
t = timeit.timeit(lambda: add2(123), number=1_000_000)
print(f"单次置位 {t/1e6*1e9:.0f} ns 量级，1 亿次置位约 {t*100:.1f}s（热数据建议 numpy/C 层批量）")
```

**追问一层**:为什么 set 的内存粗账要乘 load factor？（hash 表开放寻址，槽位约 2 倍于元素数，8/16 字节槽 + resize 峰值双倍）。
**追问二层**:如何在位图上做两个集合的交集？（`bytes` 层按块 AND：`bytes(a & b for ...)` 或 `int.from_bytes` 转大整数做位与，再转回——大整数位运算走 C 层，比逐字节循环快一个数量级）。
**追问三层**:10 亿 ID、允许 1% 误判率，标准位图会退化，用什么？（布隆过滤器：m = -n·ln p / (ln 2)² ≈ 1.2 GB @ k=7，或布谷鸟过滤器支持删除）。

## 背诵要点
- set 存 int：每元素 28B 对象 + 表开销，1 亿 ≈ 4 GB；1 bit 位图：1e8 值域仅 12.5 MB，差 300 倍。
- 位图前提是值域紧凑；稀疏 ID 用分块位图（Roaring）或 Redis bitmap，误判容忍用布隆（m ≈ 1.2GB @ 1e9/1%）。
- `buf[i>>3] |= 1 << (i&7)` 置位、同掩码查询；多线程同字节 `|=` 有竞态。

## 复盘追问
- 服务从"全量判重"升级到"10 亿 ID + 内存预算 2 GB"，位图/布隆/外部 bitmap 三个方案的迁移步骤怎么排？
- 为什么把位图转成一个大 int 再做位运算比逐字节 Python 循环快？边界（块大小、内存峰值）怎么控？
