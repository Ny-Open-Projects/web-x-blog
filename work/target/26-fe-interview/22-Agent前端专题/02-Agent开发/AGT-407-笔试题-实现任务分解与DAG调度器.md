---
title: [AGT-407] 笔试题——实现任务分解 DAG 调度器（环检测+拓扑并行）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-407：手写多 Agent 任务 DAG 调度：环检测、分层并行、失败隔离

**需求与边界**：
- 输入：任务数组 [{id, run, deps}]；输出：执行结果 Map。
- 边界要求：① 环检测在执行前（报错含环路径）；② 无依赖任务并行、有依赖拓扑序；③ 单任务失败不拖死无关分支（仅短路依赖它的下游）；④ 每任务超时独立。

**答**：
```javascript
async function scheduleDAG(tasks, { timeout = 30000 } = {}) {
  // 1. 环检测（DFS 记路径）
  const depsMap = new Map(tasks.map(t => [t.id, t.deps ?? []]));
  const state = {}, path = [];
  function visit(id) {
    if (state[id] === 2) return false;
    if (state[id] === 1) {
      const cyc = path.slice(path.indexOf(id)).concat(id);
      throw new Error('环: ' + cyc.join('->'));
    }
    state[id] = 1; path.push(id);
    for (const d of depsMap.get(id)) visit(d);
    state[id] = 2; path.pop();
    return false;
  }
  tasks.forEach(t => visit(t.id));
  // 2. 分层拓扑（Kahn）
  const indeg = new Map(tasks.map(t => [t.id, depsMap.get(t.id).length]));
  const dependents = new Map();
  for (const t of tasks) for (const d of depsMap.get(t.id))
    (dependents.get(d) ?? dependents.set(d, []).get(d)).push(t.id);
  const results = new Map(); const failed = new Set();
  let layer = tasks.filter(t => indeg.get(t.id) === 0);
  while (layer.length) {
    // 3. 层内并行，失败隔离：失败任务跳过，下游标 skipped
    const rs = await Promise.allSettled(layer.map(t =>
      t.deps.some(d => failed.has(d) || results.get(d)?.skipped)
        ? Promise.resolve({ skipped: true })
        : Promise.race([t.run(collect(t)),
          new Promise((_, rej) => setTimeout(
            () => rej(new Error(`${t.id} 超时`)), timeout))])));
    rs.forEach((r, i) => {
      const t = layer[i];
      results.set(t.id, r.status === 'fulfilled' ? r.value
        : { failed: true, reason: r.reason?.message });
      if (r.status === 'rejected') failed.add(t.id);
    });
    layer = layer.flatMap(t => dependents.get(t.id) ?? [])
      .filter(id => { const v = indeg.get(id) - 1; indeg.set(id, v); return v === 0; });
  }
  return results;
}
const collect = (t) => Object.fromEntries((t.deps ?? [])
  .map(d => [d, resultsCache.get(d)]));   // 注入依赖结果
```

**评分点**:
- 环检测带路径输出（DFS 灰白黑三色）且先于执行。
- Kahn 分层实现正确的并行批次（无依赖同层并行）。
- 失败隔离：失败/跳过的依赖传递使下游标 skipped 而非抛崩全链。
- 每任务独立超时（Promise.race），结果统一含 failed/skipped 状态可聚合。
