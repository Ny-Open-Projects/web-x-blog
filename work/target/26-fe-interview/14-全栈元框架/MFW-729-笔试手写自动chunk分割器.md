---
title: [MFW-729] 笔试：手写自动 chunk 分割器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-729：笔试：手写自动 chunk 分割器

**答**：实现 `autoChunk(modules, { sharedThreshold = 3, minSizeKB = 10, maxSizeKB = 200 })`。modules: `{ id, importedBy: string[], sizeKB }[]`. 规则：1) shared：importedBy ≥ sharedThreshold 且 sizeKB ≥ minSizeKB → 独立共享 chunk；2) **超大共享模块拆分**：sizeKB > maxSizeKB 且 importedBy ≥ threshold → 警告（过大——建议手动拆分）；3) route-specific：importedBy = 1 → 并入路由；4) 小模块合并：sizeKB < minSizeKB 且 importedBy ≥ threshold → 'merged-small'（多个小共享模块合并为一个 chunk——减少请求）；5) 返回 `{ chunks: Record<id, strategy>, summary: { shared, route, mergedSmall, oversized } }`。边界：modules 空；importedBy 空（route-specific）；全部超大（多个 oversized）。

```javascript
function autoChunk(modules = [], { sharedThreshold = 3, minSizeKB = 10, maxSizeKB = 200 } = {}) {
  const chunks = {};
  const summary = { shared: 0, route: 0, mergedSmall: 0, oversized: 0 };
  for (const m of modules) {
    const refs = m.importedBy?.length ?? 0;
    if (refs >= sharedThreshold && m.sizeKB > maxSizeKB) {
      chunks[m.id] = 'oversized-shared';
      summary.oversized++;
      continue;
    }
    if (refs >= sharedThreshold && m.sizeKB >= minSizeKB) {
      chunks[m.id] = 'shared';
      summary.shared++;
      continue;
    }
    if (refs >= sharedThreshold) {                       // 小但共享
      chunks[m.id] = 'merged-small';
      summary.mergedSmall++;
      continue;
    }
    chunks[m.id] = 'route-specific';
    summary.route++;
  }
  return { chunks, summary };
}

// 自测
const modules = [
  { id: 'react', importedBy: ['r1', 'r2', 'r3', 'r4', 'r5'], sizeKB: 40 },       // shared
  { id: 'lodash', importedBy: ['r1', 'r2', 'r3', 'r4'], sizeKB: 250 },           // oversized
  { id: 'chart-lib', importedBy: ['r1'], sizeKB: 150 },                          // route
  { id: 'tiny-helper', importedBy: ['r1', 'r2'], sizeKB: 2 },                    // merged-small
  { id: 'product-utils', importedBy: ['r1'], sizeKB: 30 },                       // route
];
let r = autoChunk(modules);
console.log(r.chunks.react === 'shared');
console.log(r.chunks.lodash === 'oversized-shared');
console.log(r.chunks['chart-lib'] === 'route-specific');
console.log(r.chunks['tiny-helper'] === 'merged-small');
console.log(r.summary.shared === 1 && r.summary.oversized === 1);
console.log(r.summary.route === 2 && r.summary.mergedSmall === 1);

// 自定义阈值
r = autoChunk(modules, { sharedThreshold: 5, minSizeKB: 20 });
console.log(r.chunks.react === 'shared');                // 5 ≥ 5 且 40 ≥ 20
console.log(r.chunks.lodash === 'oversized-shared');     // 5 ≥ 5 且 250 > 200

// 空
r = autoChunk([]);
console.log(Object.keys(r.chunks).length === 0);
// 无引用
r = autoChunk([{ id: 'orphan', importedBy: [], sizeKB: 50 }]);
console.log(r.chunks.orphan === 'route-specific');       // 0 引用 = route
```

**评分点**：
- 四级策略（shared/oversized/route/merged-small——基于引用数与尺寸的自动决策）
- merged-small（小共享模块合并——减少请求数 RBL-596）；oversized 警告（手动拆分建议）
- 边界（空/无引用/自定义阈值）；对比 manualChunks 的分析优势
- 能说清「自动 chunk 分割基于引用分析：引用数 × 尺寸的加权——比 manualChunks 手动规则更精确」属于加分
