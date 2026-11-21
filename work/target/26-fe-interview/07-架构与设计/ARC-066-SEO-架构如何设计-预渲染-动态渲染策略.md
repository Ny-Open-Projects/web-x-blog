---
title: [ARC-066] SEO 架构如何设计（预渲染/动态渲染策略）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-066：SEO 架构如何设计（预渲染/动态渲染策略）？
**答**：
- 分层策略：核心流量页（首页/分类/详情）走 SSR/ISR 保证可抓取与新鲜度；长尾低频页用预渲染（构建期生成或按需 on-demand ISR）。
- 技术配套：语义化 HTML、结构化数据（JSON-LD）、canonical、sitemap 增量生成、抓取预算意识（避免无限翻页被过度抓取）。
- CSR 应用的兜底：动态渲染（UA 判定爬虫走 headless 渲染）是遗留方案，优先选框架级 SSR。

```typescript
// on-demand ISR + 结构化数据：SEO 架构典型组合
// app/product/[id]/page.tsx
export async function generateMetadata({ params }): Promise<Metadata> {
  const p = await getProduct(params.id);
  return {
    title: `${p.title} - 价格${p.price}元`,
    alternates: { canonical: `/product/${p.id}` },      // 防重复收录
  };
}
export async function generateStaticParams() {          // 预渲染 top N 热门商品
  const hot = await getHotProducts(1000);
  return hot.map(p => ({ id: String(p.id) }));          // 冷门商品首次访问时按需生成并缓存
}

function ProductJsonLd({ product }: { product: Product }) {   // 结构化数据
  return <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify({
    '@context': 'https://schema.org', '@type': 'Product',
    name: product.title, offers: { '@type': 'Offer', price: product.price, priceCurrency: 'CNY' },
  }) }} />;
}
```
