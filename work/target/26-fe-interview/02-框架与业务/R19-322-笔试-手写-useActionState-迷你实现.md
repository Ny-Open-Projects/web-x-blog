---
title: [R19-322] 笔试：手写迷你 useActionState（含 isPending）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-322：笔试：手写迷你 useActionState
**答**：实现 `useMyActionState(action, initialState)` 返回 `[state, formAction, isPending]`：formAction(formData) 串行执行 action(prev, formData)；执行中 isPending=true；按调用顺序应用结果（防乱序）。

```javascript
function useMyActionState(action, initialState) {
  const [state, setState] = useState(initialState)
  const [pending, setPending] = useState(false)
  const seqRef = useRef(0)
  const formAction = (formData) => {
    const seq = ++seqRef.current
    setPending(true)
    Promise.resolve(action(state, formData)).then(res => {
      if (seq !== seqRef.current) return // 过期结果丢弃
      setState(res)
    }).finally(() => {
      if (seq === seqRef.current) setPending(false)
    })
  }
  return [state, formAction, pending]
}
```
**评分点**：
- seq 防乱序（串行语义核心）。
- isPending 只由最新一次请求控制。
- action 可能是同步或异步（Promise.resolve 包裹）。
- 说明真实实现里 isPending 与渲染提交绑定、action 在 transition 中执行。
