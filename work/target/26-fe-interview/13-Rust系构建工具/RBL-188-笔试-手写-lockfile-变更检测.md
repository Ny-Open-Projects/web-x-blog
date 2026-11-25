---
title: [RBL-188] 笔试：手写 lockfile 变更检测（影响哪些包与依赖树）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-188：笔试：手写 lockfile 变更检测（哪些包的依赖变了）

**答**：写 lock-diff.mjs：1) 输入新旧两份 pnpm-lock.yaml（解析为对象即可，不必真解析 yaml）；2) 对比 importers（各 workspace 包的依赖声明段）找出依赖变更的包（新增/删除/版本变化）；3) 对比 packages/snapshots 段找新增与移除的依赖版本条目；4) 输出：{ changedImporters, addedPkgs, removedPkgs }；5) changedImporters 为空但 packages 有变（如共享依赖升级）时输出标记 `shared-only: true` 提示"全仓可能需要重装"。

```javascript
// lock-diff.mjs
function diffDeps(oldD = {}, newD = {}) {
  const keys = new Set([...Object.keys(oldD), ...Object.keys(newD)]);
  const changed = [];
  for (const k of keys) {
    const ov = oldD[k], nv = newD[k];
    if (ov === undefined) changed.push({ pkg: k, change: 'added', to: nv });
    else if (nv === undefined) changed.push({ pkg: k, change: 'removed', from: ov });
    else if (ov !== nv) changed.push({ pkg: k, change: 'version', from: ov, to: nv });
  }
  return changed;
}

export function lockDiff(oldLock, newLock) {
  const changedImporters = [];
  const oldImp = oldLock.importers ?? {}, newImp = newLock.importers ?? {};
  for (const dir of new Set([...Object.keys(oldImp), ...Object.keys(newImp)])) {
    const o = { ...(oldImp[dir]?.dependencies ?? {}), ...(oldImp[dir]?.devDependencies ?? {}) };
    const n = { ...(newImp[dir]?.dependencies ?? {}), ...(newImp[dir]?.devDependencies ?? {}) };
    const d = diffDeps(o, n);
    if (d.length) changedImporters.push({ dir, changes: d });
  }
  const oldPkgs = new Set(Object.keys(oldLock.packages ?? oldLock.snapshots ?? {}));
  const newPkgs = new Set(Object.keys(newLock.packages ?? newLock.snapshots ?? {}));
  const addedPkgs = [...newPkgs].filter(p => !oldPkgs.has(p));
  const removedPkgs = [...oldPkgs].filter(p => !newPkgs.has(p));
  return {
    changedImporters,
    addedPkgs, removedPkgs,
    sharedOnly: changedImporters.length === 0 && (addedPkgs.length || removedPkgs.length) > 0,
  };
}
// 用法示例：
// lockDiff(old, new)
// → { changedImporters: [{dir:'apps/web', changes:[{pkg:'react',change:'version',from:'18.2.0',to:'18.3.0'}]}],
//     addedPkgs:['react@18.3.0'], removedPkgs:['react@18.2.0'], sharedOnly:false }
// CI 用法：changedImporters 非空 → 只重装/重缓存受影响 importer 的 node_modules。
```
**评分点**：
- importer 段与 packages/snapshots 段分开对比（两层语义）。
- 变更三类分类：added/removed/version。
- deps 与 devDeps 合并对比（都触发安装）。
- shared-only 特判（importer 无变但公共依赖变了）。
- 能对接 CI：受影响 importer 缩小缓存/重装范围。
