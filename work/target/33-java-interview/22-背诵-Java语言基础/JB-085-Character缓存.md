---
title: "[JB-085] 包装类·Character缓存（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 包装类 · Character缓存（语法语义）

- **事实**：Character 缓存范围是 0~127（与 Integer 的 -128~127 不同），valueOf 在此范围返回缓存实例。
- **原理**：Character 无负值语义，缓存从 0 开始。
- **常见误区**：
  1. Character 缓存与 Integer 完全相同是 -128~127。（错）
  2. Character 没有缓存机制。（错）
  3. Character 缓存覆盖所有 ASCII 字符。（错）
- **工程用法**：ASCII 128~255 的 Character 不在缓存内。
- **版本锚点**：JLS 5.1.7（0~127）
