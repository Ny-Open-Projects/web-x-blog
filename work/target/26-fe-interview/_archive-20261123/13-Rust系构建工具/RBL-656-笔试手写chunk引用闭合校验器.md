---
title: [RBL-656] 笔试：手写产物引用闭合校验器（缺失引用/悬空产物/循环预载）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-656：笔试：手写产物引用闭合校验器（缺失引用/悬空产物/循环预载）

**需求**：实现 `verifyClosure(chunks, entry)`。chunks: `{ id, imports: string[], dynamicImports: string[] }[]`。校验三性质并返回 `{ problems: Array<{ type, detail }> }`：1) `missing-ref`：任何 chunk（含 entry）引用的 chunk 未在产物中；2) `orphan`：产物中存在从 entry 不可达的 chunk（静态或动态引用都算可达）；3) `dynamic-cycle`：动态 import 形成的环（跨 chunk 动态循环加载会死锁——A 动态引 B、B 动态引 A）。entry 必须存在，否则返回 `missing-entry`。全绿返回空 problems。

```javascript
function verifyClosure(chunks, entry) {
  const byId = new Map(chunks.map(c => [c.id, c]));
  const problems = [];
  if (!byId.has(entry)) return { problems: [{ type: 'missing-entry', detail: entry }] };

  // 1) 缺失引用
  for (const c of chunks)
    for (const ref of [...c.imports, ...c.dynamicImports])
      if (!byId.has(ref)) problems.push({ type: 'missing-ref', detail: `${c.id} -> ${ref}` });

  // 2) 可达性（静态 + 动态都算）
  const reachable = new Set([entry]);
  const queue = [entry];
  while (queue.length) {
    const id = queue.shift();
    const c = byId.get(id);
    for (const ref of [...c.imports, ...c.dynamicImports])
      if (byId.has(ref) && !reachable.has(ref)) { reachable.add(ref); queue.push(ref); }
  }
  for (const c of chunks)
    if (!reachable.has(c.id)) problems.push({ type: 'orphan', detail: c.id });

  // 3) 动态环（只看 dynamicImports 边）
  const dynState = new Map();                            // 0 未访问 1 在栈 2 完成
  const dynCycle = (id, path) => {
    const st = dynState.get(id) ?? 0;
    if (st === 1) return path.slice(path.indexOf(id)).concat(id);   // 环路径
    if (st === 2) return null;
    dynState.set(id, 1);
    for (const d of byId.get(id).dynamicImports) {
      if (!byId.has(d)) continue;
      const r = dynCycle(d, [...path, id]);
      if (r) return r;
    }
    dynState.set(id, 2);
    return null;
  };
  for (const c of chunks) {
    const cyc = dynCycle(c.id, []);
    if (cyc) { problems.push({ type: 'dynamic-cycle', detail: cyc.join(' -> ') }); break; }
  }
  return { problems };
}

// 自测
const chunks = [
  { id: 'main', imports: ['vendor'], dynamicImports: ['admin'] },
  { id: 'vendor', imports: [], dynamicImports: [] },
  { id: 'admin', imports: ['vendor'], dynamicImports: [] },
  { id: 'ghost-chunk', imports: [], dynamicImports: [] },            // 孤儿
  { id: 'lost', imports: [], dynamicImports: [] },                   // 孤儿（同上）
];
let r = verifyClosure(chunks, 'main');
console.log(r.problems.filter(p => p.type === 'orphan').map(p => p.detail).sort().join(','));

// 缺失引用
r = verifyClosure([{ id: 'main', imports: ['nope'], dynamicImports: [] }], 'main');
console.log(r.problems[0].type === 'missing-ref' && r.problems[0].detail === 'main -> nope');

// 动态环
r = verifyClosure([
  { id: 'a', imports: [], dynamicImports: ['b'] },
  { id: 'b', imports: [], dynamicImports: ['a'] },
], 'a');
console.log(r.problems[0].type === 'dynamic-cycle' && /a -> b -> a/.test(r.problems[0].detail));

// 全绿
r = verifyClosure([
  { id: 'main', imports: ['v'], dynamicImports: ['d'] },
  { id: 'v', imports: [], dynamicImports: [] },
  { id: 'd', imports: ['v'], dynamicImports: [] },
], 'main');
console.log(r.problems.length === 0);

r = verifyClosure([], 'main');
console.log(r.problems[0].type === 'missing-entry');
```

**评分点**：
- 三性质完整：缺失引用双向（引用者->被引用者可读）、可达性含动态边、动态环单 DFS 状态机
- 可达性与孤儿判定正确（静态与动态都算可达，孤儿列出全部）
- 动态环检测不死循环（三态标记），环路径可读（a -> b -> a）
- 能说清「动态跨 chunk 循环加载会死锁所以必须禁止」属于加分
