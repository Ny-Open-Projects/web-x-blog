---
title: [AIC-224] 如何让 AI 依据团队的 ADR（架构决策记录）做评审？前提条件是什么？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-224：如何让 AI 依据团队的 ADR（架构决策记录）做评审？前提条件是什么？
**答**：
- 前提：ADR 结构化、可检索（编号、状态、决策、理由、影响范围），烂尾 ADR 反而误导。
- 评审时检索相关 ADR（按涉及模块匹配），注入给 AI 做对照。
- 让 AI 输出三类结论：符合既有决策/与某 ADR 冲突/超出 ADR 覆盖需新决策。
- 冲突项高亮 ADR 编号与原文引用，评审会直接对账。

```javascript
async function adrReview(diff: string) {
  const adrs = await searchADR(diffModules); // 按模块检索相关决策
  return llm(`你是架构评审员。以下是相关 ADR：
${adrs.map(a => `[${a.id}] ${a.decision}（理由：${a.rationale}）`).join('\n')}
变更 diff：${diff}
输出：符合项 / 冲突项（引用 ADR 编号与原文）/ 需新决策项。`);
}
r
```
