---
title: [NODE-315] SSR 深水区：组件级缓存与流式组合？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-315：SSR 深水区：组件级缓存与流式组合？
**答**:
- 组件级缓存：SSR 时纯静态段（页头/楼层框架）直接命中缓存（cache('header') → HTML 片段），只有动态数据段真渲染——renderToString 耗时降 50%+。
- 与流式组合：缓存段立即输出（TTFB 极早），动态段 Suspense 补块——页头零延迟+内容流式。
- 缓存键：组件名+参数 hash+版本；失效靠版本号或短 TTL。
- React 19 的 use cache（cacheLife/cacheTag）：框架级组件缓存——语义与手写一致。

```javascript
// 组件级缓存 + 流式
const memoizedHeader = cache(async () => renderToString(<Header/>), { ttl: 60_000 });   // 组件级
async function Page() {
  return <>
    {await memoizedHeader()}                       {/* 静态段：命中即出 */}
    <Suspense fallback={<Skel/>}><DynamicFeed/></Suspense>   {/* 动态段：流式补 */}
  </>;
}
// use cache（Next 15）：
// async function Header() { 'use cache'; cacheLife('minutes'); cacheTag('header'); return ...; }
```
