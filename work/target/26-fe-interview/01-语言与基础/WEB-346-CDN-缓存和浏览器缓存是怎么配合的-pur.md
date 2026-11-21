---
title: [WEB-346] CDN 缓存和浏览器缓存是怎么配合的？purge 是什么？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-346：CDN 缓存和浏览器缓存是怎么配合的？purge 是什么？
**答**：
- 两层缓存：浏览器先查本地，miss 才到 CDN；CDN 命中（HIT）则免回源，miss 才到源站。
- 发布新版本时浏览器端靠新 URL 绕开旧缓存；CDN 侧要么 URL 变了自然 miss，要么对旧 URL 主动 purge 刷新。
- 排查技巧：响应头 X-Cache: HIT/MISS、CF-Cache-Status、Age（已缓存秒数）判断命中层级；大促前预热 CDN（主动拉取）避免首波全 miss。

```javascript
// 请求路径: 浏览器缓存 → CDN → 源站
const read = (url) => {
  const local = disk[url]; if (local && fresh(local)) return { src: 'browser' };
  const cdn = cdnCache[url];
  return cdn ? { src: 'CDN HIT', age: cdn.age } : { src: 'MISS→回源' };
};
console.log(read('/a.js'));
// purge: POST /purge { path: '/a.js' } 清 CDN 节点缓存
```
