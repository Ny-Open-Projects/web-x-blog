---
title: "[MY-072] 类型·datetime（时间）"
date: 2026-11-18
categories: [Java面试, MySQL]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 类型 · datetime（时间）

- **事实**：时间类型选型：datetime（8 字节与时区无关）vs timestamp（4 字节 2038 上限随时区转换）
- **原理**：timestamp 优势省空间与自动时区转换，跨时区系统用 UTC+timestamp 或统一 datetime+应用层时区，bigint 存毫秒是互联网常见做法
- **常见误区**：
  1. timestamp 没有 2038 问题（错）
  2. datetime 能存时区信息（错）
  3. timestamp 精度只有秒（8.0.19+ 支持到微秒）（错）
- **工程用法**：建表规范的知识点
- **版本锚点**：实战共识
