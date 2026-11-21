---
title: [ZSM-192] 笔试：手写 useTransient（rAF 节流的瞬态更新 Hook：高频事件绕过 React 逐帧渲染）
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-192：手写 useTransient（rAF 节流的瞬态更新 Hook：高频事件绕过 React 逐帧渲染）
**需求**：实现 `useTransient(onFrame)`：1) 高频事件（pointermove/scroll）回调里只写 ref，不触发渲染；2) rAF 循环里每帧调用一次 onFrame(latest)，可命令式操作 DOM；3) 提供可选的 `commit()`：把最新值 setState 一次，结束高频阶段后「落地」进 React 世界；4) 组件卸载停止 rAF；5) 返回 { ref, commit }。用指针拖拽场景给出完整用法。

```javascript
export function useTransient(onFrame) {
  const ref = useRef({ x: 0, y: 0 })      // 瞬态值：高频写
  const raf = useRef(0)
  const frameRef = useRef(onFrame); frameRef.current = onFrame

  const start = useCallback(() => {
    cancelAnimationFrame(raf.current)
    const loop = () => {
      frameRef.current(ref.current)        // 每帧命令式消费，不走 React
      raf.current = requestAnimationFrame(loop)
    }
    raf.current = requestAnimationFrame(loop)
  }, [])

  const commit = useCallback((setter) => {
    cancelAnimationFrame(raf.current)      // 结束高频阶段
    setter(ref.current)                    // 落地：仅一次 setState
  }, [])

  useEffect(() => () => cancelAnimationFrame(raf.current), [])
  return { ref, start, commit }
}

// 用法：拖拽
function Draggable() {
  const { ref, start, commit } = useTransient(({ x, y }) => {
    elRef.current.style.transform = `translate(${x}px, ${y}px)`  // 60fps 直改 DOM
  })
  function onPointerDown(e) {
    start()
    const move = (ev) => { ref.current.x += ev.movementX; ref.current.y += ev.movementY }
    const up = () => {
      window.removeEventListener('pointermove', move)
      commit(pos => setStateModel(pos))    // 结束才进 React 状态
    }
    window.addEventListener('pointermove', move)
    window.addEventListener('pointerup', up, { once: true })
  }
  return <div ref={elRef} onPointerDown={onPointerDown}/>
}

// 评分点：
// 1. 瞬态值走 ref 不 setState，60fps 零重渲染
// 2. rAF 循环统一消费，与浏览器绘制对齐
// 3. commit 一次性落地 React 世界（transient → state 边界清晰）
// 4. 卸载取消 rAF；onFrame 用 ref 读最新闭包
// 5. 能说明「渲染频率与交互频率解耦」的原理
```
