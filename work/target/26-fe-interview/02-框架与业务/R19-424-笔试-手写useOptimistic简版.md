---
title: [R19-424] 笔试：手写 useOptimistic 简版
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 并发]
type: 笔试题
---

## R19-424：笔试：手写 useOptimistic

**答**：实现 useOptimistic 语义：① `useOptimistic(state, reducer)`——返回 [乐观值, addOptimistic]；② addOptimistic 后渲染用乐观值（reducer 基于「真实 state + pending 队列」计算）；③ transition/action 完成后（真实 state 更新）pending 队列清空，乐观值消失；④ 连续乐观操作的叠加（队列顺序应用）；⑤ 失败回滚（action 抛错 → 队列清空回真实值）。写出实现（简化版：用显式 pending 状态管理）。

```javascript
function useOptimisticShim(state, reducer) {
  const pendingRef = useRef([]);                    // 乐观操作队列
  const [, force] = useReducer(c => c + 1, 0);

  const optimistic = useMemo(() => {
    return pendingRef.current.reduce(
      (acc, action) => reducer(acc, action),
      state,                                        // 基于真实 state 叠加
    );
  }, [state, pendingRef.current.length]);

  const addOptimistic = (action) => {
    pendingRef.current.push(action);
    force();                                        // 立即渲染乐观值
  };
  const commit = async (task) => {
    try {
      await task();                                 // 提交(内部应更新真实 state)
    } finally {
      pendingRef.current = [];                      // 完成/失败都清队列(自动回滚)
      force();
    }
  };
  return [optimistic, addOptimistic, commit];
}
// 用法
const [likes, addLike, commitLike] = useOptimisticShim(likesState, (s, d) => s + d);
function onLike() {
  addLike(1);                                       // UI 立即 +1
  commitLike(async () => {
    const r = await likeAction(postId);
    setLikesState(r.count);                         // 真实更新 → 乐观消失
  });
}
```

**评分点**：
- 乐观值 = 真实 state + pending 队列按序 reduce（叠加语义）
- commit 的 finally 清队列（成功/失败都回真实值 = 自动回滚）
- 「提交后必须更新真实 state」的纪律（否则跳变）
- force 触发即时渲染（真实实现的 transition 绑定被简化）
