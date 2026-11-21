---
title: [Q1397] 隐式转换补遗: 字符集与排序规则不一致的 JOIN
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1397 · 隐式转换补遗: 字符集与排序规则不一致的 JOIN

> 难度:★★★★ | 标签:隐式转换, 字符集

**问**:两边列都有索引,JOIN 却走了全表扫描,可能是什么原因?

**答**:除了经典的类型不匹配(Q895),还有一类更隐蔽:字符集或排序规则不一致。utf8 表 join utf8mb4 表、general_ci join unicode_ci 时,优化器必须给一侧套 CONVERT 使比较语义统一,这一转换作用在列上,索引无法直接命中,连接退化为全扫或 BNL。定位看 EXPLAIN 输出里的隐式转换提示与 join 类型变差;根治是统一库、表、列的 charset 与 collation,迁移一次性改齐;临时手段是在低频侧用生成列预转换后建索引。教训是建库时就把 charset/collation 定死并写进规范,别让两张表各自演化。

```python
# file: code/04_数据库与缓存/q1397_collation_join.py
"""排序规则不一致的 JOIN: 每行转换使索引失效的代价模拟"""
import time

N_A, N_B = 20000, 20000
codes_a = [f"SKU{i:06d}" for i in range(N_A)]                            # general_ci 侧
codes_b = [f"SKU{i:06d}" if i % 2 else f"sku{i:06d}" for i in range(N_B)]  # unicode_ci 侧

a_set = set(codes_a)
a_set_lower = set(c.lower() for c in codes_a)

t0 = time.perf_counter()
hits_direct = sum(1 for v in codes_b if v in a_set)
t1 = time.perf_counter()
hits_conv = sum(1 for v in codes_b if v.lower() in a_set_lower)  # 逐行转换 无法直接命中索引
t2 = time.perf_counter()

print(f"collation 一致: 命中 {hits_direct}, {(t1 - t0) * 1000:.1f} ms")
print(f"collation 不一致逐行转换: 命中 {hits_conv}, {(t2 - t1) * 1000:.1f} ms")
print("统一 charset 与 collation, 或在生成列上预转换, 比硬扛便宜得多")
```

**追问**:
- 大小写不敏感的 collation 对唯一索引有什么影响?——'Abc' 与 'abc' 视为同一个键,唯一约束会拒绝第二条,排查唯一键冲突时要带上 collation 语义一起看。
- 为什么 CONVERT 落在列上索引就废了?——索引按原 collation 的序组织,套 CONVERT 后比较键变了,无法在 B+ 树上定位,只能全扫逐行转换。
- utf8 与 utf8mb4 混用是怎么埋下的?——5.7 默认字符集是三字节的 utf8(mb3),8.0 默认 utf8mb4;建表不显式声明就跟着默认走,新老表一 JOIN 就炸出转换。
- 生产陷阱?——升级大版本或换实例后服务器默认值变化,存量表被"悄悄改语义";规范强制建库建表显式声明 charset/collation,并纳入上线检查。

---
