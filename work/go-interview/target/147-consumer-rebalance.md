# 147 消费流程与重平衡：goroutine 数要等于分区数

> 分类：消息队列 / Kafka | 难度：L4 | 题型：流程题 | 频率：高 | 关键词：**消费组、重平衡、订阅、批次拉取、随机读、位移提交、__consumer_offsets**

> 原文锚点：第 50~74 段「consumer 订阅一个或多个 topic…Kafka 会将各个分区均匀的分配给 consumer 组中的各个 consumer 实例，这个分配的过程称为消费组的重平衡…消费者组中的某个 consumer 实例加入或者是退出，或者是订阅的 topic 的分区数量发生变化的情况下，都会再次触发消费者的重平衡…通常启用的 goroutine 个数需要等于消费的 topic 的分区的数量…从 0.9 版本开始，消费者偏移量默认就存储在一个名为 __consumer_offsets 的内部 topic 当中」

## 一句话总述
消费链路是**订阅 topic → 重平衡分配分区 → 按批次拉取 → 处理 → 提交位移**并循环；工程上**消费组内实例（goroutine）数应等于分区数**——多了空转、少了拖慢。位移从 **0.8 前存 ZooKeeper** 演进为 **0.9 起默认存 `__consumer_offsets` 内部 topic**。

## 面试官视角
P6 会说「消费者组消费 topic」；P7 要讲清**重平衡的三种触发条件**、**实例数与分区数的匹配原则**、**拉取时「先随机读定位、后顺序批读」的性能特征**，以及**位移存储演进的原因**（ZooKeeper 在性能与可扩展性上暴露问题）。

## 主问答
**Q（面试官原话）：** 消费者是怎么消费的？开几个 goroutine 合适？

1. **订阅 topic**：consumer 通过 Kafka API **订阅一个或多个 topic** 来接收消息 `[源码]`。
2. **重平衡**：订阅后 Kafka 将各分区**均匀分配给消费组中的各个 consumer 实例**，该过程即**消费组的重平衡** `[源码]`。
3. **触发条件**：除**首次消费**外，**组内实例加入或退出**、或**订阅 topic 的分区数发生变化**时，都会**再次触发重平衡** `[源码]`。
4. **实例粒度**：对应用而言，**一个处理 goroutine 就是一个 consumer 实例** `[源码]`。
5. **数量匹配**：通常启用的 **goroutine 个数需等于 topic 的分区数** `[源码]`。
6. **多于分区数**：会出现**部分 goroutine 分配不到分区而空转** `[源码]`。
7. **少于分区数**：一个 goroutine 需处理多个分区，可能**影响消费速率** `[源码]`。
8. **拉取方式**：先**根据文件名定位索引文件**，通常用**二分法**遍历索引，再到消息文件中定位并**顺序遍历**找目标消息；**首次定位属随机读、效率较低**，定位后即可**批量顺序读取**；数据按**批次**拉取 `[源码]`。
9. **处理与提交**：按业务处理消息（如入库），处理完将**消费偏移量提交给 Kafka**；偏移量用于记录已消费位置，便于**重启或故障恢复后继续消费** `[源码]`。
10. **位移存储演进**：**0.8 之前存 ZooKeeper**（分布式协调服务，偏移量作为节点数据写入），因其**性能与可扩展性**逐渐暴露问题；**0.9 起默认存 `__consumer_offsets` 内部 topic**，该 topic 本身即分布式持久化结构，可自动扩展与备份，从而**提高性能与可靠性、减少对 ZooKeeper 的依赖** `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 消费分几步？ | 答不出订阅/重平衡/拉取/处理/提交 |
| L2 | 重平衡何时触发？ | 答不出实例进出与分区数变化 |
| L3 | goroutine 数怎么定？ | 答不出等于分区数 |
| L4 | 拉取的性能特征？ | 答不出首次随机读、之后顺序批读 |
| L5 | 位移存在哪？ | 答不出 0.9 起存 __consumer_offsets |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| 0.9 起 | 位移存内部 topic | 默认 __consumer_offsets |
| 0.8 之前 | 位移存 ZooKeeper | 已淘汰，仅作演进说明 |
| 所有版本 | 重平衡 | 期间消费会短暂停止 |
| 所有版本 | 消费组 | 一个分区只被组内一个实例消费 |

## 关键代码
```go
package main

import (
	"context"
	"log"

	"github.com/IBM/sarama"
)

type handler struct{}

func (h *handler) Setup(sarama.ConsumerGroupSession) error   { return nil }
func (h *handler) Cleanup(sarama.ConsumerGroupSession) error { return nil }
func (h *handler) ConsumeClaim(sess sarama.ConsumerGroupSession, claim sarama.ConsumerGroupClaim) error {
	// 拉取是按批次进行的：首次定位为随机读，之后顺序批读
	for msg := range claim.Messages() {
		log.Printf("partition=%d offset=%d key=%s", msg.Partition, msg.Offset, string(msg.Key))
		// 处理完成后标记位移（自动提交由配置控制）
		sess.MarkMessage(msg, "")
	}
	return nil
}

func main() {
	cfg := sarama.NewConfig()
	cfg.Consumer.Offsets.Initial = sarama.OffsetNewest
	cfg.Consumer.Return.Errors = true

	// 消费组：组内实例数应与分区数匹配，多则空转、少则变慢
	group, _ := sarama.NewConsumerGroup([]string{"127.0.0.1:9092"}, "order-group", cfg)
	defer group.Close()

	for {
		if err := group.Consume(context.Background(), []string{"orders"}, &handler{}); err != nil {
			log.Println(err)
		}
	}
}
```

## 总结与追问预判
**「实例数 = 分区数」是消费端最实用的工程结论**。追问常是「为什么要从 ZooKeeper 换成内部 topic」——答案是 ZooKeeper 在**性能与可扩展性**上逐渐暴露问题，而 topic 本身就是分布式持久化结构，天然可扩可备份。写入侧可靠性见同批 147-isr-replication。

## ⚠️ 原文纠错
1. 事实核校：订阅、重平衡分配、三种触发条件、实例数匹配原则、二分索引 + 顺序批读、首次随机读、按批次拉取、处理与位移提交、0.8 前存 ZooKeeper、0.9 起存 __consumer_offsets——均与 Kafka 设计一致 `[经验]`。
2. 补充：原文未强调**重平衡期间整个消费组会短暂停止消费**；频繁重平衡（如实例反复上下线）会显著影响吞吐，生产上需调好会话超时与心跳参数 `[经验]`。
3. 崩坏词归一：源码将 Kafka、topic、分区、goroutine、偏移量、ZooKeeper 等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
