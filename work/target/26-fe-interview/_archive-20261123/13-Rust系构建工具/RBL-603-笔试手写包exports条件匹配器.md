---
title: [RBL-603] 笔试：手写 package exports 条件匹配器（通配符 + 条件优先级）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-603：笔试：手写 package exports 条件匹配器（通配符 + 条件优先级）

**需求**：实现 `matchExports(exports, subpath, conditions)`。exports 形如 `{ ".": {...} | string, "./x": ..., "./feat/*": "./src/*.js", "./nested": { "node": {...}, "default": "./n.js" } }`，subpath 如 `.`、`./x`、`./feat/a`。规则：1) 精确 key 优先于通配 key；2) 通配 `*` 把剩余部分代入目标（目标也含 `*`）；3) 值为对象时按 conditions **从左到右**深度优先匹配（对象可嵌套），无命中返回 null；4) 条件串值直接返回；5) 未列出 subpath 返回 null（封装语义）；6) 子路径不允许越过包根（`./../x` 返回 null）。

```javascript
function matchExports(exports, subpath, conditions) {
  if (!/^\./.test(subpath)) return null;
  if (subpath.includes('..') || subpath.includes('\\')) return null;   // 越根防护

  // 精确 key 优先
  if (exports[subpath] !== undefined) return resolveTarget(exports[subpath], '', conditions);
  // 通配 key：取最长匹配
  const wild = Object.keys(exports)
    .filter(k => k.includes('*'))
    .map(k => ({ k, pre: k.slice(0, k.indexOf('*')) }))
    .filter(({ pre }) => subpath.startsWith(pre))
    .sort((a, b) => b.pre.length - a.pre.length)[0];
  if (wild) {
    const rest = subpath.slice(wild.pre.length);
    return resolveTarget(exports[wild.k], rest, conditions);
  }
  return null;
}

function resolveTarget(target, wildcard, conditions) {
  if (typeof target === 'string') return target.replaceAll('*', wildcard);
  for (const k of Object.keys(target)) {                // 从左到右
    if (k === 'default' || conditions.includes(k)) {
      const r = resolveTarget(target[k], wildcard, conditions);
      if (r !== null) return r;                         // 命中即用（允许内部 null 继续下个条件？规范是命中即递归）
    }
  }
  return null;
}

// 自测
const pkg = {
  '.': { import: './esm/index.js', require: './cjs/index.cjs', default: './index.js' },
  './lite': './lite.js',
  './feat/*': './src/features/*.js',
  './env': { browser: './env.browser.js', default: './env.node.js' },
};
const conds = ['import', 'browser'];
console.log(matchExports(pkg, '.', conds));                       // './esm/index.js'
console.log(matchExports(pkg, './lite', []));                     // './lite.js'（字符串无条件）
console.log(matchExports(pkg, './feat/modal', conds));            // './src/features/modal.js'
console.log(matchExports(pkg, './env', conds));                   // './env.browser.js'
console.log(matchExports(pkg, './private', conds));               // null（封装）
console.log(matchExports(pkg, '../escape', conds));               // null（越根）
console.log(matchExports({ '.': { unknown: './a.js' } }, '.', []));  // null（条件不匹配）
console.log(matchExports({ '.': { unknown: './a.js', default: './b.js' } }, '.', []));  // './b.js'
```

**评分点**：
- 精确 key 优先与通配最长匹配正确；通配双向代入（key 的 * 与目标字符串的 *）
- 条件从左到右匹配且支持 default 兜底、嵌套对象递归
- 封装语义（未列 subpath -> null）与越根防护（.. / 反斜杠）齐全
- 能说明「同条件同时给 import/require 时按声明顺序而非 conditions 顺序」的规范细节属于加分
