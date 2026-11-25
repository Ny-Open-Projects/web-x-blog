---
title: [AIC-537] 笔试：手写 AI 代码门禁编排器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-537：笔试：手写 AI 门禁编排器

**答**：实现 `createAIGate(gates, { failFast })`。gates: `{ name, run: () => Promise<{ ok, detail? }>, critical?: boolean }[]`。规则：1) **failFast**：critical 门禁失败 → 后续门禁跳过（标记 skipped-by-fail-fast）；2) 非 failFast：所有门禁都跑（结果聚合）；3) 非 critical 失败 → 记录但不阻断（warn 语义）；4) 返回 `{ results: Record<name, { ok, detail?, skipped? }>, blocked, ok }`（blocked = 任一 critical 失败）。边界：gates 空（ok）；全部 skip（failFast 后）；单个 gate 抛错（视为失败）。

```javascript
async function runGate(gates = [], { failFast = true } = {}) {
  const results = {}; let blocked = false; let failFastTriggered = false;
  for (const gate of gates) {
    if (failFastTriggered) {
      results[gate.name] = { ok: null, skipped: true, detail: 'skipped by fail-fast' };
      continue;
    }
    try {
      const r = await gate.run();
      results[gate.name] = { ok: r.ok, detail: r.detail };
      if (!r.ok && gate.critical) {
        blocked = true;
        if (failFast) failFastTriggered = true;
      }
    } catch (e) {
      results[gate.name] = { ok: false, detail: e.message };
      if (gate.critical) { blocked = true; if (failFast) failFastTriggered = true; }
    }
  }
  const ok = !blocked;
  return { results, blocked, ok };
}
// 便捷包装
function createAIGate(gates, opts) {
  return { run: () => runGate(gates, opts) };
}

// 自测
const gates = [
  { name: 'hallucination', critical: true,
    run: async () => ({ ok: false, detail: '幻觉依赖 lodash-es-deep' }) },
  { name: 'style', critical: false,
    run: async () => ({ ok: true }) },
  { name: 'test-quality', critical: true,
    run: async () => ({ ok: true, detail: 'assertion avg 4.5' }) },
  { name: 'security', critical: true,
    run: async () => ({ ok: true }) },
];
// failFast：幻觉失败 → 后续跳过
let r = await runGate(gates, { failFast: true });
console.log(r.blocked === true && r.ok === false);
console.log(r.results.hallucination.ok === false);
console.log(r.results.style.skipped === true);           // 跳过
console.log(r.results['test-quality'].skipped === true);

// 非 failFast：所有门禁都跑
r = await runGate(gates, { failFast: false });
console.log(r.results.style.ok === true);                // 都跑了
console.log(r.results['test-quality'].ok === true);
console.log(r.blocked === true);                         // 仍然 blocked

// 全过
const allPass = gates.map(g => ({ ...g, run: async () => ({ ok: true }) }));
r = await runGate(allPass, { failFast: true });
console.log(r.ok === true && r.blocked === false);

// 非 critical 失败
const nonCritical = [{ name: 'style', critical: false,
  run: async () => ({ ok: false }) }];
r = await runGate(nonCritical, { failFast: true });
console.log(r.ok === true);                              // 非 critical 失败不阻断

// 空
console.log((await runGate([])).ok === true);
```

**评分点**：
- failFast 语义（critical 失败 → 后续 skipped——节省 CI 时间 RBL-631）
- 非 critical 失败不阻断（warn 语义——分级门禁）；门禁抛错视为失败
- 边界（空 gates/全过/非 critical 失败）；blocked 与 ok 的独立
- 能说清「AI 代码门禁 = 传统 CI + AI 专属门禁（幻觉/测试质量/信任路由）——failFast 节省 CI 时间」属于加分
