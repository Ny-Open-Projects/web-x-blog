---
title: [RBL-700] 笔试：手写 SSR 双产物 manifest 对齐校验器
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-700：笔试：手写 SSR 双产物 manifest 对齐校验器

**答**：实现 `verifySSRPair(serverOut, clientOut)`。serverOut: `{ buildId, referencedChunks: string[], modules: Array<{ id, usesBrowserGlobal, hasGuard }> }`；clientOut: `{ buildId, manifest: Map<chunkId, url> }`。校验：1) buildId 一致（原子性），不一致 → fatal `version-mismatch`；2) server 引用的 chunk 必须在 client manifest（`missing-chunk`）；3) client manifest 中存在但 server 引用闭包之外的 chunk 属正常（懒加载）不报；4) usesBrowserGlobal 且无 guard 的模块 → warning `hydration-risk`（列表）；5) 返回 `{ fatal: string[]|null, warnings: string[] }`。边界：空引用；manifest 空。

```javascript
function verifySSRPair(serverOut, clientOut) {
  if (serverOut.buildId !== clientOut.buildId)
    return { fatal: ['version-mismatch'], warnings: [] };
  const fatal = [], warnings = [];
  for (const chunk of serverOut.referencedChunks || [])
    if (!clientOut.manifest.has(chunk))
      fatal.push(`missing-chunk: ${chunk}`);
  for (const m of serverOut.modules || [])
    if (m.usesBrowserGlobal && !m.hasGuard)
      warnings.push(`hydration-risk: ${m.id}`);
  return { fatal: fatal.length ? fatal : null, warnings };
}

// 自测
const clientOut = {
  buildId: 'b1',
  manifest: new Map([['main', 'main.h1.js'], ['admin', 'admin.h2.js']]),
};
// 1) 全对齐
let r = verifySSRPair(
  { buildId: 'b1', referencedChunks: ['main'],
    modules: [{ id: 'App.tsx', usesBrowserGlobal: true, hasGuard: true }] }, clientOut);
console.log(r.fatal === null && r.warnings.length === 0);

// 2) 缺 chunk
r = verifySSRPair(
  { buildId: 'b1', referencedChunks: ['main', 'ghost'], modules: [] }, clientOut);
console.log(r.fatal[0] === 'missing-chunk: ghost');

// 3) 版本不一致
r = verifySSRPair({ buildId: 'b2', referencedChunks: [], modules: [] }, clientOut);
console.log(r.fatal[0] === 'version-mismatch');

// 4) 水合风险
r = verifySSRPair(
  { buildId: 'b1', referencedChunks: ['main'],
    modules: [{ id: 'Comp.tsx', usesBrowserGlobal: true, hasGuard: false }] }, clientOut);
console.log(r.warnings[0] === 'hydration-risk: Comp.tsx' && r.fatal === null);

// 5) 空引用 + 空 manifest
r = verifySSRPair({ buildId: 'b1', referencedChunks: [], modules: [] },
  { buildId: 'b1', manifest: new Map() });
console.log(r.fatal === null);
```

**评分点**：
- buildId 原子性校验优先（版本不一致直接 fatal 且短路后续检查）
- 缺 chunk 检测方向正确（server 引用 -> client manifest；懒加载 chunk 不在引用闭包属正常）
- 水合风险分级为 warning（不阻断，但列出模块清单可评审）
- 能说清「双产物非原子构建是 SSR 线上事故高发源」属于加分
