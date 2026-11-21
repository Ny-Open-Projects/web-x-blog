---
title: [Q1697] 字段级过期模拟: hash 里没有 HMEXPIRE
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1697 · 字段级过期模拟: hash 里没有 HMEXPIRE

> 难度:★★★★ | 标签:Redis, 设计

**问**:hash 里的某个字段需要单独过期,Redis 没有这个能力怎么办?

**答**:两种工程解法。方案一,值与到期时间戳成对存储:field 存值,旁边存 expire_at,读路径先比较时间戳做过期判定并懒清理,再加一个后台扫描兜底清理冷字段;优点是单 key 自洽,缺点是读路径有额外开销、过期精度取决于清理时机。方案二,用 zset 建到期索引:成员是字段名、分值是到期时间戳,周期 ZRANGEBYSCORE 拿到期字段,批量 HDEL 加 ZREM;优点是到期集合天然有序、批量清理高效,缺点是多维护一个索引结构的一致性。共同结论:这是模拟实现,读路径必须容忍"过期但还在"的中间态,强一致过期需求要换成每字段独立 key。

```python
# file: code/04_数据库与缓存/q1697_field_expire.py
"""字段级过期模拟: hash 没有 HMEXPIRE 时的两种工程解法"""

NOW = 1000.0

class FieldTTLHash:
    """解法一: 值与到期时间戳成对存储, 读时懒清理"""

    def __init__(self):
        self.data, self.expire_at = {}, {}

    def hset(self, field, value, ttl):
        self.data[field] = value
        self.expire_at[field] = NOW + ttl

    def hget(self, field):
        if field in self.data and NOW >= self.expire_at.get(field, NOW + 1):
            self.data.pop(field)              # 懒清理
            self.expire_at.pop(field)
            return None
        return self.data.get(field)

    def purge(self):
        dead = [f for f in self.expire_at if NOW >= self.expire_at[f]]
        for f in dead:
            self.data.pop(f, None)
            self.expire_at.pop(f, None)
        return dead

h = FieldTTLHash()
h.hset("session:a", "tok-a", 60)
h.hset("session:b", "tok-b", 5)
print("立即读 b:", h.hget("session:b"))
h.expire_at = {k: v - 6 for k, v in h.expire_at.items()}   # 时间推进 6 秒
print("6 秒后读 b:", h.hget("session:b"), "(懒清理命中)")
print("6 秒后读 a:", h.hget("session:a"))
print("后台清扫移除:", h.purge())

print("解法二: 用 zset 以到期时间为分值建索引, 周期按分数段批量删除")
deadlines = {1000 + 5: "session:b", 1000 + 60: "session:a"}
due = [f for t, f in sorted(deadlines.items()) if t <= NOW + 6]
print("zrangebyscore 到期字段:", due, "-> HDEL 批删 加 ZREM 索引")
print("要点: 字段级 TTL 是模拟实现, 读路径要懒清理, 后台要有扫描兜底; 强一致过期不要依赖它")
```

**追问**:
- 什么时候直接拆成独立 key?——字段过期精度要求高或字段数可控时,每字段一个 key 加原生 TTL 最简单,代价是 key 数量与内存开销。
- 方案二的一致性谁保证?——HDEL 与 ZREM 放同一段 Lua 里原子执行,否则索引里会残留死成员被反复扫出。

---
