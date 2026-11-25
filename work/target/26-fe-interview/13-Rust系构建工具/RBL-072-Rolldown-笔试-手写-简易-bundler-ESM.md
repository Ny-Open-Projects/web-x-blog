---
title: [RBL-072] 笔试：手写简易 ESM bundler（export 语句解析 + live binding）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-072：笔试：手写简易 ESM bundler（export 语句解析 + live binding）
**答**：在 RBL-042 基础上实现 ESM 语义：1) 解析 named export（export const/function/{}）与 default export；2) 产物用 getter 形式导出实现 live binding（`__esModule` + Object.defineProperty）；3) import 的具名成员通过访问器取值（保证循环依赖时读到最新值）；4) re-export 透传（export * from）；5) 说明为什么不能简单用值拷贝。

```javascript
function parseExports(code) {
  const named = [], hasDefault = /export\s+default/.test(code);
  for (const m of code.matchAll(/export\s+(?:const|let|var|function|class)\s+(\w+)/g))
    named.push(m[1]);
  for (const m of code.matchAll(/export\s*\{([^}]+)\}/g))
    named.push(...m[1].split(',').map(s => s.split(/\s+as\s+/).pop().trim()));
  return { named, hasDefault };
}

function bundleESM(entry) {
  // graph 构建同 RBL-042（此处省略 buildGraph），多拿 exports 信息
  const { graph, idOf } = buildGraph(entry);
  const modules = [...graph.values()].map(m => {
    const { named, hasDefault } = parseExports(m.code);
    const setters = [
      ...(hasDefault ? ['(m) => m.default'] : []),
      ...named.map(n => `(m) => m.${n}`),
    ];
    // 产物模块包装：getters 实现 live binding
    return `${m.id}: [function(exports, require){\n${m.code}\n}, ` +
      `[${m.deps.map(d => idOf.get(d))}], ${JSON.stringify(named)}, ${hasDefault}],`;
  }).join('\n');

  const runtime = `
    const cache = {};
    function require(id) {
      if (cache[id]) return cache[id].ns;
      const [factory, deps, named, hasDefault] = modules[id];
      const ns = {};                    // namespace 对象
      cache[id] = { ns };               // 先占位：循环依赖时也能拿到 ns
      const exports = {};
      Object.defineProperty(exports, '__esModule', { value: true });
      factory((x) => require(deps[x]).ns, exports);
      // live binding：导出用 getter 延迟取值，循环引用时读到最新
      for (const n of named)
        Object.defineProperty(ns, n, { enumerable: true, get: () => exports[n] });
      if (hasDefault)
        Object.defineProperty(ns, 'default', { enumerable: true, get: () => exports.default });
      return cache[id];
    }
    require(0);`;
  return `(function(){ const modules = {\n${modules}\n}; ${runtime} })();`;
}
```
**评分点**：
- exports 解析覆盖 const/function/{}/default 三类。
- 循环依赖 + live binding：占位 ns + getter 延迟求值（核心考点）。
- `__esModule` 标记（互操作契约）。
- 能答出值拷贝的问题：导入方拿到旧值，环依赖下读到 undefined。
- re-export 处理（export * 转发）加额外分。
