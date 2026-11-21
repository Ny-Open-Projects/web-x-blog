---
title: [BAS-177] iframe 的加载对主页面有什么影响？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-177：iframe 的加载对主页面有什么影响？
**答**：
- 主页面 load 事件要等所有 iframe 加载完，慢广告 iframe 会拖长整体加载时间。
- 跨源 iframe 运行在独立渲染进程（站点隔离），崩溃不影响主页面，但 postMessage 通信有成本。
- 优化：`loading="lazy"` 延迟到视口附近再加载，或 onload 后再赋 src；iframe 内资源与主页面不共享缓存键策略要单独考虑。

```html
<!-- load 事件会等 iframe，慢 iframe 拖慢主页面 -->
<iframe src="https://ads.example.com" loading="lazy" title="广告"></iframe>
<!-- loading=lazy 视口外不加载；或 JS 里先不设 src，onload 后再赋值 -->
<!-- 跨源 iframe 独立进程：崩溃隔离，但通信要走 postMessage -->
```
