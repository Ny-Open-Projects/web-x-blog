---
title: [TST-500] 笔试：整合题——实现一个迷你测试平台核心（排队/执行/报告/门禁）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-500：笔试：整合题——实现一个迷你测试平台核心（排队/执行/报告/门禁）。
**题目**：整合：RunQueue（优先级）+ Executor（分片并行 mock）+ Reporter（聚合去重）+ Gate（分级判定）。接口 `submit(suite, ref, priority)` → 返回 runId；`run(runId)` 异步执行并产出报告；`gate(runId)` 判定。写出骨架与关键方法。

```javascript
class MiniPlatform {
  #queue = []; #running = new Map(); #reports = new Map();
  submit(suite, ref, priority = 2) {
    const key = `${suite}|${ref}`;
    for (const [, run] of this.#running) if (run.key === key) return { reused: true, runId: run.id };
    const runId = `R-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`;
    this.#queue.push({ suite, ref, priority, runId, key });
    this.#queue.sort((a, b) => a.priority - b.priority);
    return { reused: false, runId };
  }
  async run(runId, { workers = 4, execTests }) {      // execTests 可注入（单测 mock 点）
    const job = this.#queue.find(j => j.runId === runId);
    if (!job) throw new Error(`未知 runId: ${runId}`);
    this.#queue = this.#queue.filter(j => j !== job);
    this.#running.set(runId, { id: runId, key: job.key });
    const tests = await execTests(job.suite);
    const shards = Array.from({ length: workers }, () => []);
    [...tests].sort((a, b) => b.ms - a.ms)
      .forEach((t, i) => shards[i % workers].push(t));
    const results = (await Promise.all(shards.map(s =>
      Promise.all(s.map(t => execOne(t)))))).flat();
    const merged = new Map(results.map(r => [r.name, r]));   // 重跑取最后
    const all = [...merged.values()];
    const report = { runId, total: all.length,
      passRate: +(all.filter(r => r.status === 'pass').length / all.length).toFixed(2),
      failed: all.filter(r => r.status !== 'pass').map(r => r.name) };
    this.#reports.set(runId, report);
    this.#running.delete(runId);
    return report;
  }
  gate(runId, { threshold = 1 } = {}) {
    const r = this.#reports.get(runId);
    if (!r) throw new Error('报告不存在');
    return { verdict: r.passRate >= threshold ? 'pass' : 'fail', ...r };
  }
}
async function execOne(t) { return { name: t.name, status: 'pass', ms: t.ms }; }

```

**评分点**：
- 四模块职责边界清晰、接口稳定。
- 优先级排队 → 分片执行（workers mock）→ 报告聚合 → 门禁判定的数据流完整。
- 幂等与去重（同 ref 进行中复用）。
- 每模块可单测（依赖注入 mock 点）。
