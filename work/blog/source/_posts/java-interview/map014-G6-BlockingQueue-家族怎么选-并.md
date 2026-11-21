---
title: "G6. BlockingQueue 家族怎么选？（并发深挖追问）"
date: 2026-11-18
categories: [Java面试, 追问地图]
tags: [Java面试, 补漏卡, 33]
type: 补漏卡
disableNunjucks: true
---

### G6. BlockingQueue 家族怎么选？（并发深挖追问）

**【参考回答（可背）】** 四类一张表（背）：① **ArrayBlockingQueue**：定长数组、单锁、内存预分配——有界要求首选；② **LinkedBlockingQueue**：可选有界（默认 Integer.MAX_VALUE！）、两把锁（读写分离）吞吐更高——Executors 的坑就是它的默认无界；③ **SynchronousQueue**：零容量、直接交接——CachedThreadPool 与高吞吐交换场景；④ **DelayQueue**：到期才能取——本地延迟任务（TTL 缓存/超时关闭）。另加 PriorityBlockingQueue（优先级）与 LinkedTransferQueue（无锁、tryTransfer）。
**【追问链】** put/take/offer/poll 四方法的阻塞语义矩阵？→ put 满阻塞、offer 立即返回/false、offer(timeout) 限时；take 空阻塞、poll 同理。
**【P10 加分项】** "线程池队列选型（第 2 章）的本质就是在这张表里选：有界保命选 Array，吞吐优先选有界 Linked，任务必快选 Synchronous。"
