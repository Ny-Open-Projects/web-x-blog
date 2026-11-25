---
title: [MFW-639] 笔试：手写 TTL 抖动分配器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-639：笔试：手写 TTL 抖动分配器

**答**：实现 `jitteredTtls(routes, { baseTtl, jitterRatio })`。routes: `string[]`。规则：1) 每路由：ttl = baseTtl × (1 + rand × jitterRatio)；2) **确定性抖动**（同路由每次构建同 TTL——route 路径 hash 决定抖动量（非 Math.random——构建产物可复现 RBL-543）；3) 分布审计：N 路由的 TTL 分布（最小/最大/中位——抖动是否有效分散：stdDev > base × 0.1）；4) 雪崩窗口计算：max(同刻过期数) < N × 20%（合格）。边界：routes 空；jitterRatio=0（全同 TTL——退化警告）；单路由。

```javascript
function jitteredTtls(routes = [], { baseTtl = 60, jitterRatio = 0.5 } = {}) {
  const djb2 = (s) => { let h = 5381; for (const c of s) h = ((h << 5) + h + c.charCodeAt(0)) >>> 0;
    return h / 2 ** 32; };                               // 0~1 确定性
  const out = {};
  for (const route of routes) {
    const factor = 1 + djb2(route) * jitterRatio;        // 1~1.5 确定性抖动
    out[route] = Math.floor(baseTtl * factor);
  }
  return out;
}
function auditJitter(ttls, baseTtl) {
  const values = Object.values(ttls);
  if (values.length < 2) return { ok: true, note: '单路由无需抖动审计' };
  const mean = values.reduce((s, v) => s + v, 0) / values.length;
  const std = Math.sqrt(values.reduce((s, v) => s + (v - mean) ** 2, 0) / values.length);
  const ok = std > baseTtl * 0.1;                        // stdDev 够大 = 分散有效
  return { ok, std: +std.toFixed(2), mean: +mean.toFixed(2),
    min: Math.min(...values), max: Math.max(...values),
    warning: ok ? null : 'TTL 分散不足——雪崩窗口仍集中' };
}

// 自测
const routes = Array.from({ length: 200 }, (_, i) => `/page/${i}`);
let ttls = jitteredTtls(routes, { baseTtl: 60, jitterRatio: 0.5 });
console.log(Object.keys(ttls).length === 200);
// 确定性：同路由同 TTL
console.log(jitteredTtls(routes, { baseTtl: 60, jitterRatio: 0.5 })['/page/0'] === ttls['/page/0']);
// 分布审计：200 路由的 stdDev 应足够大
let audit = auditJitter(ttls, 60);
console.log(audit.ok === true);
console.log(audit.min >= 60 && audit.max <= 90);         // 60~90 范围
// jitterRatio=0 退化
ttls = jitteredTtls(routes, { baseTtl: 60, jitterRatio: 0 });
audit = auditJitter(ttls, 60);
console.log(audit.ok === false && audit.warning.includes('不足'));
// 空
console.log(Object.keys(jitteredTtls([], { baseTtl: 60 })).length === 0);
```

**评分点**：
- 确定性抖动（路径 hash——构建可复现 RBL-543；Math.random 不可复现）
- 分布审计（stdDev ≥ base×10%——抖动有效性的量化判定）；ratio=0 退化告警
- 边界（空/单路由）；TTL 范围 [base, base×(1+ratio)]
- 能说清「TTL 抖动打散同刻过期（雪崩根源）——确定性 hash 抖动兼顾可复现与分散」属于加分
