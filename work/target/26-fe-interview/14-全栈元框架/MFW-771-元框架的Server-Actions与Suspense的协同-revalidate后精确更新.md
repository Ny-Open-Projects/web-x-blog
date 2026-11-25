---
title: [MFW-771] revalidate 后的精确更新
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-771：revalidate 后的精确更新

**答**:
- revalidate 后的更新粒度：1) **整页刷新**（router.refresh()——全部 RSC 重新渲染）；2) **精确失效**（revalidateTag(tag) → Router Cache 的对应 payload 失效——下次导航重新拉取）；3) **action 后的定向更新**（action 内 revalidateTag → client 的 Suspense 重新渲染受影响边界（React 的 Flight patch——只有 tag 关联的组件更新 RBL-700 竞态协调）；4) **revalidatePath vs revalidateTag**（path = 特定路由、tag = 数据维度——tag 更精确（数据变更影响多路由时 tag 一次失效）；「tag 的层级失效」RBL-578）。
- 更新的用户体验：revalidate 后的刷新 = 「无闪烁更新」（Flight patch 替换——保留 client state（RBL-552 状态保持）；router.refresh() = 全页刷新（client state 保留但 re-render——视觉闪烁小——React reconciliation）；整页导航 = 状态丢失。
- 追问钩子：为什么「revalidateTag 在 action 内调用」比「client 调 router.refresh()」更好？——action 内 revalidate = server 侧缓存失效 + client 自动更新（框架的 Flight patch 推送——client 无需手动刷新）；router.refresh() = client 侧强制刷新（全页 re-render——粒度粗且可能与 server 缓存不一致）；「server 侧精确失效 > client 侧粗刷」：revalidate 的精确性（tag 粒度）让 client 只更新受影响的边界——server 权威的失效传播优于 client 的全量刷新。

```tsx
// action 内的精确失效
'use server';
export async function addReview(productId: string, text: string) {
  await db.reviews.create({ productId, text });
  revalidateTag(`reviews:${productId}`);                 // 精确失效：只影响评论
  // 而非 router.refresh()（client 全页刷新——粗粒度）
}
// client 侧：Suspense 自动重新渲染（Flight patch 推送）
'use client';
function ReviewSection({ productId }) {
  // action 完成 → revalidateTag → Router Cache 失效
  // → Suspense 边界自动重新渲染（新数据流式到达）
  return <Suspense fallback={<Skeleton />}><Reviews id={productId} /></Suspense>;
}
// 对比：router.refresh()（client 侧粗刷）
'use client';
function ManualRefresh() {
  const router = useRouter();
  return <button onClick={() => router.refresh()}>刷新</button>;
  // 全页 RSC 重渲染——非精确——仅在无 tag 的场景使用
}
```
