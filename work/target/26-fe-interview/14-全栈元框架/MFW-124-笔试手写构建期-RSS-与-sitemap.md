---
title: [MFW-124] 笔试：手写构建期 RSS 与 sitemap 生成器
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-124：笔试：手写构建期 RSS 与 sitemap 生成器
**答**：内容站构建时要产出 `rss.xml` 与 `sitemap.xml`。实现两个函数：① `rss(posts, site)` 输出合规 RSS 2.0（channel 元信息 + item 的 title/link/pubDate/description，日期 RFC 822 格式，XML 转义）；② `sitemap(urls, site)` 输出 sitemap 0.9 格式（含 lastmod，URL 转义）；③ 都要处理特殊字符防 XML 注入。

```ts
type Post = { title: string; slug: string; pubDate: Date; description?: string };
type UrlEntry = { loc: string; lastmod?: Date; changefreq?: 'daily' | 'weekly' | 'monthly' };

function esc(s: string): string {
  // XML 五大实体转义，防内容破坏结构（XML 注入）
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;').replace(/'/g, '&apos;');
}

function rfc822(d: Date): string {
  // RSS 要求 RFC 822：Wed, 18 Nov 2026 08:00:00 GMT
  return d.toUTCString();
}

function rss(posts: Post[], site: string): string {
  const items = posts.map((p) => `
    <item>
      <title>${esc(p.title)}</title>
      <link>${site}/blog/${esc(p.slug)}</link>
      <guid isPermaLink="true">${site}/blog/${esc(p.slug)}</guid>
      <pubDate>${rfc822(p.pubDate)}</pubDate>
      ${p.description ? `<description>${esc(p.description)}</description>` : ''}
    </item>`).join('\n');

  return `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>我的博客</title>
    <link>${site}</link>
    <description>技术文章</description>
    <lastBuildDate>${rfc822(new Date())}</lastBuildDate>${items}
  </channel>
</rss>`;
}

function sitemap(urls: UrlEntry[], site: string): string {
  const entries = urls.map((u) => `
  <url>
    <loc>${esc(site + u.loc)}</loc>
    ${u.lastmod ? `<lastmod>${u.lastmod.toISOString().slice(0, 10)}</lastmod>` : ''}
    ${u.changefreq ? `<changefreq>${u.changefreq}</changefreq>` : ''}
  </url>`).join('\n');

  return `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${entries}
</urlset>`;
}

// —— 用例 ——
const posts: Post[] = [
  { title: 'RSC & <script> 注入', slug: 'rsc?tab=1', pubDate: new Date('2026-11-01') },
];
console.log(rss(posts, 'https://blog.com'));
// title 输出 RSC &amp; &lt;script&gt; 注入；link 输出 https://blog.com/blog/rsc?tab=1（& 转义在 loc 内）
```

**评分点**：
1. XML 五实体转义完整（& 最关键，必须先转义避免二次转义顺序错误）。
2. RSS 日期用 RFC 822（`toUTCString`），sitemap 用 ISO 日期——两种格式不混用。
3. guid 带 isPermaLink，channel 有 lastBuildDate——协议细节体现熟悉度。
4. URL 里的 query 参数（如 `?`、`&`）在 `<loc>` 内也被转义。
5. 能补充：5 万条上限要分片 sitemap（sitemap index）。
