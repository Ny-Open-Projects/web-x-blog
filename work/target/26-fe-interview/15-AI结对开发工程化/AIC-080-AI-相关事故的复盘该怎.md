---
title: [AIC-080] AI 相关事故（AI 生成代码引发线上问题）的复盘怎么做？复盘产出应该沉淀到哪？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-080：AI 相关事故（AI 生成代码引发线上问题）的复盘怎么做？复盘产出应该沉淀到哪？
**答**：
- 复盘特殊点：除常规「时间线/根因/责任」外，必须回答 AI 四问——① 代码哪部分是 AI 生成的 ② 生成时的 prompt/上下文是否给了足够事实 ③ AI review/人工 review 为何没拦住 ④ 该缺陷属于哪类失败模式。
- 责任定位原则不变：提交人负责（AIC-020），但流程缺陷要量化——如果 80% 同类缺陷 AI 都会犯，这是规则文件缺陷，不是人的问题。
- 沉淀去向（这是复盘的价值所在）：① 缺陷模式 → AI review 清单加一项（AIC-042）② 事实缺口 → 知识库加事实卡片（AIC-029）③ 流程漏洞 → 门禁加检查 ④ prompt 缺陷 → 模板库修订。
- 复盘要「无责化 + 可执行化」：每条 action 都落到具体文件/规则，而不是「加强意识」这种空话。
- 追问钩子：事故复盘产出是团队 AI 知识库里最高价值的资产——它直接来自真实损失。

```javascript
// 事故复盘的结构化模板（落到 incident-*.md）
const incidentTemplate = `
# 事故：${title}
时间线/影响面：...
AI 四问：
1. AI 生成部分：${files}
2. 生成上下文缺陷：${missingFacts}
3. 未拦截原因：{ai-review: ..., human-review: ...}
4. 失败模式分类：hallucination | boundary | injection | sycophancy | constraint_ignored
Action（全部落到文件）：
- review 清单 +1：...
- 知识库 fact-card +1：...
- 门禁规则 +1：...
`;
```
