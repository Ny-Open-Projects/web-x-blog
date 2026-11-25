---
title: [MFW-753] RSC 数据流可观测性
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-753：RSC 数据流可观测性

**答**:
- RSC 数据流的可观测维度：1) **数据获取链路**（每个组件的 fetch/DB 查询——RBL-542 trace 的数据流可视化：组件 → 数据源的映射图；2) **缓存层级**（Data Cache/Full Route/Router Cache 的命中路径——RBL-597 多层缓存的可观测：哪层命中哪层穿透；3) **数据变更传播**（revalidateTag 的传播路径——变更 → tag → 影响的路由/组件（失效的因果链）。
- 可观测的实现：1) **fetch wrapper**（拦截 fetch 记录 tag/缓存命中 RBL-526 的 fetch 选项审计；2) **trace 的数据流标注**（span 属性：cache-layer/cache-key/data-source——RBL-728 的数据维度；3) **revalidate 的日志**（谁触发了失效/影响了哪些路由——变更传播的审计链）。
- 追问钩子：为什么「RSC 的数据流可观测性」比传统 SPA 更复杂也更必要？——SPA 的数据流 = 显式 API 调用（client → API 的单向流——清晰）；RSC = 数据获取分散在组件树（每个组件可能有自己的 fetch——数据流是树形的且与渲染交织）；「数据流的树形分散」需要更精细的可观测（组件级 trace + 缓存层级标注 + 变更传播链）——RSC 的可观测复杂度与架构的数据分散度成正比（RBL-542 的深化）。

```typescript
// fetch wrapper 的数据流观测
import { cache } from 'react';
const observedFetch = cache(async (url, options, component) => {
  const span = tracer.startSpan(`data-fetch:${component}`);
  span.setAttribute('data.url', url);
  span.setAttribute('data.tags', options?.next?.tags?.join(',') ?? 'none');
  const t0 = performance.now();
  const res = await fetch(url, options);
  span.setAttribute('data.cache_hit', res.headers.get('x-nextjs-cache') === 'HIT');
  span.setAttribute('data.latency', performance.now() - t0);
  span.end();
  return res;
});
// 变更传播的审计链
function auditRevalidation(tag: string, source: string) {
  const affectedRoutes = tagToRoutes(tag);               // tag → 路由映射
  console.log(`revalidate: tag=${tag} source=${source} → ${affectedRoutes.length} routes affected`);
  return affectedRoutes;
}
// 数据流可视化（RBL-553 成本归因的观测版）
// Component: ProductView → fetch: /api/product/1 (Data Cache HIT, 5ms)
//   → Component: Reviews → fetch: /api/reviews/1 (MISS, 800ms) ← 慢
//   → revalidateTag('product:1') → ['/p/1', '/products'] affected
```
