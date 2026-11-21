---
title: "[SP-006] Bean 生命周期·@PostConstruct（注解）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Bean 生命周期 · @PostConstruct（注解）

- **事实**：@PostConstruct 方法由 CommonAnnotationBeanPostProcessor 在初始化阶段调用
- **原理**：JSR-250 注解，Spring 用 BPP 桥接实现，依赖注入完成后才执行
- **常见误区**：
  1. @PostConstruct 在依赖注入前执行（错）
  2. @PostConstruct 由反射直接调用与 BPP 无关（错）
  3. @PostConstruct 可以带参数（错）
- **工程用法**：初始化钩子首选注解方式
- **版本锚点**：JSR-250
