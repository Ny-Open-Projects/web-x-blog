---
title: [MFW-580] Server Component 中的乐观 UI 边界
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-580：Server Component 中的乐观 UI 边界

**答**:
- 乐观 UI 的边界：乐观状态只存在于 client 组件（useOptimistic——server 组件无状态）；「乐观区域的最小化」：只有正在变更的数据乐观化（点赞数 +1），周围数据保持 server 权威（列表其他项不动）——「乐观的粒度 = 变更的字段」而非「整个页面」。
- 乐观值的生命周期：提交前显示乐观值 → server 确认（revalidate）→ 真值替换；失败回滚（RBL-513）；「乐观窗口期」的数据一致性（乐观期间其他用户变更——并发写：乐观值可能覆盖他人变更——最后写入胜/冲突提示）。
- 混合树中的乐观：server 树内的 client 岛（ProductCard client）——乐观只在岛内（点赞数在岛内 client state）；岛外（价格）server 权威——「server/client 边界 = 乐观边界」。
- 追问钩子：为什么「乐观的粒度」要限制在变更字段而不是整页状态？——整页乐观 = client 持有整页状态副本（RSC 的 server 权威失效——回到 SPA 数据架构）；字段级乐观 = server 树不动 + 岛内小状态（RSC 优势保留）；「乐观是局部状态修补而非全局状态替代」——乐观 UI 在 RSC 下的正确形态：最小粒度 + 短生命周期 + server 确认后交还权威。

```tsx
// 字段级乐观（点赞岛）
// ProductCard.tsx ('use client') —— server 树内的 client 岛
export function LikeButton({ productId, initialLikes }) {
  const [optimisticLikes, addLike] = useOptimistic(
    initialLikes, (cur, delta) => cur + delta);
  return (
    <form action={async () => {
      addLike(1);                                        // 乐观 +1（岛内）
      await likeAction(productId);                       // server 写 + revalidate
    }}>
      <span>{optimisticLikes}</span>                     {/* 乐观窗口期 */}
      <button>Like</button>
    </form>
  );
}
// server 树（父级）不变：价格/标题保持 server 权威
// app/page.tsx
// <ProductCard productId={p.id} initialLikes={p.likes} />  ← server 传入
// <Price price={p.price} />                                 ← server 权威不乐观
```
