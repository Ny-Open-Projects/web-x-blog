---
title: "[SP-007] 循环依赖·singletonObjects（三级缓存）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 循环依赖 · singletonObjects（三级缓存）

- **事实**：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂
- **原理**：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory
- **常见误区**：
  1. 三级缓存都是存 Bean 实例的（错）
  2. 三级缓存顺序是工厂、早期、成品（错）
  3. 一级缓存存 ObjectFactory（错）
- **工程用法**：背三级缓存必背各级名称与职责
- **版本锚点**：Spring 源码
