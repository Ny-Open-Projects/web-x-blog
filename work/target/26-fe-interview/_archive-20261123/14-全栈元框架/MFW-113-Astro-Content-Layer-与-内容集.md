---
title: [MFW-113] Astro 5 的 Content Layer 和内容集合怎么做内容管理？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-113：Astro 5 的 Content Layer 和内容集合怎么做内容管理？
**答**：
- Content Layer（Astro 5 的重要升级）：内容源不再限于本地 `src/content`——glob loader 扫本地文件，remote loader 拉 CMS/API，统一进「内容集合」，查询 API 一致。老 content collections glob 也兼容。
- 集合定义用 Zod schema（`src/content.config.ts`）：frontmatter 校验在**构建期**完成，字段缺失直接构建失败——内容质量门禁。
- 查询：`getCollection('blog')` 全量 + 过滤，`getEntry` 单篇；配合 `render(entry)` 输出 HTML。Astro 5 起渲染改为 `entry.render()`（在 astro:content 中）。
- 内容更新策略：本地 markdown 走 git + CI 重建；接 CMS 用 remote loader + webhook 触发重建，或 Astro Cloudinary 类 ISR（实验性）。

```ts
// src/content.config.ts —— Astro 5 Content Layer
import { defineCollection, z } from 'astro:content';
import { glob, load } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    pubDate: z.coerce.date(),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

// 远程 CMS 集合（Astro 5 新能力）
const docs = defineCollection({
  loader: () => fetch('https://cms.example.com/api/docs')
    .then((r) => r.json())
    .then((items) => items.map((d) => ({ id: d.slug, data: d }))),
  schema: z.object({ title: z.string(), body: z.string() }),
});

export const collections = { blog, docs };
```

```astro
---
// src/pages/blog/index.astro
import { getCollection } from 'astro:content';
const posts = (await getCollection('blog', ({ data }) => !data.draft))
  .sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
---
<ul>
  {posts.map((p) => <li><a href={`/blog/${p.id}`}>{p.data.title}</a></li>)}
</ul>
```
