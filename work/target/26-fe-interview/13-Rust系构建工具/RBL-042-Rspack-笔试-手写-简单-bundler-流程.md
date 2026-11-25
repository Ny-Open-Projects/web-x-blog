---
title: [RBL-042] 笔试：手写一个简化 bundler（Rspack 核心流程思想版）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-042：笔试：手写一个简化 bundler（Rspack 核心流程思想版）
**答**：用 Node 实现 bundler 核心：1) 从 entry 出发解析 import 语句构建模块图；2) 每个模块编译成「id + 源码」并按依赖拓扑排序；3) 生成单个自执行 bundle，运行时 require 实现 ESM→内部模块映射；4) 循环依赖不崩溃（缓存已执行模块）；5) 说明 Rspack 在哪些环节把这套流程并行化。

```javascript
const fs = require('fs'), path = require('path');

function buildGraph(entry) {
  const graph = new Map(); // path -> { id, code, deps: string[] }
  const idOf = new Map();
  let nextId = 0;
  const queue = [path.resolve(entry)];
  while (queue.length) {
    const file = queue.shift();
    if (graph.has(file)) continue;           // 去重，天然处理循环引用的图构建
    const code = fs.readFileSync(file, 'utf8');
    const deps = [];
    // 简化：仅匹配 ESM 静态 import 的字符串
    for (const m of code.matchAll(/import\s+[^'"]*['"]([^'"]+)['"]/g)) {
      let dep = path.resolve(path.dirname(file), m[1]);
      if (!dep.match(/\.[cm]?js$/)) dep += '.js';
      deps.push(dep); queue.push(dep);       // BFS 层序入队
    }
    idOf.set(file, nextId);
    graph.set(file, { id: nextId++, code, deps });
  }
  return { graph, idOf };
}

function bundle(entry) {
  const { graph, idOf } = buildGraph(entry);
  const modules = [...graph.values()].map(m =>
    `${m.id}: [function(require, module, exports){\n${m.code}\n}, ` +
    `[${m.deps.map(d => idOf.get(d))}]],`);
  const runtime = `
    const cache = {};
    function require(id) {                    // 循环依赖安全：先缓存空模块
      if (cache[id]) return cache[id].exports;
      const [factory, deps] = modules[id];
      const module = { exports: {} };
      cache[id] = module;                     // 先占位再执行工厂
      factory((x) => require(deps[x]), module, module.exports);
      return module.exports;
    }
    require(0);`;
  return `(function(){ const modules = {\n${modules.join('\n')}\n}; ${runtime} })();`;
}
module.exports = { bundle };
```
**评分点**：
- BFS/队列遍历构建模块图且 visited 去重（图基础）。
- 循环依赖处理：require 前先写入 cache 占位（最容易丢的评分点）。
- 依赖表依赖 id 间接层（deps 数组下标→require(x)）。
- 生成 IIFE + 运行时注入（bundle 产物结构正确）。
- 能答出 Rspack 对应环节的并行化：parse 与 transform 并行、模块图构建后 chunk 生成算法化。

## 变体与延伸（补充）

**变体与延伸**：

1. 循环依赖在运行时为什么可能拿到 undefined？ → A 执行中 require B，B 又 require A 时命中的是 cache 里 A 的**半成品 exports**；解法是导出用 getter 延迟取值，或在模块末尾统一赋值。
2. 你这版能做 tree-shaking 吗？ → 不能。运行时 require 版本没有静态导出信息，要改成语义分析阶段收集 import/export、标记副作用，再做作用域提升与未引用导出剔除。
3. 增量构建该缓存什么？ → 模块级缓存键 = 文件内容哈希 + 依赖导出哈希 + loader 配置；任一变化沿依赖图向上游传播失效，只按文件 mtime 判断会漏掉依赖变更。
