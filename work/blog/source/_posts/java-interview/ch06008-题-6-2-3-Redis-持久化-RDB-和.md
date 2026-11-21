---
title: "题 6.2.3：Redis 持久化 RDB 和 AOF 怎么选？"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 6.2.3：Redis 持久化 RDB 和 AOF 怎么选？

**【参考回答（可背）】**
- **RDB**：定时快照（save/bgsave），**fork 子进程**写临时文件后原子替换。优点：文件小恢复快；缺点：两次快照间的数据会丢，fork 瞬间可能卡顿（内存越大越明显，COW 写时复制）。
- **AOF**：追加写命令日志。三种刷盘：always（每命令 fsync，最安全最慢）、**everysec（默认，最多丢 1 秒）**、no（交给 OS）。重写（bgrewriteaof）压缩体积（合并为最终数据集的写命令）。
- **4.0+ 混合持久化（推荐）**：重写时基础部分 RDF 格式 + 增量 AOF，恢复快且丢得少。
- 选型：纯缓存可以关持久化；有数据态（如分布式锁、计数）必须持久化 + 哨兵/Cluster 故障转移。

**【追问链】**
1. fork 卡顿怎么办？→ 大实例（10G+）监控 latest_fork_usec；控制单实例内存（建议 <10G）；物理机开大页禁用（THP off，反而 Redis 要禁 THP 否则 COW 放大内存）。
2. AOF 重写期间新命令怎么办？→ 重写缓冲区追加，写完后追加重写文件。

**【P10 加分项】**
容量与实例治理：单实例内存上限的工程共识（10~20G 内便于恢复/迁移/fork）、热 key 与大 key 排查（--bigkeys、rdb 分析工具 redis-rdb-cli）、大 key 治理（拆分、压缩、异步删除 unlink/ lazy free）。

---
