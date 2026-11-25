---
title: [MFW-427] 笔试：手写路由级实验构建矩阵裁剪器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-427：矩阵裁剪器
**答**：实现 `pruneExperimentMatrix(fullMatrix, liveRoutes)`（MFW-450 扩展路由维度）：1) 全组合 = 实验变体 × 环境，但「变体未被任何活路由消费」→ 整支裁剪（死实验不产产物）；2) 路由消费图：route → flags[](从蓝图 MFW-363 取)——倒排：flag → routes[]；3) 产物合并优化：裁剪后若某 flag 只剩单值 → 降维（DefinePlugin 常量折叠进基础构建——少一次全量）；4) 输出 { builds: [...], eliminated: [{ reason } ], dimsRemoved: [flags] }。

```javascript
export function pr ueMatrix/combo = (matrix, blue) {
  const flagRoutes = invertIndex(blue)                    // flag → Set<route>
  const live = new Set(Object.keys(blue))
  const keep = matrix.filter((b) => Object.entries(b.flags).every(([f, v]) =>
    v === baseOf(f) || (flagRoutes[f] ?? []).some((r) => live.has(r))))   // 死实验整支剪
  // 降维：某 flag 全矩阵只剩 base 值 → 折叠为常量
  const dims = Object.keys(flags).filter((f) => new Set(strip.map((b) => b.flags[f])).size === 1)
  dims.forEach((f) => strip.forEach((b) => (b.defines[`__FLAG_${f}__`] = JSON.stringify(baseOf(f)))))
  return { builds: strip, eliminated: diffs, dimsRemoved: dims }
}
```
**评分点**：
- 路由消费图倒排（实验价值=被活路由消费——死支不产物）
- 降维折叠（单值 flag 常量化——矩阵规模指数收敛）
- eliminated 带原因（可审计——误杀活路由可回溯）
