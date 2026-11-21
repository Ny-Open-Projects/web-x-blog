---
title: [V3-024] 编写 composable 有哪些最佳实践？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-024：编写 composable 有哪些最佳实践？
**答**：
- 命名必须 use 开头；输入参数支持 `T | Ref<T>` 用 unref 兼容；输出返回 refs 而不是解包值。
- 副作用（事件、定时器、订阅）必须在 onUnmounted/onScopeDispose 中清理。
- 不持有模块级可变单例状态，除非刻意做全局 store；每次调用应互相独立。
- 异步 loading/error 状态内聚在 composable 里，组件只消费结果。

```typescript
// composables/useUser.ts —— composable 命名以 use 开头
import { ref, computed } from "vue";

export function useUser(initialId: number) {
  const user = ref<{ name: string } | null>(null);
  const loading = ref(false);
  const displayName = computed(() => user.value?.name ?? "未知");

  async function load(id = initialId) {
    loading.value = true;
    try {
      const res = await fetch(`/api/user/${id}`);
      user.value = await res.json();
    } finally {
      loading.value = false;
    }
  }

  // 返回 refs 而不是解包后的值，保持响应式
  return { user, loading, displayName, load };
}
```

## 第五章 生命周期
