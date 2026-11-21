---
title: "[JA-050] LangChain4j·POJO 返回（结构化）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · POJO 返回（结构化）

- **事实**：LangChain4j 的 AiServices 接口方法可直接声明 POJO 返回类型，框架自动做结构化输出
- **原理**：接口即契约：返回 String/POJO/TokenStream 由签名决定，结构化输出框架内部处理，与 Spring AI 的 entity() 同思想
- **常见误区**：
  1. POJO 返回需要手动 JSON 解析（错）
  2. 只支持 String 返回（错）
  3. 结构化输出是付费功能（错）
- **工程用法**：声明式结构化
- **版本锚点**：LangChain4j 1.0
