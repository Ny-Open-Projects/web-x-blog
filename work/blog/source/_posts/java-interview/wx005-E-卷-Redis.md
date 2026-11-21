---
title: "E 卷 Redis"
date: 2026-11-18
categories: [Java面试, 笔试]
tags: [Java面试, 笔试题, 33]
type: 笔试题
disableNunjucks: true
---

## E 卷 Redis

**E-1（选择）** RDB + AOF（everysec）的丢失窗口？
A. RDB 两次快照间　B. AOF 最多 1 秒　C. 两者同时开启取最小　D. 不丢
**答案：B（单看 AOF）；A 是 RDB 的窗口**——混合持久化兼顾两者。

**E-2（选择）** 缓存一致性"先更新 DB 再删缓存"中，删除失败怎么办？
A. 重试直到成功　B. 抛异常回滚 DB　C. binlog 订阅异步删 + 重试队列　D. 不处理
**答案：C**（订阅 binlog 与业务解耦，失败进重试队列；TTL 兜底最终一致）。

**E-3（选择）** 布隆过滤器"返回不存在"的含义？
A. 一定不存在　B. 可能存在　C. 大概率存在　D. 无法判断
**答案：A。** 无漏判（说不在必不在）+ 有误判（说在可能不在）→ 适合当 DB 前置拦截器，误杀靠 DB 兜底。

**E-4（选择）** mem_fragmentation_ratio = 0.8 说明？
A. 碎片严重　B. 正常　C. 数据被换到 swap（比碎片更紧急）　D. 内存泄漏
**答案：C。** used_memory > RSS = 数据落到磁盘，性能塌方。

**E-5（简答）** 分布式锁四要素 + 看门狗 + RedLock 的工程结论。
**答案**：SET NX PX + 唯一 value + Lua 原子释放 + 看门狗续期；RedLock 争议（GC 停顿/时钟跳变/fencing 缺失）→ 锁分级：效率锁用 Redisson，正确性锁 DB 原子条件更新兜底。

**E-6（简答）** 热 key 和大 key 治理分别怎么做？
**答案**：热 key——本地缓存兜底 + key 打散 + 预热（是预测出来的不是故障时发现的）；大 key——分桶/压缩/UNLINK 异步删/巡检门禁，且是 Cluster 迁移的前置工程。

**E-7（简答）** Cluster 扩容时业务为什么会收到 ASK？MOVED 和 ASK 区别？
**答案**：槽迁移中源节点对未迁移 key 返回 ASK（临时跳，不更新映射缓存）；迁移完成后返回 MOVED（永久，客户端更新槽映射）。

**E-8（简答）** 没有 MQ，用 Redis 做延迟队列？
**答案**：ZSet（score=执行时间）+ ZRANGEBYSCORE 轮询 + **Lua 封装"取+删"防多消费者竞争** + 任务表补偿崩溃丢失；边界：无 Ack/无背压/轮询耗 CPU——有 MQ 就别用 Redis。

---
