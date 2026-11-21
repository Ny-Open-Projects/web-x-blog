---
title: "[SP-024] IoC·@Autowired（注入）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · @Autowired（注入）

- **事实**：@Autowired 按 byType 注入多个候选时需 @Primary 或 @Qualifier 消歧
- **原理**：按类型找到多个候选先看 @Primary 再按字段名匹配，都不确定抛 NoUniqueBeanDefinitionException
- **常见误区**：
  1. @Autowired 默认按名称注入（错）
  2. @Autowired 找不到直接跳过（错）
  3. @Qualifier 按类型过滤（它按名称限定）（错）
- **工程用法**：多实现接口注入的标准解法
- **版本锚点**：Spring 文档
