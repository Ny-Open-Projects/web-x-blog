---
title: [V3-173] Suspense 的异步组件编排（嵌套 + 错误处理）怎么做？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-173：Suspense 的异步组件编排（嵌套 + 错误处理）怎么做？
**答**：
- Suspense 等待的是 async setup 组件：子组件顶层 await 即被视为异步组件，加载期间显示 fallback。
- 嵌套编排：外层 Suspense 包多个异步组件时，整体等待最慢的子树；想做渐进加载就把 Suspense 放到子组件层级。
- 错误处理：异步组件内部 try/catch 转 error 状态，或父级 onErrorCaptured 捕获后展示降级 UI。
- 仍是实验性 API：生产可用的前提是行为固定（不在 fallback 与 content 间频繁闪烁），列表型数据建议仍用 v-if + loading。

```vue
<script setup lang="ts">
import { ref, onErrorCaptured } from "vue";
import UserPanel from "./UserPanel.vue"; // async setup 组件
import OrderPanel from "./OrderPanel.vue";

const failed = ref(false);

// 捕获异步子树的错误，切到降级 UI
onErrorCaptured((err) => {
  console.error("异步组件加载失败：", err);
  failed.value = true;
  return false; // 阻止继续向上抛
});
</script>

<template>
  <div v-if="failed" class="fallback">数据加载失败，请刷新重试</div>

  <!-- 外层 Suspense：两个异步面板并行请求，全部就绪才整体显示 -->
  <Suspense v-else>
    <template #default>
      <div class="dashboard">
        <UserPanel />
        <OrderPanel />
      </div>
    </template>
    <template #fallback>
      <div class="skeleton">面板加载中...</div>
    </template>
  </Suspense>

  <!-- 渐进式编排：把 Suspense 下放到每个面板内部，先到先显示 -->
  <!-- <UserPanel /> 内部：<Suspense><OrderList /></Suspense> -->
</template>

<style>
.fallback, .skeleton { padding: 24px; color: #999; }
.dashboard { display: grid; gap: 16px; }
</style>
```

```vue
<!-- components/UserPanel.vue —— async setup 子组件 -->
<script setup lang="ts">
import { ref } from "vue";

// 顶层 await：该组件成为异步组件，由父级 Suspense 调度
const user = await fetch("/api/me").then((r) => r.json());
const refreshCount = ref(0);

// 注意：async setup 内的 onMounted 等钩子在 await 之前注册才有效
import { onMounted } from "vue";
onMounted(() => console.log("UserPanel mounted"));
</script>

<template>
  <section>
    <h3>{{ user.name }}</h3>
    <p>刷新次数：{{ refreshCount }}</p>
  </section>
</template>
```
