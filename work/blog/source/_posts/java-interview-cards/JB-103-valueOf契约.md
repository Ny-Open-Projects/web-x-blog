---
title: "[JB-103] 包装类·valueOf契约（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 包装类 · valueOf契约（语法语义）

- **事实**：Integer.valueOf(int) 对缓存范围返回缓存实例，new Integer(int) 总是新建对象（JDK9 起构造器废弃）。
- **原理**：官方文档明确推荐 valueOf 优先。
- **常见误区**：
  1. new Integer 与 valueOf 语义完全等价且性能相同。（错）
  2. valueOf 对大数值也返回缓存。（错）
  3. new Integer 在 JDK21 仍是推荐写法。（错）
- **工程用法**：JDK9+ @Deprecated(since=9, forRemoval=true)。
- **版本锚点**：JDK9+
