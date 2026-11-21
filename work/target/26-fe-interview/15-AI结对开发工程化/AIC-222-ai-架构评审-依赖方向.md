---
title: [AIC-222] 用 AI 检查「分层架构的依赖方向违规」（如 UI 层直接引 DAO），提示词该怎么设计？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-222：用 AI 检查「分层架构的依赖方向违规」（如 UI 层直接引 DAO），提示词该怎么设计？
**答**：
- 先把分层规则形式化：给出每层允许 import 的层列表，让 AI 做匹配而非自由发挥。
- 要求输出结构化结果：文件、违规 import、所属层、规则依据、修复建议。
- 提供反例与边界说明（哪些 import 是允许的例外，如类型-only import）。
- 和静态工具交叉验证：AI 找「语义违规」（绕过接口层调用），静态工具找「语法违规」。

```javascript
你是架构评审员。分层规则：
- ui → 允许 import：hooks, components, types
- hooks → 允许 import：api, types（禁止直接 import ui）
- api → 允许 import：types, dal
例外：`import type` 不受限制。
对以下变更文件列表，输出 JSON：
[{ file, layer, violatingImport, ruleBasis, fix }]
不确定的项标 confidence: low，不要编造。
r
```
