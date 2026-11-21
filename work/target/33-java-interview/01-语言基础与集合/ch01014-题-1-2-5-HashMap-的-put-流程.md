---
title: "题 1.2.5：HashMap 的 put 流程？（JDK8）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 1.2.5：HashMap 的 put 流程？（JDK8）

**【参考回答（可背）】**（这是 Java 面试出现率第一的题，必须脱口而出）
1. 计算 key 的 hash：高 16 位异或低 16 位。
2. 若 table 未初始化（或容量 0），先 resize() 初始化。
3. `(n-1) & hash` 定位桶：
   - 桶为空 → 直接放入；
   - 桶首节点 key 相同（hash 相等且 == 或 equals）→ 覆盖；
   - 首节点是 TreeNode → 走红黑树插入；
   - 否则遍历链表：找到相同 key 就覆盖，到尾部就尾插新节点（JDK8 改为尾插）。**树化的精确触发**：bin 已有 8 个节点时，下一次插入（第 9 个）调用 treeifyBin——容量 ≥ 64 → 转红黑树；容量 < 64 → 只扩容不树化。（本机实测：64 容量表插 8 个同桶键仍是链表 Node，第 9 个才变 TreeNode，见 notes/verify）。
4. ++modCount（fail-fast 机制），++size 后若超过 threshold（容量×负载因子 0.75）→ resize 扩容为 2 倍。

**【追问链】**
1. 为什么负载因子是 0.75？→ 空间与时间的折中：太小频繁扩容浪费内存，太大冲突多查询变慢。泊松分布推导：负载 0.75 下 bin 长度达到 8 的概率约千万分之一（0.00000006），这正是选 8 做树化阈值的依据。
2. JDK7 和 JDK8 的区别？→ 头插改尾插（头插在并发扩容时会形成环形链表导致 CPU 100%，虽然 HashMap 本身就不该并发使用）；链表+红黑树（最坏从 O(n) 到 O(logn)）。
3. 为什么树化阈值是 8、退化阈值是 6？→ 阈值 8 的语义是“bin 已有 8 个节点时，下一次插入触发树化”（TREEIFY_THRESHOLD javadoc 原文：adding an element to a bin with at least this many nodes——本机实测 8 键仍是链表、第 9 个转 TreeNode）；8 来自泊松分布统计边界。退化用 6 留 2 的缓冲，防 8 附近插入删除导致树↔链表来回抖动。
4. 扩容时元素怎么迁移？→ JDK8 优化：扩容后元素要么留在原位置 i，要么去 i + oldCap，由 `hash & oldCap` 是否为 0 决定，无需重新计算 hash。

**【P10 加分项】**
- 主动讲 JDK8 红黑树实现细节：TreeNode 保留了 next 指针，树节点同时是链表节点，且树化/退化共享同一份节点对象，避免对象重建。
- 指出 HashMap 在极端 hash 攻击下的退化问题（Tomcat 曾因此改用随机 hash 种子），体现安全视角。
- 讲清 fail-fast（modCount）≠ 线程安全：ConcurrentModificationException 只是尽力而为的检测。

---
