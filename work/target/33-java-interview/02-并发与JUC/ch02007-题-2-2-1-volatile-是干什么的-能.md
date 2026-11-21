---
title: "题 2.2.1：volatile 是干什么的？能保证原子性吗？"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 2.2.1：volatile 是干什么的？能保证原子性吗？

**【参考回答（可背）】**
volatile 两个语义，一个不保证：
1. **可见性**：写 volatile 变量立即刷回主存，其他核心缓存行失效（MESI），读时强制从主存加载。
2. **禁止指令重排**：编译器在 volatile 读写前后插入**内存屏障**（写后 StoreStore+StoreLoad，读后 LoadLoad+LoadStore）。
3. **不保证原子性**：`volatile int count; count++` 依然错——读改写三步照样竞态。要原子用 AtomicInteger。

典型用途：**状态标志位**（如 `volatile boolean running` 控制优雅停机）、double-checked locking 的实例字段。

> **本机实证（2026-11-14，验证套件 notes/verify）**：同一台机器上，volatile 标志位的等待线程在写后 2 秒内退出（PASS）；而**去掉 volatile 的对照线程持续自旋 9 分钟仍未看见写入**（CPU 跑满、JVM 都无法退出，最后靠守护线程修复收场）。可见性问题不是理论——它是确定性发生的生产 bug。

**【追问链】**
1. 为什么 DCL 单例要 volatile？→ `new Singleton()` 三步：分配内存→初始化→引用赋值，2 和 3 可能重排；另一个线程拿到"已赋值但未初始化完成"的引用。volatile 禁止该重排。（更优雅方案：静态内部类 Holder 或枚举。）
2. volatile 底层怎么实现的？→ x86 上写 volatile 生成 `lock` 前缀指令（如 lock addl），lock 前缀会：锁缓存行、写回主存、使其他核心该缓存行失效。JMM 通过内存屏障抽象屏蔽各平台差异。
3. volatile 和 synchronized 怎么选？→ 一写多读用 volatile（如配置刷新）；复合操作必须锁或 CAS。

**【P10 加分项】**
讲 VarHandle（JDK9）替代 Unsafe 的意义：提供 acquire/release 模式（弱内存语义，比 volatile 更细粒度的性能选择），并指出 volatile 语义在 JSR-133 文档中的正式定义——能引到 JLS §17.4 说明你是读规范的人。

---
