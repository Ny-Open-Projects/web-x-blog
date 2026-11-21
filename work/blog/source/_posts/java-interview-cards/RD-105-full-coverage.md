---
title: "[RD-105] Cluster·full-coverage（可用性）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Cluster · full-coverage（可用性）

- **事实**：cluster-require-full-coverage 默认 yes：任一槽无主节点则整个集群拒绝服务
- **原理**：保证数据完整性（缺失槽区间不可用），设 no 则缺失部分仍服务其余槽（可用性优先），按业务对"部分可用"的容忍度选择
- **常见误区**：
  1. 该参数默认 no（错）
  2. 设 no 后数据不丢（缺失槽写入被拒）（错）
  3. 参数影响主从复制（错）
- **工程用法**：Cluster 可用性权衡
- **版本锚点**：官方文档
