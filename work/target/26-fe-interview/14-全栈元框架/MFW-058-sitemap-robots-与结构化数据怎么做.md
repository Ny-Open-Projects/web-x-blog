---
title: [MFW-058] sitemap、robots 与结构化数据在 App Router 里怎么做？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-058：sitemap、robots 与结构化数据在 App Router 里怎么做？
**答**：
- Metadata 约定文件：`sitemap.ts` / `robots.ts` 可以是函数，动态生成，几十万商品页的 sitemap 要按 `generateSitemaps` 分片（每片 5 万条以内）。
- 结构化数据（JSON-LD）直接在页面组件里输出 `<script type="application/ld+json">`，商品页给 Product schema、详情页给 FAQ schema，是搜索富摘要的入场券。
- canonical 与 OG 标签用 `generateMetadata` 按路由动态返回，分页页要指定 canonical 防重复收录。
- robots 策略要与业务一致：搜索结果页、筛选参数页一般 disallow，防爬虫把参数组合 URL 灌进索引。

```ts
// app/sitemap.ts
import type { MetadataRoute } from 'next';

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const products = await db.product.findMany({ select: { id: true, updatedAt: true } });
  return [
    { url: 'https://shop.com/', changeFrequency: 'daily', priority: 1 },
    ...products.map((p) => ({
      url: `https://shop.com/products/${p.id}`,
      lastModified: p.updatedAt,
      changeFrequency: 'daily' as const,
      priority: 0.7,
    })),
  ];
}
```

```ts
// app/robots.ts
export default function robots(): MetadataRoute.Robots {
  return {
    rules: { userAgent: '*', allow: '/', disallow: ['/search', '/api/', '/account'] },
    sitemap: 'https://shop.com/sitemap.xml',
  };
}
```

```tsx
// 商品页内输出 JSON-LD
export default function ProductPage({ product }) {
  const jsonLd = { '@context': 'https://schema.org', '@type': 'Product',
    name: product.name, offers: { '@type': 'Offer', price: product.price, priceCurrency: 'CNY' } };
  return (<><script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />…</>);
}
```
