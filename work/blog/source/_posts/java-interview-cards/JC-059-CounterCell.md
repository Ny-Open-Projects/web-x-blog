---
title: "[JC-059] 并发容器·CounterCell（CHM）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发容器 · CounterCell（CHM）

- **事实**：CHM 的 size 通过 baseCount 加 CounterCell 数组汇总且是弱一致值
- **原理**：写路径 CAS baseCount 失败则分散累加到 CounterCell 减少竞争，size 是采样汇总无强一致快照，精确计数要用外部锁或 LongAdder 思路
- **常见误区**：
  1. CHM.size() 是精确值（错）
  2. size 计算全程加锁（错）
  3. CounterCell 与 LongAdder 无关（错）
- **工程用法**：需要精确 size 就换数据结构
- **版本锚点**：JDK8 源码
