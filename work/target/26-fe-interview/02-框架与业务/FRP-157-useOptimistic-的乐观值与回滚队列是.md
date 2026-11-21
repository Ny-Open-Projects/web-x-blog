---
title: [FRP-157] useOptimistic 的乐观值与回滚队列是怎么实现的？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-157：useOptimistic 的乐观值与回滚队列是怎么实现的？

**答**：
- `useOptimistic(state, reducer)` 读到的值 = **真实 state + 未决 action 依次 reduce 的叠加结果**；传给 action 的 dispatch 把 action 入队（只影响显示，不改真实 state）。
- action 完成时（真实 state 更新），React 丢弃所有未决乐观 action——因为它们的"期望结果"已包含在真实 state 里，显示自动回落到真值。
- 失败回滚：action 抛错或返回与乐观假设不符的真值时，未决队列清空，显示回落到真实 state——乐观值"自动消失"。
- 关键细节：action 执行期间 `useOptimistic` 的 dispatch 持续生效（第二次提交叠加在第一次的乐观结果上），保证连续操作时 UI 累积乐观。

```javascript
// 简化实现，帮助理解 useOptimistic
function useOptimistic(passthrough, reducer) {
  const [optimisticState, setOptimisticState] = useState(null); // 未决队列的叠加结果

  const dispatch = (action) => {
    // 1. 叠加乐观值：基于当前显示值（可能已含前面的乐观）再 reduce
    setOptimisticState(prev =>
      reducer(optimisticState ?? passthrough, action)
    );
  };

  // React 在 transition 中执行 action：action 完成（setState 落地）后清除队列
  // —— 由框架在 commit 时自动执行，相当于：
  function clearOptimisticQueue() {
    setOptimisticState(null); // 回落到 passthrough（真实 state）
  }

  return [optimisticState ?? passthrough, dispatch];
}

// 使用：
function Thread({ messages }) {
  const [optimisticMessages, addOptimistic] = useOptimistic(
    messages,
    (current, newMsg) => [...current, { ...newMsg, sending: true }]
  );
  async function send(formData) {
    addOptimistic({ text: formData.get('text') });  // 立刻显示（带 sending 标记）
    await sendMessage(formData);                     // 真实请求（Server Action）
    // 成功：真实 messages 更新流回 -> 乐观值自动被真值覆盖
    // 失败：revalidate/错误处理 -> 队列清空，乐观消息消失
  }
  return optimisticMessages.map(m => <Bubble key={m.id} msg={m} />);
}

// —— 时序演示 ——
// 初始 messages = [A, B]
// 1. dispatch(C)：显示 [A, B, C']（C' 带 sending 标记）—— 纯本地叠加
// 2. action 执行中再次 dispatch(D)：显示 [A, B, C', D']
// 3. action 完成，真实 state = [A, B, C, D]：显示回落 [A, B, C, D]
// 4. action 失败：真实 state 不变 [A, B]：显示回落 [A, B] —— 回滚完成
// 核心不变式：乐观值永远派生自"真实 state + 未决 action"，真实 state 一变就整体重算
```
