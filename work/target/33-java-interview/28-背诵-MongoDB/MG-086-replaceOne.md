---
title: "[MG-086] 写入·replaceOne（语义）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 写入 · replaceOne（语义）

- **事实**：replaceOne 整文档替换（丢失未提供字段）与 updateOne $set 局部更新是两种语义
- **原理**：replaceOne 用于全量覆写（文档由调用方完整构造），updateOne+$set 局部修改并发安全更好，误用 replaceOne 是字段丢失事故源
- **常见误区**：
  1. replaceOne 与 updateOne 等价（错）
  2. replaceOne 保留未提供字段（错）
  3. updateOne 不能加 upsert（可加 upsert:true）（错）
- **工程用法**：写入 API 选型与事故预防
- **版本锚点**：实战共识
