---
title: [Q888] JOIN 算法: Nested Loop / Block NL / Hash Join
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q888 · JOIN 算法: Nested Loop / Block NL / Hash Join

> 难度:★★★★ | 标签:JOIN, 优化器

**问**:MySQL 的 JOIN 是怎么执行的?8.0 的 hash join 改变了什么?

**答**:MySQL 传统上是 Nested Loop Join(NLJ):外层每取一行,到内层索引里"点查"一次,内层有索引时总代价约"外层行数 × 索引查找",这是好情况;内层无可用索引则退化为 Block Nested Loop——把外层一批行装进 join buffer,整批与内层全表比对,内存换 IO 但仍是全表次数乘积级。MySQL 8.0.18 引入 Hash Join 替代 BNL:内层建哈希表后逐行探测,代价变为"两表各扫一遍 + 哈希查找",等值 join 无索引时数量级提升。SQLite/PG 一直有三算法(NL/Merge/Hash)按成本选择。Python 层面可以用列表模拟两种算法,直观看到复杂度差异。

```python
# file: code/04_数据库与缓存/q888_join_algorithms.py
"""纯逻辑实现 nested loop 与 hash join, 对比操作次数"""
from itertools import product

def nested_loop(a, b):
    ops = 0
    out = []
    for ra in a:
        for rb in b:
            ops += 1
            if ra["k"] == rb["k"]:
                out.append((ra, rb))
    return out, ops

def hash_join(a, b):
    ops = 0
    table = {}
    for rb in b:                      # build: 内表建哈希
        table.setdefault(rb["k"], []).append(rb)
    out = []
    for ra in a:                      # probe: 外表探测
        ops += 1
        for rb in table.get(ra["k"], ()):
            out.append((ra, rb))
    return out, ops

if __name__ == "__main__":
    A = [{"k": i % 100, "v": i} for i in range(1000)]
    B = [{"k": i % 100, "v": i} for i in range(1000)]
    _, ops1 = nested_loop(A, B)
    _, ops2 = hash_join(A, B)
    print(f"nested loop 比较 {ops1} 次, hash join {ops2} 次")
    print("MySQL 对照: 内表无索引的等值 JOIN 在 8.0.18 起用 hash join 替代 BNL")
```

**追问**:
- hash join 有什么限制?——只支持等值条件,哈希表要能装下(或走 grace hash 分区),排序类 join 仍需 merge join 或排序。
- 为什么说"内层表有索引"对 NLJ 至关重要?——NLJ 的每次内层访问从全表扫描降为索引点查,总代价由 M×N 降到 M×logN,这正是"小表驱动大表+索引"的根基。

---
