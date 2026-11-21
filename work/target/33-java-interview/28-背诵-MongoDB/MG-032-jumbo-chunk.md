---
title: "[MG-032] 分片·jumbo chunk（问题）"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 分片 · jumbo chunk（问题）

- **事实**：jumbo chunk：同一分片键值海量子文档导致超阈值不可分割
- **原理**：需手动拆分（细化分片键）或调整，是分片键基数不足的后果，预防靠高基数分片键
- **常见误区**：
  1. jumbo chunk 自动处理（错）
  2. jumbo chunk 影响读不影响写（错）
  3. 出现后只能删数据（错）
- **工程用法**：分片键设计失误的补救
- **版本锚点**：实战共识
