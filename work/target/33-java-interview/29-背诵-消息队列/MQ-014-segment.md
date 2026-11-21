---
title: "[MQ-014] 存储·segment（段）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 存储 · segment（段）

- **事实**：Kafka 日志按 segment 文件切分+稀疏索引（offset 索引）
- **原理**：顺序写文件+追加模式（磁盘顺序写接近内存速度），索引稀疏内存映射，按 offset/时间戳二分定位
- **常见误区**：
  1. Kafka 消息随机写（错）
  2. 索引是全量稠密（错）
  3. 顺序写不比随机写快多少（错）
- **工程用法**：存储设计原理
- **版本锚点**：官方文档
