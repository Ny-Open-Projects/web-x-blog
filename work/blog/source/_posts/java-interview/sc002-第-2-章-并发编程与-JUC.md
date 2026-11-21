---
title: "第 2 章 并发编程与 JUC"
date: 2026-11-18
categories: [Java面试, 速记卡]
tags: [Java面试, 速记卡, 33]
type: 速记卡
disableNunjucks: true
---

## 第 2 章 并发编程与 JUC

1. volatile = 可见性 + 有序性，≠ 原子性；标志位/DCL 用它。
2. 锁升级：无锁→偏向→轻量→重量；JDK15 禁用、JDK21 已彻底移除偏向锁（实测标志位 Unrecognized）。
3. 线程池口诀：先核心、再队列、后非核心、最后拒绝；禁 Executors、必有界队列。
4. 线程数靠压测，公式只是起点：N = C×U×(1+W/C)。
5. AQS = volatile state + CLH 双向队列 + park/unpark + 模板方法。
6. CAS 三坑：ABA（加版本）、自旋烧 CPU（LongAdder 分段）、单变量（封装对象）。
7. LongAdder 读弱写强；sum() 是近似快照。
8. CF 生产三件套：自定义线程池、allOf 聚合、orTimeout 超时；异常用 handle/exceptionally。
9. ThreadLocal：key 弱 value 强、用完 remove、线程池传值用 TTL。
10. happens-before 是可见性承诺，不是时间顺序；8 条规则能默写 6 条。
11. 虚拟线程：IO 密集收益大；资源模型从"线程数"迁移到"连接数/下游配额"；防 pinning。
12. commonPool 只给纯 CPU 计算；IO 进去就是全局故障域。
13. JUC 弱一致迭代器：无锁读换最终一致；强一致需求换语义不是换参数。
14. 限流/倒计数/栅栏：Semaphore 管许可、Latch 一次性、Barrier 可重用、Phaser 多阶段。
15. 死锁防固定顺序、活锁防退避、饥饿防配额；并发治理靠 CI 门禁。
