---
title: [1261] 笔试手写：实现 badcase 错误类型矩阵统计器
date: 2026-11-22
categories: [AI与Agent]
tags: [前端面试, 笔试题, 评测]
type: 笔试题
---

## 1261：笔试手写：实现 badcase 错误类型矩阵统计器

**需求**：实现 errorMatrix(cases)：cases 为 { module, errorType, severity: 1|2|3 }[]。输出：矩阵（module × errorType 计数）、每模块加权分（severity 求和）、以及热点（矩阵中计数最大格）；同分多格时全部返回。返回 { matrix, moduleScores, hotspots }。

```js
function errorMatrix(cases) {
  const matrix = {}, moduleScores = {};
  for (const c of cases) {
    matrix[c.module] ??= {};
    matrix[c.module][c.errorType] = (matrix[c.module][c.errorType] || 0) + 1;
    moduleScores[c.module] = (moduleScores[c.module] || 0) + c.severity;
  }
  let max = 0; const hotspots = [];
  for (const [mod, row] of Object.entries(matrix)) {
    for (const [et, n] of Object.entries(row)) {
      if (n > max) { max = n; hotspots.length = 0; hotspots.push({ module: mod, errorType: et, count: n }); }
      else if (n === max) hotspots.push({ module: mod, errorType: et, count: n });
    }
  }
  return { matrix, moduleScores, hotspots };
}
```

**评分点**：
- 两级嵌套计数用 ??= 初始化
- 热点判定 max 重置与并列收集
- 加权分按 severity 求和（严重度意识）
- 能讨论：矩阵驱动的修复优先级 = 频次 × severity × 模块影响面
