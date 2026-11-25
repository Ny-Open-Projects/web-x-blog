---
title: [MFW-125] Astro 在大型站点（多团队）实践里有哪些经验与局限？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-125：Astro 在大型站点（多团队）实践里有哪些经验与局限？
**答**：
- 大站用 Astro 的姿势：按「站点域」拆分仓库/工作区（marketing/blog/docs 各一个 Astro 工程），共享 UI 用 npm 包 + `@astrojs/*` 集成；不追求一个 Astro 壳吞下全部页面。
- 岛治理：给每个页面设岛预算（首屏岛 ≤2、总 JS ≤50KB），超预算要评审；公共交互（搜索、登录框）沉淀为标准岛组件统一水合策略。
- 内容管道：Content Layer + Zod 门禁 + CMS webhook 重建 + Lighthouse CI 内容质量/性能双卡口。
- 局限要诚实说：① 重交互应用不适合（岛多了就不是 Astro 的优势场景）；② 跨岛通信要靠 nanostores 等小状态库，复杂状态管理不如 SPA 顺；③ 秒级实时内容依赖 Server Islands/SSR opt-in，全静态心智要切换；④ 多框架岛混用会拉多份运行时，预算纪律必须坚持。

```astro
---
// 跨岛共享状态：nanostores（Astro 官方推荐的小状态方案）
// stores/cart.ts
import { atom } from 'nanostores';
export const cartCount = atom(0);
---
```

```tsx
// islands/CartButton.tsx —— React 岛
import { useStore } from '@nanostores/react';
import { cartCount } from '../stores/cart';

export default function CartButton() {
  const count = useStore(cartCount);
  return <button onClick={() => cartCount.set(count + 1)}>购物车 {count}</button>;
}
```

```vue
<!-- islands/CartBadge.vue —— Vue 岛读同一个 store -->
<script setup>
import { useStore } from '@nanostores/vue';
import { cartCount } from '../stores/cart';
const count = useStore(cartCount);
</script>
<template><span>{{ count }}</span></template>
```
