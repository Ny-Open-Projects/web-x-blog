---
title: "[JB-044] TreeMap·与HashMap选型（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## TreeMap · 与HashMap选型（语法语义）

- **事实**：TreeMap 换来有序性但牺牲 O(1) 访问与无序性约束（key 必须可比较）。
- **原理**：HashMap O(1) 但无序；按需求选型是集合面试的核心判断。
- **常见误区**：
  1. TreeMap 在任何场景都优于 HashMap。（错）
  2. TreeMap 的 get 是 O(1)。（错）
  3. TreeMap 允许 null 键。（错）
- **工程用法**：范围查询 headMap/tailMap/subMap 是 TreeMap 独有能力。
- **版本锚点**：集合选型通用
