---
title: "[JV-078] 类加载·ClassLoader（隔离）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 类加载 · ClassLoader（隔离）

- **事实**：不同 ClassLoader 加载的同名类是不同的类（隔离）
- **原理**：instanceof 会失败、静态变量不共享，Tomcat 应用隔离、热部署框架（Arthas redefine）都依赖此语义
- **常见误区**：
  1. 同名类加载后全局唯一（错）
  2. 不同 ClassLoader 的类可以互相赋值（错）
  3. 类隔离与安全无关（错）
- **工程用法**：理解 Arthas 与热部署的原理
- **版本锚点**：JVM 规范
