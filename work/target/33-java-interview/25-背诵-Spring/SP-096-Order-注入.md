---
title: "[SP-096] IoC·@Order 注入（顺序）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · @Order 注入（顺序）

- **事实**：@Order 控制 Bean 初始化顺序与集合注入顺序（数字小先）
- **原理**：依赖关系应靠 @DependsOn 或显式注入表达而非顺序猜测，@Order 是提示不是保证
- **常见误区**：
  1. @Order 保证 Bean 完全初始化顺序（错）
  2. @Order 数字大先执行（错）
  3. @Order 只对 @Bean 方法生效（错）
- **工程用法**：顺序敏感场景用 @DependsOn 显式声明
- **版本锚点**：Spring 文档
