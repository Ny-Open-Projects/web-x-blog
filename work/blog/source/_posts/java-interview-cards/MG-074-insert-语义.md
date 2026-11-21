---
title: "[MG-074] 写入·insert 语义（语义）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 写入 · insert 语义（语义）

- **事实**：insert 重复 _id 报错（E11000）、upsert 存在更新不存在插入、update 语义细分
- **原理**：upsert 是 CDC 幂等写基础（by _id），update one/many 区分（漏 many 是事故源），bulkWrite 组合原子批
- **常见误区**：
  1. upsert 会插入两条（错）
  2. update 默认更新所有文档（默认 one）（错）
  3. _id 重复自动覆盖（错）
- **工程用法**：写入 API 语义
- **版本锚点**：官方文档
