---
title: [WEB-342] stale-while-revalidate 和 immutable 怎么用？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-342：stale-while-revalidate 和 immutable 怎么用？
**答**：
- stale-while-revalidate=86400：过期后先返回旧内容（0 延迟），后台异步重新验证，下次拿到新的——体验与新鲜度兼顾。
- immutable：配合 max-age 告诉浏览器"有效期内永不协商"，用户强刷时带 hash 的静态资源仍可命中，强刷请求骤减。
- 适用：immutable 给指纹文件名资源；swr 给接口或半动态资源；不可用于 HTML 入口。

```javascript
// Cache-Control: max-age=31536000, immutable   → 指纹文件
// Cache-Control: max-age=60, stale-while-revalidate=300 → 接口
const策略 = (res) => res.isHashed
  ? 'max-age=31536000, immutable'
  : 'max-age=60, stale-while-revalidate=300';
console.log(策略({ isHashed: true }));
```
