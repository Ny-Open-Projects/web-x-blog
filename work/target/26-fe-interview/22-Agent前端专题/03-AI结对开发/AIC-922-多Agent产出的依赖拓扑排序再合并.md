---
title: [AIC-922] 多个 Agent 的产出存在依赖（B 用到 A 新增的类型），合并时如何做「依赖拓扑排序」避免顺序错乱？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-922：多个 Agent 的产出存在依赖（B 用到 A 新增的类型），合并时如何做「依赖拓扑排序」避免顺序错乱？
**答**：
- 先把改动抽象成依赖图：节点是 Agent 的产出/提交，边是「A 必须在 B 之前」（B 依赖 A 新增的类型/接口）——结论：合并顺序应是拓扑序，而不是提交时间。
- 用 Kahn 算法做拓扑排序：入度为 0 的先合；检测到环说明存在循环依赖，必须拆开或人工介入——环是并行分工失败的强信号。
- 落地在 CI：合并队列按拓扑序执行，非拓扑序的合并请求被延迟或拒绝；对每个产出声明 `dependsOn` 前置改动。
- 追问钩子：能说出「依赖图要显式声明而非从代码隐式推断；出现环往往意味着职责划分有问题，应回到分工而非硬解」的候选人更有架构意识。

```typescript
// 依赖拓扑排序（Kahn）
function topoMergeOrder(nodes) { // nodes: { id, dependsOn:[] }[]
  const indeg = new Map(nodes.map(n => [n.id, n.dependsOn.length]));
  const graph = new Map();
  for (const n of nodes) for (const d of n.dependsOn) {
    if (!graph.has(d)) graph.set(d, []);
    graph.get(d).push(n.id);
  }
  const queue = nodes.filter(n => indeg.get(n.id) === 0).map(n => n.id);
  const order = [];
  while (queue.length) {
    const id = queue.shift(); order.push(id);
    for (const next of graph.get(id) || []) {
      indeg.set(next, indeg.get(next) - 1);
      if (indeg.get(next) === 0) queue.push(next);
    }
  }
  return { order, hasCycle: order.length !== nodes.length }; // 有环=分工有问题
}
console.log(topoMergeOrder([{id:'types',dependsOn:[]},{id:'api',dependsOn:['types']},{id:'ui',dependsOn:['api']}]));
```
