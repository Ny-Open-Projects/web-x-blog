---
title: "[JV-049] 参数·DisableExplicitGC（显式 GC）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 参数 · DisableExplicitGC（显式 GC）

- **事实**：System.gc 只是建议，生产常用 -XX:+DisableExplicitGC 禁用
- **原理**：NIO 堆外内存依赖 System.gc 触发 DirectByteBuffer 回收时被禁用会堆外泄漏，正确做法是 -XX:+ExplicitGCInvokesConcurrent 而非禁用
- **常见误区**：
  1. System.gc 会立即执行 Full GC（错）
  2. 禁用 System.gc 没有任何副作用（错）
  3. DirectByteBuffer 与 System.gc 无关（错）
- **工程用法**：禁用显式 GC 必须评估堆外内存回收链路
- **版本锚点**：实战教训
