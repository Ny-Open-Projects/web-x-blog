---
title: [ALG-298] 多列布局分配：等高列（Pinterest 简化版）的平衡分配（最短列优先 vs 轮转 vs 反转轮转）？
date: 2026-11-19
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---
## ALG-298：多列布局分配：等高列（Pinterest 简化版）的平衡分配（最短列优先 vs 轮转 vs 反转轮转）？
**答**：卡片流多列分配：最短列优先（ALG-281）在"高度未知"时退化为轮转——顺序轮转导致列不平衡（高卡片集中一列）；改进：反转轮转（第二遍反向）+ 高度估算分桶。

**思路**：三级策略：已知高度 → 最短列；未知高度估算（历史均值）→ 估算最短列；完全未知 → 反转轮转（来回折返，相邻项落相邻列，列差 ≤ 1）。

```javascript
function assignColumns(items, cols, { estimate } = {}) {
  const heights = new Array(cols).fill(0);
  const result = new Array(cols).fill(null).map(() => []);
  let dir = 1, col = 0;
  for (const item of items) {
    const h = item.height ?? estimate?.(item) ?? 0;
    if (h > 0) {
      col = heights.indexOf(Math.min(...heights));        // 最短列优先（含估算）
    } else {
      col = Math.max(0, Math.min(cols - 1, col));         // 反转轮转：来回折返
      result[col].push(item);
      col += dir;
      if (col === cols || col < 0) { dir = -dir; col = Math.max(0, Math.min(cols - 1, col)); }
    }
    if (h > 0) { result[col].push(item); heights[col] += h; }
  }
  return result;
}
// 反转轮转（boustrophedon）：1,2,3,4,5 → 列 [1,6][2,5][3,4] —— 相邻项分散，列高方差小
// 顺序轮转：1,4,7 都落列 0 —— 高卡片集中的列超高（不平衡）
// 估算降级链：真实高度 → 历史均值估算 → 反转轮转 —— 按信息量逐级退化
// 渲染后修正：真实高度出来后局部重排（只移动新增项，已渲染不动——ALG-281 预计算正解的补充）
```

**评分点**：
- 三级降级（真实高度/估算/反转轮转）——本题核心。
- 反转轮转的平衡性质（列差 ≤ 1）与顺序轮转的失衡对照。
- 估算来源（历史均值）。
- 渲染后修正的局部性（只动新增）。
