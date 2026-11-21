---
title: "[SP-015] IoC·getObject（FactoryBean）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · getObject（FactoryBean）

- **事实**：FactoryBean 是生产 Bean 的工厂，getBean(名) 拿到 getObject 的产物
- **原理**：取 FactoryBean 本身要在名字前加 &（getBean("&xxx")），MyBatis Mapper、Spring AOP 代理、Feign 客户端都由 FactoryBean 产出
- **常见误区**：
  1. FactoryBean 与 BeanFactory 是一回事（错）
  2. getBean 直接返回 FactoryBean 实例（错）
  3. & 前缀是可选语法（错）
- **工程用法**：MyBatis MapperProxy 的注册原理
- **版本锚点**：Spring 文档
