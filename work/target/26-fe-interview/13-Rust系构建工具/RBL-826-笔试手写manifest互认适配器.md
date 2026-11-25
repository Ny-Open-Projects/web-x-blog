---
title: [RBL-826] 笔试：手写 manifest 互认适配器（双源统一 + 语义等价断言）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-826：笔试：手写 manifest 互认适配器（双源统一 + 语义断言）

**答**：实现 `fromWebpack(stats)` 与 `assertSemanticEq(m1, m2)`。webpack stats: `{ assets: Array<{ name, size, contenthash?, chunks?: string[], isEntry? }>, entrypoints?: Record<name, { assets: string[] }> }`。规则：1) role 判定：isEntry → 'entry'；chunks 含 vendor/runtime 字样 → 'vendor'；其他 → 'async'；无 chunks → 'asset'；2) closures 从 entrypoints 生成（asset → { name, role }）；3) assertSemanticEq：outputs 的 name 集合一致（排序比较），不一致抛错列出 diff（m1 有/m2 有分别列出）；同时比较 entry 数量。边界：无 entrypoints（closures 空）；contenthash 缺失用 null。

```javascript
const roleOf = (a) => a.isEntry ? 'entry'
  : a.chunks?.some(c => /vendor|runtime/i.test(c)) ? 'vendor'
  : a.chunks?.length ? 'async' : 'asset';

function fromWebpack(stats) {
  const outputs = stats.assets.map(a => ({
    name: a.name, role: roleOf(a), bytes: a.size, hash: a.contenthash ?? null,
  }));
  const closures = stats.entrypoints
    ? Object.fromEntries(Object.entries(stats.entrypoints).map(([e, v]) =>
        [e, v.assets.map(n => ({ name: n, role: roleOf(stats.assets.find(a => a.name === n) ?? {})) }))])
    : {};
  return { version: '1.0', outputs, closures };
}

function assertSemanticEq(m1, m2) {
  const names = (m) => m.outputs.map(o => o.name).sort();
  const s1 = names(m1), s2 = names(m2);
  const only1 = s1.filter(n => !s2.includes(n));
  const only2 = s2.filter(n => !s1.includes(n));
  const entries1 = Object.keys(m1.closures).length;
  const entries2 = Object.keys(m2.closures).length;
  if (only1.length || only2.length || entries1 !== entries2)
    throw new Error(`manifest 语义不等: m1独有=[${only1}] m2独有=[${only2}] entries=${entries1}/${entries2}`);
  return true;
}

// 自测
const stats = {
  assets: [
    { name: 'index.html', size: 800 },
    { name: 'main.js', size: 1000, contenthash: 'h1', isEntry: true, chunks: ['main'] },
    { name: 'vendor.js', size: 5000, contenthash: 'h2', chunks: ['vendor'] },
    { name: 'lazy.js', size: 2000, contenthash: 'h3', chunks: ['lazy'] },
  ],
  entrypoints: { main: { assets: ['main.js', 'vendor.js'] } },
};
let m = fromWebpack(stats);
console.log(m.outputs.find(o => o.name === 'main.js').role === 'entry');
console.log(m.outputs.find(o => o.name === 'vendor.js').role === 'vendor');
console.log(m.outputs.find(o => o.name === 'lazy.js').role === 'async');
console.log(m.outputs.find(o => o.name === 'index.html').role === 'asset');
console.log(m.closures.main.length === 2);

// 等价断言
const m2 = { version: '1.0',
  outputs: stats.assets.map(a => ({ name: a.name, role: roleOf(a), bytes: a.size, hash: a.contenthash ?? null })),
  closures: { main: m.closures.main } };
console.log(assertSemanticEq(m, m2) === true);

// 不等
const m3 = { ...m2, outputs: m2.outputs.filter(o => o.name !== 'lazy.js') };
let e; try { assertSemanticEq(m, m3); } catch (x) { e = x; }
console.log(/lazy\.js/.test(e.message) && /m2独有/.test(e.message));

// 无 entrypoints
console.log(Object.keys(fromWebpack({ assets: stats.assets }).closures).length === 0);
```

**评分点**：
- role 判定四态（entry/vendor/async/asset）语义对齐而非字段重命名；hash 缺省 null
- closures 从 entrypoints 生成（role 查找原 asset 元数据）；无 entrypoints 空闭包
- 断言输出可诊断（m1 独有/m2 独有/entry 计数）
- 能说清「统一 schema 是 N+M 适配替代 N×M，让构建器可替换成为架构属性」属于加分
