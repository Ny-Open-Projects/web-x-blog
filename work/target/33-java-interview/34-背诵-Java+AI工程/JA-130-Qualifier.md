---
title: "[JA-130] Spring AI·Qualifier（多模型）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · Qualifier（多模型）

- **事实**：classpath 有多个 ChatModel bean 时按 bean 名/@Qualifier 指定注入
- **原理**：多 provider 共存场景（主备/分级），builder 显式指定模型 bean，与 JA-047 属性声明配合
- **常见误区**：
  1. 多模型 bean 自动随机注入（错）
  2. Qualifier 是可选装饰（错）
  3. 多 bean 会导致启动失败必然（错）
- **工程用法**：主备模型装配
- **版本锚点**：Spring AI 1.0 GA
