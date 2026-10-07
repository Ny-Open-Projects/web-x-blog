# 1264 深挖：Tendis 集群架构、主从复制与「内存 vs 磁盘」的取舍

> 分类：数据库 / Redis 生态 | 难度：L5 | 题型：综合题 | 频率：低 | 关键词：**去中心化、gossip、CRC16、16384 槽、MOVE 协议、binlog、全量同步、增量同步、master_sequence**

> 原文锚点：第 26~32、47~54 段「Tendis 集群是基于 gossip 协议采用去中心化的集群架构，每个集群节点都拥有全部的路由信息。用户可以访问集群中的任意节点，并且可以通过 Redis 的 MOVE 协议最终路由到正确的节点…对 key 进行 CRC16 计算，得到一个数值，然后对 16384 进行取模，从而对数据进行划分…Tendis 的 binlog 也是保存在 RocksDB 当中的，它类似于 MySQL 的 row 模式的 binlog…Tendis 的主从同步也分为两步，全量同步和增量同步…master 会记录快照中最大的 binlog 序列号，也就是 master_sequence，他会把序列号从 master_sequence+1 开始的 binlog 逐条发送给 slave，从而实现增量同步」

## 思路与架构

按「**集群架构 → 数据分布 → 主从复制**」三层把握 Tendis：

1. **集群架构（去中心化）**：
   - Tendis 集群**基于 gossip 协议，采用去中心化的集群架构**；**每个集群节点都拥有全部的路由信息** `[源码]`。
   - **用户可访问集群中的任意节点**，并通过 **Redis 的 MOVE 协议**最终**路由到正确的节点** `[源码]`。
   - **主备节点之间可以通过 binlog 进行复制**；**任意两个节点之间可以通过 gossip 协议通信**；**master 节点之间支持基于 slot 的数据搬迁** `[源码]`。
   - 存储引擎基于 **RocksDB**，而 RocksDB 基于 **LSM 树**（见 `1264-lsm-tree-basics`）。
2. **数据分布（槽位计算）**：
   - **与 Redis 的哈希槽计算方法一样**：**先对 key 做 CRC16 计算得到一个数值，再对 16384 取模**，从而对数据进行划分 `[源码]`。
   - **每个节点维护属于各自的 slot 数据**，**任意两个 master 之间的 slot 数据不重复** `[源码]`。
   - 支持 **hash tag** 控制数据分布与访问，使相关 key 落到同一槽位 `[源码]`。
3. **主从复制（全量 + 增量两阶段）**：
   - **binlog 的存放与有序性**：Tendis 的 **binlog 也保存在 RocksDB 当中**，**类似 MySQL 的 row 模式 binlog**；**数据的修改操作会保证在同一个事务当中**；通过**全局递增的 ID（BINLOG ID）确保 binlog 在 RocksDB 中的有序性**；**一条 binlog 修改的数据只能对应 RocksDB 中的一对 KV** `[源码]`。
   - **全量同步**：master 收到新 slave 的同步请求时，**会给 RocksDB 做一个快照**；**快照中的数据分两部分——全量的数据集 + 写数据时生成的 binlog**；master **把快照中的数据集发送给 slave**，实现全量同步 `[源码]`。
   - **增量同步**：master **记录快照中最大的 binlog 序列号，即 master_sequence**；然后**把序列号从 master_sequence+1 开始的 binlog 逐条发送给 slave**，实现增量同步 `[源码]`。

## 方案取舍

| 关注点 | Redis（内存） | Tendis（RocksDB/磁盘） | 取舍 |
|---|---|---|---|
| 存储介质 | 内存 | 磁盘（RocksDB） | 容量换延迟 |
| 容量上限 | 受内存与节点数限制 | PB 级 | 冷数据场景优势明显 |
| 写入模型 | 原地改内存 | LSM 追加写 + compaction | 写吞吐高，但 key 频繁变化会拖垮 |
| 集群管理 | Redis Cluster（gossip） | 同款去中心化 + MOVE 路由 | 运维模型一致，迁移成本低 |
| 槽位计算 | CRC16 % 16384 | 完全一致 | 协议与分布模型对齐 |
| 复制 | RDB 全量 + 积压缓冲区增量 | 快照全量 + binlog 增量 | Tendis 的 binlog 持久化在 RocksDB |
| 命令覆盖 | 完整 | PubSub/GEO 不支持，O(N) 命令变慢 | 能力边界是迁移硬门槛 |

取舍要点：**Tendis 用"延迟上升 + 命令能力受限"换"容量成本大幅下降"**。因此正确的落地形态不是替换，而是**分级存储**：热数据留 Redis、冷数据放 Tendis。它刻意**沿用 Redis Cluster 的槽位计算、MOVE 路由与 gossip 模型**，就是为了把**接入与运维的迁移成本压到最低**。

## 答题技巧

1. **先讲"为什么"再讲"是什么"**：先把内存成本这条动因说清（Redis 数据全在内存 → 大数据量硬件成本高 → 固态存储发展 → 出现磁盘版方案），Tendis 的定位自然成立。
2. **集群部分抓三个相同点**：**gossip 去中心化**、**CRC16 % 16384 分槽**、**MOVE 协议路由**——这三点与 Redis Cluster 一致，是"能平滑迁移"的论据。
3. **复制部分抓两个不同点**：**binlog 存在 RocksDB 里**（不是内存积压缓冲区）、**用全局递增 BINLOG ID 保序 + master_sequence 定位增量起点**——这是 Tendis 相对 Redis 复制设计的差异。
4. **务必带"冷热分级"这个结论**：Tendis **不能完全替代 Redis**，正确姿势是**与 Redis 配合实现冷热数据分离**。
5. **止步档位**：能讲清集群架构与两阶段同步即达 L4；能补上槽位计算细节、"binlog 存 RocksDB + BINLOG ID 保序"的设计动因，以及内存/磁盘的取舍表，即达 L5。

## ⚠️ 原文纠错
1. 事实核校：gossip 去中心化且每节点持有全量路由、MOVE 协议路由、CRC16 % 16384 分槽、master 间 slot 不重复、binlog 存 RocksDB 且类似 MySQL row 模式、全局递增 BINLOG ID 保序、一条 binlog 对应一对 KV、全量同步用快照（全量数据集 + binlog）、增量同步从 master_sequence+1 逐条发送——均与 Tendis 设计一致 `[经验]`。
2. 补充：原文称"一条 binlog 修改的数据只能对应 RocksDB 中的一对 KV"，应理解为**一条 binlog 变更对应确定的一对 KV 写入**，用以确保复制的幂等与可回放；另本节末尾口述称"介绍了 Redis 的主从架构、全量与增量同步流程"，**与本节主体（Tendis）不符，属口误** `[经验]`。
3. 崩坏词归一：源码将 Tendis、RocksDB、gossip、binlog、CRC16、slot、RDB 等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
