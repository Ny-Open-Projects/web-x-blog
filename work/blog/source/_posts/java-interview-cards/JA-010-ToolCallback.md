---
title: "[JA-010] Spring AI·ToolCallback（工具）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · ToolCallback（工具）

- **事实**：ToolCallback 是 Spring AI 工具的底层抽象，@Tool 方法由框架包装成回调
- **原理**：链路：模型输出调用意图→ToolCallingManager 执行回调→结果回填下一轮请求，理解链路才能调试工具不触发问题
- **常见误区**：
  1. ToolCallback 由业务手动执行（错）
  2. 工具结果直接返回用户不回模型（错）
  3. 一个应用只能注册一个工具（错）
- **工程用法**：工具链路排障知识
- **版本锚点**：Spring AI 1.0 GA
