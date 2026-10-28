---
disableNunjucks: true
title: "1264 Tendis 是什么：硬盘版 Redis 的定位、特性与适用边界"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：数据库 / Redis 生态 | 难度：L3 | 题型：选型题 | 频率：中 | 关键词：**Tendis、RocksDB、Redis 协议兼容、PB 级、去中心化、gossip、冷热分离**

> 原文锚点：第 1~25 段「由于 Redis 的缓存数据全部保存在内存当中，如果需要缓存大量的数据会带来很高的硬件成本…腾讯出品的 Tendis，不能说可以完全替代 Redis，但是可以配合 Redis 实现分级存储…它完全兼容 Redis 协议，支持绝大多数的 Redis 指令…最大支持 PB 级别的存储…所有节点都是通过 gossip 协议通信的…支持扩容到一千个节点…可以自动检测故障节点，从节点会自动替代 master 节点」

## 一句话总述
**Tendis** 是腾讯开源的**硬盘版 Redis**：数据用 **RocksDB** 引擎存在磁盘上（而非内存），**完全兼容 Redis 协议**、支持绝大多数指令，最大 **PB 级**存储；采用**去中心化集群架构**（gossip 通信、hash tag 控制分布、可按 slot 迁移、支持扩到 **1000 个节点**），并具备**自动故障检测与主从切换**。它的定位不是**替代** Redis，而是**配合 Redis 做冷热分级存储**。

## 面试官视角
- 考察意图：是否知道"内存成本受限时 Redis 的替代/补充方案"，以及能否说清它的**能力边界**。
- 分档：P5 只知道 Redis 是内存的；P6 知道 Tendis/类 Pika 方案存在；P7 能讲清**存储引擎换成 RocksDB 带来的连锁影响**（容量上去了、延迟下来了、部分命令不适用了）。
- 红旗答案：把 Tendis 说成"完全替代 Redis"——原文明确说**不能说可以完全替代**，而是**配合 Redis 实现分级存储**。
- 惊艳点：**换引擎不只是换了个"硬盘"**，它把 Redis 的复杂度特征也改写了——`LINSERT`/`LREM`/`LTRIM` 这类 **O(N) 命令在磁盘上性能会明显变差** `[源码]`。

## 主问答
**Q（面试官原话）：** 数据量太大、Redis 内存成本扛不住，有什么方案？

1. **结论**：可以用 **Tendis** 配合 Redis 做**分级存储**——热数据放 Redis、冷数据放 Tendis，兼顾用户体验与业务成本；它**不是完全替代 Redis** `[源码]`。
2. **背景与动因**：Redis 性能虽高，但**缓存数据全部保存在内存**，缓存大量数据会带来**很高的硬件成本**；随着**固态存储**发展，出现了把数据放到磁盘的 Redis 替代品 `[源码]`。
3. **架构与协议**：Tendis **类似 Redis Cluster**，采用**去中心化的集群管理架构**；**完全兼容 Redis 协议，支持绝大多数 Redis 指令** `[源码]`。
4. **存储与容量**：数据使用 **RocksDB 引擎存储在硬盘**上，**支持持久化存储**，**最大支持 PB 级别** `[源码]`。
5. **扩展与运维**：所有节点通过 **gossip 协议**通信，可指定 **hash tag** 控制数据分布与访问，**使用和运维成本极低**；支持**水平扩展、增删节点**，数据可按 **slot** 在任意两个节点间迁移，**扩缩容对应用与运维人员透明**，**支持扩容到 1000 个节点** `[源码]`。
6. **高可用**：可**自动检测故障节点**，故障发生时**从节点自动替代 master 继续对外提供服务** `[源码]`。
7. **适用 / 不适用场景**：
   - **适用**：业务架构受 **Redis Cluster 内存与节点数限制**、需大幅降低资源成本；**读多写少**；与 Redis 配合做**冷热分离**（活跃数据放 Redis、非活跃数据放 Tendis）`[源码]`。
   - **不适用**：**key 经常变化**（会频繁触发压缩，影响性能）；部分 **O(N) 命令**在 list 很大时性能较差（**`LINSERT` / `LREM` / `LTRIM`**）；**不支持 PubSub 与 GEO** 相关命令；部分事务命令（**`MULTI` / `EXEC` / `WATCH` / `DISCARD`**）不支持——**但 Tendis 本身支持事务**；实际性能**落后 Redis** `[源码]`。

