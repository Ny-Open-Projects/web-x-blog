---
title: "[JA-038] LangChain4j·starter（Spring）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · starter（Spring）

- **事实**：LangChain4j 提供 Spring Boot starter（如 langchain4j-open-ai-spring-boot-starter）自动装配 ChatLanguageModel bean
- **原理**：Spring 项目里与 Spring AI 类似的体验（配置属性+自动装配），选择框架看生态契合而非能力缺失
- **常见误区**：
  1. LC4j 无法在 Spring 中使用（错）
  2. starter 会引入 Spring AI（错）
  3. 自动装配需手动 new bean（错）
- **工程用法**：Spring 集成路线
- **版本锚点**：LangChain4j 1.0
