---
title: [V3-070] 手写一个 VueUse 风格的 useTitle？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-070：手写一个 VueUse 风格的 useTitle？
**答**：
- 输入兼容 `string | Ref<string>`，内部统一 unref 处理。
- watchEffect 自动追踪依赖并同步到 document.title，组件卸载自动停止。
- 返回一个可读写的 ref，外部改值即同步标签页标题。
- 模式可推广到 useFavicon、usePageVisibility 等 DOM 副作用类工具。

```typescript
// composables/useTitle.ts —— 仿 VueUse 的 useTitle
import { ref, watchEffect } from "vue";
import type { Ref } from "vue";

export function useTitle(newTitle: string | Ref<string> = document.title) {
  const title = ref(newTitle) as Ref<string>;

  watchEffect(() => {
    document.title = title.value; // 依赖变化自动同步
  });

  return title; // 返回 ref，读写都同步到 document.title
}

// 使用：
// const title = useTitle("首页");
// title.value = "详情页"; // 标签页标题同步变化
```

## 第二十一章 组件设计实战

组件设计实战聚焦可复用组件的 API 设计：泛型驱动列配置、快照回滚、双模式 v-model、三态容器等，是大厂组件库方向的高频考点。
