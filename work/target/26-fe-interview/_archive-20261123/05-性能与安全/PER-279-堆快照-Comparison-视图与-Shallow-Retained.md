---
title: [PER-279] 堆快照里 Shallow Size 与 Retained Size 区别是什么？比较视图的 "#Delta" 怎么用？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-279：堆快照里 Shallow Size 与 Retained Size 区别是什么？比较视图的 "#Delta" 怎么用？

**答**：
- Shallow Size：对象自身占的内存（字段、指针槽），对象结构本身的大小；Retained Size：释放该对象后能连带释放的总内存（它独占支配的下游子图）——泄漏定位优先看 Retained，因为删掉泄漏源能回收的是整棵支配树。
- Retained 的大头常是"闭包 + 它捕获的作用域"或"数组 + 元素对象"；Retainers 面板从对象向上列出引用链直到 GC 根，最近的一跳通常就是修复点。
- 比较视图（Comparison）：两个快照对比，"#Delta" 是对象数量差（不是字节），"+N" 表示新增 N 个实例；配合 "Size Delta" 看字节增长。排序技巧：先按 #Delta 找"反复新增的构造函数"，再看它的 Retained Size 是否可观。
- 常见噪音：字符串与系统对象有正常波动，别被 "+几百个 string" 吓到；重点看业务构造函数（如 GoodsItem、Modal）与 Detached DOM、(closure)。

```text
Comparison 视图读法：
构造函数          #Delta   Size Delta  Retained Size（新快照）
GoodsItem         +50      +2.3MB      8MB        ← 每次操作新增 10 个，retained 大 => 泄漏
Detached <div>    +10      +800KB      3MB        ← DOM 泄漏实锤
(closure)         +10      +12KB       2MB        ← 闭包持有 GoodsItem 数组的引用链
排查顺序：Retainers(GoodsItem) → 持有者数组 → (closure) → 全局 cache = window 上的 Map
修复：unmount 时 cache.delete(key) 或改 WeakMap/LRU
```
