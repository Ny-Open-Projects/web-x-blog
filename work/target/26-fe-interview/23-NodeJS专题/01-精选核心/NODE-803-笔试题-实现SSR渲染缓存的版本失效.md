---
title: [NODE-803] 笔试题——实现 SSR 渲染缓存的主动失效（数据版本联动）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-803：手写 SSR 失效

**需求与边界**：
- 需求：SSR 页面缓存失效（SCN-NODE-756/688）——① 数据版本键（页面数据版本 hash——SCN-NODE-718 全维度）；② 数据更新触发失效（写路径失效页面缓存——SCN-FIN-688 删缓存）；③ 跨实例失效（pub/sub 广播——SCN-NODE-727）；④ 降级兜底（失效消息丢失——短 TTL 兜底）。
- 边界：① 失效粒度（页面级 vs 组件级——SCN-NODE-718 三级）；② 失效风暴（批量更新时合并失效——SCN-OPS-320 降噪）；③ 版本键的传递（数据版本从 BFF 到渲染层——SCN-NODE-718）。

**答**：
```javascript
// 数据版本键（SCN-NODE-718）
async function renderPage(req) {
  const dataVer = await dataVersion(req.url);          // 数据版本 hash（BFF 下发）
  const key = hash([req.url, dataVer, req.grayBucket, req.profile]);
  return cache.get(key) ?? renderAndCache(key, req);   // 版本变 → 自然失效
}
// 写路径触发失效（SCN-FIN-688 删缓存——版本推进）
async function afterDataUpdate(url) {
  await bumpDataVersion(url);                          // 版本号推进（原子）
  pub.publish('ssr:invalidate', url);                  // 跨实例广播（SCN-NODE-727）
}
// 合并失效（批量更新——SCN-OPS-320）
const pending = new Set(); let timer;
function invalidateMany(urls) {
  urls.forEach(u => pending.add(u));
  clearTimeout(timer); timer = setTimeout(() => {      // 100ms 合并
    pending.forEach(bumpDataVersion); pending.clear();
  }, 100);
}
```

**评分点**:
- 数据版本键驱动失效（版本变 → 自然 miss——比删缓存更稳）。
- 跨实例广播 + 短 TTL 兜底（SCN-NODE-727/640 双保险）。
- 批量失效合并（失效风暴防御——SCN-OPS-320）。
- 版本键全维度（SCN-NODE-718）。

## 变体与延伸（补充）

**变体与延伸**：

1. 批量更新 1000 个商品触发 1000 次失效，风暴怎么压 → 失效消息按 100ms 窗口合并成集合一次广播，并加 0 到 500ms 随机延迟打散，避免同一秒打满渲染层。
2. pub/sub 消息丢了，缓存一直是旧数据怎么办 → 缓存 TTL 兜底设 60s，再加每 5 分钟一次全量版本键对账，不一致即删，不能只依赖广播。
3. 版本键怎么算才既精确又不过度失效 → 用页面依赖的实体 id 加 version 组合成 hash，只失效依赖该实体的页面，而不是一动数据就全站清空。
