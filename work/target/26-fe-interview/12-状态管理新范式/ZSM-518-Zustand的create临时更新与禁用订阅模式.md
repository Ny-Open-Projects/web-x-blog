---
title: [ZSM-518] Zustand 的 transient updates 什么时候该绕过 React 渲染
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-518：Zustand 的 transient updates 什么时候该绕过 React 渲染

**答**：
- transient update（瞬态更新）：高频变化不走 `useStore` 订阅，而是 `store.subscribe` 回调里**直接改 DOM / 命令式 API**。适用于每帧更新的场景——拖拽位置、滚动联动、canvas 坐标、手势进度。
- 依据：React 渲染管线一次至少几百微秒，60fps 下每帧 16ms 的预算里，几十次 setState 会挤爆调度队列；直接写 DOM 属性（transform/translate）绕开 diff，性能稳定在帧率预算内。
- 实现三件套：1) `useEffect` 里 `subscribe`，回调里 `ref.current.style.transform = ...`；2) 读状态用 `store.getState()`（不订阅）；3) 写状态用 `setState` 但不触发任何 selector 订阅（或压根不进 store，用 ref 存）。
- 混合模式：低频字段（如「拖拽中」布尔）走 hook 订阅渲染 UI，高频坐标走 transient——「低频驱动结构、高频驱动像素」。
- 追问钩子：XState/Zustand 官方文档都把 transient 列为一等公民方案，判断标准是「变化频率 > 渲染价值」。

```javascript
const useDrag = create((set) => ({
  dragging: false,                    // 低频：驱动 UI（按钮态/提示层）
  start: () => set({ dragging: true }),
  end: () => set({ dragging: false }),
}))

function Draggable() {
  const dragging = useDrag((s) => s.dragging)   // 只订阅低频信号
  const boxRef = useRef(null)

  useEffect(() => {
    let pos = { x: 0, y: 0 }                     // 高频坐标不进 React 状态
    const onMove = (e) => {
      pos = { x: e.clientX, y: e.clientY }
      // 直接写 DOM，绕过 React 渲染
      boxRef.current.style.transform = `translate3d(${pos.x}px, ${pos.y}px, 0)`
    }
    const onDown = () => { useDrag.getState().start(); window.addEventListener('pointermove', onMove) }
    const onUp = () => { useDrag.getState().end(); window.removeEventListener('pointermove', onMove) }
    const el = boxRef.current
    el.addEventListener('pointerdown', onDown)
    window.addEventListener('pointerup', onUp)
    return () => { el.removeEventListener('pointerdown', onDown); window.removeEventListener('pointerup', onUp) }
  }, [])

  return <div ref={boxRef} style={dragging ? { cursor: 'grabbing' } : {}}>拖我</div>
}
```
