---
title: "[JA-053] Agent·Agent 三件（衔接）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Agent · Agent 三件（衔接）

- **事实**：Java 框架的 Agent 基础件：模型调用（ChatClient/ChatLanguageModel）+ 工具（@Tool）+ 循环（框架自动执行工具直到完成）
- **原理**：Spring AI 与 LC4j 都内置工具执行循环，简单 Agent 框架直接写，复杂规划/多 Agent 用 LangGraph 类编排（AI-015 联动）
- **常见误区**：
  1. Java 框架不能做 Agent（错）
  2. Agent 循环由业务手写（错）
  3. 工具执行后流程终止（错）
- **工程用法**：Java Agent 起步认知
- **版本锚点**：2025
