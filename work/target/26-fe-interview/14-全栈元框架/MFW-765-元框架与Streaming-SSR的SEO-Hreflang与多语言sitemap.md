---
title: [MFW-765] 多语言 sitemap 与 hreflang
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-765：多语言 sitemap 与 hreflang

**答**:
- 多语言 SEO 的完整链路（RBL-636+548 深化）：1) **hreflang**（每页声明语言变体——`<link rel="alternate" hreflang="en" href="...">`：搜索引擎的语言映射；2) **多语言 sitemap**（每 locale 的 URL 集合——sitemap 的 xhtml:link hreflang 注解）；3) **canonical 与 hreflang 的组合**（canonical 指向自身 + hreflang 指向其他 locale——自引用 canonical + 互引 hreflang）；4) **x-default**（无 locale 匹配时的 fallback——语言协商的默认页）。
- 多语言 sitemap 的生成：URL × locale 的笛卡尔积（RBL-709 locale 路由的 sitemap 版）；「hreflang 的完备性」：每页的所有 locale 变体都声明（漏一个 = 爬虫不知道该页有其他语言版本）；「hreflang 与 URL 一致性」：hreflang 的 URL 必须可渲染（RBL-636 死链的 hreflang 版）。
- 追问钩子：为什么「hreflang 需要双向声明」而不是「单向引用」？——hreflang 是互惠协议：A 页声明 B 页是中文版 → B 页也要声明 A 页是英文版（单向 = 爬虫只从 A 知道 B——不知道 B 的英文版是 A）；双向 = 爬虫建立完整的语言图（A↔B↔C 的语言网络）；「hreflang 的对称性」：每对页面互相声明——漏一面 = 爬虫的语言图不完整（索引错误）。

```typescript
// app/[locale]/sitemap.ts
export default async function sitemap({ params }): Promise<MetadataRoute.Sitemap> {
  const { locale } = params;
  const pages = await getPages(locale);
  return pages.map(page => ({
    url: `${BASE}/${locale}${page.path}`,
    lastModified: page.updatedAt,
    alternates: {
      languages: Object.fromEntries(
        locales.map(l => [l, `${BASE}/${l}${page.path}`])           // 每个 locale 的变体
        .concat([['x-default', `${BASE}/en${page.path}`]])),        // x-default
    },
  }));
}
// 页面级 hreflang（RSC metadata）
export async function generateMetadata({ params }) {
  return { alternates: {
    canonical: `/${params.locale}/p/${params.id}`,
    languages: Object.fromEntries(
      locales.map(l => [l, `/${l}/p/${params.id}`])),
  }};
}
// 产物：<link rel="alternate" hreflang="zh" href="/zh/p/1"/>
//       <link rel="alternate" hreflang="x-default" href="/en/p/1"/>
```
