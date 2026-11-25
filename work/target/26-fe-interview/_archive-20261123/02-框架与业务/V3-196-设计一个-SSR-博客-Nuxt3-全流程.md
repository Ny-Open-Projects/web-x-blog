---
title: [V3-196] 设计一个 SSR 博客（Nuxt3 全流程）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-196：设计一个 SSR 博客（Nuxt3 全流程）？
**答**：
- 数据层：useAsyncData/useFetch 服务端取数且自动脱水注水；文章列表分页 SSR + 详情页静态化（nitro prerender 或 ISR）。
- SEO：useSeoMeta 设置 title/description/OG 标签；sitemap 由 server route 动态生成。
- 渲染模式：列表与详情 SSR（利于收录），后台管理页切 CSR（routeRules 的 ssr: false），读写分离。
- 性能：payload 提取（数据不再二次请求）、图片 useImage/nuxt-image 自动响应式、缓存 routeRules 的 swr。

```vue
<!-- nuxt3 项目结构：pages/index.vue + pages/posts/[slug].vue -->
<script setup lang="ts">
// 列表页：SSR 渲染，服务端取数
const { data: posts } = await useAsyncData("posts", () =>
  $fetch("/api/posts", { query: { page: 1, size: 20 } })
);

// SEO：SSR 的核心收益
useSeoMeta({
  title: "我的技术博客",
  description: "Vue3 / SSR / 工程化深度文章",
  ogTitle: "我的技术博客",
  ogImage: "/og.png",
});
</script>

<template>
  <main>
    <NuxtLink v-for="p in posts?.rows" :key="p.id" :to="`/posts/${p.slug}`" class="post">
      <h2>{{ p.title }}</h2>
      <p>{{ p.summary }}</p>
    </NuxtLink>
  </main>
</template>
```

```vue
<!-- pages/posts/[slug].vue —— 详情页：静态化 + 阅读数客户端化 -->
<script setup lang="ts">
const route = useRoute();

const { data: post } = await useAsyncData(`post:${route.params.slug}`, () =>
  $fetch(`/api/posts/${route.params.slug}`)
);

useSeoMeta({
  title: () => post.value?.title ?? "文章不存在",
  description: () => post.value?.summary ?? "",
});

// 阅读数是高频变化数据：客户端再请求，不阻塞 SSR
onMounted(() => {
  $fetch(`/api/posts/${route.params.slug}/view`, { method: "POST" });
});
</script>

<template>
  <article>
    <h1>{{ post?.title }}</h1>
    <ContentRenderer :value="post?.body ?? ''" />
  </article>
</template>

<!-- nuxt.config.ts 关键配置：
     routeRules: {
       "/": { swr: 600 },                 // 列表 SWR 缓存 10 分钟
       "/posts/**": { prerender: false, swr: 3600 }, // 详情按需静态化
       "/admin/**": { ssr: false },       // 后台切 CSR
     } -->
```
