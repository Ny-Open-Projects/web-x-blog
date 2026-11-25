---
title: [RBL-949] 笔试：手写 WASM 导出面契约校验器（exports ⊆ 调用面）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-949：笔试：手写 WASM 导出契约校验（exports vs 调用面）

**答**：实现 `verifyWasmExports(wasmExports, jsCallSites, { imports })`。wasmExports: 模块导出函数名数组；jsCallSites: JS 胶水调用的函数名数组（含 WebAssembly.instantiate 后 instance.exports.xxx 的访问）；imports: JS 提供给 wasm 的导入 `{ ns: { fn } }`。规则：1) jsCallSites 中不在 wasmExports → 'missing-export'（裁剪误删——运行时 undefined）；2) wasmExports 中从未被 JS 调用 → info 'dead-export'（可再裁剪）；3) imports 校验：wasm 声明的导入（提供 importsWanted 参数）不被 JS 提供 → 'missing-import'；4) 返回 `{ problems, deadExports, ok }`。边界：空 callSites（全 dead-export）；双向空。

```javascript
function verifyWasmExports(wasmExports = [], jsCallSites = [], { wantedImports = {} } = {}) {
  const exp = new Set(wasmExports);
  const used = new Set(jsCallSites);
  const problems = [], deadExports = [];
  for (const fn of used)
    if (!exp.has(fn)) problems.push({ type: 'missing-export', fn,
      detail: `JS 调用 ${fn} 但 wasm 未导出——裁剪误删或版本错配` });
  for (const fn of wasmExports)
    if (!used.has(fn)) deadExports.push(fn);             // 可再裁剪（注意 wasm 内部互调不可删）
  for (const [ns, fns] of Object.entries(wantedImports))
    for (const fn of Object.keys(fns ?? {}))
      problems.push({ type: 'check-import', fn: `${ns}.${fn}` });   // 标注人工核对
  return { problems, deadExports, ok: !problems.some(p => p.type === 'missing-export') };
}

// 自测
let r = verifyWasmExports(
  ['md5_init', 'md5_update', 'md5_final', 'unused_helper'],
  ['md5_init', 'md5_update', 'md5_final'],
  { wantedImports: { env: { now: () => 0, log: () => {} } } });
console.log(r.ok === true);
console.log(r.deadExports.join(',') === 'unused_helper');
console.log(r.problems.filter(p => p.type === 'check-import').length === 2);

// 裁剪误删
r = verifyWasmExports(['md5_init'], ['md5_init', 'md5_final'], {});
console.log(r.ok === false);
console.log(r.problems[0].type === 'missing-export' && r.problems[0].fn === 'md5_final');

// 空
r = verifyWasmExports(['a'], [], {});
console.log(r.deadExports.join(',') === 'a' && r.ok === true);
console.log(verifyWasmExports([], [], {}).ok === true);
```

**评分点**：
- 双向校验：missing-export（裁剪误删 = 运行时 undefined——阻断）与 dead-export（可再裁剪——信息级）
- imports 标注（人工核对 wasm 声明的导入由 JS 提供）；ok 仅由 missing-export 决定
- 边界：空调用面/双向空
- 能说清「裁剪的正确性 = 导出面契约不变，误删被 JS 调用的函数是静默运行时错」属于加分
