---
title: [JS-324] import.meta 与动态 import 的工程用法
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 模块]
type: 面试题
---

## JS-324：import.meta 与动态 import 的工程用法

**答**：
- import.meta：模块元信息——url（模块地址，worker new URL 基准）、env（Vite 环境变量）、resolve（标准演进）
- 动态 import()：运行时加载返回 Promise——路由懒加载、按需加载大依赖（编辑器/图表）、条件加载平台代码
- 预加载配合：`import(/* webpackChunkName */ ...)` 或 `<link rel="modulepreload">` 提示构建器拆包与预取
- 工程守则：dynamic import 的错误处理（网络失败要 catch + 重试/降级）；SSR 环境下 import.meta.url 与 window 差异
- Top-level await + dynamic import 组合：模块级初始化资源

```javascript
// 路由懒加载
const routes = [
  { path: '/editor', component: () => import('./views/Editor.vue') },
];
// 按需加载重依赖
button.onclick = async () => {
  const XLSX = await import('xlsx');   // 只有真正用到才下载
  XLSX.utils.book_new();
};
// worker 相对路径基准
new Worker(new URL('./worker.js', import.meta.url), { type: 'module' });
```
