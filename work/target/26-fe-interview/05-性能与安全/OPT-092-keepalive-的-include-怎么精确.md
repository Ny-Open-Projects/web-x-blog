---
title: [OPT-092] keep-alive 的 include 怎么精确控制？滥用会有什么问题？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-092：keep-alive 的 include 怎么精确控制？滥用会有什么问题？

**答**：
- keep-alive 缓存组件实例：回切免重建、保留滚动与表单状态；但**缓存没有上限**，路由全开 keep-alive 等于把所有页面实例都留在内存里，多页切换后内存持续增长。
- `include/exclude` 按组件 name 白名单/黑名单控制：只缓存真正需要保态的页面（列表页、表单页），详情页等一过性页面不缓存。
- 高阶控制：`max` 设 LRU 上限兜底；配 `activated/deactivated` 钩子做数据刷新与暂停（视频/轮播在 deactivated 停掉）。
- 动态管理白名单：业务侧维护一个"可缓存路由列表"，与路由 meta 配合，比硬编码更可控。

```vue
<!-- 一一对应：keep-alive include 精确缓存 + activated 生命周期配合 -->
<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute();

// 白名单来自路由 meta，集中可维护
const cachedViews = computed(() =>
  route.matched.filter((r) => r.meta.keepAlive).map((r) => r.name)
);
</script>

<template>
  <router-view v-slot="{ Component }">
    <keep-alive :include="cachedViews" :max="10">
      <component :is="Component" />
    </keep-alive>
  </router-view>
</template>

<!-- 路由定义：只给列表页与编辑页保态 -->
<!-- { path: '/goods', name: 'GoodsList', meta: { keepAlive: true } } -->
<!-- { path: '/goods/detail/:id', name: 'GoodsDetail' }  <- 不缓存，一过性页面 -->

<script setup>
// 缓存页配合 activated 做增量刷新与资源暂停
import { onActivated, onDeactivated } from 'vue';
let timer;
onActivated(() => {
  refreshIfStale();          // 回来时只刷新脏数据，不整页重建
  timer = setInterval(polling, 30_000);
});
onDeactivated(() => {
  clearInterval(timer);      // 缓存页不销毁，定时器必须自己停，否则白吃 CPU
  videoPlayer.pause();       // 媒体类同理
});
</script>
<!-- 组件必须显式声明 name 与路由 name 一致，include 才能匹配：
     defineOptions({ name: 'GoodsList' }) -->
```
