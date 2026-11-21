---
title: [HW-148] 手写 postTask 任务编排——依赖链按优先级调度、取消传播与超时兜底
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：任务编排器：任务声明（fn/priority/dependsOn/signal）→ 依赖拓扑（ALG-226 分层）→ 每层用 scheduler.postTask 按优先级调度（user-blocking 先于 background）→ 取消传播（依赖被取消，下游级联取消）→ 整体超时兜底。

```javascript
function orchestrate(tasks, { timeout = 10000 } = {}) {
  // tasks: [{ id, fn, priority: 'user-blocking'|'user-visible'|'background', dependsOn: [] }]
  const results = new Map();
  const ctrl = new AbortController();                   // 全局取消（超时/外部中止）
  const timer = setTimeout(() => ctrl.abort('timeout'), timeout);
  const indeg = new Map(tasks.map((t) => [t.id, (t.dependsOn ?? []).length]));
  const dependents = new Map();
  for (const t of tasks) for (const d of t.dependsOn ?? []) {
    (dependents.get(d) ?? dependents.set(d, []).get(d)).push(t.id);
  }
  return new Promise((resolveAll, rejectAll) => {
    const settle = (err) => { clearTimeout(timer); err ? rejectAll(err) : resolveAll(results); };
    function run(t) {
      const signal = ctrl.signal;
      scheduler.postTask(async () => {
        results.set(t.id, await t.fn(results));         // 依赖结果作为入参
        for (const d of dependents.get(t.id) ?? []) {
          indeg.set(d, indeg.get(d) - 1);
          if (indeg.get(d) === 0) run(tasks.find((x) => x.id === d));
        }
        if (results.size === tasks.length) settle();
      }, { priority: t.priority ?? 'user-visible', signal })
      .catch((e) => { if (e.name === 'AbortError') settle(new Error('cancelled: ' + signal.reason)); });
    }
    tasks.filter((t) => indeg.get(t.id) === 0).forEach(run);
  });
}
// 用法：首屏任务编排（关键数据 user-blocking，推荐位 background）
// orchestrate([
//   { id: 'goods', fn: () => fetchGoods(), priority: 'user-blocking' },
//   { id: 'recs', fn: (r) => fetchRecs(r.get('goods')), priority: 'background', dependsOn: ['goods'] },
// ]);
```

**评分点**：
- 拓扑分层 + postTask 优先级调度（层内按 priority）——依赖与优先级正交组合。
- 全局 AbortController 超时兜底与取消传播（依赖被取消下游级联）。
- results Map 传参（下游拿上游结果）。
- 无 scheduler 环境的降级意识（PER-215 降级链）。
