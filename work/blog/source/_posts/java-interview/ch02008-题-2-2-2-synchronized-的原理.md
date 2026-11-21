---
title: "题 2.2.2：synchronized 的原理？锁升级过程？"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 2.2.2：synchronized 的原理？锁升级过程？

**【参考回答（可背）】**
- 字节码层面：同步代码块用 **monitorenter/monitorexit**（可能多个 exit 配对异常出口），同步方法用 ACC_SYNCHRONIZED 标志。每个对象头（Mark Word）+ 关联的 Monitor（C++ ObjectMonitor，含 owner、EntryList、WaitSet）。
- **锁升级**（JDK8）：无锁 → 偏向锁（首次获取后记下线程 ID，之后该线程进入无需 CAS）→ 轻量级锁（第二个线程来竞争，栈上 Lock Record + CAS 自旋）→ 重量级锁（自旋失败次数多，膨胀为 OS 互斥量，线程挂起、涉及内核态切换）。
- JDK15 起默认废弃偏向锁（维护成本 > 收益，现代应用高并发场景多），JDK18 完全移除。

**【追问链】**
1. synchronized 和 ReentrantLock 区别？→ 功能：后者可中断、可超时（tryLock）、公平锁、多 Condition；实现：前者 JVM 内置+自动释放，后者 AQS；性能：JDK6 锁升级后基本持平，无特殊需求用 synchronized。
2. 什么是锁粗化/锁消除？→ JIT 优化：锁消除基于逃逸分析（对象不会逃逸出线程则去掉锁，如局部 StringBuffer append）；锁粗化把连续加锁合并（循环里每次 append 都解锁→扩大到循环外一次）。

**【P10 加分项】**
- 指出偏向锁的撤销代价：多线程交替但无竞争场景受益；一旦竞争，撤销偏向要等全局安全点，批量重偏向/批量撤销（BiasedLockingBulkRebiasThreshold=20/40）。

> **本机实证（JDK 21.0.2）**：`java -XX:+UseBiasedLocking -version` 直接报 `Unrecognized VM option`——偏向锁代码在 JDK 21 已**彻底移除**（JDK15 禁用+废弃 → JDK18 标志废弃 → 21 移除）。讲锁升级时主动报出这条版本时间线，是"跟踪 JDK 演进"的直接证据。
- 讲 wait/notify 与 ObjectMonitor 的 WaitSet 关系，说明对"重量级锁为什么慢"的理解停在用户态/内核态切换与线程挂起调度，而不是背名词。

---
