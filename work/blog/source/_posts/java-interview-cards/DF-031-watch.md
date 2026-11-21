---
title: "[DF-031] 协调·watch（etcd）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 协调 · watch（etcd）

- **事实**：etcd：Raft 强一致 KV+watch 机制（变更推送）
- **原理**：K8s 的基石（所有组件存 etcd），watch 基于 revision 增量推送，mvcc 多版本支持历史读，与 ZK 对比：更轻更云原生
- **常见误区**：
  1. etcd 是 AP（错）
  2. watch 是轮询（错）
  3. etcd 与 K8s 无关（错）
- **工程用法**：云原生协调服务
- **版本锚点**：实战共识
