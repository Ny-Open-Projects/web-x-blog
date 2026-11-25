---
title: [NODE-268] BFF 聚合的编排模式？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-268：BFF 聚合的编排模式？
**答**:
- 三种编排：并行聚合（Promise.allSettled，独立数据）、串行编排（依赖链，A 结果决定 B 参数）、条件聚合（按上下文选择性拉取）。
- 失败语义分级：核心数据失败 → 整体失败；次要数据失败 → 降级占位（NODE-052 容错）——聚合时标注每个 slot 的 criticality。
- 预算控制：整个聚合请求一个时间预算（NODE-207 AbortSignal.any 组合）——超时后已到手的部分返回（部分成功语义）。
- 裁剪：按客户端版本/设备档裁字段（H5 拿小 payload）——聚合层是"视图组装层"不是"数据仓库"。

```typescript
// 聚合编排器
interface Slot<T> { key: string; critical: boolean; fetch: (parent?: unknown) => Promise<T>; }
async function aggregate(slots: Slot<unknown>[], parentSignal) {
  const signal = AbortSignal.any([parentSignal, AbortSignal.timeout(3000)]);   // 预算
  const results = await Promise.allSettled(slots.map(s => s.fetch().catch(e => {
    if (s.critical) throw e;
    return DEGRADED;                               // 非核心：降级占位
  })));
  const body: Record<string, unknown> = {};
  slots.forEach((s, i) => { body[s.key] = results[i].status === 'fulfilled' ? results[i].value : null; });
  return body;                                     // 部分成功：critical 失败才 500
}
```
