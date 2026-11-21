---
title: "题 2.4a.4：Semaphore、CountDownLatch、CyclicBarrier 怎么选？Phaser 是什么？"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 2.4a.4：Semaphore、CountDownLatch、CyclicBarrier 怎么选？Phaser 是什么？

**【参考回答（可背）】** 一句话区分：**Semaphore 管许可**（限流/资源配额，可复用）；**CountDownLatch 一次性倒计数**（等 N 件事完成，不可重置）；**CyclicBarrier 可重用栅栏**（N 个线程互相等到齐再一起走，适合分批同步）。Phaser 是它们的统一体：多阶段栅栏，支持动态注册/注销参与者，替代"多批次的 CyclicBarrier"。
**【追问链】** ① Semaphore 公平模式？（支持 fairness 参数，默认非公平——限流场景一般无需公平）② CountDownLatch 的 await 带超时为什么必须用？（防止参与者异常导致永久等待）。
**【P10 加分项】** 组合实战："全链路压测预热：Semaphore(并发数) 控压测并发 + CountDownLatch(1) 统一发令 + AtomicLong 统计——三个最基础工具拼出压测框架，面试讲这个组合比背 API 高级。"
