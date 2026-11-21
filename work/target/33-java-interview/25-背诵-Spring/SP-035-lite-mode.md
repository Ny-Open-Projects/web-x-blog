---
title: "[SP-035] 配置类·lite mode（proxyBeanMethods）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 配置类 · lite mode（proxyBeanMethods）

- **事实**：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理
- **原理**：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）
- **常见误区**：
  1. lite 模式下 @Bean 互调仍返回单例（错）
  2. proxyBeanMethods 默认是 false（错）
  3. @Bean 互调与代理无关（错）
- **工程用法**：性能敏感的启动优化点
- **版本锚点**：Boot 文档
