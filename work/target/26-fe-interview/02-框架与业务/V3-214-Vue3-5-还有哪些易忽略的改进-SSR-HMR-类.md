---
title: [V3-214] Vue 3.5 还有哪些易被忽略的改进（SSR/HMR/类型）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-214：Vue 3.5 还有哪些易被忽略的改进（SSR/HMR/类型）？
**答**：
- Lazy Hydration：`hydrateOnVisible/onInteraction/onIdle/onMediaQuery`——异步组件按触发条件延迟水合，首屏交互零 JS 的部分彻底懒化。
- SSR 改进：`useId`、内存与 `renderToString` 性能优化、`teleports` 的 SSR 序列化更稳。
- 响应式 props 解构稳定：3.4 实验的 `defineProps` 解构（带响应式跟踪的解构）在 3.5 默认启用。
- 类型：`TemplateRefsType` 自动推导、`defineProps` 的响应式解构类型标注增强。
- 电话号码/表单相关：`reactive` 数组 `find` 等方法返回值解包、`shallowRef` 更轻量创建等细节 API 完善度提升。

```vue
<!-- Lazy Hydration：滚动到可视区才水合，SSR 首屏照常输出 HTML -->
<script setup>
import { defineAsyncComponent } from 'vue';
const HeavyChart = defineAsyncComponent({
  loader: () => import('./HeavyChart.vue'),
  hydrate: import.meta.env.SSR ? undefined : undefined,
  // 3.5 宏糖写法：编译器识别 hydrate 修饰
  // hydrateOnVisible({ rootMargin: '200px' }),
});
// 等价详细写法
const Chart2 = defineAsyncComponent({
  loader: () => import('./Chart2.vue'),
  hydrateOnVisible: { rootMargin: '200px' },   // 3.5 新选项
});
</script>
```
