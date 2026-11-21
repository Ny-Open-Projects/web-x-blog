---
title: [AIC-208] 可以用 AI 帮团队生成/提炼 Cursor rules 吗？流程怎么设计才不跑偏？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-208：可以用 AI 帮团队生成/提炼 Cursor rules 吗？流程怎么设计才不跑偏？
**答**：
- 可以且推荐：从「历史违规样本 + 优秀代码评审意见」自动提炼规则草稿，比人凭记忆写更贴实际。
- 流程：采集样本 → AI 提炼规则草案 → 人工评审定稿 → 进评测集验证 → 发布。
- 关键约束：规则必须引用真实案例（文件/PR 链接），防止 AI 编造规范。
- 生成规则也要走规则：给「规则撰写规范」作为输入（简洁、要点式、带示例）。

```javascript
async function distillRules(violations: Array<{ desc: string; pr: string }>) {
  const prompt = `你是前端规范负责人。基于以下真实违规样本提炼 Cursor 规则。
要求：要点式、每条附替代方案与示例文件、不超过 80 行。
违规样本：\n${violations.map(v => `- ${v.desc} (PR: ${v.pr})`).join('\n')}`;
  const draft = await llm(prompt);
  return draft; // 人工评审 → evalRule 验证 → 入库
}
r
```
