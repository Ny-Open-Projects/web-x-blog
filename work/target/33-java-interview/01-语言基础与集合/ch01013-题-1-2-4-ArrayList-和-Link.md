---
title: "题 1.2.4：ArrayList 和 LinkedList 的区别？谁更快？"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 1.2.4：ArrayList 和 LinkedList 的区别？谁更快？

**【参考回答（可背）】**
- ArrayList 底层是 Object[] 数组，支持随机访问 O(1)；LinkedList 底层双向链表，随机访问 O(n)。
- 插入删除：**并非 LinkedList 一定快**。尾部追加 ArrayList 均摊 O(1)；LinkedList 虽然插入动作 O(1)，但先要遍历定位 O(n)。中间插入两者都要移动/遍历元素。
- 内存：ArrayList 连续内存、CPU 缓存友好（局部性原理）；LinkedList 每个节点额外 2 个指针 + 对象头，内存放大严重且对缓存极不友好。

**【追问链】**
1. ArrayList 扩容机制？→ 默认初始容量 10（懒加载：new ArrayList() 时数组是空的，首次 add 才扩到 10），扩容 1.5 倍（oldCapacity + (oldCapacity >> 1)），用 Arrays.copyOf 复制。
2. 为什么是 1.5 倍？→ 平衡"扩容次数"与"内存浪费"；3 倍浪费内存，1.1 倍扩容太频繁。k 倍扩容的总复制代价近似与 n·k/(k-1) 成正比。
3. 可以边遍历边删除吗？→ 不能用 for 循环 + list.remove(i)，会漏元素且索引错位；要用 Iterator.remove() 或 JDK8 的 removeIf。并发场景用 CopyOnWriteArrayList。

**【P10 加分项】**
- 明确说"工程上几乎总是选 ArrayList"，LinkedList 在 Java 标准库中被认为是设计失误的 API（它还实现了 Deque，应该只暴露 Deque 接口）。
- 提到缓存行（64 字节）与内存局部性对性能的影响，说明你理解"为什么数组快"的硬件原理，而不只是背 API。

---
