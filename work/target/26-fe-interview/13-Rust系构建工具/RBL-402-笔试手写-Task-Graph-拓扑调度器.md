---
title: [RBL-402] 笔试：手写任务图拓扑调度器（并发 + 关键路径优先）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-402：手写任务图拓扑调度器
**答**：实现 `createScheduler(tasks)`：1) tasks：`{ id, deps: string[], run: async () => void, weight? }`；2) 调度：并发执行（concurrency 上限），依赖满足即启动；3) 优先级：同批可选任务按关键路径（含自身及其下游最长耗时估计）降序启动——关键路径先跑减少总时长；4) 失败策略：任务失败后其下游任务跳过（标记 skipped），其他分支继续；5) 返回汇总 { done, failed, skipped, durations }。

```javascript
export function createScheduler(tasks, { concurrency = 4 } = {}) {
  const byId = new Map(tasks.map((t) => [t.id, t]))
  const downstream = new Map()                     // id → 下游集合
  tasks.forEach((t) => t.deps.forEach((d) => {
    if (!downstream.has(d)) downstream.set(d, [])
    downstream.get(d).push(t.id)
  }))

  function criticalPath(id, memo = new Map()) {
    if (memo.has(id)) return memo.get(id)
    const t = byId.get(id)
    const w = t.weight ?? 1
    const max = Math.max(0, ...(downstream.get(id) ?? []).map((d) => criticalPath(d, memo)))
    memo.set(id, w + max)
    return w + max
  }

  const depsLeft = new Map(tasks.map((t) => [t.id, new Set(t.deps)]))
  const result = { done: [], failed: [], skipped: [], durations: {} }

  return new Promise((resolveAll) => {
    let running = 0
    const ready = () => tasks
      .filter((t) => depsLeft.get(t.id).size === 0 && !result.done.includes(t.id)
        && !result.failed.includes(t.id) && !result.skipped.includes(t.id))
      .sort((a, b) => criticalPath(b.id) - criticalPath(a.id))

    function pump() {
      if (running === 0 && ready().length === 0) return resolveAll(result)
      while (running < concurrency) {
        const next = ready()[0]
        if (!next) break
        running++
        const t0 = Date.now()
        next.run().then(
          () => finish(next.id, 'done', t0),
          () => finish(next.id, 'failed', t0),
        )
      }
    }
    function finish(id, status, t0) {
      running--
      result[status].push(id)
      result.durations[id] = Date.now() - t0
      const downstreams = downstream.get(id) ?? []
      if (status === 'failed') markSkipped(downstreams)          // 下游跳过
      else downstreams.forEach((d) => depsLeft.get(d).delete(id))
      pump()
    }
    function markSkipped(ids) {
      for (const id of ids) {
        if (result.skipped.includes(id)) continue
        result.skipped.push(id)
        markSkipped(downstream.get(id) ?? [])
      }
    }
    pump()
  })
}
```
**评分点**：
- 并发上限 + 依赖满足即启动（pump 循环无死锁）
- 关键路径优先（weight + 下游最长链 memo 化）
- 失败传播语义正确（下游 skipped，其他分支继续）
- 终止条件完备（running=0 且无可运行任务才 resolve，防提前结束/悬挂）
