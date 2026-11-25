---
title: [AIC-569] 笔试：手写 Edge 限制适配决策器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-569：笔试：手写 Edge 适配决策

**答**：实现 `edgeActionAdapter(action, constraints)`。action: `{ name, estimatedDurationMs, memoryMB, needsNodeAPI, needsFileSystem }`。constraints: `{ maxDurationMs, maxMemoryMB, supportsNodeAPI, supportsFS }`. 规则：1) 全部满足 → 'edge-direct'（直接在 Edge 执行）；2) duration 超限或 memory 超限 → 'delegate-queue'（委派队列 RBL-569）；3) needsNodeAPI 或 needsFS 但 edge 不支持 → 'delegate-node'（切到 Node runtime）；4) 返回 `{ strategy: 'edge-direct'|'delegate-queue'|'delegate-node', reason }`。优先级：needsNodeAPI/FS > duration/memory > edge-direct。边界：constraints 空（默认 edge 全支持——edge-direct）；needsNodeAPI 且 duration 超限（delegate-node 优先——Node API 是硬约束不能绕过）；estimatedDurationMs 缺失（视为 0）。

```javascript
function edgeActionAdapter(action = {}, constraints = {}) {
  const c = { maxDurationMs: 30000, maxMemoryMB: 128,
    supportsNodeAPI: false, supportsFS: false, ...constraints };
  const a = { estimatedDurationMs: 0, memoryMB: 0,
    needsNodeAPI: false, needsFileSystem: false, ...action };
  // 硬约束：Node API / FS
  if (a.needsNodeAPI && !c.supportsNodeAPI)
    return { strategy: 'delegate-node', reason: '需要 Node API——Edge 不支持' };
  if (a.needsFileSystem && !c.supportsFS)
    return { strategy: 'delegate-node', reason: '需要文件系统——Edge 不支持' };
  // 软约束：时长 / 内存
  if (a.estimatedDurationMs > c.maxDurationMs || a.memoryMB > c.maxMemoryMB)
    return { strategy: 'delegate-queue', reason: `超出 Edge 资源限制 (${a.estimatedDurationMs}ms/${a.memoryMB}MB)` };
  return { strategy: 'edge-direct', reason: 'Edge 资源充足——直接执行' };
}

// 自测
const edgeConstraints = { maxDurationMs: 30000, maxMemoryMB: 128,
  supportsNodeAPI: false, supportsFS: false };
// 轻 CRUD → edge-direct
console.log(edgeActionAdapter({ name: 'createPost', estimatedDurationMs: 500, memoryMB: 10 }, edgeConstraints).strategy === 'edge-direct');
// 长操作 → delegate-queue
r = edgeActionAdapter({ name: 'generateReport', estimatedDurationMs: 60000, memoryMB: 50 }, edgeConstraints);
console.log(r.strategy === 'delegate-queue');
// 大内存 → delegate-queue
r = edgeActionAdapter({ name: 'processImage', estimatedDurationMs: 1000, memoryMB: 200 }, edgeConstraints);
console.log(r.strategy === 'delegate-queue');
// 需要 Node API → delegate-node
r = edgeActionAdapter({ name: 'cryptoOp', needsNodeAPI: true }, edgeConstraints);
console.log(r.strategy === 'delegate-node');
// 需要 FS → delegate-node
r = edgeActionAdapter({ name: 'writeFile', needsFileSystem: true }, edgeConstraints);
console.log(r.strategy === 'delegate-node');
// Node API 优先于时长
r = edgeActionAdapter({ name: 'x', needsNodeAPI: true, estimatedDurationMs: 60000 }, edgeConstraints);
console.log(r.strategy === 'delegate-node');             // 硬约束优先
// 空
console.log(edgeActionAdapter({}, {}).strategy === 'edge-direct');
```

**评分点**：
- 硬约束优先（Node API/FS 不可绕 → delegate-node）；软约束（duration/memory → delegate-queue）
- 三种策略（edge-direct/delegate-queue/delegate-node——RBL-568 的三种适配路径）；约束缺失默认支持
- 边界（空 constraints 全支持/Node API+duration 超限=delegate-node 优先/estimatedDurationMs 缺失）
- 能说清「Edge 限制影响架构设计而非部署选择：硬约束（Node API/FS）切 runtime、软约束（时长/内存）切队列」属于加分
