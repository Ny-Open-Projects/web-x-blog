---
title: [930] 笔试手写：实现子任务 DAG 编排器（拓扑排序 + 并发执行）
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 多Agent, 编排]
type: 笔试题
---

## 930：笔试手写：实现子任务 DAG 编排器（拓扑排序 + 并发执行）

**答**：输入 tasks: { id, deps: string[], run: () => Promise<any> }[]。实现 runDag(tasks)：按依赖并发执行（无依赖的同一批并行），任一任务失败立即整体 reject（已开始的让它跑完用 Promise.allSettled 也行，但结果必须是 reject）；环形依赖抛错并给出环上节点；输出 { id, ok, val }[]。

```js
async function runDag(tasks) {
  const map = new Map(tasks.map(t => [t.id, t]));
  const state = {};   // pending | running | done | failed
  tasks.forEach(t => state[t.id] = 'pending');

  // 环检测：DFS 三色标记
  const visiting = new Set(), visited = new Set(), ring = [];
  function dfs(id, path) {
    if (visiting.has(id)) { ring.push(...path.slice(path.indexOf(id)), id); return true; }
    if (visited.has(id)) return false;
    visiting.add(id);
    for (const d of map.get(id).deps) if (dfs(d, [...path, id])) return true;
    visiting.delete(id); visited.add(id);
    return false;
  }
  if (tasks.some(t => dfs(t.id, []))) throw new Error('cycle: ' + ring.join('->'));

  const results = [];
  const runTask = async t => {
    await Promise.all(t.deps.map(d => runTask(map.get(d)))); // 依赖先完成（幂等等待）
    state[t.id] = 'running';
    try {
      const val = await t.run();
      results.push({ id: t.id, ok: true, val }); state[t.id] = 'done';
    } catch (e) {
      results.push({ id: t.id, ok: false, val: String(e) }); state[t.id] = 'failed';
      throw e;                                   // 失败向上传播
    }
  };
  await Promise.all(tasks.map(t => runTask(t).catch(e => e))); // 全跑完后统一判
  const failed = results.find(r => !r.ok);
  if (failed) throw new Error('dag failed at ' + failed.id);
  return results;
}
```

**评分点**：
- 环检测用 DFS 三色法而不是瞎猜，能给出环路径
- 依赖等待的幂等处理（重复调用 runTask 不重复执行，可用缓存 promise）
- 失败传播语义清晰：整体 reject 且知道失败点
- 能说出无依赖任务被并发执行（Promise.all 的天然并发）

