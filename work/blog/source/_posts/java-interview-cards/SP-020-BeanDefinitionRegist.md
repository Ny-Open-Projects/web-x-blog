---
title: "[SP-020] 扩展点·BeanDefinitionRegistryPostProcessor（BDRPP）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 扩展点 · BeanDefinitionRegistryPostProcessor（BDRPP）

- **事实**：BeanDefinitionRegistryPostProcessor 在普通 BFPP 之前执行可动态注册 BeanDefinition
- **原理**：MyBatis @MapperScan 动态注册 Mapper BeanDefinition 就是该扩展点（MapperScannerRegistrar→BDRPP），比静态 @Bean 更早介入
- **常见误区**：
  1. 它比普通 BFPP 执行更晚（错）
  2. 它不能注册新 BeanDefinition（错）
  3. @MapperScan 用 BeanPostProcessor 实现（错）
- **工程用法**：动态注册 Bean 的标准扩展点
- **版本锚点**：Spring 源码
