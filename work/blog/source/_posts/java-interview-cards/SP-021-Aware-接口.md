---
title: "[SP-021] 扩展点·Aware 接口（Aware）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 扩展点 · Aware 接口（Aware）

- **事实**：Aware 回调顺序：BeanNameAware、BeanFactoryAware 在初始化前，ApplicationContextAware 由 ApplicationContextAwareProcessor 处理
- **原理**：Aware 是容器向 Bean 注入基础设施引用的通道，不同 Aware 由不同组件调用时机略异
- **常见误区**：
  1. 所有 Aware 同时回调（错）
  2. ApplicationContextAware 最先回调（错）
  3. Aware 回调可以手动触发（错）
- **工程用法**：需要容器能力时实现对应 Aware
- **版本锚点**：Spring 源码
