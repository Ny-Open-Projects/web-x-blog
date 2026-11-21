---
title: [R19-075] 手写 useInfiniteScroll 无限滚动？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-075：手写 useInfiniteScroll 无限滚动？
**答**：
- 监听一个高度 1px 的哨兵元素，IntersectionObserver 触发即加载下一页，rootMargin 提前 N 像素预加载。
- 三重守卫：loadingRef 防重入、hasMore 判断停止、observer 在没有更多时自动断开。
- loadMore 用 ref 持最新引用，observer 只创建一次，不随渲染重建。
- 失败处理：不清空已有数据，返回 error 让 UI 提供"点击重试"。

```jsx
// useInfiniteScroll：哨兵元素 + IntersectionObserver + 加载守卫
import { useCallback, useEffect, useRef, useState } from 'react';

export function useInfiniteScroll(loadMore, { hasMore = true } = {}) {
  const [loading, setLoading] = useState(false);
  const loadingRef = useRef(false);
  const sentinelRef = useRef(null);
  const loadMoreRef = useRef(loadMore);
  loadMoreRef.current = loadMore;

  const tryLoad = useCallback(async () => {
    if (loadingRef.current || !hasMore) return;    // 防重复触发
    loadingRef.current = true;
    setLoading(true);
    try { await loadMoreRef.current(); }
    finally { loadingRef.current = false; setLoading(false); }
  }, [hasMore]);

  useEffect(() => {
    const el = sentinelRef.current;
    if (!el) return;
    const observer = new IntersectionObserver(
      entries => entries[0].isIntersecting && tryLoad(),
      { rootMargin: '200px' },                     // 提前 200px 预加载，减少白屏
    );
    observer.observe(el);
    return () => observer.disconnect();
  }, [tryLoad]);

  return { sentinelRef, loading };
}

// 用法
// const { sentinelRef, loading } = useInfiniteScroll(loadNextPage, { hasMore });
// {hasMore && <div ref={sentinelRef} style={{ height: 1 }} />}
```

---

## 第十二章 状态管理实战（R19-076 ~ R19-082）
