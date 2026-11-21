---
title: "[JA-016] Spring AI·ChatOptions（选项）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · ChatOptions（选项）

- **事实**：运行时覆盖模型参数：.options(OpenAiChatOptions.builder().temperature(0.2).model(...).build())
- **原理**：默认选项来自配置文件，每次调用可用 options 局部覆盖（温度/模型/maxTokens），精细控制不同业务的生成行为
- **常见误区**：
  1. options 会修改全局默认配置（错）
  2. temperature 只能配置文件设（错）
  3. 每次调用无法换模型（错）
- **工程用法**：分级路由与参数微调
- **版本锚点**：Spring AI 1.0 GA
