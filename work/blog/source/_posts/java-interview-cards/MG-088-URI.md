---
title: "[MG-088] Java·URI（连接）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Java · URI（连接）

- **事实**：连接 URI 携带 replicaSet 参数（副本集自动发现与故障切换的前提）
- **原理**：指定 replicaSet 后驱动自动发现全部成员并在主挂时切换，不指定则只连单个节点（主挂不切换），高可用配置第一参数
- **常见误区**：
  1. 不指定 replicaSet 也能自动切换（错）
  2. URI 只能配地址（错）
  3. 参数是可选装饰（错）
- **工程用法**：Java 连接串审查项
- **版本锚点**：官方文档
