---
title: [FRP-084] useDeferredValue 的实现机制是什么？为什么需要"两次渲染"？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-084：useDeferredValue 的实现机制是什么？为什么需要"两次渲染"？

**答**：
- `useDeferredValue(value)` 返回一个**延迟版 value**：当 value 变化时，第一次渲染返回**旧值**（保证当前帧立即完成），同时以**低优先级**调度一次重渲染，第二次渲染返回**新值**。
- 内部机制：比较 prevValue 与新 value——若未变直接复用（省一次渲染）；变了则先返回旧值渲染 + `scheduleDeferredUpdate`（基于 lane 的低优先级或 idle 调度），下一轮渲染拿到新值再渲染。
- 与 useTransition 的差异：useTransition 包装**更新动作**（改 state 的那段代码），useDeferredValue 包装**值**（不控制谁触发更新，适合拿不到 setState 的场景，如收到新 props 时）。
- 本质都是双通道调度：紧急渲染用旧数据立即反馈，慢渲染用新数据随后跟上，避免长任务阻塞交互。

```javascript
// 简化实现，帮助理解 useDeferredValue 的两次渲染机制
let scheduledLowPriority = false;
let deferredState = { value: null, deferred: null };

function useMyDeferredValue(value) {
  if (deferredState.value === value) {
    return deferredState.deferred; // value 未变：直接复用，零成本
  }
  // value 变了：本次渲染先返回旧值（紧急帧），同时调度低优先级重渲染
  const prev = deferredState.deferred ?? value;
  deferredState = { value, deferred: prev };
  if (!scheduledLowPriority) {
    scheduledLowPriority = true;
    // 低优先级调度：等当前渲染帧结束后重渲染
    setTimeout(() => {
      scheduledLowPriority = false;
      deferredState = { value, deferred: value }; // 第二次渲染返回新值
      rerender();
    }, 0);
  }
  return prev; // 第一次渲染：旧值
}
let rerender = () => {};

// 验证：查询词变化时，紧急帧用旧关键词渲染列表，下一帧用新关键词
let frame = 0;
function App({ query }) {
  const deferredQuery = useMyDeferredValue(query);
  frame++;
  console.log(`frame ${frame}: 渲染列表用 query = "${deferredQuery}"`);
}
rerender = () => App({ query: 'b' });

App({ query: 'a' });   // frame 1: 用 a 渲染（立即）
App({ query: 'b' });   // frame 2: 仍用 a 渲染紧急帧 + 调度低优先级
setTimeout(() => {}, 5); // frame 3（异步）: 用 b 渲染完整列表
// 输入框更新（紧急）不被大列表重渲染阻塞 —— 与 useTransition 同源思想
```
