---
title: [ARC-248] 多语言 SEO 与服务端渲染的国际化配合？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-248：多语言 SEO 与服务端渲染的国际化配合？
**答**：
- URL 结构即 SEO 策略：子路径 `/ja/products/` > 子域名 > 参数；每语言独立可索引 URL，避免 Cookie 判语言导致爬虫只看到一种语言。
- 服务端按语言渲染：SSR 用 URL 里的语言（ARC-241 协商链第 1 优先级），HTML 的 lang 属性、hreflang 标签、canonical 一并输出；hreflang 双向声明（每语言页面互指 + x-default）。
- 内容类：结构化数据（JSON-LD）按语言本地化（价格货币、日期格式）；sitemap 分语言版本。
- 性能配合：语言包 SSR 预取（Node 端缓存），客户端水合用同一份字典（防闪变/水合错误）。

```typescript
// Next.js App Router：/app/[lang]/ 布局
export async function generateMetadata({ params }) {
  const alt = LANGS.map(l => ({ [l]: `https://example.com/${l}/products` }));
  return {
    alternates: { canonical: `https://example.com/${params.lang}/products`, languages: alt }, // hreflang
  };
}
export default async function Page({ params }) {
  const dict = await getDict(params.lang, ['products']);  // SSR 端语言包
  return <html lang={params.lang}><Products dict={dict}/></html>;
}
```
