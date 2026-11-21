---
title: "[SP-004] AOP·wrapIfNecessary（时机）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## AOP · wrapIfNecessary（时机）

- **事实**：AOP 代理在 BeanPostProcessor 的 postProcessAfterInitialization 中创建
- **原理**：AbstractAutoProxyCreator.wrapIfNecessary 在 After 阶段判断切点匹配生成代理（本项目源码级核对结论），代理创建晚于 init 回调
- **常见误区**：
  1. AOP 代理在 postProcessBeforeInitialization 创建（错）
  2. 代理在实例化阶段创建（错）
  3. 代理在属性填充阶段创建（错）
- **工程用法**：回答"AOP 代理何时创建"的精确版本
- **版本锚点**：AbstractAutoProxyCreator
