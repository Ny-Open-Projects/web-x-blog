---
title: [NODE-718] BFF 缓存策略（页面级/组件级缓存）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-718：BFF 缓存怎么做？
**答**：
- 三级缓存：页面级缓存（整页渲染结果缓存——URL+参数 hash 键——静态化页面）、组件级缓存（页面内缓存友好组件的数据缓存——分区 TTL）、数据级缓存（下游响应缓存——SCN-NODE-640）。
- 缓存键设计：URL + 端 profile + 灰度标记 + 关键参数（全维度——漏维度串数据，SCN-NODE-692 Vary 同源）；用户维度缓存谨慎（命中低+泄露面——登录后内容不页面级缓存）。
- 失效：TTL 分级（页面级短——数据时效）+ 主动失效（数据更新失效页面缓存——SCN-FIN-688 删缓存）；缓存标头透传（X-Cache: HIT/MISS——可观测）。
- 追问钩子：为什么「页面级缓存的键要含灰度标记」——灰度版本 B 的页面与版本 A 不同（A 用户的页面缓存返回给 B 用户——灰度失效）；缓存键维度 = 影响响应的所有维度（端/灰度/语言/参数），漏一个维度就是「数据串页」——SCN-NODE-692 的 Vary 原则在 BFF 缓存的直接应用。

```javascript
const pageCache = new LRUCache({ max: 10000, ttl: 30_000 });
async function renderPage(req) {
  const key = hash([req.url, req.profile, req.grayBucket, req.locale]);   // 全维度键
  const hit = pageCache.get(key);
  if (hit) { res.setHeader('X-Cache', 'HIT'); return hit; }
  const html = await render(req);
  pageCache.set(key, html);
  res.setHeader('X-Cache', 'MISS');
  return html;
}
```
