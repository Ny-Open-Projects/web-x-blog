---
title: [RBL-043] 笔试：手写模块图构建（含动态 import 与循环依赖标记）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-043：笔试：手写模块图构建（含动态 import 与循环依赖标记）
**答**：实现 buildModuleGraph(entry)：1) 识别静态 import/export from 与动态 import() 两类依赖；2) 动态 import 的依赖标记为 async（不进入同步可达集）；3) 检测循环依赖并用 DFS 染色（白/灰/黑）标记回边；4) 输出 { modules: [{id, path, deps}], cycles }；5) 文件不存在时抛出带路径的错误。

```javascript
const fs = require('fs'), path = require('path');

function parseDeps(code) {
  const deps = [];
  for (const m of code.matchAll(/import\s+(?:[\w*{}\s,]+\s+from\s+)?['"]([^'"]+)['"]/g))
    deps.push({ spec: m[1], async: false });
  for (const m of code.matchAll(/import\(\s*['"]([^'"]+)['"]\s*\)/g))
    deps.push({ spec: m[1], async: true });
  return deps;
}

function resolveFile(base, spec) {
  let p = path.resolve(path.dirname(base), spec);
  if (fs.existsSync(p) && fs.statSync(p).isFile()) return p;
  for (const ext of ['.js', '.ts', '.tsx', '/index.js', '/index.ts']) {
    const candidate = p.endsWith(ext) ? p : p + ext;
    if (fs.existsSync(candidate)) return candidate;
  }
  throw new Error(`Module not found: ${spec} (from ${base})`);
}

function buildModuleGraph(entry) {
  const modules = [], cycles = [];
  const index = new Map();        // path -> id
  const color = new Map();        // 0白 1灰(在栈) 2黑(完成)
  const stack = [];

  function visit(file) {
    if (index.has(file)) {        // 已处理：灰则说明回边（循环）
      if (color.get(file) === 1) cycles.push([...stack.slice(stack.indexOf(file)), file]);
      return index.get(file);
    }
    const id = modules.length;
    index.set(file, id);
    color.set(file, 1); stack.push(file);
    const code = fs.readFileSync(file, 'utf8');
    const deps = parseDeps(code).map(d => ({
      async: d.async, id: visit(resolveFile(file, d.spec)),
    }));
    stack.pop(); color.set(file, 2);
    modules.push({ id, path: file, deps });
    return id;
  }
  visit(path.resolve(entry));
  return { modules, cycles };
}
module.exports = { buildModuleGraph };
```
**评分点**：
- DFS 三色染色区分「已处理」与「在栈中」——循环检测正确性的核心。
- 动态 import 标记 async 且不并入同步可达集（chunk 语义基础）。
- resolveFile 处理扩展名补全与 index 文件（工程完备性）。
- 循环路径输出为环切片（stack.slice）。
- 未找到模块报错带来源路径（可诊断性）。