**加分层：** 选型结论要落到"**分级而不是替换**"——把缓存数据分级，热点数据存 Redis、其他数据存 Tendis，才能**在硬件成本与延迟之间取平衡**。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 为什么需要 Tendis？ | 答不出内存成本高 |
| L2 | 数据存在哪？ | 答不出 RocksDB + 硬盘 |
| L3 | 容量上限？ | 答不出 PB 级 |
| L4 | 集群怎么管？ | 答不出 gossip 去中心化 |
| L5 | 什么场景不能用？ | 答不出 key 频繁变化 / O(N) 命令 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Tendis（开源） | 兼容 Redis 协议 | 绝大多数指令可直接迁移 |
| 不支持 | PubSub / GEO | 这两类业务不能迁 |
| 部分不支持 | MULTI/EXEC/WATCH/DISCARD | Tendis 本身仍支持事务 |
| 性能 | 落后 Redis | 只放冷数据，热数据留 Redis |

## 关键代码
```go
// 冷热分级：热数据走 Redis，冷数据走 Tendis（协议兼容，换地址即可）
package main

import (
	"context"
	"time"

	"github.com/redis/go-redis/v9"
)

func main() {
	ctx := context.Background()

	hot := redis.NewClient(&redis.Options{Addr: "redis-hot:6379"})   // Redis：热点
	cold := redis.NewClient(&redis.Options{Addr: "tendis-cold:6379"}) // Tendis：冷数据

	// 热 key：低延迟要求，放 Redis
	hot.Set(ctx, "user:1001:profile", "hot", 10*time.Minute)

	// 冷 key：量大、延迟不敏感，放 Tendis（PB 级容量、磁盘存储）
	cold.Set(ctx, "order:2024:archive:1001", "cold", 0)

	// 读取策略：先热后冷，冷命中后可视情况回升温到 Redis
	if v, err := hot.Get(ctx, "user:1001:profile").Result(); err == nil {
		_ = v
	} else if v, err := cold.Get(ctx, "user:1001:profile").Result(); err == nil {
		_ = v
	}
}
```

## 总结与追问预判
**最爱追问的是"为什么不直接加内存/加 Redis 节点"**——答案是**成本曲线**：数据量到 TB/PB 级时内存与节点数的成本远超磁盘，而冷数据的访问频率并不值得这个成本。追问常接"迁过去要注意什么"——**O(N) 命令会变慢**、**PubSub/GEO 不支持**、**key 频繁变化会频繁触发压缩**，这三条是迁移评估的硬门槛（压缩的机理见 1264）。

## ⚠️ 原文纠错
1. 事实核校：Tendis 为腾讯开源、兼容 Redis 协议、RocksDB 存磁盘、PB 级容量、gossip 去中心化、hash tag 控分布、按 slot 迁移、支持 1000 节点、自动故障切换、冷热分级定位、四类不适用场景——均与 Tendis 公开特性一致 `[经验]`。
2. 补充：原文称 Tendis "不支持 MULTI/EXEC/WATCH/DISCARD，但它本身支持事务"，两者并不矛盾——**不支持的是这几个 Redis 事务命令，而非不支持事务能力**；另外本节结尾处口述称"介绍了 Redis 的主从架构"，**本节实际讲的是 Tendis**，属口误 `[经验]`。
3. 崩坏词归一：源码将 Tendis、RocksDB、Redis Cluster、gossip、hash tag、slot 等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
