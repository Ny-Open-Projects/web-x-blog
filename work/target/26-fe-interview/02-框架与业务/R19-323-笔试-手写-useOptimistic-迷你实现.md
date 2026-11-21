---
title: [R19-323] 笔试：手写迷你 useOptimistic
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-323：笔试：手写迷你 useOptimistic
**题**：实现 `useMyOptimistic(serverState, reducer)` 返回 `[optimisticState, addOptimistic]`：addOptimistic 入队并立即重算视图；action 结束（调用方传入的 promise settle）后清空队列回 serverState。

```javascript
function useMyOptimistic(serverState, reducer) {
  const [queue, setQueue] = useState([])
  const optimistic = useMemo(
    () => queue.reduce((s, op) => reducer(s, op), serverState),
    [serverState, queue, reducer]
  )
  const addOptimistic = (op) => setQueue(q => [...q, op])
  // 在 action 上下文中使用：
  // startTransition(async () => {
  //   addOptimistic(op)
  //   try { await action() } finally { setQueue([]) } // settle 后清空
  // })
  return [optimistic, addOptimistic, () => setQueue([])]
}
```
**评分点**：
- 队列 reducer 折叠计算（reduce 顺序 = 入队顺序）。
- serverState 变化时乐观层重算（useMemo 依赖）。
- 清空时机 = action settle（成功/失败都清）。
- 能说明真实实现把队列存在 fiber 上、由 React 自动在提交时清理。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-7ad07df4-f0b7-49bb-b4be-20ae26fa5c4d-cwd'; fi
exit "$__zcode_status"
