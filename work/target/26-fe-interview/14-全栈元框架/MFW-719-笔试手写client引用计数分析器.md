---
title: [MFW-719] 笔试：手写 client 引用计数分析器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-719：笔试：手写 client 引用计数

**答**：实现 `clientRefStrategy(routes, { sharedThreshold = 5, minRouteSizeKB = 20 })`. routes: `Record<route, { components: string[], sizeKB?: number }>`。规则：1) 引用计数：组件被 N 路由引用；2) **策略分级**：count ≥ sharedThreshold → 'shared-chunk'（独立 chunk）；count 2~4 且组件大（sizeKB ≥ minRouteSizeKB）→ 'shared-chunk'（大组件也拆——避免多路由重复传）；count ≤ 1 → 'inline-route'（并入路由）；3) **惰性标记**：动态 import 的组件 → 'lazy'（不管引用数——总是按需 RBL-596）；4) 返回 `{ strategies: Record<name, strategy>, summary: { shared, inline, lazy } }`。边界：routes 空（全部 inline）；组件重复出现在同一路由（计数 1 次）；lazy 优先于 shared。

```javascript
function clientRefStrategy(routes = {}, { sharedThreshold = 5, minRouteSizeKB = 20 } = {}) {
  const refCount = new Map();
  const lazySet = new Set();
  for (const [route, meta] of Object.entries(routes)) {
    const unique = new Set(meta.components);             // 同路由去重
    for (const c of unique) {
      if (meta.lazy?.includes(c)) { lazySet.add(c); continue; }   // lazy 优先
      refCount.set(c, (refCount.get(c) ?? 0) + 1);
    }
  }
  const strategies = {};
  const summary = { shared: 0, inline: 0, lazy: lazySet.size };
  for (const [name, count] of refCount) {
    const size = routes[Object.keys(routes).find(r =>
      routes[r].components?.includes(name))]?.sizeKB ?? 0;
    let strategy;
    if (count >= sharedThreshold) strategy = 'shared-chunk';
    else if (count >= 2 && size >= minRouteSizeKB) strategy = 'shared-chunk';
    else strategy = 'inline-route';
    strategies[name] = strategy;
    summary[strategy]++;
  }
  for (const name of lazySet) strategies[name] = 'lazy';
  return { strategies, summary };
}

// 自测
const routes = {
  '/home': { components: ['Button', 'Header', 'HeroBanner'], lazy: ['Video'] },
  '/shop': { components: ['Button', 'Header', 'ProductCard', 'FilterBar'] },
  '/cart': { components: ['Button', 'Header'] },
  '/admin': { components: ['Button', 'HeavyEditor'], sizeKB: 80 },
};
let r = clientRefStrategy(routes, { sharedThreshold: 3 });
console.log(r.strategies.Button === 'shared-chunk');     // 4 路由 ≥ 3
console.log(r.strategies.Header === 'shared-chunk');
console.log(r.strategies.HeroBanner === 'inline-route'); // 1 路由
console.log(r.strategies.Video === 'lazy');              // lazy 优先
console.log(r.strategies.HeavyEditor === 'shared-chunk');// 大组件 1 路由也拆（sizeKB 80 ≥ 20）
console.log(r.summary.lazy === 1);

// 小组件低引用 → inline
r = clientRefStrategy({ '/about': { components: ['SmallBadge'], sizeKB: 5 } },
  { sharedThreshold: 3, minRouteSizeKB: 20 });
console.log(r.strategies.SmallBadge === 'inline-route'); // 1 路由 + 小 → inline
// 空
r = clientRefStrategy({});
console.log(Object.keys(r.strategies).length === 0);
```

**评分点**：
- 引用计数 + 三级策略（shared-chunk/inline-route/lazy——lazy 优先于引用计数）
- 大组件的 shared-chunk 条件（低引用但大体积也拆——避免多路由重复传）；同路由去重
- 边界（空 routes/小组件 inline）；summary 统计
- 能说清「client 引用计数影响 chunk 分割：高引用独立 chunk 复用缓存、低引用并入路由减少 RTT」属于加分
