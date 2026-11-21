---
title: "[AD-359] 工具·fallback（降级）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 工具 · fallback（降级）

- **事实**：工具 fallback 实现：主工具失败自动切备工具（同语义工具），fallback 链配置化，降级事件记录
- **原理**：工具级降级（模型降级 JA-323 的工具版），同语义工具注册为 fallback 链，与降级知识联动
- **常见误区**：
  1. 工具失败无 fallback（错）
  2. 降级硬编码（错）
  3. 降级事件不记录（错）
- **工程用法**：工具 fallback
- **版本锚点**：实战共识
