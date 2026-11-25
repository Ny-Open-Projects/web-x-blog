---
title: [AIC-719] 结对中 AI 首次响应质量受哪些因素影响
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-719：结对中 AI 首次响应质量受哪些因素影响

**答**：
- 结论先行：首次响应质量 ≈ 「上下文相关度 × 意图清晰度 × 约束完整度」——第一印象差往往不是模型不行，而是输入没给够；先优化输入比换模型更划算。
- 三要素：1) 相关上下文（只注入相关文件，而非全仓库）；2) 明确意图（要它做什么、不做什么）；3) 可验证约束（技术栈、版本、禁用 API）。
- 首轮策略：首轮先让 AI「复述理解 + 列假设」，人确认后再让它写代码——用一轮对齐换掉后面五轮返工。
- 追问钩子：为什么「首轮先复述理解」能提升最终质量？——把误解消灭在代码生成之前，纠正成本最低（RBL-576 意图澄清）。

```javascript
// 首轮对齐：先复述理解，确认后再生成
function firstTurn(ctx, intent, constraints) {
  const brief = {
    goal: intent,
    context: ctx.files,                       // 只注入相关文件
    constraints,
    assumptions: deriveAssumptions(intent),   // AI 主动列假设
  };
  return { brief, code: null, needConfirm: true }; // 首轮不出码，先确认
}
function deriveAssumptions(intent) {
  return intent.includes('列表') ? ['假设使用现有分页组件'] : [];
}
const t = firstTurn({ files: ['List.tsx'] }, '给列表加筛选', { stack: 'React18' });
console.log(t.code === null && t.needConfirm); // 先确认再写
```
