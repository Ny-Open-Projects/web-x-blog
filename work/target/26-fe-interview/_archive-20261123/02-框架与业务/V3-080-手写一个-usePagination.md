---
title: [V3-080] 手写一个 usePagination？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-080：手写一个 usePagination？
**答**：
- 状态：page、pageSize、list、total、loading 统一放 reactive，翻页、改每页条数、重置都收敛到函数。
- 关键细节：改 pageSize 必须把 page 重置为 1，否则可能停在超出总页数的页码。
- runId 防竞态：快速翻页时只保留最后一次响应。
- 暴露 refresh 刷新当前页、reset 回到第一页重查。

```typescript
// composables/usePagination.ts
import { computed, reactive } from "vue";

interface PageResult<T> {
  list: T[];
  total: number;
}

export function usePagination<T>(
  fetcher: (p: { page: number; pageSize: number }) => Promise<PageResult<T>>,
  defaultPageSize = 10
) {
  const state = reactive({
    page: 1,
    pageSize: defaultPageSize,
    list: [] as T[],
    total: 0,
    loading: false,
  });

  const pageCount = computed(() => Math.max(1, Math.ceil(state.total / state.pageSize)));
  let runId = 0;

  async function load() {
    const id = ++runId;
    state.loading = true;
    try {
      const res = await fetcher({ page: state.page, pageSize: state.pageSize });
      if (id !== runId) return; // 快速翻页时丢弃过期响应
      state.list = res.list;
      state.total = res.total;
    } finally {
      if (id === runId) state.loading = false;
    }
  }

  function go(page: number) {
    state.page = Math.min(Math.max(1, page), pageCount.value); // 边界钳制
    return load();
  }

  function changePageSize(size: number) {
    state.pageSize = size;
    state.page = 1; // 改每页条数必须回到第一页
    return load();
  }

  function reset() {
    state.page = 1;
    return load();
  }

  return { state, pageCount, load, go, changePageSize, reset };
}
```
