---
title: [MFW-599] 大促容量规划：ISR 生成的容量与预热
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-599：大促容量规划：ISR 生成容量

**答**:
- 大促场景 ISR 的容量问题：1) **缓存失效风暴**（大促改价 10 万 SKU → 全部 product 页过期 → 并发重生成 10 万页——渲染集群打满）；2) **首访问回源**（大促新页面无缓存——CDN 回源全量渲染）；3) 预热策略（发布后主动预热 Top 页面 RBL-686）。
- 容量规划：重生成速率上限（并发限制——队列化 RBL-509 大规模清单）；生成集群的弹性（并发渲染的 worker 扩容——RBL-687 弹性决策）；「优先级失效」（热点页面先失效——RUM 流量加权：热门商品先重生成，长尾后台慢慢）。
- 失效的合并：同 SKU 多次改价 10 次 = 1 次重生成（失效去重——队列去重 by page key RBL-590 去抖）。
- 追问钩子：为什么「失效优先级按 RUM 流量加权」是大促失效管线的核心？——10 万页同时失效时：渲染资源只能先给「会被用户访问的页」（Top 1% 商品占 80% 流量）；长尾页慢点失效无感（无人访问）；「失效的公平性 vs 流量加权」：失效不是 FIFO 队列而是「按流量预期排序」——大促场景的容量约束下，失效顺序 = 用户体验顺序。

```typescript
// 大促失效队列（流量加权）
interface InvalidationTask { path: string; trafficWeight: number; }
function scheduleInvalidations(tasks: InvalidationTask[], { concurrency, worker }) {
  // 按 trafficWeight 降序：热点先重生成
  const sorted = [...tasks].sort((a, b) => b.trafficWeight - a.trafficWeight);
  const seen = new Set(); const deduped = sorted.filter(t =>
    !seen.has(t.path) && seen.add(t.path));              // 去重：多次改价一次重生成
  return createScheduler({ concurrency }).scheduleAll(deduped.map(t => () => worker(t.path)));
}
// 容量预算：重生成速率
const capacity = {
  regenPerSecond: 50,                                    // 集群渲染能力
  burstPages: 100000,
  drainSeconds: 2000,                                    // 全量重生成 ~33 分钟
  priorityCutoff: 5000,                                  // Top 5000 页 1 分钟内完成（加权排序后）
};
// 预热：发布后主动打热点页面（CDN 填充）
await Promise.allSettled(topPaths.map(p => fetch(origin + p)));   // 预热避开用户首访回源
```
