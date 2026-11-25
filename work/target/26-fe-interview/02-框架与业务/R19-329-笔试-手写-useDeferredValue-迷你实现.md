---
title: [R19-329] 笔试：手写迷你 useDeferredValue（含 isStale）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-329：笔试：手写迷你 useDeferredValue
**答**：实现 `useMyDeferredValue(value)` 返回 `[deferred, isStale]`：value 变化时输入即时可用（返回原 value 由调用方决定哪部分用 deferred）；deferred 延迟一帧跟随 value；追赶期间 isStale=true。

```javascript
function useMyDeferredValue(value) {
  const [deferred, setDeferred] = useState(value)
  const [stale, setStale] = useState(false)
  const rafRef = useRef(null)
  useEffect(() => {
    if (deferred === value) return
    setStale(true) // 落后中
    cancelAnimationFrame(rafRef.current)
    rafRef.current = requestAnimationFrame(() => {
      setDeferred(value)
      setStale(false)
    })
    return () => cancelAnimationFrame(rafRef.current)
  }, [value, deferred])
  return [deferred, stale]
}
// 用法：const [q] = useMyDeferredValue(query) // query 用于输入框，q 用于列表过滤
```
**评分点**：
- deferred 与 value 的「落后检测」→ isStale。
- 一帧延迟近似 transition 语义（真实 React 用 lane 调度，渲染可中断）。
- effect 清理 cancel。
- deferred === value 时不追加调度（幂等）。
