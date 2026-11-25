---
title: [AIC-554] AI 代码审查的注意力管理
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-554：AI 代码审查的注意力管理

**答**:
- AI 代码审查的注意力管理（RBL-532 检查点的效率优化）：1) **审查注意力衰减**（人在审查 100 行后注意力下降 50%（审查质量递减——前 50 行审查仔细、后 50 行扫过）；2) **注意力的分配策略**：高优先级段先审（T0 security > T1 logic > T2 boilerplate——RBL-505 分级）；3) **审查的 chunking**（100 行 chunk 审查 + 休息——防注意力衰减（每次审查 chunk ≤ 100 行——超量分次审）；4) **注意力标记**：AI 自动标注"高优先级区域"（安全相关/复杂逻辑/边界条件——人先审标注区）。
- 注意力管理的度量：审查发现率（审出的 bug 数 / 总 bug 数——衰减后审查发现率下降：早期 90% → 后期 40%）；「发现率曲线」= 注意力的量化度量。
- 追问钩子：为什么「审查的 chunking」比「一次性审查全部 diff」发现更多 bug？——一次性审 500 行：前 100 行发现率 90%、后 400 行发现率 40%（注意力衰减——细节被跳过）；分 5 次 100 行审：每次发现率 90%（注意力刷新——休息恢复注意力）；「chunking 的发现率提升 = 50%→90% 的后半段提升」——总发现率从 60% → 85%（同一审查时间发现更多 bug）。

```typescript
// 审查注意力管理
function planReview(diff: { path: string; lines: number; riskLevel: number }[],
  { maxChunk = 100 } = {}) {
  // 1) 按 riskLevel 降序（高优先先审 RBL-505）
  const sorted = [...diff].sort((a, b) => b.riskLevel - a.riskLevel);
  // 2) chunking：按 max 切分
  const chunks: typeof diff[] = [];
  let current: typeof diff = []; let lineCount = 0;
  for (const file of sorted) {
    if (lineCount + file.lines > maxChunk && current.length) {
      chunks.push(current); current = []; lineCount = 0;
    }
    current.push(file); lineCount += file.lines;
  }
  if (current.length) chunks.push(current);
  return {
    chunks: chunks.map((c, i) => ({
      order: i + 1, files: c.map(f => f.path),
      lines: c.reduce((s, f) => s + f.lines, 0),
      note: i > 0 ? '休息后审查——注意力已恢复' : '最高优先级——注意力最佳',
    })),
    totalChunks: chunks.length,
  };
}
```
