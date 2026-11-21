---
title: "[MG-031] 分片·balancer（chunk）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 分片 · balancer（chunk）

- **事实**：chunk 是数据切分单位，balancer 自动在分片间迁移 chunk 均衡
- **原理**：chunk 默认上限可调（split 阈值），balancer 有时间窗口配置（业务低峰迁移），4.4+ 平衡策略更细
- **常见误区**：
  1. chunk 固定 64MB 不可变（错）
  2. balancer 实时迁移影响性能（可配窗口）（错）
  3. jumbo chunk 自动拆分（错）
- **工程用法**：分片运维知识
- **版本锚点**：官方文档
