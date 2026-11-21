---
title: "[JA-089] LangChain4j·ToolExecutor（工具）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## LangChain4j · ToolExecutor（工具）

- **事实**：LC4j 的工具执行可经 ToolExecutor 接口自定义（默认反射调用 @Tool 方法）
- **原理**：需要异步执行/权限校验/审计时替换默认执行器，工具链路可插拔，与 JA-031 联动
- **常见误区**：
  1. 工具执行器固定不可换（错）
  2. 自定义执行器绕过框架（错）
  3. ToolExecutor 是模型端接口（错）
- **工程用法**：工具链路定制
- **版本锚点**：LangChain4j 1.0
