---
title: [Q1690] 大 hash 分段: 单 key 过大的拆分
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1690 · 大 hash 分段: 单 key 过大的拆分

> 难度:★★★☆ | 标签:Redis, 大 key

**问**:一个 hash 装了 100 万个字段,会有什么问题?怎么拆?

**答**:大 hash 的危害集中在读写两端:HGETALL、DEL、过期回收都是 O(N) 且单线程执行,一次操作阻塞整个实例;主从同步与持久化也会被大 value 拖慢。拆分方案是按 field 哈希路由到固定数量的桶,如 field -> hash(field) % 16,点查先算桶号再 HGET,批量读按桶分组后 pipeline,聚合统计遍历所有桶。工程纪律:路由函数上线后不可更换,换桶数等于全量迁移;删除大 hash 要 HSCAN 分批 HDEL,禁止一次性 DEL;桶内仍大可二次拆分。大 key 治理配合 SCAN 与内存分析工具定期巡检,发现即拆。

```python
# file: code/04_数据库与缓存/q1690_big_hash_split.py
"""大 hash 分段: 单 key 过大的拆分路由与聚合读取"""
import hashlib

FIELDS = 100000

def bucket_of(field, n_bucket=16):
    h = int(hashlib.md5(field.encode()).hexdigest(), 16)
    return h % n_bucket

# 拆分前: 一个 hash 10 万 field, HGETALL 会阻塞整个实例
big = {f"item:{i}": i * 2 for i in range(FIELDS)}
print(f"拆分前: 1 个 key, {FIELDS} 个 field")

# 拆分后: 按 field 哈希路由到 16 个桶
shards = [dict() for _ in range(16)]
for k, v in big.items():
    shards[bucket_of(k)][k] = v
print("拆分后各桶 field 数:", [len(s) for s in shards])

def hget(field):
    return shards[bucket_of(field)].get(field)

def hgetall():
    out = {}
    for s in shards:
        out.update(s)
    return out

print("点查路由正确:", hget("item:12345") == big["item:12345"])
print("聚合全量 field 数:", len(hgetall()))
print("工程要点: 桶数固定可预估; 批量读按桶分组再 pipeline; 删 key 要遍历所有桶;")
print("          路由函数一旦上线不可更换, 换桶数等于全量迁移; 桶内仍大可二次拆分")
```

**追问**:
- 拆多少个桶合适?——按单桶目标大小反推,常见经验是单 key 控制在几十 KB 到 1MB;桶数是 2 的幂方便取模与再分。
- 业务前缀取模为什么不好?——热点字段会集中到同一桶,哈希打散才是均匀的;前缀取模只适合天然均匀的编号型键。

---
