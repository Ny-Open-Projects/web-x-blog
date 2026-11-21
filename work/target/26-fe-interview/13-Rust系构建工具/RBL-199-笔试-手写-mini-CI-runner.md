---
title: [RBL-199] 笔试：手写 mini-CI runner（YAML 任务 → 依赖调度 → 缓存 → 报告）
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-199：笔试：手写 mini-CI runner（YAML 声明 → 调度执行 → 缓存 → 报告）

**题目**：综合题。写 mini-ci.mjs：输入 pipeline 描述对象（无需解析 yaml）：{ tasks: [{name, cmd, deps, cache: {inputs, outputs}}], concurrency }；要求：1) 按依赖图调度（可并行处并行，RBL-178 的波次/池）；2) 每个带 cache 的任务先查缓存（输入指纹 hash，RBL-176），命中跳过执行恢复产物；3) 失败任务重试 1 次后仍失败则跳过其下游任务（下游标记 skipped）；4) 生成 markdown 报告（状态/耗时/缓存命中，RBL-191 风格）；5) 全程状态可断点续跑（RBL-197）。

```javascript
// mini-ci.mjs —— 组合前三题的能力成最小可用 runner
import { runCached } from './task-cache.mjs';       // RBL-176
import { topoWaves } from './schedule.mjs';         // RBL-178

export async function runPipeline(pipeline) {
  const waves = topoWaves(pipeline.tasks);
  const state = {};                                  // name -> {status, ms, cached}
  const skipped = new Set();

  for (const wave of waves) {                        // 波间串行、波内并发池
    const pool = wave.filter(n => !skipped.has(n));
    const workers = Array.from({ length: Math.min(pipeline.concurrency ?? 4, pool.length) },
      async () => {
        while (pool.length) {
          const name = pool.shift();
          const t = pipeline.tasks.find(t => t.name === name);
          if (t.deps?.some(d => state[d]?.status !== 'ok')) { // 上游失败/跳过 → 下游跳过
            state[name] = { status: 'skipped', ms: 0, cached: false };
            skipped.add(name); continue;
          }
          const t0 = performance.now();
          try {
            let cached = false;
            if (t.cache) {
              const r = await runCached(t.name, t.cache, t.cmd); // 指纹→命中回放/miss 执行
              cached = r.cached;
            } else {
              await exec(t.cmd);
            }
            state[name] = { status: 'ok', ms: Math.round(performance.now() - t0), cached };
          } catch (e) {
            state[name] = { status: 'failed', ms: Math.round(performance.now() - t0), cached: false };
            t.deps?.length && null; // 下游在下一波按上游状态自动跳过
          }
        }
      });
    await Promise.all(workers);
  }
  const rows = pipeline.tasks.map(t => {
    const s = state[t.name] ?? { status: 'skipped', ms: 0, cached: false };
    return `| ${t.name} | ${s.status} | ${s.ms}ms | ${s.cached ? 'hit' : '-'} |`;
  });
  const failed = pipeline.tasks.filter(t => state[t.name]?.status === 'failed').length;
  return { markdown: ['| Task | 状态 | 耗时 | 缓存 |', '|---|---|---|---|', ...rows].join('\n'),
           exit: failed ? 1 : 0 };
}
// pipeline 示例：
// { concurrency: 4, tasks: [
//   { name: 'lint', cmd: 'oxlint .' },
//   { name: 'build-utils', cmd: 'pnpm --filter utils build', cache: { inputs: ['packages/utils/**'], outputs: ['packages/utils/dist'] } },
//   { name: 'build-web', cmd: 'pnpm --filter web build', deps: ['build-utils'],
//     cache: { inputs: ['apps/web/**', 'packages/utils/dist/**'], outputs: ['apps/web/dist'] } }] }
```
**评分点**：
- 三层能力组装正确：调度（波次/池）+ 缓存（指纹回放）+ 报告。
- 上游失败 → 下游 skipped（传递，不只跳过一层）。
- 缓存命中跳过执行仍计入报告（可见性）。
- 依赖关系用状态查询而非中断传播（波次模型下正确）。
- 能指出与真 CI 的差距：无 runner 分发、无 secrets、无超时守护（可挂 RBL-189）。
