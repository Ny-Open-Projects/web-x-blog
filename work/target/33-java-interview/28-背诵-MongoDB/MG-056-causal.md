---
title: "[MG-056] 副本集·causal（一致性）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 副本集 · causal（一致性）

- **事实**：因果一致性会话（causal consistency，3.6+）保证读己之写
- **原理**：会话内操作按因果序（写后读自己写的内容），跨副本集切换读节点不丢写，配合 majority 读关注是分布式会话方案
- **常见误区**：
  1. 因果一致性是默认行为（错）
  2. 它解决了所有一致性问题（错）
  3. 与 read concern 无关（错）
- **工程用法**：会话级一致性方案
- **版本锚点**：官方文档
