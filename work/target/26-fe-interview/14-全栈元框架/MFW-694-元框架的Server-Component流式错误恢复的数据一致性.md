---
title: [MFW-694] RSC 流式错误恢复的数据一致性
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-694：RSC 流式错误恢复的数据一致性

**答**:
- 流式错误后的数据一致性：1) **部分流完成**（shell 已发 + 部分 chunk 到达 → 后续 chunk 错误——已到达的内容正确 + 错误段 fallback——「部分一致性」：已显示的数据是真值、错误段是占位）；2) reset() 的重渲染（错误段重试——server 重新渲染该段——数据一致性：重渲染的段可能与已到达段有版本差（数据在两次渲染间变化——前后不一致的窗口））；3) 一致性的方案：重渲染的段带版本戳（数据 version——client 对比）；「部分一致性的可接受度」（多数场景：已显示数据稳定 + 错误段重试——版本差窗口极短可接受）。
- reset 的数据语义：reset() → React 重新 fetch 该段的 server 渲染（action/route 重渲染——不是缓存重试而是完整重渲染）；「reset 的成本」= 重新渲染整段（数据 + 渲染——非增量）。
- 追问钩子：为什么「流中错误后的 reset()」可能看到「与已显示数据不一致」的新数据？——已到达的 chunk 是 T0 渲染的数据；reset 重渲染 = T1 的数据（DB 可能已变）——同页面两个时间点的数据（前后不一致）；可接受：极短窗口（T0~T1 秒级）+ 数据变更频率低；严格一致：整页刷新（放弃增量——全部 T2 时刻数据）——一致性与增量恢复的权衡：完全一致需要整页重渲染（成本），增量恢复有版本差窗口（体验优先）。

```tsx
// 流式错误恢复
// app/products/[id]/page.tsx
export default async function Page({ params }) {
  return (
    <>
      <ProductInfo id={params.id} />                     {/* 可能已到达：T0 数据 */}
      <Suspense fallback={<Skeleton />}>
        <Reviews id={params.id} />                       {/* 错误段：T1 重渲染 */}
      </Suspense>
    </>
  );
}
// error.tsx reset → 重新渲染 Reviews（T1 数据）
'use client';
export default function ReviewsError({ reset }) {
  return <button onClick={reset}>重试评论</button>;
}
// 数据版本戳（一致性检测）
async function getReviews(id: string, version: number) {
  const [reviews, currentVersion] = await Promise.all([
    db.reviews.byProduct(id),
    db.products.version(id),                             // 数据版本号
  ]);
  return { reviews, version: currentVersion };
}
// client 对比版本：版本差 = 已显示数据与重渲染数据的时间差
```
