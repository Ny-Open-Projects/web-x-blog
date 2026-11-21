---
title: [V3-049] Pinia 的 setup store 怎么写？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-049：Pinia 的 setup store 怎么写？
**答**：
- 第二个参数传函数：ref 就是 state、computed 就是 getter、普通函数就是 action。
- 函数必须 return 全部需要暴露的成员，漏 return 的成员外部不可见。
- 相比 options store 更灵活：可以在 store 内使用组合式函数与 watch。
- store id 是唯一的，DevTools 与持久化插件依赖它。

```typescript
// stores/counter.ts —— setup store 写法（组合式 API 风格）
import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useCounterStore = defineStore("counter", () => {
  // ref -> state
  const count = ref(0);
  // computed -> getter
  const double = computed(() => count.value * 2);
  // 函数 -> action
  function increment(step = 1) {
    count.value += step;
  }
  async function fetchAndSet() {
    const res = await fetch("/api/count");
    count.value = (await res.json()).count;
  }

  return { count, double, increment, fetchAndSet }; // 必须返回全部成员
});
```
