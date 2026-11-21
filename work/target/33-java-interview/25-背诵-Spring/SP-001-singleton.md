---
title: "[SP-001] IoC·singleton（作用域）"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## IoC · singleton（作用域）

- **事实**：Spring Bean 默认作用域是 singleton 单例容器内唯一
- **原理**：单例减少对象创建开销，Spring 单例是容器级唯一而非 JVM 级唯一（多个容器各有一份）
- **常见误区**：
  1. Spring 单例是 JVM 全局唯一（错）
  2. 默认作用域是 prototype（错）
  3. singleton 与 GoF 单例模式相同（错）
- **工程用法**：回答作用域题先说默认值
- **版本锚点**：Spring 文档
