---
title: [AIC-508] 笔试：手写 AI 幻觉依赖检测器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-508：笔试：手写 AI 幻觉依赖检测

**答**：实现 `detectHallucinations(code, { lockfile, knownAPIs })`。lockfile: `Record<package, version>`；knownAPIs: `Record<global, string[]>`（全局对象 → 方法列表——如 `Array: ['push','pop','filter','map',...]`）。规则：1) **依赖幻觉**：import 的包不在 lockfile → 'hallucinated-dep'；2) **API 幻觉**：`arr.method()` 检查 method 是否在 knownAPIs.Array → 'hallucinated-api'（简化：只检查已知全局对象的方法调用）；3) **类型幻觉**：`as any` / `as unknown as` → 'type-escape'（RBL-627 类型逃逸的幻觉维度）；4) 返回 `{ hallucinations: Array<{ type, detail, line? }>, ok }`（ok = 无 hallucination）。边界：空 code；无 lockfile（跳过依赖检查）；knownAPIs 空（跳过 API 检查）；knownAPIs 命中（不报）。

```javascript
function detectHallucinations(code = '', { lockfile = {}, knownAPIs = {} } = {}) {
  const hallucinations = [];
  // 1) 依赖幻觉
  for (const m of code.matchAll(/(?:from|require\()\s*['"]([^.'"][^'"]*)['"]/g)) {
    const pkg = m[1].split('/')[0];
    if (!(pkg in lockfile))
      hallucinations.push({ type: 'hallucinated-dep', detail: `package '${pkg}' 不在 lockfile` });
  }
  // 2) API 幻觉：arr.method() 模式
  for (const m of code.matchAll(/(\w+)\s*\.\s*(\w+)\s*\(/g)) {
    const [, obj, method] = m;
    const known = knownAPIs[obj];
    if (known && !known.includes(method) &&
        !['length', 'constructor', 'toString'].includes(method))
      hallucinations.push({ type: 'hallucinated-api',
        detail: `${obj}.${method}() 不在已知 API 列表` });
  }
  // 3) 类型逃逸
  if (/as\s+any\b/.test(code) || /as\s+unknown\s+as/.test(code))
    hallucinations.push({ type: 'type-escape', detail: '类型断言逃逸' });
  return { hallucinations, ok: hallucinations.filter(h => h.type !== 'type-escape').length === 0 };
}

// 自测
const lockfile = { 'lodash-es': '4', 'react': '18' };
const knownAPIs = { Array: ['push', 'pop', 'filter', 'map', 'find', 'slice', 'join', 'reduce'] };
// 依赖幻觉
let r = detectHallucinations("import x from 'lodash-es-deep';", { lockfile });
console.log(r.hallucinations[0].type === 'hallucinated-dep');
console.log(r.ok === false);
// API 幻觉：arr.removeAt 不存在
r = detectHallucinations('const arr = []; arr.removeAt(2);', { knownAPIs });
console.log(r.hallucinations.some(h => h.type === 'hallucinated-api' && h.detail.includes('removeAt')));
// API 已知
r = detectHallucinations('const arr = []; arr.filter(x => x);', { knownAPIs });
console.log(!r.hallucinations.some(h => h.type === 'hallucinated-api'));
// 类型逃逸
r = detectHallucinations('const x = getData() as any;', { lockfile });
console.log(r.hallucinations.some(h => h.type === 'type-escape'));
console.log(r.ok === true);                              // type-escape 不阻断

// 空代码
console.log(detectHallucinations('', { lockfile }).hallucinations.length === 0);
```

**评分点**：
- 三维幻觉检测：依赖（lockfile 比对）/API（knownAPIs 白名单）/类型（逃逸检测）
- knownAPIs 白名单（已知全局对象的方法——简化但可扩展）；knownAPIs 命中不误报
- 边界（空/无 lockfile/无 knownAPIs/type-escape 不阻断）；ok 仅由 hallucinated-dep/api 决定
- 能说清「AI 幻觉的三层检测：编译期 API 幻觉、构建期依赖幻觉、运行时逻辑幻觉——各层检测能力边界不同」属于加分
