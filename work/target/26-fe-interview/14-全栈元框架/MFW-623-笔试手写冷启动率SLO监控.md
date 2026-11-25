---
title: [MFW-623] 笔试：手写冷启动率 SLO 监控
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-623：笔试：手写冷启动率 SLO

**答**：实现 `coldStartSLO(requests, { sloTarget, regionBreakdown })`。requests: `{ region, isCold, latencyMs }[]`。规则：1) 总冷启动率 = cold/total；2) 区域分桶：每区域的冷启动率（regionBreakdown=true）；3) 超标区域：冷启动率 > sloTarget（默认 5%）且样本 ≥ 20 → flagged `{ region, rate, action: 'preheat' }`（区域级预热建议——RBL-622 流量加权）；4) 预算视角：冷启动的「错误预算」（月度 5% × 请求数——超预算 = 预热投入立项）；5) 返回 `{ globalRate, byRegion: Array<{ region, rate, flagged }>, budgetLeft }`。边界：requests 空（rate 0——但标 no-data）；单区域全 cold（rate 1——flag）。

```javascript
function coldStartSLO(requests = [], { sloTarget = 0.05, regionBreakdown = true, now = Date.now } = {}) {
  if (!requests.length)
    return { globalRate: 0, noData: true, byRegion: [], budgetLeft: 1 };
  const cold = requests.filter(r => r.isCold).length;
  const globalRate = +(cold / requests.length).toFixed(4);
  const byRegion = [];
  if (regionBreakdown) {
    const groups = new Map();
    for (const r of requests)
      (groups.get(r.region) || groups.set(r.region, { total: 0, cold: 0 }).get(r.region));
    for (const r of requests) groups.get(r.region).total += 1;
    for (const r of requests) if (r.isCold) groups.get(r.region).cold += 1;
    for (const [region, g] of groups) {
      const rate = +(g.cold / g.total).toFixed(4);
      byRegion.push({ region, rate, flagged: g.total >= 20 && rate > sloTarget });
    }
  }
  const monthlyBudget = 0.05;                            // 5% 月度预算
  const budgetLeft = +Math.max(0, (monthlyBudget - globalRate) / monthlyBudget).toFixed(2);
  return { globalRate, byRegion, budgetLeft, exhausted: budgetLeft === 0 };
}

// 自测
const reqs = [
  ...Array.from({ length: 100 }, () => ({ region: 'iad1', isCold: false, latencyMs: 10 })),
  ...Array.from({ length: 10 }, () => ({ region: 'fra1', isCold: true, latencyMs: 500 })),
  ...Array.from({ length: 90 }, () => ({ region: 'fra1', isCold: false, latencyMs: 12 })),
];
let r = coldStartSLO(reqs);
console.log(r.globalRate === 0.05);                      // 10/200
console.log(r.budgetLeft === 0);                         // 恰好用完 5% 预算
console.log(r.byRegion.find(x => x.region === 'fra1').flagged === true);   // 10/100 = 10% > 5%
console.log(r.byRegion.find(x => x.region === 'iad1').flagged === false);  // 0%

// 超预算
r = coldStartSLO([{ region: 'fra1', isCold: true, latencyMs: 500 }, ...Array.from({ length: 8 },
  () => ({ region: 'fra1', isCold: false, latencyMs: 12 }))]);   // 1/9 = 11%
console.log(r.globalRate > 0.05 && r.exhausted === true);

// 空
r = coldStartSLO([]);
console.log(r.noData === true && r.budgetLeft === 1);
```

**评分点**：
- 全局率 + 区域分桶（热点区域的预热定位 RBL-622）；样本量门禁（≥20 防 noise flag）
- 错误预算视角（预算耗尽 = 预热投入立项——SLO 驱动的投资决策 RBL-905）
- 边界（空 no-data/全 cold flag）；预算公式
- 能说清「冷启动率是 Edge 的可用性 SLI——预算耗尽触发预热基础设施投入而非继续忍」属于加分
