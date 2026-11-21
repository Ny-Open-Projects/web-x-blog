---
title: "[RD-005] Hash·listpack（编码）"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Hash · listpack（编码）

- **事实**：Hash 小数据用 listpack（7.0 前是 ziplist）大数据转 hashtable
- **原理**：小 hash 紧凑存储省内存（无指针开销），超过阈值（64 字节/128 项默认）转标准 hashtable
- **常见误区**：
  1. Hash 一直是 hashtable（错）
  2. listpack 转 hashtable 后可逆（错）
  3. 阈值不可配置（错）
- **工程用法**：对象缓存的内存优化原理
- **版本锚点**：Redis 7.0
