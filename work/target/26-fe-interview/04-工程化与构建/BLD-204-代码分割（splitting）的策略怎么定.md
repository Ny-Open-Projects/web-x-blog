---
title: [BLD-204] 代码分割的策略（路由/组件/供应商怎么切）怎么定？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-204：代码分割策略怎么定？
**答**：
- 三层分割：路由级（每路由异步入口——最粗粒度稳定收益）、组件级（重组件 lazy：编辑器/图表/富文本）、供应商分割（splitChunks：框架稳定缓存）。
- splitChunks 的关键配置：chunks: 'all'、maxSize 拆大包、cacheGroups 按来源分组（react 系/vendor）、minChunks 复用阈值——过度分割会因请求开销反而变慢。
- 预加载策略：首屏 chunk preload、 hover 概率路由 prefetch（magic comments）——分割收益依赖加载编排。
- 反模式：把每个小组件都 lazy（请求碎片化）、vendor 拆得过碎（缓存粒度 vs 请求数失衡）。
- 追问钩子：为什么「vendor 拆得过碎」反而变慢——每个 chunk 有 HTTP 往返 + gzip 字典重置开销；20 个 50KB 的 chunk 比 2 个 500KB 请求更慢（连接数与头部开销）；分割粒度要让「缓存收益 > 请求开销」——常用判断是改动频率分组而非按包分割。

```javascript
// vite/webpack 分割配置
build.rollupOptions.output.manualChunks(id) {
  if (id.includes('node_modules/react')) return 'vendor-react';   // 高频稳定
  if (id.includes('node_modules')) return 'vendor';               // 一般依赖
}
// 组件级
const Editor = lazy(() => import(/* webpackPrefetch: true */ './Editor'));
```
