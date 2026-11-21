---
title: [ARC-326] 笔试题：实现 Table 列宽拖拽调整？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-326：笔试题：实现 Table 列宽拖拽调整？
**题目**：给 Table 组件实现列宽拖拽：1) 表头边缘拖拽手柄；2) 拖拽中实时更新列宽且不抖动（不重排文本）；3) 最小列宽约束；4) 释放后触发 onResize 持久化回调；5) 无障碍（键盘可调）。
**评分点**：
- pointer 事件使用正确（setPointerCapture 保证移出手柄仍跟踪）。
- 基准记录正确（起始 x + 起始宽度 → delta 模式，非绝对定位模式）。
- 最小宽度 clamp 与拖拽中防抖动处理（table-layout: fixed 或固定容器宽）。
- 释放才提交 onResize，过程用本地态；键盘支持（左右箭头 ±16px）。
```tsx
function ResizableTh({ col, onResize }) {
  const [w, setW] = useState(col.width);
  const startRef = useRef({ x: 0, w: 0 });
  const onPointerDown = (e: React.PointerEvent) => {
    e.preventDefault();
    (e.target as HTMLElement).setPointerCapture(e.pointerId);           // 2) 捕获
    startRef.current = { x: e.clientX, w };
    const move = (ev: PointerEvent) =>
      setW(Math.max(col.min ?? 80, startRef.current.w + ev.clientX - startRef.current.x)); // 3) clamp
    const up = () => {
      window.removeEventListener('pointermove', move);
      window.removeEventListener('pointerup', up);
      onResize(col.key, w);                                             // 4) 释放提交
    };
    window.addEventListener('pointermove', move);
    window.addEventListener('pointerup', up);
  };
  return (
    <th style={{ width: w, overflow: 'hidden' }}>                       {/* fixed 布局防抖 */}
      {col.title}
      <span role="separator" tabIndex={0} aria-label={`调整${col.title}列宽`}
        onPointerDown={onPointerDown}
        onKeyDown={e => {                                              // 5) 键盘
          if (e.key === 'ArrowLeft') { const nw = w - 16; setW(nw); onResize(col.key, nw); }
          if (e.key === 'ArrowRight') { const nw = w + 16; setW(nw); onResize(col.key, nw); }
        }}
        style={{ cursor: 'col-resize', position: 'absolute', right: 0, width: 6, top: 0, bottom: 0 }}/>
    </th>
  );
}
```
