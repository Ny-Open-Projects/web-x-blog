---
title: "B 组：并发与 JUC（对应第 2 章）"
date: 2026-11-18
categories: [Java面试, 快问快答]
tags: [Java面试, 快问快答, 33]
type: 快问快答
disableNunjucks: true
---

## B 组：并发与 JUC（对应第 2 章）

11. **volatile 三句话？** 可见性（MESI 刷主存）、有序性（内存屏障）、不保证原子性。
12. **DCL 为什么加 volatile？** new 三步可能重排（赋引用先于初始化），其他线程拿到半初始化对象。
13. **锁升级四态？** 无锁→偏向→轻量→重量；JDK15 禁用偏向锁，JDK21 已彻底移除（实测 -XX:+UseBiasedLocking 报 Unrecognized）。
14. **线程池执行流程口诀？** 先核心、再队列、后非核心、最后拒绝。
15. **Executors 两大罪？** Fixed 无界队列 OOM；Cached 线程数无上限爆炸。
16. **线程数怎么定？** N≈C×U×(1+W/C) 起步，压测定案，动态线程池运行时调。
17. **submit 的异常去哪了？** 被 FutureTask 存进 Future，不打印——静默丢失的经典 bug。
18. **AQS 的核心结构？** volatile state + CLH 变体双向队列 + park/unpark + 模板方法（tryAcquire 留给子类）。
19. **CAS 三坑？** ABA（版本号）、自旋烧 CPU（LongAdder 分段）、只能一变量（封装对象）。
20. **LongAdder 为什么快？** 热点分散到 Cell[]，读弱写强，sum() 是近似快照。
