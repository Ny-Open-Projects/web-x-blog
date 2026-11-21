---
title: [TST-427] 笔试：AI 视觉分类结果按置信度路由（自动判/人工审）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-427：笔试：AI 视觉分类结果按置信度路由（自动判/人工审）。
**题目**：分类结果 `[{category, confidence}]`。规则：confidence ≥ 0.8 自动生效；0.5-0.8 → 人工快审队列；< 0.5 → 视为噪声（仅记录）。输出三队列与人工队列优先级（按 1-置信度 排序）。

```javascript
function routeClassification(results) {
  const auto = [], human = [], noise = [];
  for (const r of results) {
    if (r.confidence >= 0.8) auto.push(r);
    else if (r.confidence >= 0.5) human.push(r);
    else noise.push(r);
  }
  human.sort((a, b) => a.confidence - b.confidence);   // 越不确定越优先
  return { auto, human, noise };
}
console.log(routeClassification([
  { category: 'regression', confidence: 0.9 },
  { category: 'acceptable', confidence: 0.6 },
  { category: 'noise', confidence: 0.3 },
])); // human 队列 1 条（0.6）

```

**评分点**：
- 三段路由阈值清晰（边界值归属明确）。
- 人工队列内部排序（最不确定优先）。
- 噪声队列保留记录（回流训练用）。
- 空输入返回空队列。
