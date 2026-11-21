---
title: [V3-240] useId 与懒水合在 Nuxt/SSR 项目里怎么组合落地？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-240：useId 与懒水合在 Nuxt/SSR 项目里怎么组合落地？
**答**：
- useId 的角色：懒水合组件内部也有 DOM 关联（label/aria），必须在"服务端渲染 + 延迟客户端水合"两个阶段保持一致，useId 提供稳定 id。
- 组合模式：页面骨架水合 + 非关键区块 defineAsyncComponent(hydrateOnVisible) + 区块内部用 useId 关联表单与错误提示。
- Nuxt 侧：Nuxt 3.9+ 内置 `nuxt-delay-hydration` 类方案，3.5 原生策略后可直接用 defineAsyncComponent 选项，不再依赖社区 hack。
- 注意事项：懒水合区块内的 SEO 内容已输出但不可交互期间要给用户可感知提示（骨架屏已由服务端 HTML 呈现，天然可用）。
- 收益口径：对内容型站点（首屏 20+ 组件），关键路径 JS 可减少 40%+，LCP 不变、TTI 明显下降。

```vue
<!-- Nuxt 页面：骨架即时可读，评论区滚动到才可交互 -->
<script setup>
import { defineAsyncComponent } from 'vue';
const CommentBlock = defineAsyncComponent({
  loader: () => import('~/components/CommentBlock.vue'),
  hydrateOnVisible({ rootMargin: '300px' }),
});
</script>
<template>
  <article>{{ content }}</article>      <!-- SSR HTML 即时可见 -->
  <CommentBlock />                       <!-- 延迟水合 -->
</template>
<!-- components/CommentBlock.vue 内部 -->
<!-- <script setup>const uid = useId(); 每条评论 aria-describedby=`${uid}-e-${i}` -->
```
