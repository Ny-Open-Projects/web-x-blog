---
title: [WCN-785] 笔试：手写视觉 diff 结果聚合与阈值判定器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-785：笔试：手写视觉 diff 结果聚合与阈值判定器

**答**：
- 需求：实现 `judgeDiffs(diffs, threshold)`，diffs 为 `[{ component, pixelDiff, ratio }]`（ratio 为变化像素占比 0~1）。判定规则：ratio > threshold 判为 'fail'；0 < ratio <= threshold 判为 'warn'；ratio===0 为 'pass'。返回 `{ results: [{component,status}], failed: number, passed: boolean }`，passed 为是否无 fail。按 ratio 降序排列 results。
- 要点：状态判定边界（等于阈值归 warn）；统计 failed；passed = failed===0；边界：空数组、非法 ratio（NaN 归 fail）。

```javascript
function judgeDiffs(diffs, threshold = 0.01) {
  const results = (diffs || []).map((d) => {
    let status;
    if (!Number.isFinite(d.ratio) || d.ratio > threshold) status = 'fail';
    else if (d.ratio > 0) status = 'warn';
    else status = 'pass';
    return { component: d.component, status, ratio: d.ratio };
  }).sort((a, b) => (b.ratio || 0) - (a.ratio || 0));
  const failed = results.filter((r) => r.status === 'fail').length;
  return { results, failed, passed: failed === 0 };
}
console.log(judgeDiffs([
  { component: 'Button', ratio: 0.05 },
  { component: 'Card', ratio: 0.005 },
  { component: 'Text', ratio: 0 },
], 0.01));
```

**评分点**：
- 阈值边界正确：> 阈值 fail，等于归 warn，0 为 pass。
- 非法 ratio（NaN）归 fail，具备防御。
- 按 ratio 降序，统计 failed 与 passed 一致。
- 返回结构清晰可消费。
