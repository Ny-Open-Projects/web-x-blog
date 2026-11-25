---
title: [MFW-741] Server Action 乐观更新竞态
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-741：Action 乐观更新竞态

**答**:
- 乐观更新的竞态场景：1) **快速双击**（两次 addLike——两次乐观 +1 → server 收到两次（幂等键区分 RBL-567）——乐观值 = +2（两次 add 的累积）→ server 真值 = 实际次数；2) **乐观与 revalidate 交错**（action A 提交中 → revalidate（其他用户的变更）→ 乐观值被 revalidate 数据覆盖（乐观值消失——revalidate 后真值替换 RBL-580；「乐观值的生命周期」：add → 显示 → revalidate → 真值（或 server 确认值））；3) **多 action 并发**（like + dislike 同时——两个 action 的乐观值叠加（各自独立 useOptimistic——React 的乐观状态隔离）；4) 回滚的级联（action A 失败 → A 的乐观回滚——不影响 B 的乐观值（React 的 useOptimistic 按 action 粒度隔离）。
- 追问钩子：为什么「revalidate 后乐观值消失」不是 bug 而是 React 的设计？——revalidate = server 数据变更（真值更新——server 的权威数据可能包含/不包含用户的乐观操作）；乐观值的存在意义 = 「等待 server 确认的临时状态」；revalidate 后 server 确认 = 乐观值被真值替换（乐观值完成了使命）；「乐观值的生命周期」= 从 add 到 revalidate/server confirm——短暂存在的设计意图：乐观不是持久状态而是「UI 的即时反馈层」。

```tsx
'use client';
function LikeButton({ productId, serverLikes }: { productId: string; serverLikes: number }) {
  const [optimisticLikes, addOptimisticLike] = useOptimistic(
    serverLikes,
    (current, delta: number) => current + delta           // 乐观累积
  );
  const [isPending, startTransition] = useTransition();
  return (
    <form action={async (fd) => {
      startTransition(async () => {
        addOptimisticLike(1);                              // 立即 UI +1
        await likeAction(productId);                       // server 写 + revalidate
        // revalidate 后 serverLikes 更新 → useOptimistic 自动重置
      });
    }}>
      <span>{optimisticLikes}</span>                        {/* 乐观值（serverLikes 基础上） */}
      <button disabled={isPending}>Like</button>
    </form>
  );
}
// 快速双击：两次 addOptimisticLike(1) = +2 乐观
// server：两个 action（幂等键区分）→ 实际 +2 → revalidate → serverLikes = +2
```
