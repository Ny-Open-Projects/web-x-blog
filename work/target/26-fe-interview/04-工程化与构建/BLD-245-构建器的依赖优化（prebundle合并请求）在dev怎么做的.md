---
title: [BLD-245] dev 服务器的请求优化（预构建/合并/协商缓存）怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-245：dev 请求优化怎么做？
**答**：
- 请求瀑布治理：模块请求瀑布（index → a → b 链式发现）——预构建依赖（SCN-BLD-210）+ import 分析预推（vite 预推 import 链并行请求）。
- 协商缓存：dev 转换结果带 ETag（模块内容 hash），304 免重传——HMR 触发前的常规请求秒回。
- HTTP/2 的前提：dev server 开 h2（多路复用让 unbundled 的多请求不再致命）。
- 请求上限场景：巨型依赖树（几千模块）即使 h2 也慢——预打包整个大依赖（optimizeDeps.include 强制）。
- 追问钩子：为什么「unbundled dev」在超大依赖树上仍然慢——unbundled 省的是「转换时间」（按需），但请求发现是串行瀑布（浏览器逐层 import 发现）；h2 并行化依赖「已知 URL」，瀑布中的 URL 要先请求父模块才知道——所以巨型依赖必须预打包（把瀑布压平为一个请求），按需转换只适合源码。

```javascript
// vite dev 请求优化
optimizeDeps: { include: ['antd/es', 'lodash-es'] },   // 大依赖强制预打包（压平瀑布）
server: { https: true, hmr: { port: 24678 } },        // h2 多路复用
// ETag 协商缓存（304）
transformMiddleware: etagByContentHash
```
