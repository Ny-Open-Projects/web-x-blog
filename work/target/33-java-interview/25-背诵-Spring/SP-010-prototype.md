---
title: "[SP-010] 循环依赖·prototype（限制）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 循环依赖 · prototype（限制）

- **事实**：prototype 作用域的循环依赖无法解决
- **原理**：prototype 每次获取都新建，没有缓存可提前曝光，Spring 启动或首次获取时报 BeanCurrentlyInCreationException
- **常见误区**：
  1. prototype 循环依赖也能三级缓存解决（错）
  2. 只有 singleton 才会循环依赖报错（错）
  3. prototype 报错发生在启动阶段（错）
- **工程用法**：有状态对象用 prototype 时避免环
- **版本锚点**：Spring 文档
