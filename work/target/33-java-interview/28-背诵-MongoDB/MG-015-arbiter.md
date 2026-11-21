---
title: "[MG-015] 副本集·arbiter（仲裁）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 副本集 · arbiter（仲裁）

- **事实**：arbiter（仲裁节点）只投票不存数据省资源但削弱多数派持久性
- **原理**：3 成员=2 数据+1 仲裁时，数据节点挂一个另一个成单点（仲裁无数据），生产慎用，官方文档有明确警告
- **常见误区**：
  1. arbiter 存部分数据（错）
  2. arbiter 提高数据安全性（错）
  3. 3 个 arbiter 最稳（错）
- **工程用法**：小规模副本集设计权衡
- **版本锚点**：官方文档
