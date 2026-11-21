---
title: "[MG-055] 副本集·read preference（读偏好）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 副本集 · read preference（读偏好）

- **事实**：读偏好：primary（默认）/primaryPreferred/secondary/secondaryPreferred/nearest
- **原理**：secondary 分摊读压力但读旧数据（复制延迟），nearest 就近读（跨机房），与 write concern 组合构成一致性与延迟矩阵
- **常见误区**：
  1. 读偏好影响写入（错）
  2. secondary 读保证最新（错）
  3. nearest 是最快一定优先（错）
- **工程用法**：读写分离策略
- **版本锚点**：官方文档
