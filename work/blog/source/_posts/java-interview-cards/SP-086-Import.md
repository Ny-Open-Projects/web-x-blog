---
title: "[SP-086] 容器·Import（扩展）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 容器 · Import（扩展）

- **事实**：@Import 三种用法：普通类、ImportSelector、ImportBeanDefinitionRegistrar
- **原理**：Selector 按条件批量导入（@EnableAutoConfiguration 原理），Registrar 完全自定义注册（@MapperScan 原理），是框架级扩展的入口
- **常见误区**：
  1. @Import 只能导入配置类（错）
  2. 三种用法行为相同（错）
  3. @Import 会覆盖已有 Bean（错）
- **工程用法**：读框架源码的钥匙
- **版本锚点**：Spring 文档
