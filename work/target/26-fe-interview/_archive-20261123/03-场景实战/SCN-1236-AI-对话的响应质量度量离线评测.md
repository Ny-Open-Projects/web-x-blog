---
title: [SCN-1236] AI 对话的响应质量度量（离线评测）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1236：AI 对话的响应质量度量（离线评测）

**答**：
- 评测：回答质量评测集（正确性/相关性/格式）定期跑分（模型/版本对比）。
- 线上：用户负反馈率（1220）与评测分联动（回归检测）。
- 门禁：模型/Prompt 变更评测达标才上线（门禁）。

```javascript
// 评测门禁
async function evalGate(modelVersion, evalSet) {
  const scores = await runEval(modelVersion, evalSet);
  return {
    scores: scores.map(s => ({ dim: s.dim, score: +s.score.toFixed(2) })),
    pass: scores.every(s => s.score >= s.threshold),
    note: scores.some(s => s.score < s.threshold)
      ? `未达标维度: ${scores.filter(s => s.score < s.threshold).map(s => s.dim)}` : '通过',
  };
}
async function runEval(v, set) { return set; }
```
