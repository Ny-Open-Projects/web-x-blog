---
title: [V3-087] 手写一个 Pinia 持久化插件？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-087：手写一个 Pinia 持久化插件？
**答**：
- Pinia 插件签名：接收 `{ store, options }`，options 是 store 定义时写的自定义字段（需 TS 模块扩充声明）。
- 恢复：初始化时读 localStorage，有旧值就 `$patch` 进 store。
- 保存：`store.$subscribe` 监听任意状态变更，序列化写回；支持 paths 只持久化白名单字段。
- 敏感字段（token 除外）不要持久化；也可以换成 sessionStorage 或加过期时间。

```typescript
// stores/plugins/persist.ts
import type { PiniaPluginContext } from "pinia";

// 类型扩充：让 defineStore 第三个参数认识 persist 选项
declare module "pinia" {
  export interface DefineStoreOptionsBase<S, Store> {
    persist?: { paths?: (keyof S)[] };
  }
}

export function persistPlugin({ store, options }: PiniaPluginContext) {
  const conf = (options as { persist?: { paths?: string[] } }).persist;
  if (!conf) return; // 没声明 persist 的 store 直接跳过

  const key = `pinia:${store.$id}`;

  // 1. 恢复：初始化时把旧数据 patch 回去
  const raw = localStorage.getItem(key);
  if (raw) {
    try {
      store.$patch(JSON.parse(raw));
    } catch {
      localStorage.removeItem(key);
    }
  }

  // 2. 保存：订阅状态变化写回，只存白名单字段
  store.$subscribe(() => {
    const state = store.$state as Record<string, unknown>;
    const picked = conf.paths
      ? Object.fromEntries(conf.paths.filter((p) => p in state).map((p) => [p, state[p]]))
      : state;
    localStorage.setItem(key, JSON.stringify(picked));
  });
}

// 使用：
// defineStore("user", { ... }, { persist: { paths: ["token", "profile"] } })
```
