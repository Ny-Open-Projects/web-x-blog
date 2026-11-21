---
title: "[AI-079] 成本·prompt caching（缓存）"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 成本 · prompt caching（缓存）

- **事实**：供应商 prompt caching：相同前缀（system prompt/few-shot）命中缓存按折扣计费
- **原理**：system prompt 与 few-shot 每次请求重复且最长，前缀缓存命中可省 50-90% 输入费用，要求前缀稳定（动态内容放后缀）
- **常见误区**：
  1. 缓存命中自动发生无需设计（前缀稳定性要设计）（错）
  2. prompt caching 存储我的数据（是临时会话缓存）（错）
  3. 缓存降低输出成本（只影响输入计费）（错）
- **工程用法**：成本优化（AI-026 四招之一）
- **版本锚点**：2024-2025
