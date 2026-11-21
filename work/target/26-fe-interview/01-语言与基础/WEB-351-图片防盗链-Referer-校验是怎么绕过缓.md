---
title: [WEB-351] 图片防盗链 Referer 校验是怎么绕过缓存的？有什么副作用？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-351：图片防盗链 Referer 校验是怎么绕过缓存的？有什么副作用？
**答**：
- 网关按 Referer/Referer 白名单决定是否发图片；带 Referer 校验的响应若被缓存，后续不同 Referer 的请求会命中同一份缓存 → 误放/误拒。
- 正确姿势：CDN 侧把 Referer 纳入缓存 key（等同 Vary），或者防盗链在边缘执行且结果不缓存。
- 前端配合：referrerPolicy 控制 no-referrer/partial，跨站图片注意 Referer 策略导致的 403。

```javascript
// CDN 缓存 key = URL + Vary: Referer
const key = (req) => req.url + '|' + (req.referer?.startsWith('https://my.com') ? 'allow' : 'deny');
console.log(key({ url: '/a.png', referer: 'https://my.com/x' }));  // allow
// meta name=referrer content=no-referrer → 外站引用图片 403
```
