---
title: [V3-266] Nuxt 的 SEO 元信息（title/meta/OG）如何统一管理？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-266：Nuxt 的 SEO 元信息（title/meta/OG）如何统一管理？
**答**：
- 页面级：`useHead({ title, meta, link, script })` 响应式头部管理；`useSeoMeta` 提供 OG/Twitter 的类型安全速写。
- 组合层级：app.vue 默认 head → layout → page 覆盖，深层组件可再覆盖（last-write-wins），titleTemplate 拼接站名。
- 数据驱动：SEO 信息来自接口时放 async setup 里（SSR 就能带上），`refreshNuxtData` 后自动更新。
- 社交爬虫：OG 图片用 `og:image` + 绝对 URL；动态 OG 图可用 satori 服务端生成。
- 校验：上线前用爬虫模拟（curl + og 解析）验证而非只看浏览器，部分爬虫不执行 JS——SSR 输出必须直接可读。

```vue
<script setup>
const { data: article } = await useAsyncData('article', () => queryContent().findOne());
useSeoMeta({
  title: () => article.value?.title,
  titleTemplate: '%s · 我的技术站',
  description: () => article.value?.excerpt,
  ogTitle: () => article.value?.title,
  ogImage: () => `https://cdn.example.com/og/${article.value?.id}.png`,
  twitterCard: 'summary_large_image',
});
useHead({ link: [{ rel: 'canonical', href: () => `https://example.com/blog/${article.value?.slug}` }] });
</script>
```
