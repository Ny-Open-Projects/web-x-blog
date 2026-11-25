---
title: [RBL-044] 笔试：手写简化 splitChunks 策略（公共依赖提取）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-044：笔试：手写简化 splitChunks 策略（公共依赖提取）
**答**：给定模块图 { entry: 'a', deps: Set<string>[] }（多个入口），实现 split(entries, { minChunks, minSize })：1) 统计每个模块被多少入口同步可达；2) 被 ≥ minChunks 个入口共享且合并体积 ≥ minSize 的模块抽成 chunk 'shared'；3) 其余模块归属各自入口 chunk；4) 动态 import 的模块不参与公共抽取（独立 async chunk）；5) 返回 chunk 划分映射。

```javascript
function reachableSync(entry, deps, asyncDeps) {
  const seen = new Set();
  const stack = [entry];
  while (stack.length) {
    const m = stack.pop();
    if (seen.has(m)) continue;
    seen.add(m);
    for (const d of deps[m] || []) stack.push(d);
    // 注意：asyncDeps[m] 的模块不入同步栈 —— 动态导入形成独立边界
    for (const d of asyncDeps[m] || []) seenAsync.add(d);
  }
  return seen;
}
const seenAsync = new Set(); // 简化示意：动态可达集单独收集

function split(entries, deps, asyncDeps, { minChunks = 2, minSize = 30 } = {}, sizes = {}) {
  const reachMap = new Map();  // module -> 命中的入口数
  for (const e of entries) {
    for (const m of reachableSync(e, deps, asyncDeps)) {
      reachMap.set(m, (reachMap.get(m) || 0) + 1);
    }
  }
  const chunks = { shared: [], async: [...seenAsync] };
  chunks.shared = [...reachMap.entries()]
    .filter(([m, n]) => n >= minChunks && (sizes[m] || 0) >= minSize)
    .map(([m]) => m);
  for (const e of entries) {
    const sync = reachableSync(e, deps, asyncDeps);
    chunks[e] = [...sync].filter(m => !chunks.shared.includes(m));
  }
  return chunks; // { shared: [...], main: [...], pageA: [...], async: [...] }
}
module.exports = { split };
```
**评分点**：
- 多入口同步可达计数（reachMap 语义 = webpack minChunks）。
- 动态 import 模块排除出同步可达与公共抽取（async 边界，易漏）。
- minSize 体积阈值判断（防止过度分割碎片化）。
- 共享模块从入口 chunk 中剔除（划分互斥）。
- 能联系到 webpack/Rspack 中 cacheGroups priority 的优先级语义。
