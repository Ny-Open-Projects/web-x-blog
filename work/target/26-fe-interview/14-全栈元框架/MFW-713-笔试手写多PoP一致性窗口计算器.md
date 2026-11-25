---
title: [MFW-713] 笔试：手写多 PoP 一致性窗口计算
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-713：笔试：手写多 PoP 一致性窗口

**答**：实现 `consistencyWindow(pops, { propagateMs, swrMs })`。pops: `{ id, lastRenderedAt }[]`（各 PoP 的内容渲染时间戳）。规则：1) 一致性窗口 = max(lastRenderedAt) − min(lastRenderedAt)（最旧与最新的差——不一致的最大时间跨度）；2) 全局窗口 = 窗口 + propagateMs（失效广播延迟）+ swrMs（SWR 窗口——用户可能看到的旧数据总时长）；3) 容忍度判定：全局窗口 > maxAcceptableMs → 'degraded'（不一致窗口超容忍——需要缩短 SWR 或加速广播）；4) 返回 `{ window, globalWindow, verdict, oldestPop, newestPop }`。边界：pops 空（0）；单 PoP（窗口 0）；pops 全同（0——一致）。

```javascript
function consistencyWindow(pops = [], { propagateMs = 500, swrMs = 60000, maxAcceptableMs = 120000 } = {}) {
  if (!pops.length) return { window: 0, globalWindow: 0, verdict: 'ok', oldestPop: null, newestPop: null };
  const times = pops.map(p => p.lastRenderedAt);
  const window = Math.max(...times) - Math.min(...times);
  const globalWindow = window + propagateMs + swrMs;
  const oldest = pops.reduce((a, b) => a.lastRenderedAt < b.lastRenderedAt ? a : b);
  const newest = pops.reduce((a, b) => a.lastRenderedAt > b.lastRenderedAt ? a : b);
  return {
    window,
    globalWindow: window + propagateMs + swrMs,
    verdict: globalWindow > maxAcceptableMs ? 'degraded' : 'ok',
    oldestPop: oldest.id, newestPop: newest.id,
  };
}

// 自测
const pops = [
  { id: 'iad', lastRenderedAt: 1000 },
  { id: 'fra', lastRenderedAt: 2000 },                   // 比 iad 新 1s
  { id: 'sin', lastRenderedAt: 1500 },
];
let r = consistencyWindow(pops, { propagateMs: 500, swrMs: 60000, maxAcceptableMs: 65000 });
console.log(r.window === 1000);                          // 2000-1000
console.log(r.globalWindow === 61500);                   // 1000+500+60000
console.log(r.verdict === 'ok');                         // 61500 < 65000
console.log(r.oldestPop === 'iad' && r.newestPop === 'fra');

// 超容忍
r = consistencyWindow(pops, { propagateMs: 500, swrMs: 60000, maxAcceptableMs: 50000 });
console.log(r.verdict === 'degraded');                   // 61500 > 50000

// 单 PoP
r = consistencyWindow([{ id: 'single', lastRenderedAt: 1000 }]);
console.log(r.window === 0 && r.verdict === 'ok');
// 空
console.log(consistencyWindow([]).window === 0);
```

**评分点**：
- 窗口公式正确（max-min 的 PoP 间差 + propagate + swr——用户可见的旧数据总时长）
- verdict 判定（maxAcceptableMs 的业务容忍度——超容忍触发 SWR 缩短或广播加速）
- 边界（空/单 PoP/全同）；oldest/newest 的 PoP 定位（哪个节点落后）
- 能说清「Edge SSG 的一致性窗口 = PoP 间渲染差 + 广播延迟 + SWR——比中心 SSG 更大因为多副本独立刷新」属于加分
