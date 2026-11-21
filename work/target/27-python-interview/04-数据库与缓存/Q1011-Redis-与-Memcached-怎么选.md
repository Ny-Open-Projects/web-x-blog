---
title: [Q1011] Redis 与 Memcached 怎么选
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1011 · Redis 与 Memcached 怎么选

> 难度:★★★☆ | 标签:选型, 缓存

**问**:同样是内存 KV,Redis 与 Memcached 的核心差异是什么?

**答**:Memcached 是纯缓存:多线程、简单 KV(只 string)、内存预分配 slab、超容量即淘汰、无持久化;Redis 单线程(6.0 IO 多线程)命令丰富(五种结构+模块)、可持久化(RDB/AOF)、支持复制与集群、Lua 脚本、发布订阅。选型:纯"string 级缓存"且要极致吞吐、多核利用率(如 session、fragment 缓存)Memcached 依然能打;需要结构化操作(zset 排行榜、hash 对象)、持久化容灾、锁/队列等高级语义,选 Redis。现实工程默认 Redis(生态与运维工具完善),Memcached 只在"超大内存池 + 简单 KV"的特定场景(如老牌社交 feed)保留。面试补充:两者都不适合做数据库,Redis 持久化也代替不了 DB。

```python
# file: code/04_数据库与缓存/q1011_redis_vs_memcached.py
"""两种缓存的能力矩阵对照"""
MATRIX = """
能力            Redis            Memcached
数据结构        string/hash/list/zset/stream   仅 string
持久化          RDB/AOF/混合      无
高可用          哨兵/集群/复制    客户端一致性哈希
原子脚本        Lua               无(仅 cas)
内存模型        按需分配+淘汰     slab 预分配
多线程          6.0 io 多线程     多线程工作线程
适用            结构化+高级语义   纯 KV 大内存池缓存
"""
if __name__ == "__main__":
    print(MATRIX)
    print("选型: 要结构/持久化/锁 -> Redis; 纯 string 缓存要极致多核 -> Memcached")
```

**追问**:
- Memcached 为什么曾更"抗大流量"?——多线程吃满多核、无持久化 fork 卡顿,纯 GET/SET 场景延迟稳定;Redis 6.0 IO 多线程后差距缩小。
- 两者淘汰行为差异?——Memcached slab 内按 LRU 淘汰(可能立刻顶掉刚写入的),Redis 按全局 maxmemory 策略(可配置 noeviction),语义更可控。

---
