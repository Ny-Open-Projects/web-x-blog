---
title: [NODE-273] SSR 的数据预取与 ISR？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-273：SSR 的数据预取与 ISR？
**答**:
- 数据预取：路由级 loader（Next getServerSideProps/loader）在渲染前拉数据——数据失败时的策略（降级渲染/整页 5xx）要在 loader 层明确。
- ISR（增量静态再生）：页面静态化 + 后台重生成（TTL 后首个请求触发）——流量峰谷解耦（大促前预生成，大促联动）。
- 渲染策略矩阵：SSG（纯静态）→ ISR（静态+过期重渲染）→ SSR（每请求）→ 流式 SSR（骨架+补块）——按页面实时性要求选档。
- 缓存键：ISR 的 revalidate tag 精确失效（数据变更 → 精确到页面）。

```javascript
// Next.js 渲染策略矩阵
// SSG：export const dynamic = 'force-static';
// ISR：export const revalidate = 60;        // 60s 后台重渲染
// SSR：export const dynamic = 'force-dynamic';
// 页面级缓存标签（精确失效）：
async function getProduct(id: string) {
  return fetch(`/api/product/${id}`, { next: { tags: [`product:${id}`] } });   // tag
}
// 数据变更：revalidateTag(`product:${id}`) → 只失效该页面（NODE-265 同款反向索引）
```
