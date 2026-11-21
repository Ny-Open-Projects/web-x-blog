---
title: [V3-031] Pinia 为什么取代了 Vuex？核心差异是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-031：Pinia 为什么取代了 Vuex？核心差异是什么？
**答**：
- Pinia 去掉了 mutation，action 中直接修改状态，模板代码减半。
- store 之间可以直接互相引用，模块天然扁平化，不需要 modules 嵌套。
- 完整 TS 推断：state/getters/actions 类型自动推导，无需手写 Payload 类型。
- Vue2/3 均可用、支持 SSR、DevTools 支持完善，是 Vue 官方推荐。

```typescript
// Vuex4：mutation 是同步修改状态的唯一途径，模板代码多
const vuexLikeStore = {
  state: { count: 0 },
  mutations: {
    increment(state: { count: number }) {
      state.count++;
    },
  },
  actions: {
    asyncIncrement(context: { commit: (t: string) => void }) {
      setTimeout(() => context.commit("increment"), 100);
    },
  },
};

// Pinia：去掉 mutation，action 里可直接改状态，天然 TS 推断
import { defineStore } from "pinia";

export const useCounterStore = defineStore("counter", {
  state: () => ({ count: 0 }),
  actions: {
    increment() {
      this.count++; // 直接修改，无需 commit
    },
  },
});
```
