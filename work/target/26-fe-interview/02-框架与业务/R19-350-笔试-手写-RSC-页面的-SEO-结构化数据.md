---
title: [R19-350] 笔试：手写商品页的 SEO 元信息与 JSON-LD 生成
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-350：笔试：手写商品页的 SEO 元信息与 JSON-LD
**答**：在服务端组件中：生成 title/description/canonical/OG；商品数据生成 Product JSON-LD（含价格/库存/评分）；同一数据源复用避免重复请求（cache()）；未找到商品调 notFound()。

```javascript
import { cache } from 'react'
const getGoods = cache((id) => db.goods.find(id)) // 请求级记忆化：metadata 与页面共用

export async function generateMetadata({ params }) {
  const goods = await getGoods(params.id)
  if (!goods) return { title: '商品不存在' }
  return {
    title: `${goods.title} - 商城`,
    description: goods.summary.slice(0, 120),
    alternates: { canonical: `/goods/${goods.id}` },
    openGraph: { title: goods.title, images: [goods.cover], type: 'website' }
  }
}
export default async function GoodsPage({ params }) {
  const goods = await getGoods(params.id) // cache 命中，不二次查询
  if (!goods) notFound()
  const schema = {
    '@context': 'https://schema.org', '@type': 'Product',
    name: goods.title, image: goods.cover,
    offers: { '@type': 'Offer', price: goods.price, priceCurrency: 'CNY',
      availability: goods.stock > 0 ? 'InStock' : 'OutOfStock' },
    aggregateRating: goods.rating ? { '@type': 'AggregateRating', ratingValue: goods.rating, reviewCount: goods.reviews } : undefined
  }
  return (
    <>
      <script type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(schema) }} />
      <h1>{goods.title}</h1>
    </>
  )
}
```
**评分点**：
- cache() 让 metadata 与页面共享查询（核心性能点）。
- notFound() 的 SEO 语义（404 状态码）。
- JSON-LD 与页面内容一致性（价格/库存同步）。
- availability 状态映射、无评分时省略字段。
