---
title: "[JV-031] GC 日志·GC(n)（格式）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## GC 日志 · GC(n)（格式）

- **事实**：JDK9+ 统一日志格式如 GC(12) Pause Young (Normal) 1024M->256M
- **原理**：JDK8 的 PrintGCDetails 格式完全不同，统一日志用 -Xlog:gc* 输出，看日志先认版本（本项目 JDK 21 实测格式一致）
- **常见误区**：
  1. JDK9 之后日志格式与 JDK8 相同（错）
  2. GC(n) 中的 n 是堆序号（错）
  3. -Xlog:gc* 在 JDK8 可用（错）
- **工程用法**：现场排查先确认 JDK 版本再读日志
- **版本锚点**：JEP 158 实测
