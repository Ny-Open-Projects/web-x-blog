---
title: "[DF-002] 理论·ZooKeeper（CP）"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 理论 · ZooKeeper（CP）

- **事实**：CP 场景代表：ZooKeeper/etcd（协调类：锁、配置、选主）
- **原理**：协调服务要求强一致（锁不能双持），牺牲分区时的可用性（少数派不可用）
- **常见误区**：
  1. ZK 是 AP 系统（错）
  2. 锁服务可以用 AP 实现（错）
  3. CP 与 AP 无区别（错）
- **工程用法**：协调组件选型依据
- **版本锚点**：理论共识
