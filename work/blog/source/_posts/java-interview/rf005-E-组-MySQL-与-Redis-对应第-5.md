---
title: "E 组：MySQL 与 Redis（对应第 5、6 章）"
date: 2026-11-18
categories: [Java面试, 快问快答]
tags: [Java面试, 快问快答, 33]
type: 快问快答
disableNunjucks: true
---

## E 组：MySQL 与 Redis（对应第 5、6 章）

41. **B+ 树为什么矮胖？** 非叶节点只存键扇出极大，3~4 层覆盖千万行；叶子链表支持范围扫。
42. **二级索引为什么回表？** 叶子只存索引列+主键，其他列要回聚簇索引取；覆盖索引免回表。
43. **MVCC 可见性判断？** 版本链 + ReadView（m_ids/min/max/creator），RC 每语句、RR 每事务一次视图。
44. **两阶段提交顺序？** redo prepare → 写 binlog → redo commit；崩溃恢复看 binlog 完整性定夺。
45. **分片键四原则？** 高频查询带分片键、分布均匀、业务身份相关（user_id）、避免跨片事务。
46. **缓存三大问题口诀？** 穿透挡（布隆/空值）、击穿合（单飞/逻辑过期）、雪崩抖（TTL 随机+多级）。
47. **缓存一致性标准方案？** 先更新 DB 再删缓存 + binlog 异步删 + TTL 兜底最终一致。
48. **分布式锁四要素？** SET NX PX、唯一 value、Lua 原子释放、看门狗续期；正确性靠 DB 兜底。
49. **哨兵选主四步？** replica-priority → offset 最大 → runid 最小；主观下线→客观下线→Raft 选 leader→执行转移。
50. **热 key 治理？** 本地缓存兜底 + key 打散分片 + 大促预热；热 key 是预测出来的不是故障时发现的。
