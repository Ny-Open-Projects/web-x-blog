---
title: [DP-230] 源码识别：Redux DevTools / 时间旅行中的命令与快照？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-230：源码识别：Redux DevTools / 时间旅行中的命令与快照？
**答**：
- 命令模式：每个 action 被 DevTools 拦截记录（中间件），时间旅行 = 重放命令序列到第 N 条（dispatch 到第 N 个）。
- 备忘录：state 历史列表是快照流；跳转（jumpToState）直接取历史快照恢复——Redux 不可变性是时间旅行可行的前提。
- 观察者：DevTools 与 store 双向订阅（store.subscribe → devtools 同步；devtools 面板操作 → store.dispatch）。
- 识别要点：能说清"时间旅行的成本是快照存储（性能与内存），生产方案是 action 重放而非全量快照"。

```javascript
// 时间旅行最小实现
const history = [];          // { action, state } 序列
let pointer = -1;
function dispatchTracked(action) {
  history.splice(pointer + 1);               // 丢弃未来（新命令进入）
  const state = reducer(currentState(), action);
  history.push({ action, state });           // 命令 + 快照都存
  pointer = history.length - 1;
  return state;
}
function jumpTo(n) {                         // 时间旅行
  pointer = Math.min(Math.max(0, n), history.length - 1);
  store.replaceState(history[pointer].state);   // 快照恢复
}
function replayTo(n) {                       // 重放（action 流时）
  store.replaceState(history[0].state);
  history.slice(1, n + 1).forEach(h => reducer(currentState(), h.action));
}
// DevTools 中间件：store.dispatch 被装饰为 dispatchTracked（DP-205 装饰链的延伸）
```
