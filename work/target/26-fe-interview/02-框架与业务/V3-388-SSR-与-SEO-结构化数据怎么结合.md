---
title: [V3-388] SSR 与 SEO 结构化数据怎么结合？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-388：SSR 与 SEO 结构化数据怎么结合？
**答**：
- 服务端输出完整 title/description/canonical/OG（useSeoMeta/useHead），商品/内容页附加 JSON-LD 结构化数据（Product/Article schema）。
- 关键点：JSON-LD 由服务端从真实数据生成，与页面可见内容一致（不一致会被判作弊）。
- 动态路由：sitemap.xml 由 server route 动态生成（分片 + lastmod），配合 prerender。
- 验证：Google Rich Results Test / Search Console 监控结构化数据覆盖率与错误。
- SPA 页面 fallback：ssr:false 的页面提供静态 HTML 兜底或 sitemap 补充，避免核心页不被收录。
```javascript
useSeoMeta({ title: goods.title, ogTitle: goods.title, description: goods.summary })
useHead({ script: [{ type: 'application/ld+json', innerHTML: JSON.stringify(goodsSchema) }] })
```
