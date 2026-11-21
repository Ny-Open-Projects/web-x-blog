---
title: "[JA-014] Spring AI·DocumentReader（ETL）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · DocumentReader（ETL）

- **事实**：Spring AI 的 ETL 管道：DocumentReader 读→DocumentTransformer 切→DocumentWriter 存
- **原理**：TokenTextSplitter 把长文档切分为带元数据的 Document 列表，TikaDocumentReader 支持解析 PDF/Word 等格式
- **常见误区**：
  1. ETL 三步可以乱序（错）
  2. DocumentTransformer 负责写入向量库（错）
  3. Tika 是内置无需依赖（错）
- **工程用法**：知识入库管道
- **版本锚点**：Spring AI 1.0 GA
