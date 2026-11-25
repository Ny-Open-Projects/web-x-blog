---
title: [NODE-316] SSR 深水区：流式渲染的 SEO 与 meta 处理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-316：SSR 深水区：流式渲染的 SEO 与 meta 处理？
**答**:
- 流式下 SEO 的关键：标题/meta/结构化数据必须在 shell（首段 HTML）里——慢数据不要进 head；React 的 generateMetadata 在流式前已解析（框架保证）。
- 结构化数据（JSON-LD）随首段输出；评论区等非 SEO 内容放 Suspense 后段。
- 爬虫兼容：Google 支持 streaming HTML（渐进解析）；部分老爬虫按完整文档解析——重要页面可用预渲染兜底（prerender 大客户 UA 或全量 ISR）。
- 验证：用 Google Rich Results Test 与 search console 实测流式页面索引效果。

```javascript
// Next App Router 流式 + SEO
export async function generateMetadata({ params }) {
  const product = await getProduct(params.id);   // shell 前完成 → head 在首段
  return { title: product.title, openGraph: { images: [product.cover] } };
}
export default async function Page({ params }) {
  const product = await getProduct(params.id);   // 同一请求缓存复用（request memoization）
  return <>
    <script type="application/ld+json">{jsonLd(product)}</script>
    <Suspense fallback={<Skel/>}><Reviews id={params.id}/></Suspense>   // 非 SEO 内容后段
  </>;
}
```
