---
title: [MFW-061] next/dynamic 与 ssr: false 的适用边界是什么？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-061：next/dynamic 与 ssr: false 的适用边界是什么？
**答**：
- `ssr: false` 只该用在**依赖浏览器 API 或窗口尺寸**的组件（图表 canvas、地图、编辑器），其他场景默认让组件参与 SSR，能流式渲染就别关。
- App Router 里 `ssr: false` 只能在 **Client Component** 中使用——Server Component 里没有「渲染时关掉 SSR」的概念，SSR 与否是服务端整体决定的。
- 代码分割角度：首屏不需要的重库（富文本、Excel 导出）用 dynamic 拆出去，配合骨架屏避免布局抖动。
- 与 RSC 思路的对比：dynamic 是「整块拆包延迟加载」，RSC 是「服务端执行只传结果」，重展示组件优先考虑后者。

```tsx
'use client';
import dynamic from 'next/dynamic';

// 1. 浏览器专属库：关闭 SSR，骨架屏占位防 CLS
const Chart = dynamic(() => import('./Chart'), {
  ssr: false,
  loading: () => <div style={{ height: 300 }} className="animate-pulse bg-gray-100" />,
});

// 2. 首屏不需要的重库：参与 SSR 但延迟到交互时才拉 chunk
const ExportDialog = dynamic(() => import('./ExportDialog'), {
  loading: () => <Spinner />,
});

export default function Dashboard() {
  return (
    <>
      <Chart />
      <ExportTrigger onClick={() => /* 打开时才加载 chunk */ 0} />
    </>
  );
}
```

**追问**：

1. `ssr: false` 的组件为什么在 App Router 里必须 `'use client'`？→ 「跳过 SSR」本身是客户端渲染决策，Server Component 在服务端已经执行完，没有这个开关。
2. 拆包后首屏 CLS 怎么控？→ loading 占位给固定宽高而不是 min-height，骨架尺寸与真实组件一致，否则加载完必然跳动。
3. 什么时候该用 RSC 而不是 dynamic？→ 组件只是取数加展示、不依赖浏览器 API 时用 RSC，整块 JS 都不下发，比 dynamic 更省。
