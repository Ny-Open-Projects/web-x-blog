---
title: "题 1.2.6：ConcurrentHashMap 如何保证线程安全？（JDK8）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 1.2.6：ConcurrentHashMap 如何保证线程安全？（JDK8）

**【参考回答（可背）】**
- JDK7 是分段锁（Segment 继承 ReentrantLock，默认 16 段，并发度=段数）。
- JDK8 抛弃分段锁，改为 **CAS + synchronized 锁单个桶头节点**：
  1. 桶为空 → CAS 放入头节点，失败自旋重试；
  2. 桶非空 → synchronized 锁住头节点后链表/树插入；
  3. 正在扩容的桶（ForwardingNode）→ 当前线程帮助迁移（多线程协助扩容）；
  4. size 用 baseCount + CounterCell[] 分段计数（思想同 LongAdder），避免所有线程争抢一个计数器。
- get 全程无锁：Node.val 和 next 用 volatile 保证可见性；table 用 volatile 读。

**【追问链】**
1. 为什么 JDK8 用 synchronized 而不是 ReentrantLock？→ 锁粒度已经细到单个桶，冲突概率低，synchronized 经锁升级优化后（偏向/轻量级）性能不吃亏，且省内存（无 AQS 队列节点）、JVM 可继续优化。
2. ConcurrentHashMap 的 key/value 能为 null 吗？→ 都不能。二义性问题：get 返回 null 无法区分"不存在"还是"值就是 null"（HashMap 可以，因为它容许并发出错再重查；并发容器必须一次确定）。这与 Hashtable 一致。
3. size() 准确吗？→ 返回的是统计瞬间的近似值（并发下无全局锁），强一致需求要用 synchronized 包裹或改用其他结构。
4. 多线程 put 会丢数据吗？→ 不会丢（CAS+锁），但"check-then-act"复合操作（先 get 判断再 put）依然需要 putIfAbsent/computeIfAbsent 这类原子方法。

**【P10 加分项】**
- 讲清多线程协助扩容的 transfer 细节：按桶区间（stride，最小 16）认领迁移任务，ForwardingNode 作为"此处已迁移"的路标。
- 指出 computeIfAbsent 的死循环坑（JDK8 中若回调里又操作同一个 key 的桶会卡住，JDK9 修复）——这是真实生产事故素材。

---
