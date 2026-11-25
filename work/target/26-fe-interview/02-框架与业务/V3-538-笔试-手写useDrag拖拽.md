---
title: [V3-538] 笔试：手写 useDrag（指针拖拽 composable）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## V3-538：笔试：手写 useDrag

**答**：实现 `useDrag(targetRef, { onDragStart, onDrag, onDragEnd, axis })`：① Pointer Events 统一鼠标/触摸；② 位移计算：dx/dy 相对按下点，axis 限制（'x'|'y'|undefined）；③ setPointerCapture 保证移出元素仍跟踪；④ 惯性可选（速度追踪，松手回调带 velocity）；⑤ 生命周期清理。写出实现。

```javascript
export function useDrag(targetRef, { onDragStart, onDrag, onDragEnd, axis } = {}) {
  const dragging = ref(false);
  const pos = ref({ x: 0, y: 0 });
  let start = null, last = null;

  function onDown(e) {
    dragging.value = true;
    start = last = { x: e.clientX, y: e.clientY, t: performance.now() };
    targetRef.value.setPointerCapture(e.pointerId);   // 移出元素仍跟踪
    onDragStart?.(start);
  }
  function onMove(e) {
    if (!dragging.value) return;
    let dx = e.clientX - start.x, dy = e.clientY - start.y;
    if (axis === 'x') dy = 0;
    if (axis === 'y') dx = 0;
    pos.value = { x: dx, y: dy };
    const now = performance.now();
    const dt = now - last.t || 16;
    const velocity = { vx: (e.clientX - last.x) / dt, vy: (e.clientY - last.y) / dt };
    last = { x: e.clientX, y: e.clientY, t: now };
    onDrag?.({ dx, dy, pos: pos.value, velocity });
  }
  function onUp(e) {
    if (!dragging.value) return;
    dragging.value = false;
    const dt = performance.now() - last.t || 16;
    onDragEnd?.({ pos: pos.value, velocity: { vx: (e.clientX - last.x) / dt, vy: (e.clientY - last.y) / dt } });
  }
  useEventListener(targetRef, 'pointerdown', onDown);
  useEventListener(targetRef, 'pointermove', onMove);
  useEventListener(targetRef, 'pointerup', onUp);
  useEventListener(targetRef, 'pointercancel', onUp);
  return { dragging, pos };
}
// 用法: 卡片拖拽 + 松手惯性
useDrag(el, { axis: 'x', onDragEnd: ({ velocity }) => flick(velocity.vx) });
```

**评分点**：
- Pointer Events + setPointerCapture（移出跟踪）
- axis 约束与位移计算
- 速度追踪（最近采样差分）供惯性判定
- pointercancel 兜底与生命周期清理
