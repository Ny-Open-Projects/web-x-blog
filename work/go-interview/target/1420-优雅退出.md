# 1420 优雅退出：异步生产者不 flush 会丢消息

> 分类：消息队列 / Kafka | 难度：L4 | 题型：排错题 | 频率：高 | 关键词：**异步生产者、channel、优雅退出、消息丢失、consumer.Close**

> 原文锚点：第 63~76 段「如果操作系统向我们程序发出一个退出信号，我们会调用 consumer 的 close 方法，这个 consumer 把我们读取到 channel 的这些消息先处理完成…如果是一个异步的生产者，我们需要注意的是，因为异步生产者是在我们的 SDK 的 channel 里面进行提交的，所以这里一定要对我们的消费者程序进行等待…程序退出时我们需要把生产者发送到 channel 里的这些消息提交到 Kafka 集群之后才能退出，否则的话就可能会导致消息的丢失」

## 一句话总述
异步生产者的消息先在 SDK 的 channel 中排队、由后台线程批量提交，**程序退出前必须等待消息真正提交到 Kafka**；消费者侧则要在收到退出信号后调用 `Close()`，先把已读取的消息处理完再退出。

## 面试官视角
P6 知道要 `defer Close()`；P7 必须讲清**异步发送的两段式**——业务调用只是把消息放进内存 channel，真正落盘在后台；直接退出会丢掉 channel 里尚未提交的消息，这是「异步 = 可能丢」的核心风险点。

## 主问答
**Q（面试官原话）：** 程序重启后丢了一批消息，你们用的是异步发送，问题出在哪？

1. **异步发送的两段式**：调用发送只是把消息**提交到 SDK 的 channel**，真正发往 Kafka 由后台完成 `[源码]`。
2. **因此必须等待**：使用异步生产者时，**一定要对程序进行等待**，不能发送完立刻退出 `[源码]`。
3. **丢消息的根因**：若退出时 channel 中仍有未提交的消息，这些消息**不会到达 Kafka 集群，直接丢失** `[源码]`。
4. **正确做法**：程序退出前让 channel 中积压的消息**全部提交到 Kafka 之后再退出** `[源码]`。
5. **同步生产者无此问题**：同步发送会阻塞等待结果，返回即已提交（受 Acks 配置影响） `[经验]`。
6. **消费者侧收尾**：监听**操作系统退出信号**，收到后调用消费者的 `Close()` 方法 `[源码]`。
7. **Close 的语义**：`Close()` 会**先把已读取到 channel 的消息处理完成**再真正关闭，避免处理一半中断 `[源码]`。
8. **错误通道**：消费过程中的错误通过独立的**错误 channel** 读取，应与消息通道一并监听 `[源码]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 异步发送的消息先去哪？ | 答不出「先进 SDK channel」 |
| L2 | 直接退出会怎样？ | 答不出丢消息 |
| L3 | 怎么避免丢？ | 答不出等待提交完成 |
| L4 | 消费者收到退出信号做什么？ | 答不出调用 Close |
| L5 | Close 的语义？ | 答不出「先处理完已读消息」 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Kafka 全版本 | 异步为内存队列 + 后台提交 | 退出前必须 flush |
| 全版本 | 同步发送 | 阻塞等待，无积压风险 |
| 全版本 | 优雅退出 | 监听信号 + Close |
| 全版本 | 错误通道 | 消息与错误两个 channel 都监听 |

## 关键代码
```go
package main

import (
	"os"
	"os/signal"
	"syscall"

	"github.com/IBM/sarama"
)

func main() {
	cfg := sarama.NewConfig()
	cfg.Producer.Return.Successes = true
	producer, _ := sarama.NewAsyncProducer([]string{"127.0.0.1:9092"}, cfg)

	// 必须并发监听成功/失败两个 channel，否则缓冲区满会阻塞发送
	go func() {
		for range producer.Successes() {
		}
	}()
	go func() {
		for err := range producer.Errors() {
			_ = err // 生产环境应记录日志并考虑补偿
		}
	}()

	producer.Input() <- &sarama.ProducerMessage{Topic: "demo", Value: sarama.StringEncoder("hello")}

	// 优雅退出：等待信号后调用 Close，Close 会 flush 掉 channel 中积压的消息
	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGINT, syscall.SIGTERM)
	<-sig

	// 关键：AsyncClose 不等待，Close 会等待积压消息提交完成
	if err := producer.Close(); err != nil {
		panic(err)
	}
}
```

## 总结与追问预判
**异步发送 = 内存队列 + 后台提交，退出不等待就是丢消息**。追问常是「Successes 和 Errors 不消费会怎样」——缓冲区打满后发送会阻塞，这是异步生产者第二个经典坑。SDK 选型见同批 1420-kafka-go-sdk。

## ⚠️ 原文纠错
1. 事实核校：异步发送先进 channel 由后台提交、退出前必须等待、否则丢消息、消费者监听退出信号并调用 Close、Close 先处理完已读消息、错误通过独立 channel 读取——均与 sarama 行为一致 `[经验]`。
2. 补充：原文强调「对程序进行等待」是正确的；实现上应选 `Close()` 而非 `AsyncClose()`，后者不等待积压消息提交完成，仍存在丢失风险 `[经验]`。
3. 崩坏词归一：源码将 Kafka、异步生产者、channel、退出信号等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
