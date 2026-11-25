---
title: [RBL-103] 笔试：手写增量 DAG 调度器（拓扑重算 + 并发执行）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-103：笔试：手写增量 DAG 调度器（拓扑重算 + 并发执行）
**答**：实现 createScheduler(tasks, deps)：1) tasks 为 Map<name, async fn>，deps 为依赖边（先跑依赖）；2) schedule(changed)：重算 changed 及其所有下游，未受影响任务跳过；3) 并发执行：无依赖关系的任务同时跑（Promise.all 分层）；4) 同一轮内任务去重；5) 失败任务阻断其下游（下游标记 skipped）。

```javascript
function createScheduler(tasks, deps) {
  const results = new Map();   // name -> value
  const downstream = new Map(); // 反向边
  for (const [t, ds] of deps)
    for (const d of ds)
      if (!downstream.has(d)) downstream.set(d, new Set());
      // downstream[d] = 依赖 d 的任务集合

  function downstreamOf(changed) {
    const set = new Set(changed), q = [...changed];
    while (q.length) {
      const cur = q.pop();
      for (const n of downstream.get(cur) || []) {
        if (!set.has(n)) { set.add(n); q.push(n); }
      }
    }
    return set;
  }

  async function schedule(changed) {
    const toRun = downstreamOf(changed);
    const skipped = new Set();
    // 分层：按依赖层级逐层并发
    const layers = topoLayers(toRun, deps);
    for (const layer of layers) {
      const active = layer.filter(t => {
        const failedDep = (deps.get(t) || []).some(d => results.get(d) === 'FAIL' || skipped.has(d));
        if (failedDep) { skipped.add(t); results.set(t, 'SKIPPED'); return false; }
        return true;
      });
      await Promise.all(active.map(async t => {
        try { results.set(t, await tasks.get(t)()); }
        catch { results.set(t, 'FAIL'); }
      }));
    }
    return { results, skipped: [...skipped] };
  }
  return { schedule, results };
}

function topoLayers(subset, deps) {
  const indeg = new Map([...subset].map(t => [t, 0]));
  for (const t of subset)
    for (const d of deps.get(t) || [])
      if (indeg.has(d)) indeg.set(t, indeg.get(t) + 1);
  const layers = [];
  let cur = [...subset].filter(t => indeg.get(t) === 0);
  let total = 0;
  while (cur.length && total < subset.size) {
    layers.push(cur); total += cur.length;
    const next = [];
    for (const t of cur)
      for (const n of subset)
        if ((deps.get(n) || []).includes(t)) {
          indeg.set(n, indeg.get(n) - 1);
          if (indeg.get(n) === 0) next.push(n);
        }
    cur = next;
  }
  return layers;
}
module.exports = { createScheduler };
```
**评分点**：
- 下游集合计算（反向传播受影响任务）。
- 分层拓扑并发（无依赖任务 Promise.all 同层并行）。
- 失败阻断下游（skipped 标记，不误执行）。
- 顶层入度计算正确（DAG 基础）。
- 能对应 Turbopack/Turbo 引擎：任务图 + 增量重算 + 并发调度即其内核模型。
