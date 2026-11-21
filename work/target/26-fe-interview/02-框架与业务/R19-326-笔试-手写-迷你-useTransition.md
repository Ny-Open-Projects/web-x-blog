---
title: [R19-326] 笔试：手写迷你 useTransition（可中断渲染模拟）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-326：笔试：手写迷你 useTransition
**题**：实现简化版：`useMyTransition()` 返回 `[isPending, start]`；start(fn) 中 setState 标记 pending、fn 内的更新延迟到下一帧（模拟低优先级）、完成后清除 pending；连续 start 取消前一次未完成的更新。

```javascript
function useMyTransition() {
  const [pending, setPending] = useState(false)
  const rafRef = useRef(null)
  const start = (fn) => {
    cancelAnimationFrame(rafRef.current) // 取消前一次
    setPending(true)
    rafRef.current = requestAnimationFrame(() => {
      fn()                               // 低优先级执行更新（真实 React 在此可中断）
      setPending(false)
    })
  }
  useEffect(() => () => cancelAnimationFrame(rafRef.current), [])
  return [pending, start]
}
```
**评分点**：
- pending 标记生命周期与更新完成绑定。
- 取消前一次（rafRef cancel）模拟「保留最后意图」。
- 清理副作用防泄漏。
- 能指出真实实现基于 lane 调度（TransitionLanes）与可中断 render，非简单延迟。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-b308f3d0-ab94-444f-9afa-8434e76d4849-cwd'; fi
exit "$__zcode_status"
