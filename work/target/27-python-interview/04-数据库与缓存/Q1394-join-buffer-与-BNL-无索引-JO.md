---
title: [Q1394] join buffer 与 BNL: 无索引 JOIN 的两条退路
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1394 · join buffer 与 BNL: 无索引 JOIN 的两条退路

> 难度:★★★☆ | 标签:SQL 调优, JOIN

**问**:JOIN 的关联列没索引会怎样?Block Nested Loop 和 Hash Join 怎么救?

**答**:没索引时每行外表都要全扫一次内表,plain NLJ 的代价是 m×n 次比较。BNL 的救法是把外表按 join_buffer_size 分块装载,每块只扫一遍内表,比较次数降到 n×ceil(m/buffer);代价是内表要被反复扫。MySQL 8.0.18 起等值 JOIN 默认改用 Hash Join:对小侧建哈希表、大侧逐行探测,比较量从乘法降为加法,内存够就一次成活。共同结论:join buffer / hash 表都吃内存,不是越大越好;真正的根治仍然是被驱动表的关联列建索引,让优化器根本用不上这两条退路。

```python
# file: code/04_数据库与缓存/q1394_join_buffer.py
"""无索引 JOIN 的两条路: 块嵌套循环 BNL 与 hash join 的比较量对比"""
import random

random.seed(4)
N_L, N_R, BUF = 500, 5000, 100
left = [{"uid": i} for i in range(N_L)]
right = [{"uid": random.randrange(N_L)} for _ in range(N_R)]

def bnl_cost(l, r, buf):
    cmp = 0
    for i in range(0, len(l), buf):
        block = l[i:i + buf]
        for row in r:
            for b in block:
                cmp += 1
                if b["uid"] == row["uid"]:
                    pass
    return cmp

def hash_join_cost(l, r):
    ht = {}
    for row in l:
        ht.setdefault(row["uid"], []).append(row)
    return len(r)              # 内表逐行探测哈希表, 每次 O(1)

c1 = bnl_cost(left, right, BUF)
c2 = bnl_cost(left, right, N_L)
c3 = hash_join_cost(left, right)
print(f"join buffer=100: 约 {c1} 次比较")
print(f"join buffer=全表: 约 {c2} 次比较, 用内存换内表扫描遍数")
print(f"hash join: {c3} 次探测, MySQL 8.0.18 起等值 join 默认取代 BNL")
```

**追问**:
- 为什么 hash join 只在等值条件下用?——非等值无法用哈希桶定位,只能退回 NLJ/BNL 逐对比较。
- hash join 内存不够会怎样?——构建侧装不下 join_buffer_size 时分批构建与探测,内表要多扫几遍,代价从近似 O(m+n) 退化回接近 BNL。
- 构建侧怎么选?——优化器估算两侧过滤后的行数,拿小的一侧建哈希表省内存;统计信息失真时可能选错侧,大侧建表直接撑内存。
- 生产陷阱?——hash join 是无索引时的退路,buffer 按连接分配,高并发大 JOIN 会并发吃内存;别把退路当常态,根治仍是被驱动表关联列建索引。

---
