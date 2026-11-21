---
title: "[SP-025] IoC·@Resource（注入）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · @Resource（注入）

- **事实**：@Resource 是 JSR-250 标准默认按名称注入
- **原理**：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同
- **常见误区**：
  1. @Resource 默认按类型注入（错）
  2. @Resource 是 Spring 的注解（错）
  3. 两者行为完全一致（错）
- **工程用法**：JDK17+ 移除 javax.annotation 后 Boot 3 需显式依赖 jakarta.annotation
- **版本锚点**：JSR-250
