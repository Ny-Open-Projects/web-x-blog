---
title: [RBL-865] 笔试：手写 staging/prod 产物差异审计器（预期差异白名单 + 意外暴露）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-865：笔试：手写 staging/prod 差异审计器（白名单 + 意外）

**答**：实现 `diffAudit(staging, prod, { expected })`。双方为统一 manifest（RBL-826）：`{ buildId, outputs: Record<name, { bytes, hash, env? }> }`；expected: 允许差异的 env 字段名数组（如 ['API_BASE']）。规则：1) 文件集合 diff：任一方独有 → unexpected 'file-set'；2) 同名文件 hash 不同 → 检查该文件的 env 注入字段：全部 ∈ expected → 'expected-env'（ok）；否则 unexpected 'content-diff'（列出非白名单差异）；3) 返回 `{ unexpected: Array<{ type, detail }>, ok }`。边界：双方完全一致；expected 空（任何 hash 差异都意外）。

```javascript
function diffAudit(staging, prod, { expected = [] } = {}) {
  const unexpected = [];
  const s = new Set(Object.keys(staging.outputs ?? {}));
  const p = new Set(Object.keys(prod.outputs ?? {}));
  for (const n of s) if (!p.has(n))
    unexpected.push({ type: 'file-set', detail: `staging 独有: ${n}` });
  for (const n of p) if (!s.has(n))
    unexpected.push({ type: 'file-set', detail: `prod 独有: ${n}` });
  for (const n of s) {
    if (!p.has(n)) continue;
    const so = staging.outputs[n], po = prod.outputs[n];
    if (so.hash === po.hash) continue;
    const envDiff = Object.keys(so.env ?? {}).filter(k => so.env[k] !== po.env?.[k]);
    const outside = envDiff.filter(k => !expected.includes(k));
    if (outside.length || envDiff.length === 0)
      unexpected.push({ type: 'content-diff', detail: `${n}: hash 不同，env 差异=[${envDiff}] 白名单外=[${outside}]` });
  }
  return { unexpected, ok: unexpected.length === 0 };
}

// 自测
const mk = (env) => ({ buildId: 'x',
  outputs: {
    'main.js': { bytes: 100, hash: 'h-main', env },
    'api.js': { bytes: 50, hash: env?.API_BASE === 'https://stg' ? 'h-stg' : 'h-prod', env },
  } });
const expected = ['API_BASE'];
let r = diffAudit(mk({ API_BASE: 'https://stg' }), mk({ API_BASE: 'https://prod' }), { expected });
console.log(r.ok === true && r.unexpected.length === 0);   // env 差异全在白名单

// 白名单外差异
const stg = mk({ API_BASE: 'https://stg', SECRET_MODE: 'staging' });
r = diffAudit(stg, mk({ API_BASE: 'https://prod', SECRET_MODE: 'prod' }), { expected });
console.log(r.unexpected.some(u => u.type === 'content-diff' && u.detail.includes('SECRET_MODE')));

// 文件集差异
r = diffAudit(
  { buildId: 'a', outputs: { 'extra.js': { bytes: 1, hash: 'x' } } },
  { buildId: 'b', outputs: {} }, {});
console.log(r.unexpected[0].type === 'file-set');
console.log(r.ok === false);

// 完全一致
r = diffAudit(mk({}), mk({}), {});
console.log(r.ok === true);
console.log(diffAudit(mk({ X: '1' }), mk({ Y: '2' })).ok === false);   // expected 空
```

**评分点**：
- 双级审计：文件集合 diff 与内容 hash diff；env 差异与白名单比对（预期差异精确化到字段）
- 「hash 不同但无 env 差异」视为意外（依赖漂移的信号 RBL-771）；expected 空则一切 hash 差异意外
- 边界：完全一致/文件集差异/双方为空 outputs
- 能说清「staging 的价值是发现意外差异（依赖浮动/配置泄漏），输入一致性检查应左移到构建」属于加分
