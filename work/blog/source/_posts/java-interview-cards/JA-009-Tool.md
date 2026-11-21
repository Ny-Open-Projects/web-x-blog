---
title: "[JA-009] Spring AI·@Tool（工具）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · @Tool（工具）

- **事实**：Spring AI 用 @Tool 注解声明工具方法，框架自动包装为 ToolCallback
- **原理**：模型通过 function calling 输出工具调用，框架执行方法并回填结果，业务只写普通 Java 方法
- **常见误区**：
  1. 工具方法必须实现特定接口（错）
  2. @Tool 方法不能有参数（错）
  3. 工具执行在模型侧进行（错）
- **工程用法**：让模型操作业务能力（查订单/发通知）
- **版本锚点**：Spring AI 1.0 GA
