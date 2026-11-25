---
title: [MFW-607] 全栈搜索：SSR 搜索页与索引策略
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-607：全栈搜索：SSR 搜索页与索引

**答**:
- 搜索页的渲染策略：searchParams 动态路由（每 query = 不同页面——缓存爆炸 vs no-store）——策略：热门 query 预渲染（query 清单化 RBL-535）+ 长尾动态；「搜索页 SEO」：结果页要被索引（fetch 慢→搜索引擎放弃）——SSR 保证首包含结果。
- 搜索的防滥用：query 注入（SQL/搜索引擎注入——参数化搜索）；限流（搜索是昂贵操作——全量倒排查询：rate limit RBL-601）；空结果与拼写纠错。
- 分页与游标：搜索结果的游标（相关性排序无稳定键——cursor 用 rank + id；深分页的性能（offset 深分页 O(n)——cursor skip-free）。
- 追问钩子：为什么搜索页「热门 query 预渲染」的收益远超通用缓存？——搜索流量高度集中（Top 100 query = 80% 流量 Zipf 分布）；预渲染热门 = CDN 命中 80% 流量（零 server 成本）；长尾 no-store（长尾重复率低——缓存命中率极低不值得）；「Zipf 分布」是缓存策略的黄金假设：内容型流量集中——按流行度分层缓存（RBL-583 A/B 变体的流量加权）。

```typescript
// app/search/page.tsx
export async function generateStaticParams() {
  return (await topQueries(100)).map(q => ({ q }));      // Top 100 query 预渲染
}
export default async function SearchPage({ searchParams }) {
  const query = searchParams.q ?? '';
  const results = await search({ q: query, limit: 20 });
  return <Results items={results} query={query} />;
}
// rate limit（昂贵操作）
export async function GET(req: Request) {
  const ip = req.headers.get('x-forwarded-for');
  if (!(await rateLimit(ip, 10, 60)))                    // 10 次/分钟
    return new Response('Too many', { status: 429 });
  const results = await search({ q: sanitize(params.q) });   // 参数化搜索
  return NextResponse.json(results);
}
// Zipf 分层缓存
const cacheStrategy = (q) =>
  isTopQuery(q) ? { revalidate: 3600 }                   // 热门：ISR
  : { cache: 'no-store' };                               // 长尾：实时
```
