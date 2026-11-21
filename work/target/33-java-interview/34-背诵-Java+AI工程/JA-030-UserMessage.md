---
title: "[JA-030] LangChain4j·@UserMessage（注解）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · @UserMessage（注解）

- **事实**：@SystemMessage 与 @UserMessage 注解在接口方法上定义提示词模板，参数经占位符注入
- **原理**：模板与 Java 代码同文件管理，{{it}} 注入单参数，多参数按名绑定
- **常见误区**：
  1. 注解只能标在类上（错）
  2. 占位符语法是 {0} 下标式（错）
  3. 提示词无法复用资源文件（错）
- **工程用法**：声明式提示词管理
- **版本锚点**：LangChain4j 1.0
