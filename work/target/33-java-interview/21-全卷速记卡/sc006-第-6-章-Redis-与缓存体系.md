---
title: "第 6 章 Redis 与缓存体系"
date: 2026-11-18
categories: [Java面试, 速记卡]
tags: [Java面试, 速记卡, 33]
type: 速记卡
disableNunjucks: true
---

## 第 6 章 Redis 与缓存体系

1. Redis 快四因：内存、epoll、单线程无锁、专用数据结构。
2. ZSet = 跳表 + 字典双结构；小对象 listpack 压缩。
3. 过期 = 惰性 + 定期抽样；淘汰必配 allkeys-lru/lfu。
4. 穿透挡（布隆/空值）、击穿合（单飞/逻辑过期）、雪崩抖（TTL 随机+多级）。
5. 一致性标准答案：先更新 DB 再删缓存 + binlog 异步删 + TTL 兜底。
6. 锁：SET NX PX + 唯一 value + Lua 删 + 看门狗；正确性靠 DB 兜底。
7. RDB 快恢复丢数据，AOF everysec 丢 1 秒，4.0 混合是推荐默认；fork 卡顿看 latest_fork_usec。
8. 哨兵：主观→客观→Raft 选 leader→四步选从；奇数 ≥3 防脑裂。
9. 热 key：本地缓存+打散；大 key：UNLINK+分桶+巡检；大 key 是 Cluster 扩容前置工程。
10. 单实例内存 <10G；KEYS 禁用；Lua 三红线（10 行内/单 key 组/O(1)）。
11. 碎片 ratio>1.5 用 activedefrag；<1 是 swap 更紧急；无界增长查大 key。
12. 版本演进主线：编码简化（listpack）→ IO 并行化（多线程 IO/Sharded PubSub）。
