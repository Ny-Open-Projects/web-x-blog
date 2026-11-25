---
title: [1211] 笔试手写：实现并发乐观更新的 patch 回滚
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, TanStack Query]
type: 笔试题
---

## 1211：笔试手写：实现并发乐观更新的 patch 回滚

**答**：实现 PatchList：apply(patch)（记录并返回 applyFn 应用于数据的函数——patch 为 { id, changes } 针对列表按 id 更新）；rollback(patchId) 只撤销指定 patch（从记录移除并重放剩余 patch 到基线）。data 存于闭包，base 由构造传入。要求并发 apply 后单条回滚不污染其他 patch。

```js
function createPatchList(base) {
  let data = structuredClone(base);
  const patches = new Map();   // id -> patch
  const applyPatch = p => {
    data = data.map(item =>
      item.id === p.id ? { ...item, ...p.changes } : item);
  };
  const replay = () => {
    data = structuredClone(base);
    patches.forEach(applyPatch);           // 从基线重放全部存活 patch
  };
  return {
    apply(id, patch) { patches.set(id, patch); applyPatch(patch); return data; },
    rollback(id) {
      if (!patches.has(id)) return data;
      patches.delete(id);
      replay();                            // 重放剩余 patch（不污染他人）
      return data;
    },
    get data() { return data; },
  };
}
const pl = createPatchList([{ id: 1, s: 'a' }, { id: 2, s: 'b' }]);
pl.apply('p1', { id: 1, changes: { s: 'A' } });
pl.apply('p2', { id: 2, changes: { s: 'B' } });
console.log(pl.rollback('p1'));   // p1 回滚，p2 保留 -> [{id:1,s:'a'},{id:2,s:'B'}]
```

**评分点**：
- 快照重放策略（回滚指定 patch = 基线 + 剩余重放——对比快照法的并发正确性优势）
- structuredClone 防基线污染
- Map 管理 patch 生命周期（重复回滚幂等）
- 能讨论：重放成本 vs 快照栈成本的权衡、patch 顺序敏感操作的局限（非交换操作需顺序保真）

