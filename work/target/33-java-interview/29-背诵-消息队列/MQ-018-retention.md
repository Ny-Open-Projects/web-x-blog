---
title: "[MQ-018] 运维·retention（保留）"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 运维 · retention（保留）

- **事实**：消息保留策略：按时间（默认 7 天）与按大小，压缩主题（compact）按 key 保留最新
- **原理**：retention 只影响磁盘不丢已消费（消费位移独立），compact 适合状态快照主题，磁盘规划=吞吐×保留期
- **常见误区**：
  1. 保留期到了已消费消息也删（错）
  2. compact 主题会丢历史（按 key 留最新）（错）
  3. retention 影响消费位移（错）
- **工程用法**：磁盘与保留策略
- **版本锚点**：官方文档
