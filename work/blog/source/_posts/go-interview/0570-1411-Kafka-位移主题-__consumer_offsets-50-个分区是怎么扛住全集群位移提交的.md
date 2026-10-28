---
disableNunjucks: true
title: "1411 Kafka 位移主题 __consumer_offsets：50 个分区是怎么扛住全集群位移提交的？"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：消息中间件 / Kafka | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**__consumer_offsets**/**位移主题**/**消费位移**/**哈希取模**/**offsets.topic.num.partitions**/**副本因子**/**日志压实**
> 原文锚点：第 7~16 段「所谓的位移主题其实就是 Kafka 0.9 版本开始用于存储消费者在每个分区上消费的消息偏移量信息中的一个 Kafka 内部的 topic…Kafka 默认为这个 topic 创建了五十个分区，并且会对这个 groupID 进行哈希取模运算…它的默认值通常是三」
> [边界] 本文只讲**位移主题这个内部 topic 自身的结构与机制**：位移提交的开关与重复消费问题见 1417，重平衡的分区分配流程见 147，存储与刷盘见 146，均不重述。

## 一句话总述
`__consumer_offsets` 是 Kafka **从 0.9 起**内置的**一个**内部 topic，专门持久化**消费组在各分区上的消费进度**。它把消息存成 **KV**——**key 是（消费组 ID、topic、分区号）三元组，value 是"下一条要消费的位移"**；默认 **50 个分区**，用 **`abs(groupID.hashCode()) % 分区数`** 打散写入压力，副本因子默认 **3**，并靠**日志压实**按 key 只保留最新位移。

## 面试官视角
- 考察意图：这是**"Kafka 怎么做元数据存储"的分水岭**。答得出 50 分区与哈希取模，说明你真看过内部机制，而不是只用过 API。
- 分档：P5 知道位移存在 Kafka 里；P6 能说出 `__consumer_offsets` 这个名字；P7 能讲出**KV 三元组结构**、**50 分区 + 哈希取模的动机**、**副本因子 3**、**日志压实的作用**，以及**记录的是"下一条"而不是"最后一条"**。
- 红旗答案：「每个消费组都有一个自己的位移主题」——**错**。全集群**只有一个** `__consumer_offsets`，消费组只是按哈希落到它的**某个分区**。
- 惊艳点：补一句「`__consumer_offsets` 不只存位移，**还存消费组的元数据**——成员列表、`generation ID`、组 `leader` 都由它承载；也正因如此它不能用普通清理策略，必须靠**日志压实**」[经验]。

## 主问答
**Q（面试官原话）：** 什么是位移主题？它有什么用，为什么默认要建 50 个分区？

**A：**
1. **它是什么**：从 **Kafka 0.9** 开始，消费位移不再存 ZooKeeper，改存到一个 **Kafka 内部 topic `__consumer_offsets`**；它和普通 topic 一样有分区、有副本、可自动扩展 [经验]。
2. **为什么要换**：旧客户端把位移存 ZooKeeper，后者在**性能与扩展性**上逐渐暴露问题；挪进 Kafka 的 topic 后可直接复用 topic 的**自动扩展与多副本备份**，既提升性能与可靠性，又**减少对 ZooKeeper 的依赖** [经验]。
3. **消息长什么样**：可以理解成 **KV 格式**——**key 是由「消费组 ID + topic + 分区号」组成的三元组**，**value 是该分区消费到的 offset**；因为一个消费组会消费多个分区，所以**位移提交是按分区粒度进行的** [经验]。
4. **一个容易说错的细节**：位移记录的是**消费者下一条要消费的消息的位移**，而**不是当前最新已消费消息**的位移——差一位，答错就是没真懂 [经验]。
5. **为什么是 50 个分区**：生产环境里往往有大量消费者与消费组，若它们**同时提交位移**，单一分区会变成写入热点。默认 **50 个分区** + 对 `groupID` **哈希取模**，把负载分散到不同分区 [经验]。
6. **取模怎么算**：取消费组 ID 的哈希值，再对分区数取余，即 `abs(hashCode) % 分区数`；实测 `order-service` 落到 **26** 号、`pay-cg` 落到 **19** 号、`user-log` 落到 **30** 号 [实测]。
7. **副本与可靠性**：副本数由 `offsets.topic.replication.factor` 决定，**默认 3**——即 **1 个 leader 副本 + 2 个 follower 副本**，不同版本会有差异 [经验]。
8. **什么场景会用到它**：① **故障恢复 / 重启**后消费者从记录的位移续消费，不重复处理已消费的消息；② **重平衡**时新接手分区的消费者能拿到该分区的进度，从正确位置续消费 [经验]。
9. **谁来创建**：由 Kafka **自动创建和管理**，用户**无需手动创建**；集群中**第一次有消费者消费**时触发 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 消费进度存在哪？ | 位置 | 内部 topic `__consumer_offsets` | P5 停 |
| L2 | 消息的 key 是什么？ | 结构 | 组ID + topic + 分区号 三元组 | P6 停 |
| L3 | 为什么默认 50 个分区？ | 动机 | 分散大量消费组的并发提交压力 | P6 停 |
| L4 | groupID 怎么映射到分区？ | 机制 | `abs(hashCode) % 分区数` | P7 停 |
| L5 | 记录的是"已消费"还是"待消费"？ | 细节 | **下一条**要消费的位移 | P7+ 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Kafka 0.8.x 及更早 | 位移存 **ZooKeeper** | 老集群才这么答 |
| Kafka 0.9 起 | 引入新消费者，改存内部 topic | **现行标准答案** |
| Kafka 2.x 起 | `__consumer_offsets` 兼存**消费组元数据** | 不只存位移 |
| 默认配置 | 分区数 **50**、副本因子 **3** | 记住这两个常数 [源码] |
| 单 broker 开发机 | 副本因子 3 **超过 broker 数** | 自动创建会失败，需手动调成 1 |
| 已创建之后 | 再改 `num.partitions` **不生效** | 只能重建或手工扩容 |

