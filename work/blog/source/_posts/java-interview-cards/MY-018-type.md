---
title: "[MY-018] explain·type（type）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## explain · type（type）

- **事实**：explain type 等级：const>eq_ref>ref>range>index>ALL
- **原理**：const 主键/唯一等值、eq_ref join 主键、ref 普通索引等值、range 范围、index 全索引扫、ALL 全表扫，线上要求至少 range
- **常见误区**：
  1. ALL 比index 快（错）
  2. type 是扫描行数指标（错）
  3. const 表示常量查询不扫索引（错）
- **工程用法**：explain 解读第一指标
- **版本锚点**：MySQL 文档
