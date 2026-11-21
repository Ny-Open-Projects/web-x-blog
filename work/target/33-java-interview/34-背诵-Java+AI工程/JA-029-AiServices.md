---
title: "[JA-029] LangChain4j·AiServices（AiServices）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · AiServices（AiServices）

- **事实**：LangChain4j 声明式 AI 服务：AiServices.builder(接口.class).chatLanguageModel(model).build() 生成动态代理
- **原理**：接口方法即 AI 调用（注解定义提示词），返回类型决定结构化输出行为，是 LC4j 的招牌设计
- **常见误区**：
  1. AiServices 需要继承抽象类（错）
  2. 生成的代理不能返回 POJO（错）
  3. 与动态代理无关（错）
- **工程用法**：声明式 AI 服务落地
- **版本锚点**：LangChain4j 1.0
