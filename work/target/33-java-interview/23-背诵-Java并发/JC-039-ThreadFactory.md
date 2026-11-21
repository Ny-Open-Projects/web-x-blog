---
title: "[JC-039] 线程池·ThreadFactory（误用）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · ThreadFactory（误用）

- **事实**：线程池必须通过 ThreadFactory 给线程命名
- **原理**：默认线程名 pool-1-thread-N 无法定位问题，命名规则建议业务-pool-序号，dump 分析时一眼归因
- **常见误区**：
  1. 线程名默认包含业务信息（错）
  2. 命名只是美观不影响排查（错）
  3. ThreadFactory 参数可传 null（错）
- **工程用法**：所有线程池统一命名规范
- **版本锚点**：阿里手册
