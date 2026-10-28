---
disableNunjucks: true
title: "148 Kafka 重平衡的五步流程：Coordinator、Leader 与 STW 代价"
date: 2026-10-10 00:11:41
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：消息队列 / Kafka | 难度：L3 | 题型：流程题 | 频率：高 | 关键词：**GroupCoordinator**/**JoinGroup**/**GroupLeader**/**SyncGroup**/**STW**
> 原文锚点：第 1~30 段「rebalance 本质是一种协议，规定了 consumergroup 下所有 consumer 如何达成一致来分配订阅 topic 的每个分区…Kafka 会为每个消费组指定一个 groupcoordinator…选举出一个消费者作为 groupleader…groupleader 负责为消费组内的其他消费者分配 topic 分区…rebalance 过程中所有消费者实例都会停止工作等待完成」

## 一句话总述
重平衡本质是**达成一致的协议**，五步走：**触发**（成员数/订阅 topic 数/分区数变化、首次启动）→ **JoinGroup**（全员向 GroupCoordinator 报到）→ **选举 GroupLeader**（Coordinator 挑一个消费者当组长）→ **Leader 制定分配方案**（哪个消费者管哪些分区）→ **SyncGroup**（Coordinator 把方案下发全员）；期间**整组 STW**——所有消费者停止消费等重平衡完成。

## 面试官视角
- 考察意图：区分「背过触发条件」与「真懂流程」——面试官要听清 **Coordinator 与 Leader 的分工**（协调者管流程、领导者定方案）与 STW 代价，这是本题的分水岭。
- 分档：P5 知道重平衡是重新分配分区；P6 能报全五步与两个角色；P7 能讲清 STW 代价、低峰期操作建议、以及 Go SDK 分区数变化的坑。
- 红旗答案：「重平衡就是重新连一下 broker」；以为分配方案是 Coordinator 算的（实际是 **GroupLeader** 算，Coordinator 只负责收发与流程控制）。
- 惊艳点：「**Coordinator 是 broker 侧角色、Leader 是消费者侧角色**——分工是『服务端管流程、客户端算方案』」+ 「Go 版 SDK 在分区数变化时可能不自动触发重平衡，需要手动重启消费者」 [经验]。

## 主问答
**Q（面试官原话）：** 消费组的重平衡过程是怎样的？
**A：**
1. **第一步：触发**。四类条件——① **组内成员数变化**（新消费者加入 / 旧消费者离开：进程退出、心跳超时、崩溃）；② **订阅 topic 数变化**；③ **topic 分区数变化**（分区支持动态扩）；④ **消费组首次启动**。生产实践通常一个组只订阅一个 topic（不同 topic 消息结构不同，各配回调），成员与分区变化是日常主因 [源码]。
2. **第二步：JoinGroup 报到**。每个消费组对应一个 **GroupCoordinator**——它是**特殊的 broker**，负责管理该组的重平衡流程。消费者加入时向它发 **JoinGroup 请求**，携带消费者 ID、支持的协议类型、订阅的 topic [源码]。
3. **第三步：选举 GroupLeader**。Coordinator 收齐全员 JoinGroup 后，选出**一个消费者**作为 GroupLeader（通常是第一个加入的）——注意这是**消费者侧的角色**，不是 broker [源码]。
4. **第四步：Leader 制定分配方案**。**GroupLeader 根据各成员的订阅信息，决定哪个消费者负责哪些 topic 的哪些分区**（分配策略如 Range/RoundRobin/Sticky，方案质量见深卡 [边界]），然后把结果交回 Coordinator [源码]。
5. **第五步：SyncGroup 下发生效**。Coordinator 把分配结果同步给组内所有消费者，各自开始消费自己的分区。**代价：整个过程整组 STW——所有消费者停止消费，直到重平衡完成**，延迟敏感业务要把改分区数、重启消费服务放在**业务低峰期** [源码]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 什么是重平衡？ | 概念 | 组内成员一致分配分区的过程 | P5 停 |
| L2 | 哪些情况触发？ | 条件 | 成员数/订阅数/分区数变化、首次启动 | P5 停 |
| L3 | Coordinator 和 Leader 各干什么？ | 角色分工 | broker 管流程收发请求；消费者 Leader 算分配方案 | P6 停 |
| L4 | 重平衡期间还能消费吗？ | 代价 | 不能，整组 STW 直到完成 | P6 停 |
| L5 | 频繁重平衡怎么治理？ | 工程化 | 稳定心跳参数、静态成员、Sticky 策略、低峰操作 | P7 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 经典消费者组协议 | JoinGroup/SyncGroup 两阶段，整组 STW | 按本卡五步答 |
| Kafka 2.4+ | **静态成员**（`group.instance.id`）：成员重启不触发重平衡 | 滚动发布的治本手段 |
| Kafka 2.4+ | **增量协作重平衡**（incremental cooperative）：只迁移受影响分区，不全组停 | 新协议逐步取代 Eager 全量重平衡 |
| 分区扩容 | Go 版 SDK 可能不自动触发重平衡 | 改分区数后手动重启消费者确认生效 |
| 位移存储 | 0.9 起存 `__consumer_offsets`（ZK 之前） | 演进原因见 147 [边界] |

## 关键代码
```go
// 消费端处理重平衡通知的工程模式 (sarama ConsumerGroup 接口形态 [源码])
func (h *handler) Setup(s sarama.ConsumerGroupSession) error {
	// 重平衡完成、分区已分配: 在这里做初始化(如按分区建本地状态)
	log.Printf("assigned partitions: %v (generation %d)",
		s.Claims(), s.Generation())
	return nil
}
func (h *handler) Cleanup(s sarama.ConsumerGroupSession) error {
	// 重平衡开始前/分区被回收: 清理本地状态, 避免串分区
	log.Println("revoked, cleaning up")
	return nil
}
// 要点: Setup/Cleanup 是消费端感知重平衡的两个钩子;
// 分区被回收前必须完成位移提交, 否则重复消费
```

## 总结与追问预判
一句话记忆：**「五步走：触发 → JoinGroup → 选 Leader → Leader 分区 → SyncGroup；期间整组 STW；Coordinator 管流程、Leader 管方案」**。重平衡的定义、触发条件与 goroutine 数匹配原则见 147 [边界]。常追问「重平衡为什么慢」——答 STW + 全员重新入组 + 方案下发，组越大越慢（万人组的经典痛点）；再追问「怎么治理」——按版本表答静态成员 + 增量协作重平衡 + 心跳参数调优（session.timeout.ms / max.poll.interval.ms）。

## ⚠️ 原文纠错
1. 术语归一：[经验] 源为语音转写，「帕奇卡夫卡」应为 Apache Kafka，「aptopic」应为 topic，「pertition」应为 partition，「ggroupaudidioror」应为 GroupCoordinator，统一为规范术语。
2. 表述纠错：源称「选举出一个消费者作为 groupleader」未点明其**消费者侧**属性，与 broker 侧 Coordinator 易混，本卡已强化对比。
3. 补充：源未提分配策略（Range/RoundRobin/Sticky）与静态成员、增量协作重平衡等治理手段，本卡深挖卡已补 [经验]。
