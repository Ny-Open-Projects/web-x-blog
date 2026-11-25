---
title: [BLD-034] 动态 import 的魔法注释有哪些？webpackChunkName、webpackPrefetch、webpackPreload 分别生成什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-034：动态 import 的魔法注释有哪些？webpackChunkName、webpackPrefetch、webpackPreload 分别生成什么？
**答**：
- webpackChunkName: "xxx"：命名异步 chunk，产物名变成 xxx.[contenthash].js，配合 chunkFilename 调试友好。
- webpackPrefetch: true：构建出 `<link rel="prefetch" href="...">`，浏览器空闲时低优先级下载——适合"大概率会被访问的下一屏"。
- webpackPreload: true：生成 `<link rel="preload">`，与父 chunk 并行高优先级加载——适合"当前 chunk 渲染前必需"的资源（如关键 chunk 依赖的 chunk）。
- 其他：webpackMode（eager/demand）、webpackIgnore（跳过打包直接留 URL）、webpackInclude/Exclude（表达式动态 import 过滤）。
- 面试点：prefetch 不阻塞当前页，preload 会与关键路径抢带宽，别滥用 preload。

```javascript
// src/routes.js：魔法注释全家桶
const routes = [
  {
    path: '/report',
    // 命名 chunk + 空闲时预取
    component: () => import(
      /* webpackChunkName: "report" */
      /* webpackPrefetch: true */
      './views/Report.vue'
    ),
  },
  {
    path: '/detail',
    // 与当前 chunk 并行高优加载 必需资源
    component: () => import(
      /* webpackChunkName: "detail" */
      /* webpackPreload: true */
      './views/Detail.vue'
    ),
  },
  {
    path: '/force',
    // eager：跳过 jsonp 拉取 直接打进父 chunk
    component: () => import(
      /* webpackChunkName: "force" */
      /* webpackMode: "eager" */
      './views/Force.vue'
    ),
  },
];

// 产物验证（text 代码块）：
// dist/report.3f9a2c1b.js
// index.html 中出现 <link rel="prefetch" href="report.3f9a2c1b.js" as="script">
```
