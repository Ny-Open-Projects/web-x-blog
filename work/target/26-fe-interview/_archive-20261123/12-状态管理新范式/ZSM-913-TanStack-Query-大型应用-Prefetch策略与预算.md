---
title: [913] TanStack Query 的 prefetch 策略怎么控制预算
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 预取]
type: 面试题
---

## 913：TanStack Query 的 prefetch 策略怎么控制预算

**答**：
- 预取时机分级：路由匹配即预取（hover/触摸导航项）、空闲预取（requestIdleCallback 预取下一页）、关键路径预取（loader 强制 ensure）——三级预算从可丢弃到必须。
- 预算控制：并发预取上限（信号量——避免 hover 一排列表项 = 20 个请求）、去重（ensureQueryData 天然去重——inflight 与新鲜缓存不重发）、预取黑名单（贵接口/写副作用接口永不预取）。
- 预取的取消：hover 快速扫过时未完成的预取可容忍完成（靠去重兜底），不必精细取消——简单性优先。
- 追问钩子：prefetch 失败要不要重试？——不重试（预取是投机性的，失败静默丢弃，真正进入页面时按正常 query 流程重试）。

```ts
const limiter = new Semaphore(4);                // 并发预算
function prefetchList(items) {
  for (const it of items) {
    if (PRESET_BLACKLIST.has(it.type)) continue;
    limiter.run(() => qc.prefetchQuery({
      queryKey: itemKeys.detail(it.id),
      queryFn: () => fetchItem(it.id),
      staleTime: 60_000,
    }).catch(() => {}));                          // 静默失败
  }
}
```

