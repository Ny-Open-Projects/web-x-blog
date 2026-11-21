---
title: "[DF-008] 一致性·Raft（Raft）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 一致性 · Raft（Raft）

- **事实**：Raft 把共识拆解为 leader 选举、日志复制、安全性三个子问题易理解易实现
- **原理**：leader 全权管理日志复制（follower 被动接收），term 单调递增保证时序，工业界主流（etcd/TiKV/Dledger），本项目 AQS/Redis/MySQL 知识多处关联
- **常见误区**：
  1. Raft 比 Paxos 性能更高（是易理解性优势）（错）
  2. Raft 允许多 leader（错）
  3. follower 主动拉取日志与 Raft 相符（是推模式）（错）
- **工程用法**：共识协议的工程标准答案
- **版本锚点**：Raft 论文
