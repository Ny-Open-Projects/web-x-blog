---
title: "[SP-013] IoC·prototype 注入（误用）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · prototype 注入（误用）

- **事实**：singleton 中注入 prototype Bean 只注入一次失去多例语义
- **原理**：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取
- **常见误区**：
  1. Spring 会自动按需创建新 prototype（错）
  2. 注入后每次调用返回新实例（错）
  3. 加 @Lazy 后每次都是新实例（错）
- **工程用法**：每次需要新实例用 ObjectProvider.getBean
- **版本锚点**：经典陷阱
