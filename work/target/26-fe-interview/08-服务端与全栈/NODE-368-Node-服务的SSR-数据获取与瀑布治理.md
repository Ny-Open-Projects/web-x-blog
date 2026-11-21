---
title: [NODE-368] Node 服务的 SSR 数据获取瀑布（waterfall）治理如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-368：SSR 数据获取瀑布治理
**答**:
- 瀑布成因：数据请求在组件树渲染中逐层触发（A 渲染 → 发现要数据 → 请求 → 渲染 B → 又请求），串行叠加 RTT。治理目标：请求数与依赖深度最小化。
- 手段一：请求上提——路由级预取（匹配路由即并行发起该页全部关键请求，不依赖组件渲染顺序）；框架能力（React 19 的 preload/RSC fetch 去重，Next loader 并行）。
- 手段二：依赖重排——真正有依赖的串行保留，无依赖的声明并行（Promise.all + 数据 map 注入组件）；批量接口合并（DataLoader，NODE-365）。
- 手段三：切分关键/非关键——首屏必需数据阻塞渲染，其余流式补（Suspense 边界后置）。
- 度量：SSR 渲染耗时分解（数据等待 vs 组件执行 vs 序列化），瀑布深度（最大串行链）作为核心指标；单个页面瀑布深度 > 2 层即优化项。
```javascript
// 路由级并行预取
router.get('/detail/:id', async (ctx) => {
  const [goods, reviews, recommend] = await Promise.all([        // 一次并行
    svc.goods(ctx.params.id), svc.reviews(ctx.params.id, { first: 10 }),
    svc.recommend(ctx.params.id).catch(() => [])                 // 非关键降级
  ]);
  ctx.body = renderApp({ goods, reviews, recommend });           // 数据注入渲染
});
```
