---
title: "[MY-090] 实践·flush（抖动）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 实践 · flush（抖动）

- **事实**：性能周期性抖动常见根因：脏页比例接近阈值触发激进刷盘（连击）
- **原理**：innodb_max_dirty_pages_pct 触控刷脏、redo 快满强制 checkpoint，抖动时刻看脏页比例与 checkpoint age，容量规划 SSD 减轻
- **常见误区**：
  1. 抖动一定是 CPU 不足（错）
  2. 刷脏只在凌晨执行（错）
  3. 抖动与 buffer pool 无关（错）
- **工程用法**：线上性能抖动诊断
- **版本锚点**：实战共识
