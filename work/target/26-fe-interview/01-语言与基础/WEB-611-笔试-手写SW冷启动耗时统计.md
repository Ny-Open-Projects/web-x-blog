---
title: [WEB-611] 笔试：手写 Service Worker 冷启动耗时统计
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 可观测]
type: 笔试题
---

## WEB-611：笔试：手写 Service Worker 冷启动耗时统计

**答**：实现 SW 冷启动统计方案：① SW 侧在脚本顶层记录 install 时间戳（脚本开始求值时间用 Date.now），fetch 事件里把「页面请求发出 → SW 处理开始」的延迟通过响应头 `x-sw-delay` 返回；② 页面侧读取该头并上报分布；③ SW 用 IndexedDB 持久化「最近一次被终止时间」，唤醒时计算空闲时长（判别冷/热启动）；④ 区分 navigationPreload 开启前后。写出页面侧与 SW 侧实现。

```javascript
// sw.js
const swStart = Date.now(); // 脚本求值开始 ≈ 冷启动开始
let lastAlive = 0;
self.addEventListener('activate', async () => {
  const db = await openDb();
  lastAlive = (await db.get('meta', 'lastAlive')) || 0;
  await db.set('meta', { key: 'lastAlive', t: Date.now() });
});
self.addEventListener('fetch', (e) => {
  const coldStartDelay = Date.now() - swStart; // SW 脚本求值到首个 fetch
  e.respondWith((async () => {
    const res = await fetch(e.request);
    const r = new Response(res.body, res);
    r.headers.set('x-sw-delay', String(coldStartDelay));
    r.headers.set('x-sw-idle', String(swStart - lastAlive)); // 空闲时长判冷热
    return r;
  })());
});
// 页面侧
async function reportSwDelay() {
  const res = await fetch(location.href, { cache: 'no-store' });
  const delay = Number(res.headers.get('x-sw-delay'));
  const idle = Number(res.headers.get('x-sw-idle'));
  beacon({ cold: delay > 100, delay, idle }); // 分布上报
}
```

**评分点**：
- 双侧配合方案完整：SW 打标 + 页面采集
- 冷/热判别用「上次终止时间」持久化（SW 全局变量会被终止重置）
- 响应头透传需要处理 Response 头不可变性（new Response 或 res.headers 可写性）
- 能提出 navigationPreload 抵消冷启动延迟的优化方向
