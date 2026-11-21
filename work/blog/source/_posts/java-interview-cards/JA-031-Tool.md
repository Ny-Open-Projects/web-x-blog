---
title: "[JA-031] LangChain4j·@Tool（工具）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · @Tool（工具）

- **事实**：LangChain4j 的 @Tool 注解声明工具方法，AiServices.tools(obj) 挂载后模型可调用
- **原理**：框架把方法反射为 ToolSpecification（名称/描述/schema）传给模型，模型回填参数后本地执行
- **常见误区**：
  1. LC4j 工具要手动拼 JSON（错）
  2. @Tool 方法不能重载（错）
  3. 工具在模型服务端执行（错）
- **工程用法**：Agent 工具接入（与 Spring AI 的 @Tool 同思想）
- **版本锚点**：LangChain4j 1.0
