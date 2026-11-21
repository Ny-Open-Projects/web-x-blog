---
title: [AIC-212] 前后端混合仓库里，AI 有时把前端模式套到后端代码上，怎么用规则隔离开？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-212：前后端混合仓库里，AI 有时把前端模式套到后端代码上，怎么用规则隔离开？
**答**：
- 用 glob 精确圈定规则生效路径：server/** 只注入后端规则，src/** 只注入前端规则。
- 规则开头声明身份：「本规则适用于 Node.js BFF 层」，给模型一个自检锚点。
- 跨层文件（如共享类型）单独建规则，明确双端约定。
- 把「先识别当前代码层再写代码」写进 always 层规则。

```javascript
# server-rules.mdc
# globs: ["server/**/*.ts", "packages/shared/**/*.ts"]
# ---
# 你在 Node.js BFF 层工作。
# - 不要引入 React/Vue 等前端依赖；错误处理用统一 Result 类型
# - DAO 只在 server/dal 中定义，禁止在 route handler 内直接写 SQL
r
```
