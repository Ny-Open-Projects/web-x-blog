---
title: [WEB-348] no-store、no-cache、private、public 到底怎么选？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-348：no-store、no-cache、private、public 到底怎么选？
**答**：
- no-store：任何环节都不许存，最严格（敏感接口如验证码、账单）。
- no-cache：可以存但每次必须协商验证（HTML 入口、时效接口）。
- private：只许浏览器缓存，CDN/共享代理不许存（含用户数据的接口）；public 才允许共享缓存。
- 常见组合：HTML no-cache；指纹资源 public+max-age+immutable；用户接口 private 或 no-store。

```javascript
const policy = {
  'index.html': 'no-cache',
  'app.9f2c1.js': 'public, max-age=31536000, immutable',
  '/api/me': 'private, no-cache',
  '/api/captcha': 'no-store',
};
console.log(JSON.stringify(policy, null, 1));
```
