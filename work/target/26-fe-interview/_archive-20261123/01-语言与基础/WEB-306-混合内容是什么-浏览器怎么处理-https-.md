---
title: [WEB-306] 混合内容是什么？浏览器怎么处理 https 页面里的 http 资源？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, HTTPS]
type: 面试题
---

## WEB-306：混合内容是什么？浏览器怎么处理 https 页面里的 http 资源？
**答**：
- https 页面引用 http 子资源即混合内容：主动内容（script/iframe/xhr）现代浏览器直接 block；被动内容（img/audio/video）多数浏览器允许但地址栏降级警示。
- 标准修复：CSP upgrade-insecure-requests 让浏览器把 http 子资源自动升级为 https；或服务端全量重定向。
- 排查手段：Console 的混合内容警告、CSP report-uri 收集上报，再逐域修复。

```javascript
// CSP 头：Content-Security-Policy: upgrade-insecure-requests
function rewrite(src, csp) {
  if (csp.includes('upgrade-insecure-requests') && src.startsWith('http://')) {
    return src.replace('http://', 'https://'); // 图片升级失败则不加载
  }
  return src;
}
console.log(rewrite('http://cdn.old.com/a.jpg', 'upgrade-insecure-requests'));
```
