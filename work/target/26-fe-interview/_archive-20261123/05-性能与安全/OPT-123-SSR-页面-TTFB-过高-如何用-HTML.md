---
title: [OPT-123] SSR 页面 TTFB 过高，如何用 HTML 片段缓存/组件级缓存优化？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-123：SSR 页面 TTFB 过高，如何用 HTML 片段缓存/组件级缓存优化？

**答**：
- SSR TTFB 高的根因：每次请求都完整执行 renderToString + 数据拉取。定位后按"组件热点"分级缓存。
- 组件级缓存：导航、推荐位、页头这类低频变化组件 renderToString 一次，结果按 key（如 category+hour）存内存/Redis，命中直接拼 HTML。
- 页面级缓存：登录无关页整页 HTML 缓存 1~5 分钟，配合 revalidate；登录相关页用 ESI/边缘片段。
- 缓存要挂"失效钩子"：CMS 发布/库存变更时主动 purge，避免等 TTL。

```javascript
// 一一对应：SSR 组件级缓存——热点组件 renderToString 结果复用
const LRU = require('lru-cache');
const fragmentCache = new LRU({ max: 500, ttl: 1000 * 60 * 5 }); // 5 分钟

async function renderWithFragmentCache(Component, props, cacheKey) {
  const hit = fragmentCache.get(cacheKey);
  if (hit) return hit; // 命中：跳过数据拉取 + renderToString
  const data = await Component.fetchData(props);          // 组件自带数据获取
  const html = require('react-dom/server').renderToString(
    React.createElement(Component, { ...props, ...data })
  );
  fragmentCache.set(cacheKey, html);
  return html;
}

// Express 路由：页面 = 三个片段（两冷一热）拼接
app.get('/p/:id', async (req, res) => {
  const [header, recList] = await Promise.all([
    renderWithFragmentCache(Header, {}, `header:${Math.floor(Date.now() / 36e5)}`), // 按小时缓存
    renderWithFragmentCache(Recommend, { page: req.params.id }, `rec:${req.params.id}`),
  ]);
  const detail = await renderDetailFresh(req.params.id); // 详情实时渲染
  res.send(`<!doctype html><html><body>${header}<main>${detail}</main>${recList}</body></html>`);
});
```
