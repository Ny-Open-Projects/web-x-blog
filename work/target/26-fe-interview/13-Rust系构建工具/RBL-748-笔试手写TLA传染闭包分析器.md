---
title: [RBL-748] 笔试：手写 TLA 传染闭包分析器（异步闭包判定 + 格式冲突检测）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-748：笔试：手写 TLA 传染闭包分析器（异步闭包 + 格式冲突）

**答**：实现 `analyzeTLA(modules)`。modules: `Map<id, { code, format: 'es'|'cjs', deps: string[] }>`（TLA 判定：es 格式且 code 含模块级 `await ` 语句——行首或分号后）。返回 `{ asyncClosure: string[], conflicts: Array<{ mod, importer, reason }>, syncRoots: string[] }`：1) asyncClosure = TLA 模块的「导入者闭包」（含 TLA 模块自身，环去重）；2) conflicts：闭包中 format!=='es' 的模块（TLA 传染到 CJS 是错误）记录冲突对；3) syncRoots = 既不在异步闭包又非 CJS 的模块（可安全合同步 chunk）。边界：无 TLA；TLA 模块互相引用（环）。

```javascript
function analyzeTLA(modules) {
  const hasTLA = (m) => m.format === 'es' &&
    /(^|[;}\n])\s*await\s+(?!\s*function|async)/.test(m.code);
  const tlaRoots = [...modules.entries()].filter(([, m]) => hasTLA(m)).map(([id]) => id);

  const closure = new Set();
  const importersOf = (id) =>
    [...modules.entries()].filter(([, m]) => m.deps.includes(id)).map(([k]) => k);
  const spread = (id) => {
    if (closure.has(id)) return;
    closure.add(id);
    for (const p of importersOf(id)) spread(p);
  };
  tlaRoots.forEach(spread);

  const conflicts = [];
  for (const id of closure) {
    const m = modules.get(id);
    if (m.format !== 'es')
      for (const dep of m.deps)
        if (tlaRoots.includes(dep) || closure.has(dep))
          conflicts.push({ mod: id, importer: dep, reason: `CJS 模块 ${id} 依赖 TLA 闭包` });
  }
  const syncRoots = [...modules.keys()].filter(id =>
    !closure.has(id) && modules.get(id).format === 'es');
  return { asyncClosure: [...closure], conflicts, syncRoots };
}

// 自测
const modules = new Map([
  ['entry', { code: 'import "./a";', format: 'es', deps: ['a'] }],
  ['a', { code: 'const c = await cfg();', format: 'es', deps: ['b'] }],     // TLA
  ['b', { code: 'export default 1;', format: 'es', deps: [] }],
  ['legacy', { code: 'require("./a");', format: 'cjs', deps: ['a'] }],      // CJS 依赖 TLA -> 冲突
  ['pure', { code: 'export const x = 1;', format: 'es', deps: [] }],
]);
let r = analyzeTLA(modules);
console.log(r.asyncClosure.sort().join(','));            // a,entry,legacy
console.log(r.conflicts.some(c => c.mod === 'legacy'));
console.log(r.syncRoots.sort().join(','));               // b,pure

// 无 TLA
r = analyzeTLA(new Map([['x', { code: 'const y = 1;', format: 'es', deps: [] }]]));
console.log(r.asyncClosure.length === 0 && r.conflicts.length === 0 && r.syncRoots.join(',') === 'x');

// TLA 环
r = analyzeTLA(new Map([
  ['p', { code: 'await x();', format: 'es', deps: ['q'] }],
  ['q', { code: 'await y();', format: 'es', deps: ['p'] }],
]));
console.log(r.asyncClosure.sort().join(',') === 'p,q');  // 环收敛不爆栈
```

**评分点**：
- TLA 判定合理（es 格式 + 模块级 await 的正则近似，能说明声明式 await vs 函数内 await 的区分努力）
- 传染闭包 = 导入者反向闭包（含环去重）；CJS 冲突记录带方向
- syncRoots 正确（异步闭包外且 es）；无 TLA 边界
- 能说清「TLA 传染决定 chunk 合并约束（异步闭包不可进同步 chunk）」属于加分
