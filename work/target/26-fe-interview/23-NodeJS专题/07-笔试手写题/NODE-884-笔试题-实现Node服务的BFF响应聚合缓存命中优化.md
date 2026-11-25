---
title: [NODE-884] 笔试题——实现 BFF 聚合缓存命中优化（部分命中渲染）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-884：手写部分命中

**需求与边界**：
- 需求：聚合部分命中（SCN-NODE-823）——① 聚合响应的组件级缓存（SCN-NODE-823）；② 部分命中渲染（命中组件直接用缓存、MISS 组件回源——SCN-NODE-823）；③ 缓存命中率看板（SCN-NODE-718）；④ 命中优化的建议（哪些组件 TTL 调整——SCN-NODE-718）。
- 边界：① 缓存与降级交互（缓存命中优先于降级——SCN-NODE-778 级联首层）；② 命中率下降告警（SCN-NODE-718）；③ 缓存键维度对齐（SCN-NODE-805）。

**答**：
```javascript
async function aggregateWithCache(spec, ctx) {
  const out = {}; const misses = [];
  for (const d of spec) {                              // SCN-NODE-740 DAG
    const key = cacheKey(d, ctx);                      // SCN-NODE-805
    const hit = componentCache.get(key);
    if (hit) out[d.key] = hit; else misses.push(d);    // 部分命中（SCN-NODE-823）
  }
  const fresh = await dagOrchestrate(misses, ctx);     // 只编排 MISS（SCN-NODE-813）
  fresh.forEach(f => componentCache.set(cacheKey(f, ctx), f.data, { ttl: d.ttl }));
  const hitRate = 1 - misses.length / spec.length;
  if (hitRate < 0.5 && spec.length > 5)                // 命中率下降告警（SCN-NODE-718）
    alert({ type: 'CACHE_HIT_LOW', hitRate, suggest: tuneTtls(spec) });
  return { data: { ...out, ...fresh } };
}
```

**评分点**:
- 部分命中渲染（命中跳过编排——SCN-NODE-823）。
- DAG 编排只跑 MISS（SCN-NODE-813）。
- 命中率告警 + TTL 调优建议（SCN-NODE-718）。
- 缓存键全维度（SCN-NODE-805）。
