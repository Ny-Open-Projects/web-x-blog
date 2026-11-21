---
title: "[JB-019] equals体系·可变key（误用）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## equals体系 · 可变key（误用）

- **事实**：把可变字段参与 hashCode 计算的对象放入 HashMap 后修改字段，会导致 key"丢失"（get 返回 null 且无法 remove）。
- **原理**：hash 已按旧字段计算定桶，字段变化后再 get 用新 hash 定位到不同的桶。
- **常见误区**：
  1. 修改对象字段后 HashMap 会自动重新计算它的位置。（错）
  2. key 丢失后调用 remove 可以删除旧条目。（错）
  3. 可变对象做 key 是官方推荐。（错）
- **工程用法**：value 泄漏 + 业务读不到数据，是真实事故类型。
- **版本锚点**：HashMap 源码语义
