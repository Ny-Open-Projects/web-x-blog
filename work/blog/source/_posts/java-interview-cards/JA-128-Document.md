---
title: "[JA-128] Spring AI·Document（文档）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · Document（文档）

- **事实**：Spring AI 的 Document 聚合 id/text/metadata 三元组，入库与检索的基本单位
- **原理**：元数据承载来源/权限/类目（AI-061 联动），检索过滤与溯源都靠它
- **常见误区**：
  1. Document 只有正文（错）
  2. metadata 是可选装饰（错）
  3. id 自动生成无法指定（错）
- **工程用法**：RAG 数据结构
- **版本锚点**：Spring AI 1.0 GA
