---
title: [WCN-775] 笔试：手写编译产物体积预算检查器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-775：笔试：手写编译产物体积预算检查器

**答**：
- 需求：实现 `checkBudget(artifacts, budget)`：artifacts 为 `{ [file]: bytes }`，budget 为 `{ [file]: limitBytes }` 或含 `default` 兜底。返回超预算的文件数组 `[{ file, actual, limit, over }]`，按超出量降序。边界：未列预算的文件用 default（若有）否则忽略；limit<=0 视为禁止该文件有体积。
- 要点：遍历 artifacts，取 budget[file] ?? budget.default；超限判断 actual>limit；按 over 降序；边界防御。

```javascript
function checkBudget(artifacts, budget) {
  const out = [];
  for (const [file, actual] of Object.entries(artifacts || {})) {
    const limit = budget[file] ?? budget.default;
    if (limit === undefined) continue;                 // 无预算则忽略
    if (actual > limit) out.push({ file, actual, limit, over: actual - limit });
  }
  return out.sort((a, b) => b.over - a.over);
}
console.log(checkBudget(
  { 'core.js': 31, 'btn.js': 9, 'utils.js': 100 },
  { 'core.js': 30, 'btn.js': 8, default: 50 }
));
```

**评分点**：
- 优先取文件专属预算，缺省用 default，否则忽略（优先级正确）。
- 正确计算 over 并按降序排列，便于优先处理大头。
- limit<=0 的禁止语义由 actual>0 自动满足。
- 返回结构化结果，边界防御完整。
