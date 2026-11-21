---
title: "[JV-074] GC·to-space（并发失败）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## GC · to-space（并发失败）

- **事实**：G1 出现 to-space exhausted 表示晋升时 Survivor/Old Region 不足
- **原理**：并发标记期间老年代同时被消耗，晋升失败触发 Full GC，解法：预留空间（-XX:G1ReservePercent 默认 10）、提前并发标记（InitiatingHeapOccupancyPercent）
- **常见误区**：
  1. to-space exhausted 只影响性能无实际危害（错）
  2. G1ReservePercent 默认是 50（错）
  3. 晋升失败不会触发 Full GC（错）
- **工程用法**：G1 运维告警关键字
- **版本锚点**：G1 调优
