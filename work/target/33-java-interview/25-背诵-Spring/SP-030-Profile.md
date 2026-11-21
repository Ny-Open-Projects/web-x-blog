---
title: "[SP-030] Boot·@Profile（环境）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · @Profile（环境）

- **事实**：@Profile 按激活的 profile 决定 Bean 是否装配
- **原理**：@SpringBootTest 可设 profile，dev/test/prod 隔离数据源与中间件地址，spring.profiles.active 指定
- **常见误区**：
  1. @Profile 是运行时动态切换（错）
  2. 多个 profile 不能同时激活（错）
  3. @Profile 与 @Conditional 无关（错）
- **工程用法**：环境隔离标准方案
- **版本锚点**：Boot 文档
