---
title: [ZSM-264] Redux DevTools 的时间旅行 rehydrate 是怎么实现的
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-264：Redux DevTools 的时间旅行 rehydrate 是怎么实现的

**答**:
- 机制：devtools 扩展记录每次 dispatch 的 action 与对应 state 快照；点历史条目时调用 store 的 dispatch({ type: '@@redux/REPLACE', state }) 整体替换当前 state
- 所以时间旅行的前提：reducer 纯函数 + 所有状态可序列化——含函数/Proxy/循环引用的 state 会序列化失败导致回放损坏
- 限制一：副作用（middleware 里的请求/埋点）不会重放，跳到过去再 dispatch 未来 action 是「状态重放」不是「行为重放」
- 限制二：外部数据源（非 Redux 状态）不参与，替换后与外部状态脱钩；这就是 dispatch({type:'@@redux/REPLACE'}) 被 lint 禁掉也要能识别的原因

```javascript
// devtools 回放的本质
store.dispatch({
  type: '@@redux/REPLACE',
  state: JSON.parse(localStorage.getItem('snapshot')),  // 整树替换
})
// 纯 reducer 保证：任意状态 S0 + 重放 action 流 a1..an = 确定 Sn
```
