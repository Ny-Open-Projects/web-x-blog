---
title: "[JB-070] Object·clone陷阱（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Object · clone陷阱（语法语义）

- **事实**：Object.clone 是浅拷贝（引用字段复制引用），深拷贝需重写 clone 递归复制或改用拷贝构造器/序列化。
- **原理**：Cloneable 是空标记接口且 clone 语义脆弱，Effective Java 建议用拷贝构造器替代。
- **常见误区**：
  1. Object.clone 默认就是深拷贝。（错）
  2. 实现 Cloneable 接口后 clone 会自动变深拷贝。（错）
  3. 拷贝构造器比 clone 更脆弱。（错）
- **工程用法**：防御性拷贝优先用拷贝构造器，避免暴露可变内部状态。
- **版本锚点**：Object.clone javadoc / Effective Java
