---
title: "[SP-076] MyBatis·@MapperScan（集成）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## MyBatis · @MapperScan（集成）

- **事实**：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean
- **原理**：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理
- **常见误区**：
  1. Mapper 接口由 JDK 反射直接调用（错）
  2. @MapperScan 是 BeanPostProcessor 实现（错）
  3. Mapper 接口需要写实现类（错）
- **工程用法**：框架集成扩展点实战案例
- **版本锚点**：MyBatis-Spring
