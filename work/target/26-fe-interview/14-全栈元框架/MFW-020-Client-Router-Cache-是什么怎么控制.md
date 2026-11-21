---
title: [MFW-020] Client Router Cache 是什么？为什么点返回链接有时数据是旧的？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-020：Client Router Cache 是什么？为什么点返回链接有时数据是旧的？
**答**：
- Client Router Cache：浏览器内存中保存**已访问过路由的 RSC Payload**，`router.back()`/Link 返回时直接用缓存渲染，不发请求——体验快，但可能展示过期数据。
- 默认新鲜度：静态路由（无动态函数）staleTime **5 分钟**，动态路由 **30 秒**；过期后导航仍先展示缓存并后台重新请求（stale-while-revalidate 体感）。
- 主动刷新手段：`router.refresh()`（重新拉当前路由 Payload）、`router.revalidate`（新版本）；或 `next.config.js` 的 `experimental.staleTimes` 调整。
- 设计上：Router Cache 是纯客户端内存缓存，**刷新页面即清空**；和 Full Route Cache（服务端）无关，两边要分别失效。
- 实战：列表→详情→返回的场景，列表用 Router Cache 保持滚动位置与数据；详情页数据要求强实时时用动态路由（30s）+ router.refresh()。

```jsx
// next.config.js —— 收紧 Router Cache 新鲜度
module.exports = {
  experimental: {
    staleTimes: { dynamic: 10, static: 60 }, // 默认 30s/5min，改为更激进
  },
};
```

```jsx
'use client';
import { useRouter } from 'next/navigation';

export function RefreshButton() {
  const router = useRouter();
  return (
    <button onClick={() => router.refresh()}>
      {/* 重新向服务端请求当前路由的 RSC Payload，覆盖 Router Cache 中的旧数据 */}
      刷新数据
    </button>
  );
}

// 返回导航命中缓存：back() 不发请求，直接回放缓存的 Payload
export function BackLink() {
  const router = useRouter();
  return <button onClick={() => router.back()}>返回列表</button>;
}
```
