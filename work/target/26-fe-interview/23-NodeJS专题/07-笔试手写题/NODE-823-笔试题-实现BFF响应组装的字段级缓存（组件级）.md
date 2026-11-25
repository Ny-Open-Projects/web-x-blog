---
title: [NODE-823] 笔试题——实现组件级数据缓存（分区 TTL）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-823：手写组件级缓存

**需求与边界**：
- 需求：组件级缓存（SCN-NODE-718）——① 页面分区缓存（页面内组件各自 TTL——SCN-NODE-718 三级）；② 缓存键分区（组件参数 hash——SCN-NODE-805 全维度）；③ 独立失效（组件数据更新只失效该组件——粒度）；④ 组装（多组件缓存拼装——混合 HIT/MISS）。
- 边界：① 分区 TTL 声明（热榜 10s/商品 5min/推荐 1min——变更频率准则，SCN-BLD-226）；② MISS 时的部分渲染（部分组件缓存命中——只渲染 MISS 组件）；③ 缓存雪崩防御（分区 TTL 抖动——SCN-NODE-640）。

**答**：
```javascript
const zoneCache = new Map();                           // 组件级缓存（SCN-NODE-718）
const ZONES = { hot: { ttl: 10_000 }, goods: { ttl: 300_000 }, recommend: { ttl: 60_000 } };
async function assemblePage(req) {
  const out = {};
  const misses = [];
  for (const [zone, cfg] of Object.entries(ZONES)) {   // 分区独立 TTL（变更频率——SCN-BLD-226）
    const key = hash([zone, req.params, req.grayBucket]);   // 全维度（SCN-NODE-805）
    const hit = zoneCache.get(key);
    if (hit) out[zone] = hit; else misses.push({ zone, key, cfg });
  }
  const fresh = await Promise.all(misses.map(m =>      // 只渲染 MISS（部分渲染）
    renderZone(m.zone, { signal: deadline(m.cfg.ttl) })));
  fresh.forEach(({ zone, data, key }) => {
    zoneCache.set(key, data, { ttl: cfg.ttl + jitter(cfg.ttl * 0.1) });   // TTL 抖动（SCN-NODE-640）
    out[zone] = data;
  });
  res.setHeader('X-Cache', summarize(out));            // HIT/MISS 汇总（SCN-NODE-718 可观测）
  return out;
}
```

**评分点**:
- 分区独立 TTL（变更频率准则——SCN-BLD-226）。
- MISS 部分渲染（缓存命中组件跳过——性能）。
- 全维度键（SCN-NODE-805）+ TTL 抖动（SCN-NODE-640）。
- HIT/MISS 汇总（可观测——SCN-NODE-718）。
