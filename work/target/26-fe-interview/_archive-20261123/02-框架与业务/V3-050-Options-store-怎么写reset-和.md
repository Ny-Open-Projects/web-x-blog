---
title: [V3-050] Options store 怎么写？$reset 和 $patch 怎么用？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-050：Options store 怎么写？$reset 和 $patch 怎么用？
**答**：
- state 必须是返回新对象的工厂函数，getters 是基于 state 的派生，actions 写业务逻辑。
- `store.$patch(对象或函数)` 批量修改，只触发一次订阅回调。
- Options store 自带 `\$reset()` 恢复初始 state；setup store 需要自己实现 reset action。
- `store.$subscribe` 可监听状态变化，常用于做持久化。

```typescript
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    token: "",
    profile: null as { name: string } | null,
  }),
  actions: {
    setToken(token: string) {
      this.token = token;
    },
    reset() {
      this.$reset(); // Options store 自带 $reset；setup store 需自行实现
    },
  },
});

const store = useUserStore();

// $patch 批量修改，只触发一次更新
store.$patch({ token: "abc" });
store.$patch((state) => {
  state.profile = { name: "Tom" };
});

// $subscribe 监听状态变化
const unsubscribe = store.$subscribe((mutation, state) => {
  console.log(mutation.type, state.token);
});
```
