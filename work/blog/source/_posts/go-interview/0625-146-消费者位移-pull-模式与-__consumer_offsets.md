---
disableNunjucks: true
title: "146 消费者位移：pull 模式与 __consumer_offsets"
date: 2026-10-07 11:00:27
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：消息中间件 / Kafka | 难度：L3 | 题型：原理题 | 频率：高 | 关键词：**offset、pull 模式、__consumer_offsets、ZooKeeper、容错、端到端压缩**

> 原文锚点：第 57~68 段「每条消息有递增 offset 作唯一标识…consumer 用 pull 模式拉取并保存位置…早期 offset 存 ZooKeeper 低效，0.10.1+ 改存 __consumer_offsets topic…压缩端到端保持」

## 一句话总述
消息在分区内以递增 offset 唯一标识；消费者用 pull 模式拉取，定期把已消费 offset 提交给 Kafka。早期 offset 存在 ZooKeeper（频繁写低效、不利扩展），0.10.1 起改存内部 topic `__consumer_offsets`，故障恢复按提交位重拉，不丢消息。

## 面试官视角
P6 能说出 pull 模式与 offset 提交；P7 要讲清「为何弃 ZooKeeper」——频繁写 zk 低效且影响集群吞吐，内部 topic 借 Kafka 自身能力更稳更易扩展；并点出端到端压缩。

## 主问答
**Q（面试官原话）：** 消费者位移存在哪？为什么不用 ZooKeeper？

1. **offset 标识**：分区内消息以递增 offset 唯一标识，消费者记录已消费位置 `[源码]`。
2. **pull 模式**：consumer 主动从服务端拉取并保存位置，宕机恢复按提交位重拉 `[源码]`。
3. **早期存 zk**：offset 曾存 ZooKeeper，但频繁写 zk API 低效、限制水平扩展 `[源码]`。
4. **内部 topic**：0.10.1 起改存 `__consumer_offsets` topic，借 Kafka 自身能力，稳且易扩展 `[源码]`。
5. **端到端压缩**：broker 存压缩态、consumer 取压缩态、处理时才解压，省 IO `[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | offset 是？ | 答不出唯一标识 |
| L2 | pull 模式？ | 答不出主动拉取 |
| L3 | 早期存哪？ | 答不出 ZooKeeper |
| L4 | 为何弃 zk？ | 答不出写低效扩展难 |
| L5 | 现存哪？ | 答不出 __consumer_offsets |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| <0.10.1 | offset 存 zk | 频繁写低效 |
| ≥0.10.1 | __consumer_offsets | 内部 topic |
| 任意版本 | pull 模式 | consumer 拉取 |

## 关键代码
```go
// 手动提交位移（pull 后显式提交，故障恢复按此重拉）
for msg := range claim.Messages() {
    handle(msg)
    session.MarkMessage(msg, "") // 或同步 CommitMessages
}
```

## 总结与追问预判
**offset 是消费进度的唯一真相**。回到存储全景——见同批 146-storage-model。

## ⚠️ 原文纠错
1. 事实核校：offset 唯一标识、pull 模式、早期存 ZooKeeper 低效、0.10.1+ 存 __consumer_offsets、端到端压缩——均准确 `[经验]`。
2. 补充：原文「0.10.1 起存 __consumer_offsets」，精确 0.9 已引入该 topic、0.10.1 默认关闭 zk 存储 `[经验]`。
3. 崩坏词归一：源码将 Kafka、broker、ZooKeeper、偏移量、压缩、消费者等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
