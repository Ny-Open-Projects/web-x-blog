---
title: "[JA-039] 选型·Spring AI vs LC4j（对比）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 选型 · Spring AI vs LC4j（对比）

- **事实**：框架选型核心差异：Spring AI 深度集成 Spring 生态（advisor/observation/自动配置），LangChain4j 胜在 provider 广度与轻量
- **原理**：团队能力与现有栈决定：Spring 项目优先 Spring AI，非 Spring 或需多 provider 快换可 LC4j，两者思想同构（模型抽象+RAG 组件+工具）
- **常见误区**：
  1. 两者 API 完全相同（错）
  2. 只能二选一不能共存（错）
  3. 选型只看 GitHub star 数（错）
- **工程用法**：框架选型论证
- **版本锚点**：2025
