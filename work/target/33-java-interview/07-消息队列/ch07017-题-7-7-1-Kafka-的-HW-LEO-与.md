---
title: "题 7.7.1：Kafka 的 HW/LEO 与 min.insync.replicas 的可用性代价？"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 7.7.1：Kafka 的 HW/LEO 与 min.insync.replicas 的可用性代价？

**【面试官意图】** 检验你对副本一致性机制的量化理解，而不是背 ISR 名词。
**【参考回答（可背）】** LEO 是各副本日志末端位移；HW 是 ISR 中最小 LEO，消费者只能读到 HW 之前——保证读到的都是"已被多数派确认"的。min.insync.replicas=2 与 acks=all 组合意味着 ISR 少于 2 个副本时写入直接失败（NotEnoughReplicasException）：**用可用性换一致性**，这是 CAP 取舍在 Kafka 的具体落点。副本失效判定靠 replica.lag.time.max.ms（默认 10s 追不上即踢出 ISR）。
**【追问链】** ① HW 截断与数据丢失窗口？（leader 崩溃前 follower 已复制但未提交部分会被截断，unclean 选举禁止后此风险收敛到 minISR 内）② 为什么不能无限调大 minISR？（副本抖动时集群大面积写入失败，一般是 2 of 3）。
**【P10 加分项】** 给出容量规划公式：minISR=⌊replicas/2⌋+1，并说明"3 副本 + minISR=2"能容忍 1 副本故障；再讲 KRaft 元数据替代 ZooKeeper 后，元数据一致性由 Raft 保证，分区扩容速度大幅提升——跟版本演进的人在这里明显高一档。
