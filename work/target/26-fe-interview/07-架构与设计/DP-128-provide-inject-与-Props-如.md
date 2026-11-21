---
title: [DP-128] provide/inject 与 Props 如何选型？各自的模式语义是什么？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-128：provide/inject 与 Props 如何选型？各自的模式语义是什么？（高频）
**答**：
- Props = 显式数据流（组合模式的父子契约），适合"组件 API 的一部分"——层级浅、值会被组件真正使用与透传。
- provide/inject = 隐式依赖注入（DP-072），适合"环境能力"——层级深、逐层透传会产生 props 钻井（每层只是搬运不使用）。
- 决策口诀：删掉中间层后中间层还需要这个值吗？需要 → props；不需要 → inject。跨层级强耦合的 provide 必须用类型化 key + 注释声明契约（DP-126）。

```vue
<!-- 反例：props 钻井 —— 中间层 UserGroup 不使用 id，纯粹搬运 -->
<UserPage :user-id="id">
  <UserGroup :user-id="id">        <!-- 只转发 -->
    <UserCard :user-id="id" />     <!-- 真正使用，隔了两层 -->
  </UserGroup>
</UserPage>
```

```vue
<script setup>
// 正例：环境能力走 inject，组件 API 走 props
// UserCard.vue —— id 是"环境上下文"，不是卡片 API
import { inject } from 'vue';
import { UserContextKey } from './keys';                       // 类型化 key（DP-126）
const props = defineProps<{ size?: 'sm' | 'lg' }>();           // size 属于卡片自身 API → props
const ctx = inject(UserContextKey);                            // userId 属于环境 → inject
if (!ctx) throw new Error('UserCard 必须在 UserPage 内使用');   // 结构约束
</script>
<template>
  <section :class="`card card-${props.size}`">{{ ctx.userName }}</section>
</template>
<!-- UserPage 内 provide(UserContextKey, { userId })，中间层零改动 -->
```
