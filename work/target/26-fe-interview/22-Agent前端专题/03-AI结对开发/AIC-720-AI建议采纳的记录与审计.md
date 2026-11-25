---
title: [AIC-720] 结对开发中如何记录 AI 建议的采纳过程以便审计
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-720：结对开发中如何记录 AI 建议的采纳过程以便审计

**答**：
- 结论先行：采纳审计 = 对每条 AI 建议记录「是否被采纳、由谁、依据、结果」——这既是合规证据（谁批准了 AI 代码），也是改进 prompt 的反馈数据（哪些建议常被拒）。
- 记录要素：建议 ID、采纳决策（accept/reject/modify）、决策人、理由、关联提交、事后是否有 bug；缺一都难做归因。
- 用途：1) 事故追溯（哪段 AI 代码谁放行）；2) 质量分析（高拒绝率的任务类型要改 prompt）；3) 合规证明（人工审查确实发生）。
- 追问钩子：为什么「修改后采纳」要单独标记？——它既不是全盘接受也不是拒绝，是「人机协作」的真实形态，最能反映 AI 建议的有效度。

```javascript
// 采纳审计记录
function recordAdoption(suggestion, decision) {
  return {
    id: suggestion.id,
    decision,                                  // accept | reject | modify
    reviewer: decision.reviewer,
    reason: decision.reason ?? '',
    commit: decision.commit ?? null,
    ts: Date.now(),
  };
}
const log = [
  recordAdoption({ id: 'S1' }, { decision: 'accept', reviewer: 'alice', commit: 'abc' }),
  recordAdoption({ id: 'S2' }, { decision: 'modify', reviewer: 'bob', reason: '边界未处理' }),
];
const rejected = log.filter(l => l.decision !== 'accept' && l.decision !== 'modify');
console.log(log[1].reason); // 边界未处理（改进 prompt 的线索）
console.log(rejected.length === 0);
```
