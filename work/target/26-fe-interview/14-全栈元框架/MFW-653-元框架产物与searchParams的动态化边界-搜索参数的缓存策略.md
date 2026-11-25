---
title: [MFW-653] searchParams 的缓存策略：动态化的边界与分层
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-653：searchParams 的缓存策略

**答**:
- searchParams 的动态化语义：page 组件读 searchParams = 路由动态化（每 query 组合一个渲染——缓存键爆炸 RBL-607）；策略分层：1) **关键参数进路由**（filter/category → 路径段 `/cat/electronics`（静态化友好）；2) 次要参数 client 处理（排序/页码 → client state（不触发 server 渲染——软导航）；3) 搜索 query → 保留动态（RBL-607 Zipf 分层）。
- searchParams 的规范 URL：参数顺序规范化（sort=a&filter=b vs filter=b&sort=a——规范化避免缓存键分裂）；「URL 规范化」在路由层的实现（canonical URL——RBL-582 键规范化）。
- searchParams 的 SEO：过滤组合页的索引策略（无限组合 = 爬虫预算爆炸——canonical 到无参版本 + noindex 组合页（仅索引核心页））。
- 追问钩子：为什么「关键参数进路径段」优于「全放 query string」？——路径段 = 静态化友好（/cat/electronics 可 ISR 预渲染；/products?cat=electronics = 每 query 动态）；「路径段的结构性」：URL 结构表达信息架构（可导航/可分享/可索引）；query string 适合「无结构的临时态」（排序/页码——不进缓存键）——参数的分类（结构性 vs 临时态）决定路由化还是 query 化。

```tsx
// 参数分层
// 结构性参数：路径段（可静态化）
// app/products/[category]/page.tsx: /cat/electronics → ISR 预渲染
export async function generateStaticParams() {
  return (await db.categories.all()).map(c => ({ category: c.slug }));
}
// 临时态参数：client 处理（不触发 server 渲染）
'use client';
function SortControl() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const setSort = (s: string) => {
    router.replace(`/products?sort=${s}`, { scroll: false });  // 软导航——payload 重新拉但缓存友好
  };
  return <select onChange={(e) => setSort(e.target.value)} />;
}
// URL 规范化（缓存键统一）
function canonicalUrl(path: string, params: Record<string, string>) {
  const sp = new URLSearchParams(params);
  sp.sort();                                             // 参数排序规范化
  return `${path}?${sp.toString()}`;
}
// SEO：组合页 canonical
export const metadata = { alternates: { canonical: '/products?cat=x&sort=price' } };   // 规范化版本
```
