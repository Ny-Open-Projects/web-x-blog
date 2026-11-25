---
title: [R19-255] 路由切换的 Suspense 时序怎么优化（预取链路）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-255：路由切换的 Suspense 时序怎么优化？
**答**：
- 优化链路：hover/曝光预取路由 chunk → 预取数据 promise → 点击导航 → 边界内 use 命中已就绪数据 → 直接渲染无 fallback。
- 框架层：Next 的 <Link prefetch> 已做 RSC payload 预取（静态路由默认、动态路由可配）。
- 手动层：路由 loader 模式（React Router lazy + 数据 loader 并行）、自建 promise 缓存。
- 度量：路由切换「fallback 可见时长」作为指标，目标 < 200ms 或零感知。
- 边界：预取数据可能过期——预取结果带 TTL，命中检查新鲜度，过期重取（展示 skeleton）。
