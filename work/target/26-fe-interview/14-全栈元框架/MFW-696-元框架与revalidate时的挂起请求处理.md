---
title: [MFW-696] revalidate 时的挂起请求处理
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-696：revalidate 时的挂起请求

**答**:
- revalidate 与在途请求的交互：1) **revalidate 时有在途渲染**（某路由正在 SSR 渲染 → revalidateTag 到达——「正在渲染的数据用旧缓存还是新数据」——框架语义：渲染开始时的缓存快照（请求开始时读取缓存——revalidate 不影响已开始的请求 RBL-505）；2) 挂起请求的完成（渲染完成写 Full Route Cache——写入的可能是旧数据（渲染期间数据变了）——覆盖 vs 跳过（revalidate 后的写入应丢弃——旧数据覆盖新缓存））。
- 覆盖 vs 跳过的语义：revalidate 的失效时间戳（t_revalidate）> 渲染开始时间（t_render_start）→ 渲染结果过期（写入跳过——避免旧数据覆盖）；「渲染结果的时间戳」与「失效时间戳」的比较——竞态的正确处理（RBL-563 的缓存竞态版）。
- client 侧：Router Cache 的失效通知（revalidateTag 的 client 通知——挂起的导航请求（payload 请求在途——收到的是旧 payload——导航后 refresh）。
- 追问钩子：为什么「revalidate 后在途渲染的写入」要丢弃？——在途渲染用旧缓存（渲染开始时缓存未失效）→ 渲染结果 = 旧数据；revalidate 发生 = 缓存应失效 → 旧数据写入 = 污染缓存（revalidate 语义被覆盖——静默旧数据 RBL-956）；「写入的时间戳比较」是标准解：t_render > t_revalidate = 丢弃——竞态的一致性（写后读 RBL-633 的缓存竞态版）。

```typescript
// revalidate 与在途渲染的竞态处理
const invalidationTimestamps = new Map<string, number>();   // key -> last revalidate ts
async function renderAndCache(key: string, render: () => Promise<string>) {
  const renderStart = Date.now();
  const result = await render();
  // 竞态检查：渲染期间是否发生 revalidate
  const lastInvalidate = invalidationTimestamps.get(key) ?? 0;
  if (renderStart < lastInvalidate) {
    // 渲染开始于 revalidate 之前 → 结果是旧数据 → 丢弃写入
    console.warn(`丢弃过期渲染: ${key}（渲染开始于 revalidate 之前）`);
    return;                                              // 跳过写入（缓存保持失效态）
  }
  await cache.set(key, result);                          // 安全写入
}
function revalidate(key: string) {
  invalidationTimestamps.set(key, Date.now());           // 记录失效时间戳
  cache.invalidate(key);
}
// 时序：render_start(1000) → revalidate(1100) → render_done(1200)
// → render_start(1000) < last_invalidate(1100) → 丢弃（旧数据不覆盖）
```