## 关键代码
```go
package main

import "fmt"

// 复刻 Java String.hashCode（Kafka 用 Java/Scala 实现）：
// s[0]*31^(n-1) + s[1]*31^(n-2) + ... ，按 32 位有符号整数溢出
func javaHash(s string) int32 {
	var h int32
	for _, c := range []byte(s) {
		h = h*31 + int32(c)
	}
	return h
}

// partitionFor 对应 Kafka GroupMetadataManager 的定位逻辑：
// abs(groupId.hashCode) % offsets.topic.num.partitions
func partitionFor(groupID string, numPartitions int32) int32 {
	p := javaHash(groupID) % numPartitions
	if p < 0 {
		p = -p // Utils.abs，注意 hashCode 可能为负
	}
	return p
}

func main() {
	const numPartitions = int32(50) // offsets.topic.num.partitions 默认 50
	for _, g := range []string{"order-service", "pay-cg", "user-log", "test", ""} {
		fmt.Printf("group=%-14q hashCode=%12d -> partition %d\n",
			g, javaHash(g), partitionFor(g, numPartitions))
	}
}
```

> 验证（`[实测]` 输出，go1.26.5 / macOS）：`group="order-service" hashCode=562889526 %50 = 26`；`group="pay-cg" hashCode=-995269719 %50 = 19`；`group="user-log" hashCode=-267639230 %50 = 30`；`group="test" hashCode=3556498 %50 = 48`；空串 `hashCode=0 %50 = 0`。可见负哈希必须取绝对值，否则会落到负分区号——这正是 `Utils.abs` 存在的意义。

## 总结与追问预判
- 一句话收尾：**"一个 topic、50 个分区、哈希分桶、KV 三元组、副本三份、压实保留最新"**——这 6 个短语背下来，这道题就稳了。
- 大概率被追的三问：① 位移主题会不会无限涨（不会，靠**日志压实**按 key 去重，只保留每个三元组的最新位移）；② 消费者怎么知道去哪读（启动时自动订阅该 topic，按自身 `groupID` 定位分区）；③ 0.9 之前怎么办（存 ZooKeeper，性能与扩展性差，已淘汰）。
- 反向加分：主动指出**"每个消费组一个位移主题"是常见误解**，正确说法是**全集群共用一个 `__consumer_offsets`，组按哈希落到固定分区**。

## ⚠️ 原文纠错
1. 源码称「每个消费组都有一个与之关联的位移主题」——错，全集群**只有一个** `__consumer_offsets`，组按哈希落分区 [经验]。
2. 源码称位移主题「作用只有一个」——它还存**消费组元数据**：成员、`generation`、组 leader [经验]。
3. 源码未提 `offsets.topic.num.partitions` 默认 50 可调，且**已存在后再改不生效** [经验]。
4. 源码未提副本因子默认 3 时，**broker 数不足 3 会导致自动创建失败** [经验]。
5. 源码未提该 topic 依赖**日志压实**按 key 去重，只保留最新位移，否则会无限膨胀 [经验]。
6. 源码只说「哈希取模」——准确公式是 **`abs(hashCode) % 分区数`**，负哈希必须取绝对值 [经验]。
