---
title: [MFW-187] 笔试：手写一个简化版 useOptimistic
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-187：笔试：手写一个简化版 useOptimistic
**题目**：实现 `useOptimistic(state, reducer)` 的核心机制（不必精确复刻 React 内部实现，语义对即可）：① 返回 `[optimisticState, addOptimistic]`；② `addOptimistic(action)` 立即把 reducer 应用到当前值上，UI 即时更新；③ 外部真实 state 变化（过渡结束）时自动回落到真实值并丢弃未确认的乐观值；④ 与 `startTransition`/`useTransition` 的 isPending 联动：过渡未结束时保持乐观态。

```tsx
import { useState, useTransition, useRef } from 'react';

export function useOptimistic<T, A>(state: T, reducer: (base: T, action: A) => T) {
  const [optimistic, setOptimistic] = useState<T | null>(null); // null = 无乐观态
  const [, startTransition] = useTransition();
  const confirmedRef = useRef(state); // 最近一次服务端确认的真实值

  const addOptimistic = (action: A) => {
    const base = optimistic ?? state; // 叠加：已有乐观值之上继续叠
    const next = reducer(base, action);
    setOptimistic(next);
    // 用 transition 包裹：任何一次真实 state 更新都会终结这个过渡，
    // 组件重渲染时「过渡结束 + state 变化」触发回落
    startTransition(() => {
      confirmedRef.current = state; // 占位引用真实 state，促使过渡被渲染
      setOptimistic(null);          // ③ 过渡结束回落真实值
    });
  };

  return [optimistic ?? state, addOptimistic] as const; // ① 有乐观值用乐观值
}

// 用法：点赞按钮
function LikeButton({ likes, addLike }: { likes: number; addLike: () => Promise<void> }) {
  const [optimisticLikes, addOptimistic] = useOptimistic(likes, (n) => n + 1);
  return (
    <button onClick={async () => {
      addOptimistic(null);        // 即时 +1
      await addLike();            // 服务端确认后 state.likes 更新，回落真实值
    }}>{optimisticLikes} 赞</button>
  );
}
```

**评分点**：
1. 拆出「乐观值层」与「真实值层」两个来源，渲染时优先乐观值——这是 useOptimistic 的本质模型。
2. addOptimistic 支持叠加：下一次乐观计算以当前乐观值为 base，不是每次都从真实值重来。
3. 理解回落时机由 React transition 机制驱动（服务端确认 → state 更新 → 过渡结束），能口头讲清这条链路。
4. 正确说明失败场景：Action throw 时真实 state 不变、乐观值随过渡结束被丢弃，UI 自动回滚。
5. 指出真实 API 中 reducer 是纯函数、addOptimistic 不能在事件外随意调用（渲染期间禁止 setState 约束）。
