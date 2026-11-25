---
title: [V3-536] 笔试：手写 useInfiniteScroll（无限加载）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## V3-536：笔试：手写 useInfiniteScroll

**答**：实现 `useInfiniteScroll(containerRef, loadMore, { distance = 200 })`：① 滚动接近底部（distance px 内）触发 loadMore；② 加载中锁（防重复触发）；③ 无更多数据停止（返回值 { done } 或 loadMore 返回空数组）；④ 失败重试入口（不自动重试，暴露 retry）；⑤ 与 IntersectionObserver 方案的对比说明。写出实现。

```javascript
export function useInfiniteScroll(containerRef, loadMore, { distance = 200 } = {}) {
  const loading = ref(false);
  const done = ref(false);
  const error = ref(null);

  async function maybeLoad() {
    const el = containerRef.value;
    if (!el || loading.value || done.value) return;
    const nearBottom = el.scrollHeight - el.scrollTop - el.clientHeight < distance;
    if (!nearBottom) return;
    loading.value = true;
    error.value = null;
    try {
      const items = await loadMore();
      if (!items?.length) done.value = true;      // 空页 = 无更多
    } catch (e) {
      error.value = e;                            // 保留触发条件, 用户可重试
    } finally { loading.value = false; }
  }

  useEventListener(containerRef, 'scroll', () => requestAnimationFrame(maybeLoad), { passive: true });
  const retry = () => { done.value = false; maybeLoad(); };
  return { loading, done, error, retry };
}
// IO 方案对比: 底部哨兵元素 + IntersectionObserver 更省(不监听 scroll),
// 但需要哨兵 DOM; scroll 方案实现简单且阈值可控. 优先 IO, 兼容场景用 scroll.
```

**评分点**：
- 三重守卫（loading 锁/done/距离阈值）
- 空页判定 done（分页协议约定）
- 失败保留可重试（不自动重试，error + retry 暴露）
- rAF 合帧与 IO 方案取舍的认知
