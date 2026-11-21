---
title: "[JC-019] 线程基础·InterruptedException（中断）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程基础 · InterruptedException（中断）

- **事实**：捕获 InterruptedException 后必须恢复中断标志或继续向上抛
- **原理**：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）
- **常见误区**：
  1. catch 后什么都不做是最安全的（错）
  2. InterruptedException 应转为运行时异常直接打日志了事（错）
  3. 中断标志自动保留无需恢复（错）
- **工程用法**：吞异常必须注释说明理由并恢复标志位
- **版本锚点**：C1.5 手册
