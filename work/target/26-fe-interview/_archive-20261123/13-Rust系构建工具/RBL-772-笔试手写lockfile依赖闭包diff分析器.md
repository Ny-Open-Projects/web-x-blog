---
title: [RBL-772] 笔试：手写 lockfile 闭包 diff 分析器（直接/传递分类 + 风险关键词）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-772：笔试：手写 lockfile 闭包 diff 分析器（直接/传递 + 风险词）

**需求**：实现 `lockDiff(before, after)`。两份 lockfile 均为 `Record<name, { version, depth, requiredBy: string[] }>`（depth 0=直接依赖）。返回：1) `{ added: Array<{ name, version, depth, risk }>, removed: string[], upgraded: Array<{ name, from, to, depth, risk }>, transitiveCount }`；2) risk 判定：depth > 1 → 'transitive'（被动升级）；任一 requiredBy 为空且 depth>0 → 'orphan'（异常）；3) upgraded 且 depth === 0 计 major 风险（版本号 major 变化 → risk 'major'）；4) transitiveCount = depth>1 的升级+新增数。边界：两份完全相同返回全空；包消失。

```javascript
function lockDiff(before, after) {
  const added = [], removed = [], upgraded = [];
  let transitiveCount = 0;
  const names = new Set([...Object.keys(before), ...Object.keys(after)]);

  for (const name of names) {
    const b = before[name], a = after[name];
    if (b && !a) { removed.push(name); continue; }
    if (!b && a) {
      const risk = a.depth > 1 ? 'transitive' : (a.requiredBy?.length ? 'ok' : 'orphan');
      if (a.depth > 1) transitiveCount++;
      added.push({ name, version: a.version, depth: a.depth, risk });
      continue;
    }
    if (b.version !== a.version) {
      const majorChanged = b.version.split('.')[0] !== a.version.split('.')[0];
      const risk = a.depth > 1 ? 'transitive'
        : majorChanged ? 'major'
        : (a.requiredBy?.length ? 'minor-patch' : 'orphan');
      if (a.depth > 1) transitiveCount++;
      upgraded.push({ name, from: b.version, to: a.version, depth: a.depth, risk });
    }
  }
  const s = (arr, k) => arr.sort((x, y) => (x[k] > y[k] ? 1 : -1));
  s(added, 'name'); s(upgraded, 'name');
  return { added, removed: removed.sort(), upgraded, transitiveCount };
}

// 自测
const before = {
  react: { version: '18.2.0', depth: 0, requiredBy: [] },
  lodash: { version: '4.17.20', depth: 0, requiredBy: [] },
  'react-dom': { version: '18.2.0', depth: 0, requiredBy: [] },
  scheduler: { version: '0.23.0', depth: 1, requiredBy: ['react-dom'] },
  loose: { version: '1.0.0', depth: 2, requiredBy: ['lodash'] },
};
const after = {
  react: { version: '19.0.0', depth: 0, requiredBy: [] },          // major 升级
  lodash: { version: '4.17.21', depth: 0, requiredBy: [] },        // patch
  'react-dom': { version: '19.0.0', depth: 0, requiredBy: [] },
  scheduler: { version: '0.24.0', depth: 1, requiredBy: ['react-dom'] },
  'new-trans': { version: '2.1.0', depth: 3, requiredBy: ['react'] },  // 传递新增
};
let r = lockDiff(before, after);
console.log(r.upgraded.find(u => u.name === 'react').risk === 'major');
console.log(r.upgraded.find(u => u.name === 'lodash').risk === 'minor-patch');
console.log(r.upgraded.find(u => u.name === 'scheduler').risk === 'minor-patch');  // depth 1 非 transitive
console.log(r.added[0].name === 'new-trans' && r.added[0].risk === 'transitive');
console.log(r.transitiveCount === 1);
console.log(r.removed.length === 1 && r.removed[0] === 'loose');

console.log(JSON.stringify(lockDiff(before, before)) ===
  JSON.stringify({ added: [], removed: [], upgraded: [], transitiveCount: 0 }));
```

**评分点**：
- 三类变化齐全（added/removed/upgraded）；depth>1 判传递被动升级
- risk 分级正确：major（直接依赖跨主版本）、transitive（depth>1）、orphan（无 requiredBy 异常）
- transitiveCount 统计准确；相同 lockfile 返回全空
- 能说清「传递依赖被动升级是升级风险的暗礁，需 diff 全闭包」属于加分
