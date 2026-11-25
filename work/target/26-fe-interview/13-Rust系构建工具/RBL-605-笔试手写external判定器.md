---
title: [RBL-605] 笔试：手写 external 判定器（场景配置 + 子路径 + 防误判）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-605：笔试：手写 external 判定器（场景配置 + 子路径 + 防误判）

**答**：实现 `isExternal(id, importer, ctx)`。ctx: `{ env: 'web'|'ssr'|'sdk', globals: string[], peers: string[], aliases: string[] }`。规则：1) 相对路径（./ ../）与绝对路径永外置 false；2) alias 命中（全等或前缀子路径）按 alias 目标处理（视为可解析，false）；3) env=ssr：裸导入全外置；4) env=sdk：仅 peers 及其 `/子路径` 外置；5) env=web：globals 列表外置（全等即可，不含子路径除非列表项以 `/` 结尾表示前缀匹配）；6) `data:` / `virtual:` 前缀（虚拟模块）返回特殊标记 `{ virtual: true }` 不走普通流程；7) 内置模块（node: 前缀）在 env=ssr 时外置、web 时报错级别返回 `{ error: true }`。

```javascript
function isExternal(id, importer, ctx) {
  if (id.startsWith('virtual:') || id.startsWith('\0')) return { virtual: true };
  if (id.startsWith('./') || id.startsWith('../') || path.isAbsoluteSafe(id)) return false;
  if (id.startsWith('node:')) return ctx.env === 'ssr' ? true : { error: true };
  if (ctx.aliases.some(a => id === a || id.startsWith(a + '/'))) return false;  // alias 可解析
  if (ctx.env === 'ssr') return true;                    // 裸导入全外置
  if (ctx.env === 'sdk')
    return ctx.peers.some(p => id === p || id.startsWith(p + '/'));
  // web
  return ctx.globals.some(g =>
    g.endsWith('/') ? id.startsWith(g) : id === g);
}
path.isAbsoluteSafe = (s) => s.startsWith('/');

// 自测
const ssr = { env: 'ssr', globals: [], peers: [], aliases: ['@app'] };
const sdk = { env: 'sdk', globals: [], peers: ['react'], aliases: ['@app'] };
const web = { env: 'web', globals: ['react', 'lodash/'], peers: [], aliases: ['@app'] };

console.log(isExternal('./util', '/a.js', ssr) === false);          // 相对不外置
console.log(isExternal('react', '/a.js', ssr) === true);            // ssr 全外置
console.log(isExternal('@app/core', '/a.js', ssr) === false);       // alias 不外置
console.log(isExternal('react/jsx-runtime', '/a.js', sdk) === true);// sdk peers 含子路径
console.log(isExternal('vue', '/a.js', sdk) === false);             // 非 peer 内联
console.log(isExternal('lodash/cloneDeep', '/a.js', web) === true); // web 前缀匹配
console.log(isExternal('lodash-es', '/a.js', web) === false);       // 非全等不误伤
console.log(isExternal('virtual:css', '/a.js', web).virtual === true);
console.log(isExternal('node:fs', '/a.js', web).error === true);    // web 中内置模块报错
console.log(isExternal('node:fs', '/a.js', ssr) === true);
```

**评分点**：
- 相对/绝对路径硬性不外置（防函数式 external 最常见的误判事故）
- alias 命中先于场景规则（用户显式配置优先）
- 子路径语义正确：sdk peers 含 `/` 子路径、web globals 全等或显式前缀
- 虚拟模块与 node: 内置的特殊处理路径完整（返回结构化标记而非布尔）
