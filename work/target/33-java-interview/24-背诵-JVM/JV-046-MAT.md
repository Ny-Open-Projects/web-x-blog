---
title: "[JV-046] OOM·MAT（分析）"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## OOM · MAT（分析）

- **事实**：MAT 用支配树与泄漏报告定位大内存对象
- **原理**：Leak Suspects 自动给嫌疑人，支配树看"谁抓住对象不放"，配合 GC Roots 路径定位泄漏源头
- **常见误区**：
  1. MAT 会自动修复内存泄漏（错）
  2. MAT 只能看字符串与数字（错）
  3. dump 文件大小等于堆大小的一半（错）
- **工程用法**：dump 分析（MAT/JProfiler）是 OOM 定案工具
- **版本锚点**：实战共识
