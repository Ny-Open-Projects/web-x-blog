---
title: [ZSM-031] Zustand 的 transient updates（瞬时更新）是什么？拖拽、动画为什么不该走 setState 重渲染？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-031：Zustand 的 transient updates（瞬时更新）是什么？拖拽、动画为什么不该走 setState 重渲染？
**答**：
- 瞬时更新：状态变化**不进 React 渲染流**，用 subscribe + 直接操作 DOM（ref.style）更新，绕过 reconciliation。
- 拖拽/鼠标跟随每秒触发几十上百次 setState，走渲染会带来大量 reconciliation 和掉帧；改 transform 不触发 layout。
- 模式：store 存「落点」用于持久化，运动中的坐标用 subscribe 推给 ref；组件渲染仍订阅 store 拿初始值。
- 追问钩子：useSyncExternalStore 之外的第二条路，体现「状态不一定要驱动渲染」。

```javascript
const usePos = create(set => ({ x: 0, y: 0, setPos: (x, y) => set({ x, y }) }))

function Draggable() {
  const ref = useRef(null)
  useEffect(() => {
    // 高频：直接写 DOM，不触发 React
    const unsub = usePos.subscribe(({ x, y }) => {
      ref.current.style.transform = `translate(${x}px, ${y}px)`
    })
    return unsub
  }, [])
  const x = usePos(s => s.x) // 渲染只关心落点
  return <div ref={ref} style={{ transform: `translate(${x}px, 0px)` }} />
}
```
