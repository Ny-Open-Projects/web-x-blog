---
title: [V3-241] Suspense 的 pending/resolve 状态机与 fallback 切换细节是怎样的？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-241：Suspense 的 pending/resolve 状态机与 fallback 切换细节是怎样的？
**答**：
- 状态机：Suspense 实例持有 `pendingCount`，子树中每个异步依赖（async setup 返回 promise / defineAsyncComponent 加载）resolve 后计数-1，归零进入 resolved，切出真实内容。
- fallback 延迟与超时：`timeout` 到期前显示 fallback 之外还可以先显示 default（避免闪烁），`delay`（默认 200ms）控制"短暂加载不闪 fallback"。
- 内容切换动画：default ↔ fallback 之间支持 `<Transition>` 包裹，Suspend 时出/入场动画按 Transition 模式编排。
- 嵌套语义：内层 Suspense resolve 之前外层保持 pending；内层新依赖出现会重新进入 pending（3.3+ 支持嵌套稳定）。
- 常见坑：async setup 里抛错不会触发 fallback 循环重试，需 onErrorCaptured 捕获并重置 key 才能重试。

```vue
<template>
  <Suspense @resolve="onResolved" @pending="onPending" :timeout="5000">
    <template #default><AsyncProfile /></template>
    <template #fallback>
      <Transition name="fade"><div class="skeleton">加载中…</div></Transition>
    </template>
  </Suspense>
</template>
<script setup>
// 子组件：async setup 返回 promise，Suspense 等它
const AsyncProfile = defineAsyncComponent(async () => {
  const data = await fetch('/api/profile').then((r) => r.json());
  return { render: () => h('div', data.name) };
});
function onResolved() { track('profile_ready'); } // 全部依赖完成才触发
</script>
```
