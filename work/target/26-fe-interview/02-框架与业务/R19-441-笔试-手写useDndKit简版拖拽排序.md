---
title: [R19-441] 笔试：手写 useDragSort（列表拖拽排序）
date: 2026-11-21
categories: [React19]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## R19-441：笔试：手写 useDragSort

**答**：实现 `useDragSort(items, onReorder)`：① 按下记录起始 index，move 中计算目标 index（基于位移与 item 高度），实时预览（transform 偏移拖拽项 + 其他项让位动画）；② 松手提交 onReorder(from, to)（state 重排）；③ 触摸兼容（pointer events + touch-action: none）；④ 边界钳制（不出列表）；⑤ 拖拽项样式（提起阴影 + zIndex）。写出实现。

```javascript
export function useDragSort(items, onReorder) {
  const [dragging, setDragging] = useState(null);   // { index, offsetY }
  const itemRefs = useRef(new Map());

  function onPointerDown(e, index) {
    const el = itemRefs.current.get(index);
    el.setPointerCapture(e.pointerId);
    const startY = e.clientY;
    const itemH = el.offsetHeight;
    setDragging({ index, offsetY: 0, startY, itemH, target: index });

    const onMove = (ev) => {
      const dy = ev.clientY - startY;
      const target = clamp(index + Math.round(dy / itemH), 0, items.length - 1);
      setDragging({ index, offsetY: dy, itemH, target });
    };
    const onUp = () => {
      setDragging((d) => {
        if (d && d.target !== d.index) onReorder(d.index, d.target);
        return null;
      });
      el.removeEventListener('pointermove', onMove);
      el.removeEventListener('pointerup', onUp);
    };
    el.addEventListener('pointermove', onMove);
    el.addEventListener('pointerup', onUp);
  }
  function itemStyle(index) {
    if (!dragging) return {};
    const d = dragging;
    if (index === d.index)
      return { transform: `translateY(${d.offsetY}px)`, zIndex: 10, boxShadow: '0 8px 24px #0003', opacity: .9 };
    // 让位: 被「跨过」的项反向偏移
    const crossed = (index > d.index && index <= d.target) || (index < d.index && index >= d.target);
    return crossed ? { transform: `translateY(${index < d.index ? d.itemH : -d.itemH}px)`, transition: 'transform .15s' } : {};
  }
  return { itemRefs, onPointerDown, itemStyle, dragging };
}
function clamp(v, min, max) { return Math.min(max, Math.max(min, v)); }
```

**评分点**：
- 目标 index 由位移/高度推算 + 边界钳制
- 让位动画（被跨过项的反向 transform 过渡）
- pointer capture 保证移出跟踪 + touch-action: none 提示
- 松手提交 onReorder（state 重排而非 DOM 手动排序）
