---
title: "[JV-050] 堆外·DirectByteBuffer（DirectMemory）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 堆外 · DirectByteBuffer（DirectMemory）

- **事实**：NIO 的 DirectByteBuffer 数据在堆外受 -XX:MaxDirectMemorySize 限制
- **原理**：避免堆内到堆外拷贝提升 IO 性能，回收靠 Cleaner 虚引用加 System.gc 提示，泄漏表现为堆正常但 RSS 持续增长
- **常见误区**：
  1. DirectByteBuffer 数据存在堆内（错）
  2. 堆外内存受 -Xmx 限制（错）
  3. 堆外内存无泄漏风险（错）
- **工程用法**：Netty 大量使用堆外，必须监控 RSS 与 PooledByteBufAllocator 指标
- **版本锚点**：实战共识
