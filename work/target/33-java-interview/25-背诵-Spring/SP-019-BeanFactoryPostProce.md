---
title: "[SP-019] 扩展点·BeanFactoryPostProcessor（BFPP）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 扩展点 · BeanFactoryPostProcessor（BFPP）

- **事实**：BeanFactoryPostProcessor 在 Bean 实例化前修改 BeanDefinition
- **原理**：作用于"配方"阶段（改定义），与 BeanPostProcessor（改实例）区分，属性占位符解析（PropertySourcesPlaceholderConfigurer）就是 BFPP
- **常见误区**：
  1. BFPP 在 Bean 创建后执行（错）
  2. BFPP 与 BPP 没有区别（错）
  3. BFPP 可以修改 Bean 实例属性（错）
- **工程用法**：配置占位符、动态注册 BeanDefinition 的入口
- **版本锚点**：Spring 源码
