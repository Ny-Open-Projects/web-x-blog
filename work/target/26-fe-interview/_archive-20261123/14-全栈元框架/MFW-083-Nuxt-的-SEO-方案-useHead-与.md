---
title: [MFW-083] Nuxt 怎么做 SEO？useHead 和 useSeoMeta 有什么区别？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-083：Nuxt 怎么做 SEO？useHead 和 useSeoMeta 有什么区别？
**答**：
- 底层是 Unhead：SSR 时把 head 标签注入到 HTML 里（不是客户端后补），所以爬虫能读到。`useHead` 是通用接口（任意标签/link/style），`useSeoMeta` 是**扁平键值的 SEO 专用糖**（title、og:*、twitter:*，键名拼错会直接被 TS 报错）。
- 动态 SEO 与 Next 的 `generateMetadata` 对应：在 setup 里基于响应式数据声明，SSR 输出终值；标题模板用 `titleTemplate` 实现全站统一后缀。
- 内容站标配 Nuxt Content：markdown 自动生成 frontmatter 元数据 + sitemap；结构化数据照旧手写 JSON-LD。
- 注意 404/错误页也要有合适的状态码与 meta（`setResponseStatus(event, 404)`），很多站死链返回 200 + 正常页面，SEO 直接扣分。

```vue
<script setup lang="ts">
const { data: product } = await useFetch(`/api/products/${useRoute().params.id}`);

// 扁平 SEO 键：类型安全，og:image 等全部有提示
useSeoMeta({
  title: () => product.value?.name ?? '商品',
  description: () => product.value?.summary,
  ogTitle: () => product.value?.name,
  ogImage: () => product.value?.cover,
  robots: 'index, follow',
});

// 全局模板：nuxt.config 或 app.vue
// useHead({ titleTemplate: (t) => t ? `${t} - 好商城` : '好商城' })

// 任意标签：canonical
useHead({
  link: [{ rel: 'canonical', href: `https://shop.com/products/${useRoute().params.id}` }],
});
</script>
```

```ts
// server/middleware/http-status.ts —— 死链必须 404 而非 200
export default defineEventHandler((event) => {
  if (event.path.startsWith('/products/') && !(await existsProduct(event))) {
    setResponseStatus(event, 404);
  }
});
```
