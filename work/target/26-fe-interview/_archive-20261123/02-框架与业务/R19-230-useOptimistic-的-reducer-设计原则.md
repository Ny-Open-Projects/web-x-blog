---
title: [R19-230] useOptimistic 的 reducer 有哪些设计原则（可重放/纯函数/幂等）？
date: 2026-11-19
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-230：useOptimistic 的 reducer 有哪些设计原则？
**答**：
- 纯函数：不读外部变量、不产生副作用，只 (serverState, optimisticAction) → 新状态。
- 可重放：同一操作应用到「任何时刻的 serverState」结果都合理——避免依赖具体版本号/顺序号之外的状态。
- 幂等友好：操作语义用「设值」优于「增减」时优先设值（likes: 5 vs likes + 1），重放安全。
- 不做校验：乐观层不做业务校验（那是 action 的事），只做「视图会怎么变」的描述。
- 不可变更新：返回新对象/数组（浅拷贝），避免 mutation 导致 React 漏渲染。
```javascript
const [optimisticLikes, addOptimistic] = useOptimistic(
  likes, // server state
  (cur, op) => op.type === 'like' ? cur + 1 : Math.max(0, cur - 1)
)
```
