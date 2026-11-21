---
title: "[JB-020] equals体系·instanceof陷阱（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## equals体系 · instanceof陷阱（语法语义）

- **事实**：equals 中使用 instanceof 会破坏传递性：子类与父类互比可能不对称。
- **原理**：《Effective Java》推荐 getClass 精确比较或把类设计为 final。
- **常见误区**：
  1. instanceof 是 equals 的标准写法。（错）
  2. instanceof 不会造成对称性问题。（错）
  3. 传递性违反不影响集合行为。（错）
- **工程用法**：P10 层会追问 getClass 与 instanceof 的取舍条件。
- **版本锚点**：JLS 15.20.2
