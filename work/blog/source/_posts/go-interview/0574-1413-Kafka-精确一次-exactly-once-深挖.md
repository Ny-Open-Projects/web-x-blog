---
disableNunjucks: true
title: "1413 Kafka 精确一次（exactly-once）深挖"
date: 2026-10-10 08:49:56
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：消息中间件 / Kafka | 难度：L3 | 题型：深挖 | 频率：中 | 关键词：**exactly-once** / **端到端** / **消费端幂等** / **跨会话跨topic** / **性能代价**
> 原文锚点：第 1~44 段「幂等/事务生产者；二者都避免重复发送；幂等单分区单会话、事务跨分区跨会话跨topic；事务性能差；consumer端仍需额外机制」

## 思路与架构
Kafka 精确一次语义分两层，常被混淆：
- **producer 端（发送不丢不重）**：幂等生产者（单分区单会话）或事务生产者（跨分区/会话/topic）兜底，broker 去重。
- **端到端（消费不重不丢）**：producer 机制管不到 consumer；须消费逻辑幂等 + 事务型 offset 提交，才能做到"处理一次"。

## 方案取舍
```text
精确一次手段对比：
──────────────────────────────────────────────────────────
手段                范围                  性能        何时用
幂等生产者         单分区单会话去重       轻          仅防 producer 重试重发
事务生产者         跨分区/会话/topic 原子 重(两阶段)  多步原子/消费转换写回
消费逻辑幂等       consumer 端去重        中          端到端精确一次最后一道网
事务型 offset 提交 消费位移随事务原子     中          consume-transform-produce 防重投

代价提示：
- 事务性能明显差于幂等，非必要不开
- 事务支持跨 topic（多 topic 写入同一事务），幂等做不到
- consumer offset 提交与处理顺序错位 → 仍可能重投/丢失
```

## 答题技巧
```text
面试话术（先分层，再给边界，最后收尾）：
1. 分层：精确一次分 producer 端 与 端到端 两层，别混
2. producer 端：幂等(单分区) / 事务(跨分区会话topic)，broker 去重
3. 边界：二者都只管发送端，consumer 因 offset 错位仍可能重投
4. 端到端：消费逻辑幂等 + 事务型 offset 提交，才做到处理一次
5. 选型：单分区去重用幂等；跨分区/跨 topic/消费转换才上事务
6. 收尾：事务性能差，按需启用，非必要不开
```

> 边界：producer 机制概述见 1418；消费端幂等见 1418；提交机制见 1417；本卡只深挖"Kafka 精确一次分层与选型"不重述各基础机制。

## 细节与核心 API

**producer 端：幂等（单分区单会话）vs 事务（跨分区/会话/topic）：**

```go
// 幂等生产者（0.11+，broker 按 PID+序列号去重）
config.Producer.Idempotent = true
config.Net.MaxOpenRequests = 1 // 配合幂等

// 事务生产者（consume-transform-produce 原子）
config.Producer.TransactionalID = "txn-1"
producer.BeginTransaction()
producer.SendMessage(bizMsg)                 // 写业务 topic
producer.SendOffsetsToTransaction(offsets, group) // 消费位移随事务原子提交
producer.CommitTransaction()
```

**端到端精确一次（producer 机制管不到 consumer）：**

```text
消费逻辑幂等 + 事务型 offset 提交 = 处理一次
- 幂等只防 producer 重试重发；consumer offset 错位仍可能重投
- 事务性能明显差，非必要不开；跨 topic/多步原子才上事务
```
