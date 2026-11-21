---
title: "[SP-031] Boot·@Conditional（条件装配）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Boot · @Conditional（条件装配）

- **事实**：@Conditional 族按条件决定 Bean 是否注册（OnClass/OnMissingBean/OnProperty 等）
- **原理**：Spring Boot 自动配置的全部开关逻辑基于条件装配，@ConditionalOnMissingBean 让用户定义优先于默认配置
- **常见误区**：
  1. @Conditional 在 Bean 创建后求值（错）
  2. 条件注解可以加在方法体内部（错）
  3. OnMissingBean 与加载顺序无关（错）
- **工程用法**：自定义 starter 的核心机制
- **版本锚点**：Boot 文档
