---
title: "[JC-021] 线程基础·join（协作）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程基础 · join（协作）

- **事实**：线程 A 调用 B.join() 会等待 B 终止且建立 happens-before
- **原理**：join 内部是 B.isAlive() 的 wait 循环，B 终止时 notify，A 恢复后能看到 B 的全部结果
- **常见误区**：
  1. join 会立即返回无论线程是否结束（错）
  2. join 不提供内存可见性保证（错）
  3. join 与 wait 语义无关（错）
- **工程用法**：主线程收集并行结果用 join 或 Future
- **版本锚点**：JLS 17.2.3
