---
title: [TST-504] 大规模 monorepo 下测试架构如何分层治理
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-504：大规模 monorepo 下测试架构如何分层治理

**答**：
- 结论：按「包（package）自治 + 受影响范围执行」治理。每个包自带单测与构建缓存，CI 只跑「变更包 + 反向依赖包」的测试，避免全量。
- 关键机制：Nx/Turbo 式依赖图计算 affected；远端缓存让未变更任务秒级命中；统一 test/setup 基座但允许包级 override，避免一刀切。
- 追问钩子：包之间循环依赖导致 affected 爆炸怎么办？——用边界lint（如 nx enforce-module-boundaries）在架构层切断环，测试治理问题本质常是架构问题。

```javascript
// 依赖图计算 affected：从变更包出发做反向 BFS
function affectedPackages(changed, graph) { // graph: pkg -> 依赖它的包[]
  const seen = new Set(changed), queue = [...changed];
  while (queue.length) {
    const pkg = queue.shift();
    for (const dependent of (graph[pkg] || [])) {
      if (!seen.has(dependent)) { seen.add(dependent); queue.push(dependent); }
    }
  }
  return [...seen];
}
const graph = { ui: ['checkout'], core: ['ui', 'checkout'], checkout: [] };
console.log(affectedPackages(['core'], graph)); // ['core','ui','checkout']
```
