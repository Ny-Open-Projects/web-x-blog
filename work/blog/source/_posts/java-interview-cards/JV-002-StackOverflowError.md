---
title: "[JV-002] 运行时数据区·StackOverflowError（异常）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运行时数据区 · StackOverflowError（异常）

- **事实**：线程栈默认 1MB 左右（-Xss 可调）递归过深抛 StackOverflowError
- **原理**：每方法调用压一帧，栈容量固定，无边界递归或深递归触发
- **常见误区**：
  1. StackOverflowError 是堆溢出的一种（错）
  2. 栈抛的是 OutOfMemoryError（错）
  3. 加大栈内存能解决无限递归（错）
- **工程用法**：-Xss256k 可压测栈深，线上先查递归出口
- **版本锚点**：HotSpot 默认
