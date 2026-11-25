---
title: [R19-394] 并发渲染边界：useOptimistic 的回滚时机与竞态
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 并发]
type: 面试题
---

## R19-394：并发渲染边界：useOptimistic 的回滚时机与竞态

**答**：
- 生命周期：useOptimistic(state, reducer)——「pending action 期间」显示乐观值；action（通常是 transition 里的异步提交）完成后 React 自动「重放真实状态」——乐观值消失
- 回滚语义：action 抛错 → 乐观值消失回真实状态（自动回滚）；action 成功但真实状态未更新（忘记 setState）→ UI 跳变（乐观值消失但真实数据旧）——「提交后必须更新真实状态」是纪律
- 连续乐观操作：多次 addOptimistic 排队（基于真实 state 逐个 reducer 应用）——乐观值的正确叠加依赖 reducer 纯度
- 与 server action 结合：useActionState + useOptimistic 的标准组合——乐观显示提交，server 返回后 state 校正
- 边界：乐观值不能用于「不可逆操作」（支付）——网络失败回滚的可感知成本高；乐观适合「高价值低风险」（点赞/评论）

```jsx
const [optimisticLikes, addOptimistic] = useOptimistic(
  likes,
  (state, delta) => [...state, { id: tempId, pending: true }],
);
async function like() {
  addOptimistic(1);                        // UI 立即 +1 (pending 标记)
  startTransition(async () => {
    const r = await likeAction(postId);    // 提交
    setLikes(r.likes);                     // 真实状态更新 → 乐观值消失
  });
}
```
