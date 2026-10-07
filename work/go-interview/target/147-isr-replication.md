# 147 ISR 复制机制：在同步与异步之间做权衡

> 分类：消息队列 / Kafka | 难度：L4 | 题型：原理题 | 频率：高 | 关键词：**ISR、同步复制、异步复制、已提交、leader、follower、控制器、副本选举**

> 原文锚点：第 29~49 段「Kafka 为分区引入多副本机制，通过增加副本的数量可以提升容灾能力…leader 副本负责处理读写请求，追随者副本只负责与 leader 副本进行消息同步…Kafka 的复制机制既不是完全的同步复制，也不是单纯的异步复制…Kafka 使用了 ISR 列表来维护所有与主副本同步的追随者副本，注意这里的 ISR 列表只包含了一部分追随者副本…当一条消息被 ISR 列表里面的所有副本写入之后，这条消息才会被认为已提交，只有已提交的消息才可以被消费者消费」

## 一句话总述
Kafka 既不用**全同步复制**（太慢）也不用**纯异步复制**（会丢数据），而是用 **ISR 列表**折中：消息被 **ISR 内所有副本写入**才算**已提交**，且**只有已提交的消息才可被消费**；leader 故障由**控制器**从 ISR 中选新 leader。

## 面试官视角
P6 知道有副本；P7 必须讲清**三种复制方式的取舍**（同步慢、异步丢、ISR 折中）、**「已提交才可被消费」这条语义**，以及**ISR 只含一部分 follower** 这个常被忽略的细节——它决定了「哪些副本有资格参与提交判定和新 leader 竞选」。

## 主问答
**Q（面试官原话）：** Kafka 的副本是怎么同步的？什么算写入成功？

1. **多副本目的**：为分区引入**多副本机制**，通过**增加副本数量提升容灾能力** `[源码]`。
2. **副本角色**：同一分区的不同副本保存**相同的消息**，但**同一时刻副本之间数据并非完全一样**；副本之间是**主从关系** `[源码]`。
3. **leader 与 follower**：**leader 副本负责处理读写请求**；**追随者副本只负责与 leader 同步消息**；**生产者和消费者只与 leader 副本交互** `[源码]`。
4. **故障转移**：副本分布在不同 broker 中，**leader 故障时重新选举新 leader**；通过多副本实现**故障自动转移**，某个 broker 失效时仍保证可用性 `[源码]`。
5. **同步复制的代价**：要求**所有能工作的 follower 都复制完**才确认提交，**极大影响性能** `[源码]`。
6. **异步复制的风险**：leader 写入即认为提交；若 follower 尚未复制而 leader 宕机，**会导致数据丢失** `[源码]`。
7. **ISR 折中**：Kafka 用 **ISR 列表**维护**所有与主副本同步的 follower**；**注意 ISR 只含一部分 follower 副本** `[源码]`。
8. **提交判定**：当消息被 **ISR 列表中所有副本写入**后，才被认为**已提交**；**只有已提交的消息才可被消费者消费** `[源码]`。
9. **选举机制**：leader 故障离线触发**副本重新选举**；**控制器负责管理选举过程**，它**从 ISR 列表中选择一个 follower 作为新 leader**，并通知其他 follower 同步新 leader 数据 `[源码]`。
10. **核心结论**：ISR 有效权衡了**数据可靠性与性能**之间的关系 `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 副本有哪两种角色？ | 答不出 leader / follower |
| L2 | 同步复制的代价？ | 答不出极大影响性能 |
| L3 | 异步复制的风险？ | 答不出 leader 宕机丢数据 |
| L4 | 什么时候算已提交？ | 答不出 ISR 全部写入 |
| L5 | ISR 包含哪些副本？ | 答不出「只含一部分 follower」 |
| L6 | 新 leader 怎么选？ | 答不出控制器从 ISR 中选 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Kafka 全版本 | ISR 机制通用 | 语义稳定 |
| 早期版本 | 位移存 ZooKeeper | 0.9 起改存内部 topic |
| 所有版本 | acks=all | 等价于等 ISR 全部写入 |
| 配置项 | unclean.leader.election | 开启则会选非 ISR 副本，可能丢数据 |

## 关键代码
```go
package main

import "github.com/IBM/sarama"

func main() {
	cfg := sarama.NewConfig()

	// acks=all（WaitForAll）：等 ISR 中所有副本写入后才认为提交并返回
	// 这是"只有已提交消息才可被消费"在生产者侧的对应配置
	cfg.Producer.RequiredAcks = sarama.WaitForAll

	// 最低 ISR 副本数：低于该值 broker 将拒绝写入（配合 acks=all 使用）
	// broker 端配置项：min.insync.replicas
	cfg.Producer.Return.Successes = true

	producer, _ := sarama.NewSyncProducer([]string{"127.0.0.1:9092"}, cfg)
	defer producer.Close()

	_, _, _ = producer.SendMessage(&sarama.ProducerMessage{
		Topic: "orders",
		Key:   sarama.StringEncoder("order-10086"),
		Value: sarama.StringEncoder("paid"),
	})
}
```

## 总结与追问预判
**「已提交 = ISR 全部写入，且只有已提交才可被消费」是本卡题眼**。面试官常追问「ISR 之外的 follower 落后太多怎么办」——会被**踢出 ISR**，直到追上后再重新加入；这是 ISR 动态调整的含义。消费端流程见同批 147-consumer-rebalance。

## ⚠️ 原文纠错
1. 事实核校：多副本提容灾、leader 处理读写、follower 只同步、生产者消费者只连 leader、同步复制性能差、异步复制会丢数据、ISR 只含部分 follower、ISR 全部写入才提交、已提交才可被消费、控制器从 ISR 选新 leader——均与 Kafka 设计一致 `[经验]`。
2. 补充：原文提到 leader 故障会重新选举，但未说明**「若开启 unclean leader election，可能从非 ISR 副本中选 leader，从而丢数据」**；生产环境通常关闭该开关以优先保证一致性 `[经验]`。
3. 崩坏词归一：源码将 Kafka、broker、副本、控制器、消费者等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
