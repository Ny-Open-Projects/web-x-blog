---
title: "[JA-069] Spring AI·ToolContext（工具）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · ToolContext（工具）

- **事实**：@Tool 方法可注入 ToolContext 参数携带调用上下文（如用户身份），上下文不进模型 schema
- **原理**：业务上下文随工具执行传递，模型只看到工具的业务参数，安全与审计的隔离层
- **常见误区**：
  1. ToolContext 会暴露给模型（错）
  2. 上下文必须写进提示词（错）
  3. 工具方法不能有第二参数（错）
- **工程用法**：工具侧租户隔离
- **版本锚点**：Spring AI 1.0 GA
