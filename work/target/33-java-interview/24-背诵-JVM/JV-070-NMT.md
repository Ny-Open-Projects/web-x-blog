---
title: "[JV-070] 排查·NMT（NMT）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 排查 · NMT（NMT）

- **事实**：NMT 开启后 jcmd VM.native_memory summary 分项展示内存去向
- **原理**：分类包括 Java Heap、Class、Thread、Code、GC、Internal、Other，把"消失的内存"按项对号，开销约 5%（detail 模式更高）
- **常见误区**：
  1. NMT 默认开启（错）
  2. NMT 能精确到对象级别（错）
  3. NMT 是分析工具不影响性能（错）
- **工程用法**：堆外内存问题第一步
- **版本锚点**：JDK 文档
