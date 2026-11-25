---
title: [MFW-087] Nuxt Content 做内容站的方案是什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-087：Nuxt Content 做内容站的方案是什么？
**答**：
- Nuxt Content 把 `content/` 目录的 markdown/mdx/yaml 变成**可查询的内容数据库**：`queryCollection` 支持 where/sort/limit，frontmatter 即元数据，代码高亮、TOC、图片优化开箱即用。
- 与构建期 SSG 组合：营销文档/博客全量预渲染，内容更新触发 CI 重建；配合 routeRules 的 `prerender` 把目录路径全部静态化。
- SEO 链路：frontmatter 里的 title/description 接 useSeoMeta；`@nuxtjs/sitemap` 从 queryCollection 自动生成 sitemap。
- 适用判断：纯内容展示（博客、文档）首选 Content/Astro；内容+重交互应用才需要全量元框架能力。

```vue
<!-- app/pages/blog/[...slug].vue -->
<script setup lang="ts">
const route = useRoute();
const { data: post } = await useAsyncData(`post:${route.path}`, () =>
  queryCollection('blog').where('path', '=', route.path).first(),
);
if (!post.value) throw createError({ statusCode: 404, fatal: true });

useSeoMeta({
  title: () => post.value!.title,
  description: () => post.value!.description,
});
</script>

<template>
  <article>
    <h1>{{ post!.title }}</h1>
    <ContentRenderer :value="post!" /> <!-- 渲染 markdown，含组件嵌入 -->
  </article>
</template>
```

```ts
// content.config.ts —— 集合定义（类型化 frontmatter）
import { defineContentConfig, defineCollection, z } from '@nuxt/content';

export default defineContentConfig({
  collections: {
    blog: defineCollection({
      type: 'page',
      source: 'blog/*.md',
      schema: z.object({
        title: z.string(),
        description: z.string().optional(),
        date: z.date(),
        tags: z.array(z.string()).default([]),
      }),
    }),
  },
});
```
