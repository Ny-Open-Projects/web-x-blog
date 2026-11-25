---
title: [MFW-631] 笔试：手写 PR 流水线编排器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-631：笔试：手写 PR 流水线编排器

**答**：实现 `runPRPipeline(stages, { maxMinutes })`。stages: `{ id, needs: string[], run: () => Promise<{ ok, detail? }>, critical?: boolean }[]`（typecheck/build/e2e 等——RBL-630 五段）。规则：1) 依赖就绪即并行（needs 全 ok/跳过——非 critical 失败不阻塞下游？——critical 失败阻塞所有未启动任务）；2) 总时长超 maxMinutes → 停止新启动任务（在途等完）→ 超时结论 `{ timeout: true }`；3) 返回 `{ results: Record<id, { ok, ms, detail? }>, ok, timeout? }`（ok = 全部成功）；4) 非 critical 失败：记录但不阻塞（warn 语义）。边界：无 stages（ok）；环（needs 环——抛错 RBL-644）；needs 指向不存在的 stage → 抛错。

```javascript
async function runPRPipeline(stages = [], { maxMinutes = 10 } = {}) {
  const byId = new Map(stages.map(s => [s.id, s]));
  for (const s of stages)
    for (const n of s.needs ?? [])
      if (!byId.has(n)) throw new Error(`needs 指向不存在的 stage: ${n}`);
  // 环检测
  const visit = (id, stack = new Set()) => {
    if (stack.has(id)) throw new Error(`stage 环: ${[...stack, id].join('->')}`);
    for (const n of byId.get(id).needs ?? []) visit(n, new Set([...stack, id]));
  };
  stages.forEach(s => visit(s.id));
  const deadline = Date.now() + maxMinutes * 60000;
  const results = {}; const failedCritical = new Set();
  let timedOut = false;
  const ready = (s) => (s.needs ?? []).every(n => results[n]?.ok !== false || !byId.get(n)?.critical);
  await Promise.all(stages.map(async (s) => {
    // 等依赖完成
    for (const n of s.needs ?? [])
      while (!results[n]) await sleep(10);
    const blocked = (s.needs ?? []).some(n =>
      byId.get(n)?.critical && results[n]?.ok === false);
    if (Date.now() > deadline) { timedOut = true; return; }
    if (blocked) { results[s.id] = { ok: false, ms: 0, detail: 'blocked by critical fail' }; return; }
    const t0 = Date.now();
    try {
      const r = await s.run();
      results[s.id] = { ...r, ms: Date.now() - t0 };
      if (!r.ok && s.critical) failedCritical.add(s.id);
    } catch (e) {
      results[s.id] = { ok: false, ms: Date.now() - t0, detail: e.message };
      if (s.critical) failedCritical.add(s.id);
    }
  }));
  const ok = !timedOut && stages.every(s => results[s.id]?.ok !== false || !s.critical);
  return { results, ok, ...(timedOut && { timeout: true }) };
}
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// 自测
const stages = [
  { id: 'lint', needs: [], critical: true, run: async () => ({ ok: true }) },
  { id: 'build', needs: ['lint'], critical: true, run: async () => ({ ok: true }) },
  { id: 'e2e', needs: ['build'], critical: false, run: async () => ({ ok: false, detail: '1 flaky' }) },
  { id: 'budget', needs: ['build'], critical: true, run: async () => ({ ok: true }) },
];
let r = await runPRPipeline(stages, { maxMinutes: 1 });
console.log(r.ok === true);                              // e2e 非 critical：不影响 ok
console.log(r.results.build.ok === true && r.results.e2e.ok === false);

// critical 失败阻塞下游
const stages2 = [
  { id: 'build', needs: [], critical: true, run: async () => ({ ok: false }) },
  { id: 'deploy', needs: ['build'], critical: true, run: async () => ({ ok: true }) },
];
r = await runPRPipeline(stages2, { maxMinutes: 1 });
console.log(r.ok === false && r.results.deploy.detail.includes('blocked'));

// 环检测
let e; try { await runPRPipeline([
  { id: 'a', needs: ['b'], critical: true, run: async () => ({ ok: true }) },
  { id: 'b', needs: ['a'], critical: true, run: async () => ({ ok: true }) },
]); } catch (x) { e = x; }
console.log(/环/.test(e.message));

console.log((await runPRPipeline([], { maxMinutes: 1 })).ok === true);
```

**评分点**：
- 依赖并行（needs 就绪即跑——RBL-816 关键路径的 PR 版）；critical 阻塞语义（非 critical 失败不阻塞）
- 超时语义（停新启动、在途等完——不悬挂）；环/幽灵 needs 抛错
- ok 的定义（critical 全过且非 timeout）；边界
- 能说清「PR 流水线 = 关键路径压缩 + critical 门禁——非 critical 失败记录不阻塞保验证速度」属于加分
