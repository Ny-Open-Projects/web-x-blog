---
title: [R19-211] useActionState 的 prevState 链式累积是怎么工作的？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-211：useActionState 的 prevState 链式累积是怎么工作的？
**答**：
- action 签名 `(prevState, formData) => newState`：每次提交拿到上一轮 state，可实现计数、错误列表追加、多字段编辑合并。
- 典型用法：`fieldErrors: prev?.fieldErrors` 保留未出错字段的旧校验结果，只更新本次出错的。
- 累积语义要幂等设计：连续两次提交间 state 是唯一真相，避免在 state 里叠副作用（如通知队列）——通知用事件层。
- 竞态：React 保证 action 按调用顺序应用 state，prevState 一定是最新一轮的结果。
- 与 useReducer 的对照：action ≈ dispatch 一个「提交事件」，state 结构设计直接决定 UI 可维护性。
```javascript
const [state, formAction, pending] = useActionState(async (prev, fd) => {
  const errors = validate(fd)
  return { ...prev, values: Object.fromEntries(fd), fieldErrors: errors }
}, { values: {}, fieldErrors: {} })
```
