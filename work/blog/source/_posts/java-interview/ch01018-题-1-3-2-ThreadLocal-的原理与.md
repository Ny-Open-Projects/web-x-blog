---
title: "题 1.3.2：ThreadLocal 的原理与内存泄漏？"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 面试题, 进阶题, 33]
type: 面试题
disableNunjucks: true
---

### 题 1.3.2：ThreadLocal 的原理与内存泄漏？

**【参考回答（可背）】**（放本章因为它是"语言级"机制，第 2 章会再用它）
- 每个 Thread 内有一个 ThreadLocalMap，key 是 ThreadLocal 对象的**弱引用**，value 是强引用。
- set/get 时先拿当前线程的 map，以 ThreadLocal 自身为 key。
- 泄漏路径：ThreadLocal 外部引用消失后，key 被 GC 回收变成 null，但 value 仍被 Thread→map→entry 强引用链持有；线程池中线程不死，value 就一直无法释放。
- 正确姿势：**用完必须 remove()**，且放在 finally 中；框架层面（如 Spring 的 RequestContextFilter）用 try-finally 清理。

**【追问链】**
1. 为什么 key 用弱引用？→ 缓解而非根治泄漏：让"ThreadLocal 实例本身"可被回收；且 set/get/remove 时会顺带清理 key 为 null 的 stale entry（探测式清理 expungeStaleEntry）。
2. 为什么 value 不用弱引用？→ 若 value 也弱引用，外部没有引用时 value 会随时被回收，业务数据会无故丢失——宁可泄漏（可通过 remove 清理）也不能丢数据。
3. InheritableThreadLocal 和 TransmittableThreadLocal 区别？→ 前者仅在线程创建时复制给子线程，线程池复用线程时不生效；阿里开源的 TTL 通过装饰 Runnable/Callable，在提交任务时捕获、执行时回放、结束时恢复，解决线程池上下文传递（链路 traceId 传递的标准方案）。

**【P10 加分项】**
结合真实事故讲：一次压测中 ThreadLocal 泄漏导致老年代缓慢上涨最终 Full GC 频繁，通过 jmap histo 找到 ThreadLocalMap 中大量 null-key entry 定位。这体现了"把语言知识接到 JVM 排查能力"的 P10 闭环。

---
