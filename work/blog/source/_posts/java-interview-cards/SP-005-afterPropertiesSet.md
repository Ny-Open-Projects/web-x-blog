---
title: "[SP-005] Bean 生命周期·afterPropertiesSet（顺序）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Bean 生命周期 · afterPropertiesSet（顺序）

- **事实**：初始化回调顺序：@PostConstruct、InitializingBean.afterPropertiesSet、init-method
- **原理**：注解最早（由 BPP 调用）、接口次之、XML/bean 方法最后，三者可同时存在按序执行
- **常见误区**：
  1. init-method 先于 afterPropertiesSet（错）
  2. @PostConstruct 在初始化之后执行（错）
  3. 三个回调互斥只能选一个（错）
- **工程用法**：初始化逻辑拆层时按此顺序安排
- **版本锚点**：Spring 文档
