---
title: "[JB-086] 包装类·Boolean与Byte（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 包装类 · Boolean与Byte（语法语义）

- **事实**：Boolean 缓存仅 true/false 两个实例；Byte 因范围小（-128~127）全部缓存。
- **原理**：小范围类型的所有值都值得缓存。
- **常见误区**：
  1. Byte 只有部分值被缓存。（错）
  2. Boolean 有四个缓存实例。（错）
  3. Boolean.valueOf 与 Boolean.parseBoolean 返回相同类型但用途不同（包装类 vs 基本类型）。（错）
- **工程用法**：Boolean.valueOf 返回包装类，parseBoolean 返回基本类型。
- **版本锚点**：JLS 5.1.7
