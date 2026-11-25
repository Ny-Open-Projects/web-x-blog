---
title: [RBL-923] 笔试：手写 DSL 渐进迁移流水线（分批 + 语义验证 + 失败兜底）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-923：笔试：手写 DSL 渐进迁移流水线（分批 + 验证 + 兜底）

**答**：实现 `migrateAll(pages, { migrate, verify, save, batchSize, maxFailRate })`。pages: `{ id, json }[]`。规则：1) 分批执行：每批内逐页 migrate → verify（语义等价，注入函数返回 { ok, reason? }）→ save；2) 单页失败记录不中断批次；3) **批次熔断**：本批失败率 > maxFailRate → 暂停整个迁移（返回 { paused: true, at }——失败率异常说明迁移器 bug）；4) 结束返回 `{ ok, failed: Array<{ id, reason }>, doneRate, paused? }`；5) verify 未提供时视为通过（信任 migrate）。边界：pages 空；batchSize 大于总量。

```javascript
async function migrateAll(pages = [], { migrate, verify, save, batchSize = 100, maxFailRate = 0.2 } = {}) {
  let ok = 0; const failed = []; let paused = false;
  const total = pages.length;
  for (let i = 0; i < total; i += batchSize) {
    const batch = pages.slice(i, i + batchSize);
    let batchFail = 0;
    for (const p of batch) {
      try {
        const v2 = await migrate(p.json);
        const v = verify ? await verify(p.json, v2) : { ok: true };
        if (!v.ok) throw new Error(v.reason ?? 'verify-failed');
        await save(p.id, v2);
        ok++;
      } catch (e) {
        batchFail++; failed.push({ id: p.id, reason: e.message });
      }
    }
    if (batchFail / batch.length > maxFailRate) {
      paused = true;
      break;                                             // 批次熔断：失败率异常
    }
  }
  return { ok, failed, doneRate: total ? +(ok / total).toFixed(3) : 0,
    paused, pausedAt: paused ? ok : undefined };
}

// 自测
const pages = Array.from({ length: 10 }, (_, i) => ({
  id: `p${i}`, json: { v: 1, good: i % 5 !== 0 }         // 每 5 个一个「坏页」（20% 失败率）
}));
let calls = 0;
let r = await migrateAll(pages, {
  migrate: async (json) => { calls++; if (!json.good) throw new Error('dirty-data');
    return { ...json, v: 2 }; },
  verify: async (a, b) => ({ ok: b.v === 2 }),
  save: async () => {},
  batchSize: 5, maxFailRate: 0.2,
});
// 第一批 5 页：p0 坏（1/5=20%）不熔断（不大于）；第二批 p5 坏 -> 20% 不熔断
console.log(r.ok === 8 && r.failed.length === 2 && !r.paused && r.doneRate === 0.8);

// 熔断：失败率超限
const badPages = Array.from({ length: 4 }, (_, i) => ({ id: `b${i}`, json: { bad: true } }));
r = await migrateAll(badPages, {
  migrate: async () => { throw new Error('x'); },
  save: async () => {}, batchSize: 2, maxFailRate: 0.2,
});
console.log(r.paused === true && r.failed.length === 2); // 第一批全失败即熔断

// verify 拦截
r = await migrateAll([{ id: 'v', json: {} }], {
  migrate: async () => ({ v: 2 }), verify: async () => ({ ok: false, reason: 'layout-drift' }),
  save: async () => {},
});
console.log(r.failed[0].reason === 'layout-drift');

console.log((await migrateAll([], { migrate: async () => ({}), save: async () => {} })).doneRate === 0);
```

**评分点**：
- 分批 + 单页失败不中断；批次熔断语义正确（失败率 > 阈值暂停整个迁移——迁移器 bug 的止损）
- verify 闸门（未提供视为通过的可选性）；doneRate 精度
- 边界：空 pages、batchSize 超量
- 能说清「大规模数据迁移必须有失败兜底路径与熔断——失败率异常 = 迁移器 bug 而非数据问题」属于加分
