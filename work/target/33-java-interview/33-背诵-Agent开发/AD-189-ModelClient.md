---
title: "[AD-189] 手写·ModelClient（抽象）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 手写 · ModelClient（抽象）

- **事实**：ModelClient 接口抽象：chat(messages, tools) → ModelResponse，实现类注入（真实/OpenAI/mock），面向接口则 mock 测试（AD-039）天然支持
- **原理**：接口抽象是可测试性的根（JA-041 落地），手写 Agent 也遵守（与生产框架同思想），接口窄化（只暴露需要的方法）
- **常见误区**：
  1. 手写版硬编码模型调用（错）
  2. 接口抽象是过度设计（错）
  3. mock 与手写无关（错）
- **工程用法**：抽象层设计
- **版本锚点**：实战共识
