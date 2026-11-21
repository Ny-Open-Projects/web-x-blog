---
title: "卡片 1：CAP 与 BASE"
date: 2026-11-18
categories: [Java面试, 分布式]
tags: [Java面试, 概念卡, 33]
type: 概念卡
disableNunjucks: true
---

### 卡片 1：CAP 与 BASE
- **CAP**：网络分区（P）发生时，一致性与可用性**二选一**。P 是必选项（分布式系统生命周期内网络故障迟早发生），所以真实选择是 CP（ZK/etcd：分区时拒绝服务保一致）vs AP（Eureka/Nacos AP 模式：返回旧数据保可用）。
- **BASE**：基本可用（Basically Available）、软状态（Soft state）、最终一致（Eventually consistent）——AP 的工程化表达。
- 常见误区：CAP 不是"三选二"，无分区时 C 和 A 可以兼得；分区只是概率事件。
