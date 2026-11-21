---
title: "[JB-074] 语言杂项·字符串switch（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 语言杂项 · 字符串switch（语法语义）

- **事实**：switch 对 String 从 JDK7 起支持，底层编译为 hashCode 分两次跳转（先 hash 后 equals 防冲突）。
- **原理**：String 的 switch 不是语法糖直接变 if-else，而是 hash 跳转+equals 校验。
- **常见误区**：
  1. String 的 switch 从 Java 5 就支持。（错）
  2. String 的 switch 只依赖 equals 不依赖 hashCode。（错）
  3. String switch 的性能与 if-else 链完全相同。（错）
- **工程用法**：hashCode 相同的字符串会走 equals 校验分支。
- **版本锚点**：JDK7+
