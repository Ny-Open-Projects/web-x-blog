---
title: [H5-252] SW 为什么更新不生效，skipWaiting 与 clients.claim
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, PWA]
type: 面试题
---

## H5-252：SW 为什么更新不生效，skipWaiting 与 clients.claim

**答**：
- 更新判定：浏览器每次导航重新拉 sw.js，字节不同才触发更新流程；sw.js 本身绝不能被缓存（Cache-Control: no-cache）
- 不生效三原因：新 SW 卡在 waiting（旧 SW 还在控制页面）、页面自己被 SW 缓存了旧 HTML、缓存优先策略读了旧资源
- 三招解决：sw.js 响应头 no-cache + 修改版本号注释；新 SW 里 skipWaiting() 快速接管；activate 后通知页面 reload
- 用户侧体验：不要无脑自动 reload（打断输入），提供「新版本可用，点击刷新」提示条
- 排查工具：chrome://serviceworker-internals 看 SW 状态，DevTools Application 面板「Update on reload」调试

```javascript
// sw.js
self.addEventListener('message', (e) => {
  if (e.data === 'SKIP_WAITING') self.skipWaiting(); // 立即激活
});
// 页面侧检测更新
setInterval(async () => {
  await registration.update(); // 手动触发检查（默认导航时才查）
  if (registration.waiting) showUpdateToast();
}, 60000);
```
