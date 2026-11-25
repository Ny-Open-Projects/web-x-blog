---
title: [H5-239] Worker 里能不能用 fetch/XHR/importScripts
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-239：Worker 里能不能用 fetch/XHR/importScripts

**答**：
- 都可以：Worker 是独立的全局环境，自带 fetch、XMLHttpRequest、WebSocket、importScripts（同步导入脚本）
- importScripts：模块 worker（type: 'module'）里用 import 语句替代；经典 worker 里 importScripts 同步加载多个依赖
- 模块支持：`new Worker('a.js', { type: 'module' })` 后可 import npm 包（配合打包器处理 worker 产物）
- 同源规则与主线程一致：跨域 fetch 需要 CORS；importScripts 也要同源或 CORS
- 实用组合：Worker 里 fetch + 分片解析 + progress 回传，是导入大文件（Excel/CSV）的标配架构

```javascript
// 经典 worker
importScripts('lib/papaparse.min.js', 'lib/lodash.min.js'); // 同步加载
self.onmessage = async ({ data }) => {
  const res = await fetch(data.url);       // ✅ Worker 里可直接 fetch
  const rows = Papa.parse(await res.text()).data;
  postMessage({ rows: rows.length });
};
```
