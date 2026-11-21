---
title: "[SP-097] IoC·@DependsOn（顺序）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · @DependsOn（顺序）

- **事实**：@DependsOn 显式声明初始化依赖顺序
- **原理**：初始化缓存 Bean 与使用 Bean 的关系、静态资源准备，比 @Order 强（保证创建完成顺序）
- **常见误区**：
  1. @DependsOn 与 @Order 等价（错）
  2. 它只影响注入不影响初始化（错）
  3. 不需要它 Spring 会自动分析依赖（错）
- **工程用法**：显式依赖的标准工具
- **版本锚点**：Spring 文档
