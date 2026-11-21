---
title: "[SP-051] 事务·REQUIRED（传播）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 事务 · REQUIRED（传播）

- **事实**：REQUIRED 是默认传播行为：有事务加入无事务新建
- **原理**：7 种传播行为的核心，大多数业务场景用它，理解其余 6 种都从它出发
- **常见误区**：
  1. 默认传播是 REQUIRES_NEW（错）
  2. REQUIRED 总是新建事务（错）
  3. 它与非事务调用组合必然回滚（错）
- **工程用法**：传播行为题的基准点
- **版本锚点**：Spring 文档
