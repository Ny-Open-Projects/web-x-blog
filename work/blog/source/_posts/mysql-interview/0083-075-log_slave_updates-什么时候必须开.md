---
disableNunjucks: true
title: "075 log_slave_updates 什么时候必须开"
date: 2026-10-16 03:45:24
categories: [MySQL面试题集]
tags: [MySQL面试题集]
---

> 分类：日志类 | 难度：L3 | 题型：工程题 | 频率：中 | 关键词：**log_slave_updates** / **级联复制** / **GTID** / **log_replica_updates**
> 原文锚点：第 405~408 段「默认情况下，从库上的二进制日志并不会记录从主上同步过来的二进制日志的内容…比如需要进行级联复制，或者需要使用 GTID 复制时」

## 一句话总述
从库默认**不把主库同步来的事件写进自己的 binlog**；要做**级联复制**（从库再当别人的主）或依赖从库 binlog 做**备份/回放**时，必须开 `log_slave_updates`。

## 面试官视角
- **考察意图**：你是否做过真实的多级复制拓扑，而不是只搭过一主一从。
- **P5** 知道有这个参数 / **P6** 知道级联复制要开 / **P7** 会顺带讲 **GTID 场景下从库 binlog 是丢失事务的"唯一副本"** 这一备份论点。
- **红旗**：① 认为"从库不需要 binlog"；② 开启后忘了磁盘容量翻倍；③ 不知道 8.0 改了参数名。
- **惊艳点**：开了它 + 从库 binlog，就能把**备份放到从库**做，主库零负担 `[经验]`。验证：从库 `SHOW BINARY LOGS` 有增长即生效。

## 主问答
**Q（面试官原话）：** 从库要不要开 binlog？什么时候必须开？

**A：**
1. **先给结论**：默认不需要（`log_slave_updates=OFF`）；**级联复制**、**GTID 复制**、**从库做备份/时间点恢复**这三类场景必须开。
2. **再给机制**：从库的 SQL 线程回放 relay log 后，只有开启该参数才会把事件**再写一份进自己的 binlog**，下一级从库才有得可拉；否则从库 binlog 里只有本地直写的数据，链路在这一级断掉。
3. **最后给边界**：开启后从库**写放大 + 磁盘占用上升**，容量与 IO 要按主库规格评估；参数**非动态**，需改配置文件**重启**实例。

**加分层**：MySQL 8.0.26 起参数改名为 `log_replica_updates`（slave→replica 术语调整），老参数名仍兼容一段时间 `[经验]`。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
|---|---|---|---|---|
| L1 | 从库有 binlog 吗 | 概念 | 可以有，但默认不记同步来的 | 换题 → 不及格 |
| L2 | 由什么参数控制 | 参数 | log_slave_updates | 判 P5 |
| L3 | 什么场景必须开 | 场景 | 级联 / GTID / 从库备份 | 判 P6 |
| L4 | 代价是什么 | 成本 | 磁盘与写放大 | 判 P6+ |
| L5 | 8.0 叫什么 | 版本视野 | log_replica_updates | 答上判 P7 |

## 版本与兼容性
| 结论成立版本 | 变化点 | 现在该怎么答 |
|---|---|---|
| ≤ 8.0.25 | log_slave_updates | 配置文件写这个 |
| ≥ 8.0.26 | 更名 log_replica_updates | 新名优先，老名兼容 |
| 全版本 | 静态参数 | 需重启，非 SET GLOBAL |

## 关键代码
```sql
SHOW VARIABLES LIKE 'log_slave_updates';
SHOW BINARY LOGS;            -- 开启后从库 binlog 才会随主库事件增长
```
```ini
# my.cnf（静态参数，需重启）
[mysqld]
log_bin = /data/mysqllog/mysql-bin
log_slave_updates = ON       -- 8.0.26+ 写 log_replica_updates = ON
```

## ⚠️ 原文纠错
原文未提及 **8.0.26 起参数更名为 `log_replica_updates`**，也未提示该参数为**静态、需重启**，卡面已补充并标注 `[经验]`。原文"级联复制 / GTID 复制需要记录从主同步过来的日志"结论正确。机翻「slaver」「flavor」「logslaverupdate」还原为 slave / replica / log_slave_updates。核对范围：第 405~408 段。

## 总结与追问预判
- 一句话判据：**从库要当"源"就必须开**。
- 代价：磁盘 + 写放大；静态参数需重启。
- 下一题：见 072（relay log）、05 单元 GTID 相关卡。
