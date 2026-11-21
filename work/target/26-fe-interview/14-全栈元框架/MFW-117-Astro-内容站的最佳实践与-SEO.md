---
title: [MFW-117] 用 Astro 做内容站的最佳实践是什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-117：用 Astro 做内容站的最佳实践是什么？
**答**：
- 架构默认值：全站 SSG + 少量岛；图片用 `astro:assets`（自动 AVIF/WebP、宽高防 CLS）；字体 `@fontsource` 或 astro-font 自托管；MDX 用于「内容中嵌组件」。
- SEO 全家桶：`@astrojs/sitemap` 自动生成、每页 `<title>/meta/OG`、文章 JSON-LD（BlogPosting）、RSS（`@astrojs/rss`）。canonical 在分页/翻页上别遗漏。
- 性能预算纪律：岛数量按页面预算（首屏 ≤2 个）、`client:visible` 优先、第三方脚本用 `<Script strategy>` 控制加载时机；用 Lighthouse CI 卡门槛。
- 内容规模化：Content Layer 集合 + Zod schema 门禁；搜索用构建期生成索引（pagefind）而不是运行时服务——纯静态的全文搜索。

```astro
---
// src/pages/blog/[...slug].astro —— 文章页模板
import { getCollection, render } from 'astro:content';
export async function getStaticPaths() {
  const posts = await getCollection('blog', ({ data }) => !data.draft);
  return posts.map((p) => ({ params: { slug: p.id }, props: { post: p } }));
}
const { post } = Astro.props;
const { Content } = await render(post);
---
<html>
  <head>
    <title>{post.data.title}</title>
    <meta name="description" content={post.data.description} />
    <link rel="canonical" href={`https://blog.com/blog/${post.id}`} />
    <script type="application/ld+json" set:html={JSON.stringify({
      '@context': 'https://schema.org', '@type': 'BlogPosting',
      headline: post.data.title, datePublished: post.data.pubDate,
    })} />
  </head>
  <body>
    <article><Content /></article>
    <!-- 全文搜索：pagefind 构建期索引，零运行时服务 -->
    <div id="search"></div>
    <Comments client:visible />  <!-- 唯一的岛 -->
  </body>
</html>
```
