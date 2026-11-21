---
title: "[JC-108] 并发容器·foreach（ConcurrentHashMap）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 并发容器 · foreach（ConcurrentHashMap）

- **事实**：CHM 支持并行 forEach 与 search 等 bulk 操作（JDK8+）
- **原理**：forEach(parallelismThreshold, action) 超过阈值的条目并行处理，search/findAny 语义，大数据量遍历可用
- **常见误区**：
  1. CHM 遍历必须加锁（错）
  2. bulk 操作默认串行（错）
  3. 并行遍历会修改容器（错）
- **工程用法**：离线统计任务用并行遍历
- **版本锚点**：JDK8 文档
