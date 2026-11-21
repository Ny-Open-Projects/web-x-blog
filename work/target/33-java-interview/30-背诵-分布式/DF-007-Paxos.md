---
title: "[DF-007] 一致性·Paxos（Paxos）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 一致性 · Paxos（Paxos）

- **事实**：Paxos 是分布式一致性的理论基石（多数派+提案编号）
- **原理**：Basic Paxos 单值共识，Multi-Paxos 多值（日志），工程实现少（难懂难实现），Raft 是其工程化替代
- **常见误区**：
  1. Paxos 已被淘汰（理论仍是根基）（错）
  2. Paxos 不需要多数派（错）
  3. Paxos 工程广泛直接使用（错）
- **工程用法**：理论深度题
- **版本锚点**：理论共识
