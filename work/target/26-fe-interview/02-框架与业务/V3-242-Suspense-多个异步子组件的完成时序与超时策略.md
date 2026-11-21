---
title: [V3-242] Suspense 包多个异步子组件时完成时序如何判定？超时怎么处理？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-242：Suspense 包多个异步子组件时完成时序如何判定？超时怎么处理？
**答**：
- 时序判定：Suspense 注册全局 pending 计数，任一异步 setup 都 +1，全部 resolve 才切 default；**最慢的子组件决定整体展示时间**（串行瀑布会更糟）。
- 超时语义：`timeout` 到期后即使依赖未完成也会**显示 fallback**（并把未完成子树先卸载/隐藏），之后依赖完成会重新尝试切换 default。
- 优化实践：把慢接口放进内层 Suspense，让外壳快速展示骨架；慢区块用 defineAsyncComponent 的 loadingComponent 单独兜底。
- 竞态：切换路由时旧 Suspense 的 pending 依赖 resolve 不应触发新视图更新——Suspense 内部用当前树快照判断，过期 resolve 丢弃。
- 监控建议：给每个 async setup 打点，记录 pending 时长分布，找出拖累整树的接口。

```vue
<template>
  <Suspense :timeout="3000">                       <!-- 外层：3s 未齐就显示骨架 -->
    <Dashboard />
    <template #fallback><PageSkeleton /></template>
  </Suspense>
</template>
<script setup>
// Dashboard 内部：慢图表独立一层 Suspense，不影响外壳先出
const Chart = defineAsyncComponent(async () => {
  await slowApi(); // 8s
  return ChartComp;
});
// 结构：Dashboard(快速数据) > <Suspense><Chart/></Suspense>（慢区块独立兜底）
</script>
```
