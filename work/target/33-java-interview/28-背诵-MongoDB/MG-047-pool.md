---
title: "[MG-047] Java·pool（连接池）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Java · pool（连接池）

- **事实**：MongoDB Java 驱动连接池：maxConnectionPoolSize 默认 100 与服务实例数联动
- **原理**：连接池与驱动内部线程模型（每个连接独立），高并发突发看 pool 指标（连接等待时间），与服务副本数×线程数估算
- **常见误区**：
  1. maxConnectionPoolSize 无默认值（错）
  2. 连接池越大越好（错）
  3. 连接池与性能无关（错）
- **工程用法**：驱动调优
- **版本锚点**：官方文档
