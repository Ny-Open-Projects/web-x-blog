---
title: [ZSM-028] Zustand 里在事件回调中连续读 getState 和在渲染中读 selector 有什么区别？为什么回调里必须用 getState？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-028：Zustand 里在事件回调中连续读 getState 和在渲染中读 selector 有什么区别？为什么回调里必须用 getState？
**答**：
- 渲染期读 selector：值在本次渲染内是快照，用于计算 UI；store 后续变化会触发新的渲染。
- 事件回调（setTimeout、async 后续、原生事件）里读渲染闭包中的变量拿到的是**旧快照**；`getState()` 每次调用返回最新 state，是唯一安全的读法。
- 连续多次 set 后再 get 也能拿到合并后的最新值（set 同步生效）。
- 反例：`const count = useStore(s => s.count)` 后在 onClick 里用它自增，连点会丢更新；应改 `set(s => ({ count: s.count + 1 }))` 或 getState().count。

```javascript
const useCounter = create(set => ({ count: 0 }))

function Demo() {
  const count = useCounter(s => s.count) // 渲染快照
  const onClick = () => {
    console.log(count)                        // 旧值！闭包捕获渲染时的快照
    console.log(useCounter.getState().count)  // 最新值
    useCounter.setState(s => ({ count: s.count + 1 })) // 函数式 set：基于最新值
  }
  return <button onClick={onClick}>{count}</button>
}
```
