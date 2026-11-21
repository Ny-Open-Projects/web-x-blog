---
title: [PER-234] 为什么 CrUX 只有高流量 URL 才有数据？低流量页面怎么验收性能？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-234：为什么 CrUX 只有高流量 URL 才有数据？低流量页面怎么验收性能？

**答**：
- 隐私约束：CrUX 必须保证单条数据背后有足够多的真实用户，无法反推个体。URL 级数据要求该页面 28 天内达到最低样本量（官方未公开具体值，业界经验约数百次有效访问），否则只聚合到 origin。
- origin 兜底数据的误用：低流量页拿 origin 级 p75 说"我达标了"是错的——origin 是全站平均，混入了其他页面的表现。必须明确告知这是"站点级参考值"。
- 低流量页的验收方案：① 自建 RUM——自己的数据自己说了算，p75 口径与 CrUX 对齐；② 实验室回归——Lighthouse CI 对关键模板页跑分，用 TBT/LCP 近似验证；③ 合并同类模板——同一模板的多个低流量 URL 在 RUM 里按模板路由分组聚合，样本量自然达标。
- 面试要点：能说清"CrUX 是抽样数据集 + 隐私下限"这个本质，以及不把 origin 数据当 URL 数据用。

```javascript
// 自建 RUM 按模板聚合：把 /goods/123、/goods/456 归到 /goods/:id 模板
function routeTemplate(pathname) {
  return pathname
    .replace(/\/\d+/g, '/:id')             // 数字 id
    .replace(/\/[0-9a-f]{8,}/gi, '/:hash') // hash id
    .replace(/\/(skus|spus)\/[^/]+/, '/:sku');
}
// 上报时带 routeTemplate(location.pathname)，看板按模板聚合出 p75，
// 低流量单页样本不足的问题在模板粒度上自动解决
```
