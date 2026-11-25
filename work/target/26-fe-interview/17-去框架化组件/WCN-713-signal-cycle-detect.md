---
title: [WCN-713] 依赖图出现环会导致 Signals 死循环，如何检测并预防？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-713：依赖图出现环会导致 Signals 死循环，如何检测并预防？

**答**：
- 结论：在 computed/effect 建立依赖边时做环检测——若新边指向当前正在求值的节点或其上游，则判定成环并抛错/告警，阻止订阅写入。
- 预防手段：effect 中只允许「读」，写操作进入下一微任务；对自引用 computed 直接拦截；开发期维护依赖邻接表并跑拓扑排序检测。
- 追问钩子：异步数据回来后再写 signal 算不算环？考察「时间维度上的环」与 epoch 版本号治理。

```javascript
const edges = new Map();                 // node -> Set(deps)
function addEdge(from, to) {
  if (!edges.has(from)) edges.set(from, new Set());
  // 检测：to 是否能沿依赖链回到 from（成环）
  const stack = [to], seen = new Set();
  while (stack.length) {
    const n = stack.pop();
    if (n === from) throw new Error('依赖环 detected');
    if (seen.has(n)) continue; seen.add(n);
    for (const d of edges.get(n) || []) stack.push(d);
  }
  edges.get(from).add(to);
}
const a = 'a', b = 'b';
addEdge(a, b);
try { addEdge(b, a); } catch (e) { console.log(e.message); }
```
