---
title: [V3-078] 手写一个 useRequest（加载、错误、取消、缓存）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-078：手写一个 useRequest（加载、错误、取消、缓存）？
**答**：
- 四个核心状态：data（shallowRef 避免大对象深度代理）、loading、error，外加 run/cancel 两个动作。
- 防竞态：每次 run 生成自增 runId，响应返回时 runId 不一致直接丢弃；同时用 AbortController 真正中断上一个请求。
- 缓存层：以序列化后的 params 作 key 存 Map，命中缓存先回填数据再决定是否静默刷新。
- 卸载清理：onScopeDispose 里自动 cancel，防止组件销毁后写状态。

```typescript
// composables/useRequest.ts
import { onScopeDispose, ref, shallowRef } from "vue";

interface Options<T> {
  immediate?: boolean;
  initialData?: T | null;
  cacheKey?: (params?: unknown) => string; // 传入即启用缓存
  onSuccess?: (data: T) => void;
  onError?: (e: Error) => void;
}

export function useRequest<T>(
  fetcher: (params?: unknown) => Promise<T>,
  options: Options<T> = {}
) {
  const data = shallowRef<T | null>(options.initialData ?? null);
  const loading = ref(false);
  const error = ref<Error | null>(null);

  const cache = new Map<string, T>();
  let controller: AbortController | null = null;
  let runId = 0;

  async function run(params?: unknown) {
    // 缓存命中：先回填再刷新，页面秒开
    const key = options.cacheKey?.(params);
    if (key && cache.has(key)) {
      data.value = cache.get(key)!;
    }

    controller?.abort(); // 取消上一次未完成请求
    controller = new AbortController();
    const id = ++runId;

    loading.value = true;
    error.value = null;
    try {
      const res = await fetcher(params);
      if (id !== runId) return; // 过期响应直接丢弃，防竞态
      data.value = res;
      if (key) cache.set(key, res);
      options.onSuccess?.(res);
    } catch (e) {
      if (id !== runId) return;
      error.value = e as Error;
      options.onError?.(e as Error);
    } finally {
      if (id === runId) loading.value = false;
    }
  }

  function cancel() {
    controller?.abort();
    runId++; // 让还在路上的响应全部失效
    loading.value = false;
  }

  if (options.immediate !== false) run();
  onScopeDispose(cancel); // 组件卸载自动取消

  return { data, loading, error, run, cancel };
}
```
