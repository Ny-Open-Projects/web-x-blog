---
title: "[SP-036] 配置类·@Bean 互调（陷阱）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 配置类 · @Bean 互调（陷阱）

- **事实**：full 模式下 @Configuration 类内 @Bean 方法互调被 CGLIB 拦截返回同一单例
- **原理**：配置类被 CGLIB 子类化拦截方法调用，保证语义等价于容器查找，这就是 proxyBeanMethods 区分 full/lite 的原因
- **常见误区**：
  1. @Bean 方法互调会创建两个实例（错）
  2. 配置类不用 CGLIB 增强（错）
  3. lite 与 full 模式行为相同（错）
- **工程用法**：理解配置类原理的经典题
- **版本锚点**：Spring 源码
