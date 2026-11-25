---
title: [H5-240] Vite/webpack 里 Worker 怎么打包（new Worker(new URL)）
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-240：Vite/webpack 里 Worker 怎么打包（new Worker(new URL(...))）

**答**：
- 标准写法：`new Worker(new URL('./worker.js', import.meta.url), { type: 'module' })`——构建器识别后自动拆分 chunk、处理依赖与产物路径
- Vite 加餐：`new MyWorker()` 直接 import worker 文件（`?worker` 后缀），或 `?worker&inline` 内联成 blob 避免 CSP file:// 问题
- 打包细节：worker 的 import 依赖会被单独打包；worker 里的动态 import 也支持
- 内联场景：blob URL 方案在「严格 CSP（worker-src）」或单文件 HTML 分发时必需
- 常见错误：直接 `new Worker('./worker.js')` 在打包后路径失效（相对路径基于 HTML 而非 JS chunk）——这就是必须用 new URL 的原因

```javascript
// 推荐写法：构建器友好
const worker = new Worker(new URL('./parse.worker.js', import.meta.url), { type: 'module' });
// Vite 简写
import ParseWorker from './parse.worker?worker';
const w = new ParseWorker();
```
