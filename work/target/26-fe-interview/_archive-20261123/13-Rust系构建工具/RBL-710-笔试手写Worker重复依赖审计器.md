---
title: [RBL-710] 笔试：手写 Worker 重复依赖审计器（跨 chunk 归属 + 体积影响评估）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-710：笔试：手写 Worker 重复依赖审计器（跨 chunk 归属 + 体积影响）

**需求**：实现 `auditDuplication(chunks, modules)`。chunks: `{ name, kind: 'main'|'worker'|'shared', modules: string[] }[]`；modules: `Record<id, { sizeKB, isVendor }>`. 检测：1) 同一 vendor 模块（isVendor）同时出现在 main 与 worker chunk → 重复项 `{ module, sizeKB, mainChunks: n, workerChunks: m, wastedKB }`（wastedKB = sizeKB × min(两个世界的引用数) 保守估计）；2) 相同 kind 的 chunk 间重复（如两个 main chunk 都含同一 vendor）也报，wastedKB = sizeKB × (refs−1)；3) 按 wastedKB 降序；4) shared chunk 中的模块不算重复。返回 `{ duplicates: Array, totalWastedKB }`。边界：无 vendor、单 chunk。

```javascript
function auditDuplication(chunks, modules) {
  const holder = new Map();                              // module -> Array<{ chunkName, kind }>
  for (const c of chunks)
    for (const m of c.modules)
      if (modules[m]?.isVendor)
        (holder.get(m) || holder.set(m, []).get(m)).push({ name: c.name, kind: c.kind });

  const duplicates = [];
  for (const [mod, holders] of holder) {
    if (holders.length <= 1) continue;
    const size = modules[mod].sizeKB;
    const byKind = {};
    for (const h of holders) byKind[h.kind] = (byKind[h.kind] || 0) + 1;
    // 去重逻辑：同一 kind 内重复算 refs-1；跨 kind（main vs worker）至少各留一份
    let wasted = 0;
    if (byKind.main && byKind.worker) {
      wasted = size * (holders.length - 2);              // 两世界各保留一份
    } else {
      wasted = size * (holders.length - 1);
    }
    if (wasted > 0) duplicates.push({
      module: mod, sizeKB: size, mainChunks: byKind.main ?? 0, workerChunks: byKind.worker ?? 0,
      wastedKB: wasted,
    });
  }
  duplicates.sort((a, b) => b.wastedKB - a.wastedKB);
  return { duplicates, totalWastedKB: +duplicates.reduce((s, d) => s + d.wastedKB, 0).toFixed(1) };
}

// 自测
const chunks = [
  { name: 'main', kind: 'main', modules: ['lodash', 'react', 'app-core'] },
  { name: 'worker-a', kind: 'worker', modules: ['lodash', 'moment'] },
  { name: 'worker-b', kind: 'worker', modules: ['lodash'] },
  { name: 'chunk-x', kind: 'main', modules: ['react'] },
];
const modules = {
  lodash: { sizeKB: 70, isVendor: true },
  react: { sizeKB: 130, isVendor: true },
  moment: { sizeKB: 60, isVendor: true },
  'app-core': { sizeKB: 40, isVendor: false },
};
const r = auditDuplication(chunks, modules);
// lodash: 3 holders，跨 kind（1 main + 2 worker）-> wasted = 70×(3−2)=70
// react: 2 holders 同 main kind -> wasted = 130
// moment: 单 holder 不算
console.log(r.duplicates[0].module === 'react');        // wasted 130 最大
console.log(r.duplicates[1].module === 'lodash' && r.duplicates[1].wastedKB === 70);
console.log(r.duplicates.length === 2 && r.totalWastedKB === 200);

const r2 = auditDuplication([chunks[0]], modules);
console.log(r2.duplicates.length === 0 && r2.totalWastedKB === 0);
```

**评分点**：
- 跨 kind（main vs worker）与同 kind 重复的 wasted 计算区分（两世界各保留一份）
- 非 vendor 模块不参与（业务代码重复是预期——chunk 划分需要）；排序按 wastedKB 降序
- 边界：无重复/单 chunk 返回空；shared chunk 的豁免逻辑体现在过滤条件
- 能说清「worker 独立副本是正确性默认，报告是给优化决策不是自动合并」属于加分
