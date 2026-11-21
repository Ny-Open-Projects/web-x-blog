---
title: [RBL-096] 笔试：手写按需编译 server（请求驱动 + 缓存命中）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-096：笔试：手写按需编译 server（请求驱动 + 缓存命中）
**题目**：实现 lazyCompiler：1) handle(reqPath) 处理模块请求（如 /src/App.tsx）；2) 首次请求：递归收集该模块的同步依赖子图并编译，返回产物；3) 再次请求：缓存命中直接返回；4) 子图中任一文件变更时只编译受影响链；5) 并发请求同模块去重（in-flight 合并）。

```javascript
const fs = require('fs'), path = require('path');

function createLazyCompiler(root) {
  const product = new Map();   // file -> 编译产物
  const depMap = new Map();    // file -> [deps]
  const inflight = new Map();  // 并发去重

  function resolveImport(from, spec) {
    let p = path.resolve(path.dirname(from), spec);
    for (const ext of ['.tsx', '.ts', '.js', '/index.ts']) {
      if (fs.existsSync(p + ext)) return p + ext;
      if (fs.existsSync(p) && fs.statSync(p).isDirectory()
        && fs.existsSync(path.join(p, 'index.ts'))) return path.join(p, 'index.ts');
    }
    return null;
  }

  function compile(file) { // 编译单文件（模拟转换）
    if (product.has(file)) return product.get(file);
    const code = fs.readFileSync(path.join(root, file), 'utf8');
    const deps = [];
    for (const m of code.matchAll(/import\s+[^'"]*['"]([^'"]+)['"]/g)) {
      const d = resolveImport(path.join(root, file), m[1]);
      if (d) { const rel = path.relative(root, d); deps.push(rel); compile(rel); }
    }
    depMap.set(file, deps);
    const out = `/* ${file} */\n${code.replace(/import\s+/g, '// import ')}`;
    product.set(file, out);
    return out;
  }

  function invalidate(file) { // 变更：沿反向传播失效
    product.delete(file);
    for (const [f, deps] of depMap)
      if (deps.includes(file)) invalidate(f);
  }

  return {
    async handle(reqPath) {
      if (product.has(reqPath)) return { hit: true, code: product.get(reqPath) };
      if (inflight.has(reqPath)) return inflight.get(reqPath); // 去重合并
      const p = (async () => {
        try { return { hit: false, code: compile(reqPath) }; }
        finally { inflight.delete(reqPath); }
      })();
      inflight.set(reqPath, p);
      return p;
    },
    onFileChange: invalidate,
  };
}
module.exports = { createLazyCompiler };
```
**评分点**：
- 请求驱动编译（不预构建全图）+ 命中返回。
- in-flight 请求合并（并发去重，易漏）。
- 递归编译子图并记录 depMap（失效传播的基础）。
- 反向失效沿依赖引用方传播。
- 能对应 Turbopack：请求驱动 + 函数级缓存正是其 dev 架构，本题是其模块级简化版。
