---
title: [V3-063] Vue3 的 tree-shaking 体现在哪里？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-063：Vue3 的 tree-shaking 体现在哪里？
**答**：
- Vue3 所有 API 通过命名导入提供，未用到的 Transition、KeepAlive、v-model 指令等编译后直接被摇掉。
- Vue2 的全局 API 挂在 Vue 构造函数上，无法被 tree-shaking。
- 全局 API 改为具名导出：createApp、nextTick、useCssModule 等。
- 效果：基础 Hello World 体积明显小于 Vue2。

```typescript
import { createApp, ref, computed } from "vue";

// 按需引入：未用到的 Transition/KeepAlive/nextTick 等会被 tree-shaking 移除
const app = createApp({
  setup() {
    const count = ref(0);
    const double = computed(() => count.value * 2);
    return { count, double };
  },
});

// Vue2 的 API 挂在 Vue 原型上无法摇树；Vue3 全部具名导出，按需打包
app.mount("#app");
```
