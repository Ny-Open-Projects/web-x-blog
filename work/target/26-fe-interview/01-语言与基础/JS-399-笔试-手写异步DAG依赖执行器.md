---
title: [JS-399] 笔试：手写异步 DAG 依赖执行器（拓扑排序 + 并发）
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## JS-399：笔试：手写异步 DAG 依赖执行器

**答**：实现 `runDAG(nodes)`：nodes 为 `{ id, deps: string[], run: (depResults) => Promise }` 数组。要求：① 依赖就绪后并发执行（无依赖的立即跑）；② 检测环依赖（抛错并列出环路径）；③ 缺失依赖报错；④ 每个节点结果传给依赖它的节点 run(deps map)；⑤ 返回全部结果 Map。写出实现。

```javascript
async function runDAG(nodes) {
  const byId = new Map(nodes.map(n => [n.id, n]));
  // 缺失依赖检查
  for (const n of nodes)
    for (const d of n.deps)
      if (!byId.has(d)) throw new Error(`node ${n.id} depends on missing ${d}`);

  // 环检测: DFS 三色
  const state = new Map();   // 0=未访问 1=访问中 2=完成
  const stack = [];
  const check = (id) => {
    if (state.get(id) === 2) return;
    if (state.get(id) === 1) throw new Error(`cycle: ${[...stack.slice(stack.indexOf(id)), id].join(' → ')}`);
    state.set(id, 1); stack.push(id);
    for (const d of byId.get(id).deps) check(d);
    stack.pop(); state.set(id, 2);
  };
  for (const n of nodes) check(n.id);

  // 执行: 依赖完成度驱动的 Promise
  const results = new Map();
  const promises = new Map();
  const get = (id) => promises.get(id) ?? promises.set(id, (async () => {
    const node = byId.get(id);
    const depResults = Object.fromEntries(
      await Promise.all(node.deps.map(async d => [d, await get(d)])));
    const r = await node.run(depResults);
    results.set(id, r);
    return r;
  })()).get(id);
  await Promise.all(nodes.map(n => get(n.id)));
  return results;
}
// 用法: b 依赖 a, c 依赖 a, d 依赖 b+c → a 先跑, b/c 并行, d 最后
```

**评分点**：
- DFS 三色环检测并输出环路径
- 缺失依赖前置校验（比运行时 undefined 崩溃友好）
- Promise 记忆化实现「依赖完成即触发」（每个节点一次执行）
- depResults 按依赖名注入 run 回调
