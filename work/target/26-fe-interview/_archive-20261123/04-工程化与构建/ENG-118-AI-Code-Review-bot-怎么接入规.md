---
title: [ENG-118] AI Code Review bot 怎么接入？规则与 LLM 混合审查怎么设计？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-118：AI Code Review bot 怎么接入？规则与 LLM 混合审查怎么设计？
**答**：
- 架构是"规则引擎打底 + LLM 语义增强"：确定性检查（lint、类型、危险 API）交给规则，架构与语义问题交给 LLM。
- 混合审查的分工：规则引擎秒级给出确定性意见；LLM 审 diff 与上下文，产出可读的语义级建议。
- 关键工程点：意见去重与分级（block/suggest）、LLM 输出必须可执行（附文件行号与修复示例）、控制成本（只审 diff 周边代码）。
- 红线：AI 意见只评论不阻断高危（除非规则引擎判定），最终合入决策留在人，避免误报阻断研发。

```typescript
// AI review bot 核心逻辑：规则先筛，LLM 审语义
const diff = await getPRDiff(pr.number);

// 1. 规则引擎：确定性意见，秒级
const ruleFindings = await runRuleEngine(diff); // 禁用 API、危险操作、规模超限

// 2. LLM 审查：只喂 diff 与相关上下文，控制 token 成本
const prompt = buildReviewPrompt(diff, { maxContextLines: 200 });
const llmFindings = await gatewayChat({
  scenario: 'code-review',
  messages: [{ role: 'user', content: prompt }],
});

// 3. 汇总去重分级：block 级由规则决定，LLM 一律 suggest
const merged = dedupeAndRank(ruleFindings, llmFindings, {
  llmMaxSeverity: 'suggest',
});
await postReviewComments(pr.number, merged);
```
