---
title: [V3-176] hasInjectionContext 等工具 API 有哪些？版本升级要注意什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-176：hasInjectionContext 等工具 API 有哪些？版本升级要注意什么？
**答**：
- 3.3 新增 hasInjectionContext：让 composable 能判断"是否在组件上下文中"，从而决定走 inject 还是全局兜底，库作者高频使用。
- 3.4/3.5 关键 API：defineModel 转正（3.4）、useTemplateRef 与 useId、onWatcherCleanup、Teleport defer、shallowRef 数据性能优化（3.5）。
- 升级注意：Vue 3.5 移除了部分废弃 API 的 silent 行为；@vue/compat 用于大版本迁移灰度；组合式 API 全量替代 mixin 的时机。
- 库设计应用：工具函数用 hasInjectionContext 做环境探测，使同一份代码既能在组件内用也能在纯 JS 环境跑。

```typescript
// src/composables/useI18nSafe.ts —— 库设计中的环境探测
import { inject, hasInjectionContext, ref, type Ref } from "vue";

interface I18nContext {
  locale: Ref<string>;
  t: (key: string) => string;
}

// 全局兜底：无组件上下文时也能工作（工具函数、store 内）
const globalLocale = ref("zh-CN");
const globalT = (key: string) => `${globalLocale.value}:${key}`;

export function useI18nSafe(): I18nContext {
  // 3.3+：先判断是否处于组件 setup 上下文
  if (hasInjectionContext()) {
    const ctx = inject<I18nContext>("i18n");
    if (ctx) return ctx; // 组件树内：用祖先提供的实例
  }
  // 组件外（store/工具函数/单测）：退回全局实例
  return { locale: globalLocale, t: globalT };
}

// 版本注意点速查（面试口述）：
// 3.3：defineOptions、defineSlots、generics 组件、hasInjectionContext
// 3.4：defineModel 转正、v-bind 同名简写、更快的虚拟 DOM
// 3.5：useTemplateRef（ref 取代模板 ref 命名耦合）、useId（SSR 稳定 id）、
//       onWatcherCleanup（watch 清理回调）、Teleport defer、响应式系统大提速
// 升级动作：先升 3.5 看 deprecation 警告，再用 @vue/compat 做大跨度迁移灰度
```

## 第三十七章 Vue 与其他技术集成

命令式库（Canvas/WebGL/地图）与 Vue 的集成有统一模式：命令式实例活在 onMounted，响应式数据经 watch 单向流入，实例方法经 defineExpose 流出，onUnmounted 完整销毁。
