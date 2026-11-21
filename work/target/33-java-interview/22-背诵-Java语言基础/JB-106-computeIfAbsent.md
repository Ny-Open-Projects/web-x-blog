---
title: "[JB-106] CHM·computeIfAbsent（语法语义）"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## CHM · computeIfAbsent（语法语义）

- **事实**：computeIfAbsent(key, k->新值) 原子地"不存在则计算并放入"，是并发缓存的标准实现。
- **原理**：check-then-act 两步在并发下有竞态窗口。
- **常见误区**：
  1. computeIfAbsent 与 get 后 put 等价。（错）
  2. computeIfAbsent 的映射函数可以返回 null 且会存入 null。（错）
  3. computeIfAbsent 在 JDK7 就存在。（错）
- **工程用法**：映射函数返回 null 则不建立映射；函数内再操作同 map 有递归更新风险（JDK9 文档明确）。
- **版本锚点**：JDK 8+
