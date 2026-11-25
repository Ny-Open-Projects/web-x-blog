---
title: [DP-377] 乐观 UI 模式：结构化实现
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 面试题, 设计模式]
type: 面试题
---

## DP-377：乐观 UI 结构化

**答**：
- 乐观 UI 的结构化：不是「先改 state 再请求」的随意——标准协议：onMutate（快照+乐观写）→ 请求 → onSuccess（服务端值校正）/ onError（快照回滚+通知）
- 实战要点：乐观值的「pending 标记」（UI 显示乐观态的视觉区分——待确认/已确认）；并发乐观操作的叠加（队列化——按序 reducer）
- 适用判定：高频低风险（点赞）乐观；低频高风险（支付）不乐观——「乐观的风险矩阵」
- 与 useOptimistic 的关系：React 19 内置了该模式的自动化（pending 期间乐观、结束回真实）——手写理解协议，生产用内置
- 深水点：乐观 UI 的「真值校正」——服务端返回与乐观值不同时以服务端为准（reconcile）——不校正会产生「乐观值成为事实」的幻觉

```javascript
async function optimisticLike(postId, state) {
  const snapshot = structuredClone(state);
  state.set({ ...state.get(), likes: state.get().likes + 1, pending: true });   // 乐观
  try {
    const real = await api.like(postId);
    state.set({ likes: real.count, pending: false });   // 校正
  } catch (e) {
    state.set(snapshot);                                // 回滚
    toast('点赞失败');
  }
}
```
