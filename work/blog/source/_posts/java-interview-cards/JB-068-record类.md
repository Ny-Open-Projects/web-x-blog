---
title: "[JB-068] 语言杂项·record类（版本）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 语言杂项 · record类（版本）

- **事实**：JDK16 转正 record 类：不可变数据载体，自动生成构造器/访问器/equals/hashCode/toString。
- **原理**：record 明确表达"这是纯数据"，字段 final、不能继承其他类（可实现接口）。
- **常见误区**：
  1. record 可以有可变字段。（错）
  2. record 可以继承其他类。（错）
  3. record 需要手写 equals 和 hashCode。（错）
- **工程用法**：DTO/值对象/配置项是 record 的标准使用场景。
- **版本锚点**：JDK16+
