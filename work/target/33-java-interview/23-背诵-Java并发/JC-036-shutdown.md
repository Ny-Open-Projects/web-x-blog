---
title: "[JC-036] 线程池·shutdown（生命周期）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · shutdown（生命周期）

- **事实**：shutdown 后已提交任务继续执行完而 shutdownNow 尝试中断并返回未执行任务
- **原理**：shutdown 拒绝新任务但处理完队列，shutdownNow 遍历中断工作线程，两者都不等任务真正结束，需配合 awaitTermination
- **常见误区**：
  1. shutdown 会立即中断所有任务（错）
  2. shutdownNow 保证所有任务停止（错）
  3. 调用 shutdown 后线程池立即不可用（错）
- **工程用法**：优雅停机顺序：shutdown、awaitTermination、shutdownNow 兜底
- **版本锚点**：JDK 文档
