---
title: "[JA-189] LangChain4j·token 粒度（切分）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · token 粒度（切分）

- **事实**：DocumentSplitters.recursive(size, overlap, tokenizer) 支持 token 粒度切分（配 Tokenizer）
- **原理**：与 Spring AI TokenTextSplitter 对等（JA-068），token 切分对齐上下文计量，中英混排按 tokenizer 差异处理
- **常见误区**：
  1. 切分只有字符粒度（错）
  2. 重叠必须为零（错）
  3. tokenizer 是可选装饰（错）
- **工程用法**：RAG 切分对等
- **版本锚点**：LangChain4j 1.0
