---
title: [MFW-515] Metadata 管线：SEO 标签的流式生成与优先级合并
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-515：Metadata 管线：SEO 标签生成与优先级合并

**答**:
- Metadata 的三源合并：layout 声明 → 父 layout → page 的 generateMetadata——**就近覆盖**（page 覆盖 layout 同名字段，未覆盖字段继承）；合并语义按字段（title.template：`'%s | 商城'` 模板拼接）。
- 流式生成的时序：generateMetadata 与页面渲染并行（Promise.all）——metadata 先完成 → head 先发（爬虫尽早拿到）；page 慢时 head 等还是先发？——先发已完成的 metadata（流式 head），数据依赖的 metadata（标题来自 fetch）随流补——爬虫兼容性考量（Google 支持流式 head 但部分爬虫不全）。
- 动态 OG 图：ImageResponse（edge 渲染 OG 图）——构建期生成（静态路由）vs 请求时生成（动态参数路由 + 缓存）——OG 图生成的成本与缓存（RBL-618 缓存策略的图版）。
- 追问钩子：为什么 generateMetadata 与页面渲染并行而不是串行？——串行（先数据后渲染 head）= TTFB 翻倍（metadata fetch + page fetch 串行）；并行 = 两者同时流式（head 与 body 交错到达）；代价是「metadata 与正文数据不一致」的可能（两次 fetch 的时间差）——一致性 vs TTFB 的权衡：SEO 关键字段可复用同一 fetch（request memoization 去重 RBL-508）。

```javascript
// 三源合并 + 并行生成
export async function generateMetadata({ params }) {
  const product = await getProduct(params.id);           // 与 page 内同名 fetch 去重
  return {
    title: product.name,
    description: product.summary,
    openGraph: { images: [`/og/${params.id}`] },         // 动态 OG
  };
}
// layout 层模板
export const metadata = { title: { template: '%s | 商城', default: '商城' } };
// page: title: '商品A' → 渲染 <title>商品A | 商城</title>
// 动态 OG 图（请求时生成 + 缓存）
import { ImageResponse } from 'next/og';
export async function GET({ params }) {
  const product = await getProduct(params.id);
  return new ImageResponse(<OgCard title={product.name} />, {
    width: 1200, height: 630,
    headers: { 'Cache-Control': 'public, max-age=86400, immutable' },   // 内容寻址由 URL 保证
  });
}
```
