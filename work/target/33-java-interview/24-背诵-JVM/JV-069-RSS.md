---
title: "[JV-069] 排查·RSS（堆外）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 排查 · RSS（堆外）

- **事实**：堆外内存泄漏排查看进程 RSS 与堆内存差值
- **原理**：RSS 持续增长但堆与元空间平稳，怀疑 DirectByteBuffer/Netty/JNI/线程栈/Code Cache，用 NMT（NativeMemoryTracking）分项定位
- **常见误区**：
  1. RSS 等于堆大小（错）
  2. 堆外内存无法监控（错）
  3. NMT 是 JDK 外部工具（错）
- **工程用法**：-XX:NativeMemoryTracking=summary + jcmd VM.native_memory
- **版本锚点**：实战共识
