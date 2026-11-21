---
title: [V3-083] 手写 useStorage，如何实现跨标签页同步？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-083：手写 useStorage，如何实现跨标签页同步？
**答**：
- 本地值：ref 初始化时从 localStorage 读，读不到用默认值，JSON 反序列化带 try/catch 容错。
- 写入：watch 深度监听，序列化回写 localStorage。
- 跨页同步：监听 window 的 storage 事件——其它标签页修改同名 key 时会触发本页的 storage（注意本页自己写不触发）。
- 卸载时移除监听，避免重复绑定。

```typescript
// composables/useStorage.ts
import { onScopeDispose, ref, toRaw, watch } from "vue";

export function useStorage<T>(key: string, initial: T) {
  function read(): T {
    try {
      const raw = localStorage.getItem(key);
      return raw === null ? initial : (JSON.parse(raw) as T);
    } catch {
      return initial; // 反序列化失败时退回默认值
    }
  }

  const data = ref<T>(read()) as { value: T };

  watch(
    data,
    () => {
      localStorage.setItem(key, JSON.stringify(toRaw(data.value)));
    },
    { deep: true }
  );

  // 其它标签页修改了同一个 key 时同步到本页
  function onStorage(e: StorageEvent) {
    if (e.key !== key || e.newValue === null) return;
    try {
      data.value = JSON.parse(e.newValue);
    } catch {
      /* 忽略非法数据 */
    }
  }

  window.addEventListener("storage", onStorage);
  onScopeDispose(() => window.removeEventListener("storage", onStorage));

  return data;
}

// 使用：
// const settings = useStorage("settings", { theme: "light" });
// 两个标签页里改 settings 会互相同步
```
