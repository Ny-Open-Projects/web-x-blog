---
title: [MFW-617] 笔试：手写 Server Bundle 瘦身审计器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-617：笔试：手写 Server Bundle 审计器

**答**：实现 `auditServerBundle(manifest, opts)`。manifest: `{ totalMB, deps: Record<name, sizeMB>, entryCount, coldStartMs }`。opts: `{ budgetMB = 100, coldBudgetMs = 400, lazyCandidates: string[] }`. 规则：1) 总体积超预算 → blocker；2) **冷启动超时** → blocker（体积影响冷启动——RBL-518）；3) lazyCandidates 中「未被动态 import」的（manifest.staticImports 包含）→ warn 'lazy-candidate'（应懒加载的重依赖）；4) top3 依赖输出（瘦身靶点）；5) 修复建议生成（体积大头 → 具体动作：替换/external/lazy）。返回 `{ blockers, warnings, topDeps, suggestions }`。边界：deps 空（totalMB 为 0）；coldStartMs 缺失（跳过冷启动检查）。

```javascript
function auditServerBundle(manifest, { budgetMB = 100, coldBudgetMs = 400, lazyCandidates = [] } = {}) {
  const blockers = [], warnings = [], suggestions = [];
  if (manifest.totalMB > budgetMB)
    blockers.push({ type: 'over-budget', detail: `server bundle ${manifest.totalMB}MB > ${budgetMB}MB` });
  if (manifest.coldStartMs != null && manifest.coldStartMs > coldBudgetMs)
    blockers.push({ type: 'cold-start', detail: `冷启动 ${manifest.coldStartMs}ms > ${coldBudgetMs}ms——瘦身/懒加载` });
  const staticHeavy = lazyCandidates.filter(dep => manifest.staticImports?.includes(dep));
  staticHeavy.forEach(dep =>
    warnings.push({ type: 'lazy-candidate', dep, detail: `${dep} 被静态引入——改为动态 import 降冷启动` }));
  const topDeps = Object.entries(manifest.deps ?? {})
    .sort((a, b) => b[1] - a[1]).slice(0, 3);
  for (const [name, size] of topDeps) {
    if (/moment|lodash$/.test(name)) suggestions.push(`${name} → dayjs/lodash-es（摇树友好）`);
    else if (size > 20) suggestions.push(`${name} ${size}MB → 考虑 external 或动态 import`);
  }
  return { blockers, warnings, topDeps, suggestions };
}

// 自测
const manifest = { totalMB: 120, coldStartMs: 500,
  deps: { moment: 5, 'aws-sdk': 60, lodash: 3, 'heavy-analytics': 25 },
  staticImports: ['heavy-analytics', 'lodash'] };
let r = auditServerBundle(manifest, { lazyCandidates: ['heavy-analytics', 'sharp'] });
console.log(r.blockers.length === 2);                    // 超预算 + 冷启动
console.log(r.warnings[0].dep === 'heavy-analytics');    // 静态引入的懒加载候选
console.log(r.topDeps[0][0] === 'aws-sdk' && r.topDeps[0][1] === 60);
console.log(r.suggestions.some(s => s.includes('dayjs')));   // moment 替换建议
console.log(r.suggestions.some(s => s.includes('aws-sdk')));

// 达标
r = auditServerBundle({ totalMB: 80, coldStartMs: 300,
  deps: { dayjs: 0.1 }, staticImports: [] });
console.log(r.blockers.length === 0 && r.warnings.length === 0);
// 无冷启动数据
r = auditServerBundle({ totalMB: 200, deps: {} });
console.log(r.blockers.length === 1);                    // 只有体积 blocker（无冷启动检查）
```

**评分点**：
- 双 blocker（体积 + 冷启动——两者不同维度 RBL-518）；lazyCandidates 的静态引入检测（动态 import 机会）
- topDeps 排序 + 建议生成（依赖替换/external/lazy——可执行的建议 RBL-829 修复建议风格）
- 边界（无冷启动数据跳过检查——不误报）；建议与归因联动（top 依赖 = 靶点）
- 能说清「server bundle 的 ROI 在冷启动与基础设施成本——用户感知优先但 serverless 场景下冷启动即用户感知」属于加分
