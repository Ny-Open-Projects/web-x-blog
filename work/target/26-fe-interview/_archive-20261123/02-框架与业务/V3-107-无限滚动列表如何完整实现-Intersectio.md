---
title: [V3-107] 无限滚动列表如何完整实现（IntersectionObserver）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-107：无限滚动列表如何完整实现（IntersectionObserver）？
**答**：
- 在列表末尾放一个哨兵元素，IntersectionObserver 观察它进入视口即触发 loadMore，比 scroll 事件监听性能好。
- 三重防护：loading 加锁防重复触发、hasMore 为 false 后不再请求、rootMargin 提前 200px 预加载消除等待感。
- 数据加载完若内容不足一屏，哨兵持续可见会再触发一次，loadMore 内部 hasMore 判断自然终止。
- 卸载时 observer.disconnect 防泄漏。

```vue
<!-- components/InfiniteList.vue -->
<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from "vue";

const props = defineProps<{
  loadMore: () => Promise<boolean>; // 返回是否还有更多
}>();

const sentinel = ref<HTMLElement | null>(null);
const loading = ref(false);
const hasMore = ref(true);
let observer: IntersectionObserver | null = null;

async function load() {
  if (loading.value || !hasMore.value) return; // 加锁 + 终止条件
  loading.value = true;
  try {
    hasMore.value = await props.loadMore();
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  observer = new IntersectionObserver(
    (entries) => {
      if (entries[0]?.isIntersecting) load();
    },
    { rootMargin: "200px" } // 提前 200px 触发，消除等待感
  );
  if (sentinel.value) observer.observe(sentinel.value);
});

onBeforeUnmount(() => observer?.disconnect());
</script>

<template>
  <div class="infinite-list">
    <slot />
    <div ref="sentinel" class="sentinel">
      {{ loading ? "加载中…" : hasMore ? "" : "没有更多了" }}
    </div>
  </div>
</template>
```
