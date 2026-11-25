---
title: [WEB-407] 无头浏览器（Puppeteer/Playwright）在前端的自测场景有哪些？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-407：无头浏览器（Puppeteer/Playwright）在前端的自测场景有哪些？
**答**：
- 回归自测：关键路径 e2e（登录→下单）、视觉回归（页面截图 diff）、控制台错误监控（page.on console error 监听）。
- 性能采集：CDP 拿 Performance metrics、模拟弱网/CPU 节流跑 Lighthouse CI；定时跑防性能劣化。
- 注意：headless 特征与真实浏览器有差异（字体/UA/渲染），结果做相对比较而非绝对值。

```javascript
const b = await chromium.launch();
const p = await b.newPage({ deviceScaleFactor: 2 });
await p.goto(url);
const errors = [];
p.on('pageerror', e => errors.push(e.message));
await p.screenshot({ path: 'home.png' });
console.log(errors.length === 0 ? 'clean' : errors);
console.log('截图 diff + 错误监听 = 最轻量回归');
```
