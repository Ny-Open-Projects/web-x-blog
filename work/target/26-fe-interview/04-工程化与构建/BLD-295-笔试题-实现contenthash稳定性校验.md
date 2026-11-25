---
title: [BLD-295] 笔试题——实现 contenthash 稳定性校验（无关变更不传染）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-295：手写 hash 稳定性校验

**需求与边界**：
- 需求：验证「无关变更不传染」——变更模块 A 后，只有包含 A（或受 A 影响）的 chunk hash 变化，其余 chunk hash 不变（SCN-BLD-219 长缓存核心）。
- 边界：① module ID 稳定性检测（自增 ID 平移会让全部 chunk 变——检测方式：插入新模块后对比其他模块的 ID）；② 跨 chunk 引用传染（shared chunk 变化传染所有引用者——预期行为，报告区分）；③ 输出传染报告（哪些 chunk 变了/为什么）。

**答**：
```javascript
async function hashStabilityCheck(bundler, project) {
  const base = await bundler.build(project);           // 基线
  // 1. 插入新模块（检测 ID 平移）
  const withInsert = await bundler.build(insertNewModule(project));
  const idShift = detectIdShift(base.moduleIds, withInsert.moduleIds);
  // 2. 无关变更传染检测
  const unrelated = await bundler.build(touchModule(project, 'unrelated-module.ts'));
  const changed = diffChunks(base.chunks, unrelated.chunks);   // hash 变化的 chunk
  const expected = chunksContaining('unrelated-module');
  const unexpected = changed.filter(c => !expected.includes(c.name) && !isSharedDependency(c));
  return {
    moduleIdsStable: !idShift,                        // deterministic ID 检查
    contagion: { changed: changed.map(c => c.name), expected: expected.map(c => c.name),
                 unexpected },                        // 传染报告
    verdict: !idShift && unexpected.length === 0 ? 'STABLE' : 'UNSTABLE',
    fix: idShift ? '启用 deterministic moduleIds（SCN-BLD-219）' : null,
  };
}
```

**评分点**:
- 两个不变式（ID 稳定 + 无关变更不传染）。
- 传染报告区分预期（共享依赖传染）与异常（unexpected）。
- ID 平移检测方法（插入新模块对比）。
- 修复建议映射（deterministic IDs）。
