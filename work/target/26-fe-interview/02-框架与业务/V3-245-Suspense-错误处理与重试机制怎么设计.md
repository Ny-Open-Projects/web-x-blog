---
title: [V3-245] Suspense 的错误处理与重试机制怎么设计？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-245：Suspense 的错误处理与重试机制怎么设计？
**答**：
- 捕获链路：async setup 抛出的错误沿组件链冒泡，最近的有 `onErrorCaptured` 的祖先接收；配合 ErrorBoundary（onErrorCaptured 返回 false 阻断冒泡）实现"区域级降级"。
- 重试实现：Suspense 本身无重试 API，通用做法是给 Suspense 绑定 `:key`，重试时 key++ 触发整棵子树重新创建、重新 pending。
- 区分错误类型：网络类错误自动重试（指数退避 2 次），鉴权类跳登录，业务类展示错误态 + 手动重试按钮。
- fallback 期间出错：fallback 视图本身抛错同样走 onErrorCaptured，注意别让骨架组件依赖未就绪数据。
- 埋点：resolve/pending/rejected 全事件上报，形成"页面可用率"指标（resolve 成功次数 / 总进入次数）。

```vue
<script setup>
import { onErrorCaptured, ref } from 'vue';
const suspenseKey = ref(0);
const errMsg = ref('');
onErrorCaptured((err, instance, info) => {
  errMsg.value = err.message;
  if (isRetryable(err)) { retry(); return false; } // 拦截 + 自动重试
  return true; // 继续冒泡到全局兜底
});
function retry() { errMsg.value = ''; suspenseKey.value++; } // key 变化触发重新挂载
</script>
<template>
  <Suspense :key="suspenseKey">
    <Dashboard />
    <template #fallback><PageSkeleton v-if="!errMsg" /></template>
  </Suspense>
  <ErrorPanel v-if="errMsg" :msg="errMsg" @retry="retry" />
</template>
```
