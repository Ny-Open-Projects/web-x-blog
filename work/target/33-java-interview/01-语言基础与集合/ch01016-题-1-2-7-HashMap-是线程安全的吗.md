---
title: "题 1.2.7：HashMap 是线程安全的吗？多线程下会发生什么？用什么替代？"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 1.2.7：HashMap 是线程安全的吗？多线程下会发生什么？用什么替代？

**【参考回答（可背）】**
不安全。JDK7 并发扩容可能形成环形链表 → get 死循环 CPU 100%；JDK8 修复了成环，但仍会丢数据、size 不一致。替代方案：
1. 只读场景：Collections.unmodifiableMap 或 Map.copyOf（不可变）。
2. 并发写：ConcurrentHashMap。
3. 需要保持插入/访问顺序：Collections.synchronizedLinkedHashMap 或自己加锁。
4. 高频读低频写：读写锁 + 不可变快照（Copy-On-Write 思想）。

**【P10 加分项】**
区分"线程安全"与"复合操作原子性"：即使换成 ConcurrentHashMap，`if(!map.containsKey(k)) map.put(k,v)` 仍不是原子的，必须用 putIfAbsent——大量生产 bug 出在这里，说明你被真实场景毒打过。

---
