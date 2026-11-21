---
title: [V3-079] 手写 useFetch，如何解决接口竞态问题？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-079：手写 useFetch，如何解决接口竞态问题？
**答**：
- 竞态场景：先请求 A 后请求 B，A 的慢响应后到，覆盖了 B 的新数据。
- 双保险：AbortController 中断旧请求（省流量）+ 局部 isCurrent 标记丢弃过期响应（防中断失败）。
- URL 变化用 watch 触发重新请求，immediate 立即执行一次。
- 可选 keepPreviousData：翻页时保留旧数据避免白屏，配合 loading 展示遮罩。

```typescript
// composables/useFetch.ts
import { ref, shallowRef, watch, type Ref } from "vue";

export function useFetch<T>(url: Ref<string>, keepPreviousData = false) {
  const data = shallowRef<T | null>(null);
  const loading = ref(false);
  const error = ref<Error | null>(null);
  let controller: AbortController | null = null;

  async function exec(currentUrl: string) {
    controller?.abort(); // 中断上一次请求
    const localController = new AbortController();
    controller = localController;

    loading.value = true;
    error.value = null;
    if (!keepPreviousData) data.value = null;

    try {
      const res = await fetch(currentUrl, { signal: localController.signal });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const json = (await res.json()) as T;
      if (localController !== controller) return; // 已有更新的请求，过期响应丢弃
      data.value = json;
    } catch (e) {
      if (localController !== controller) return; // 被 abort 的请求不算错误
      error.value = e as Error;
    } finally {
      if (localController === controller) loading.value = false;
    }
  }

  watch(url, (u) => exec(u), { immediate: true });

  return { data, loading, error };
}
```
