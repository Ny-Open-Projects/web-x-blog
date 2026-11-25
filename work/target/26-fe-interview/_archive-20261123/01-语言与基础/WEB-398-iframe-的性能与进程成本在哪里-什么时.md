---
title: [WEB-398] iframe 的性能与进程成本在哪里？什么时候该用？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-398：iframe 的性能与进程成本在哪里？什么时候该用？
**答**：
- 成本：独立文档树（完整加载解析）、独立进程（跨站点时，内存爆炸）、主线程事件与渲染互不共享、同层渲染在移动端有坑。
- 合理场景：真正的第三方隔离（支付、广告、编辑器沙箱）、微前端隔离需求；不合理：仅当"分割代码"用。
- 优化：iframe loading=lazy 延迟加载、content-visibility 配合、通信用 postMessage 节流、能换 Web Component/模块联邦就换。

```javascript
<iframe src="https://pay.example.com" loading="lazy" sandbox="allow-scripts allow-same-origin"></iframe>
const cost = (iframes) => iframes * '~50-100MB 进程内存（跨站点）';
console.log('iframe 是进程级隔离，不是轻量组件');
```
