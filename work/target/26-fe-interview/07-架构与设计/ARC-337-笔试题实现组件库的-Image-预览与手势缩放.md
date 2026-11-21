---
title: [ARC-337] 笔试题：实现组件库的 Image 预览与手势缩放？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-337：笔试题：实现组件库的 Image 预览与手势缩放？
**题目**：实现图片预览器：1) 滚轮缩放（以鼠标位置为缩放中心）；2) 拖拽平移；3) 双指捏合缩放（touch 事件计算）；4) 缩放范围 0.2~5 与重置；5) transform 组合正确（scale 围绕中心点）。
**评分点**：
- 缩放中心数学正确（newOffset = mouse - (mouse - offset) * ratio）。
- 拖拽与缩放状态复合（translate(x,y) scale(s) 顺序一致）。
- 双指捏合：初始距离与当前距离比值作为 scale 增量。
- 边界 clamp 与重置动画。
```tsx
function ImagePreview({ src }) {
  const [st, setSt] = useState({ x: 0, y: 0, s: 1 });
  const drag = useRef<{ px: number; py: number; ox: number; oy: number } | null>(null);
  const pinch = useRef<{ d0: number; s0: number } | null>(null);
  const wheel = (e: React.WheelEvent) => {
    const rect = (e.currentTarget as HTMLElement).getBoundingClientRect();
    const mx = e.clientX - rect.left, my = e.clientY - rect.top;
    setSt(({ x, y, s }) => {
      const ns = Math.min(5, Math.max(0.2, s * (e.deltaY < 0 ? 1.15 : 0.87)));  // 4) clamp
      const r = ns / s;
      return { s: ns, x: mx - (mx - x) * r, y: my - (my - y) * r };             // 1) 中心缩放
    });
  };
  const onPointerDown = (e: React.PointerEvent) => {
    (e.target as HTMLElement).setPointerCapture(e.pointerId);
    drag.current = { px: e.clientX, py: e.clientY, ox: st.x, oy: st.y };
  };
  const onPointerMove = (e: React.PointerEvent) => drag.current &&
    setSt(s => ({ ...s, x: drag.current!.ox + e.clientX - drag.current!.px,
                            y: drag.current!.oy + e.clientY - drag.current!.py }));  // 2) 平移
  const onTouchMove = (e: React.TouchEvent) => {
    if (e.touches.length === 2) {
      const [a, b] = e.touches as unknown as TouchList;
      const d = Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY);
      if (!pinch.current) pinch.current = { d0: d, s0: st.s };
      setSt(s => ({ ...s, s: Math.min(5, Math.max(0.2, pinch.current!.s0 * d / pinch.current!.d0)) })); // 3) 捏合
    }
  };
  return <div onWheel={wheel} onPointerDown={onPointerDown} onPointerMove={onPointerMove}
    onPointerUp={() => (drag.current = null)} onTouchMove={onTouchMove} onTouchEnd={() => (pinch.current = null)}>
    <img src={src} draggable={false} style={{ transform: `translate(${st.x}px,${st.y}px) scale(${st.s})` }}/> {/* 5) */}
  </div>;
}
```
