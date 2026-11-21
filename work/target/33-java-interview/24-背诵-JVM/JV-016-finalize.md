---
title: "[JV-016] 回收·finalize（finalization）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 回收 · finalize（finalization）

- **事实**：finalize 机制不可靠已被标记废弃，替代方案是 Cleaner 与 try-with-resources
- **原理**：finalize 执行时机不确定且可能复活对象拖垮 GC，JDK9 弃用、JDK18 deprecated for removal
- **常见误区**：
  1. finalize 保证会被调用（错）
  2. finalize 是推荐的资源清理方式（错）
  3. finalize 在对象回收前同步执行（错）
- **工程用法**：资源清理一律显式关闭或 Cleaner
- **版本锚点**：JEP 421
