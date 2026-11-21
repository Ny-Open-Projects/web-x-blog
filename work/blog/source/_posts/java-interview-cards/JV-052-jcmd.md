---
title: "[JV-052] 排查·jcmd（工具）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 排查 · jcmd（工具）

- **事实**：jcmd 是 JDK7+ 推荐的诊断全家桶（替代 jmap/jstack 的大部分功能）
- **原理**：jcmd PID GC.heap_dump、Thread.print、VM.flags、GC.class_histogram 等子命令覆盖诊断需求，同一进程多工具并发可能冲突
- **常见误区**：
  1. jcmd 只能查看 GC 日志（错）
  2. jcmd 与 jmap 不能同时用于同一进程（其实加 -F 强制时会）（错）
  3. jcmd 是 JDK8 之前的老工具（错）
- **工程用法**：现场诊断优先 jcmd
- **版本锚点**：JDK 文档
