---
title: "[JA-136] LangChain4j·core 分工（模块）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · core 分工（模块）

- **事实**：LangChain4j 构件分工：langchain4j-core 是抽象层，langchain4j 主构件含 AiServices 等实现
- **原理**：依赖治理需分清（只换 provider 引 provider 模块即可），与 BOM 知识（JA-106）联动
- **常见误区**：
  1. core 与主构件是同一个（错）
  2. 只引 core 就有 AiServices（错）
  3. 模块划分不存在（错）
- **工程用法**：依赖治理
- **版本锚点**：LangChain4j 1.0
