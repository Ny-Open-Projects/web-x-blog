---
title: [WCN-096] 笔试：手写 Signals 版拖拽排序（高频坐标 → rAF 合帧渲染）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-096：笔试：手写 Signals 版拖拽排序

**题目**：① `dragState` signal：`{ id, x, y, overIndex }` 或 null；② pointermove 高频写入坐标，渲染必须 rAF 合帧（每帧最多一次 transform 更新）；③ `overIndex` 变化时插入占位符（其余项让位）；④ pointerup 提交新顺序并清空 dragState；⑤ 未变不渲染（坐标相等短路）；⑥ 拖拽期间禁用文本选中与滚动穿透。

**答**：

```javascript
import { createSignal, effect, untrack } from './mini.js';

export function setupDragSort(listEl, items, onCommit) {
  const [drag, setDrag] = createSignal(null);   // { id, x, y, overIndex }
  let raf = 0, lastXY = '';

  function renderItem(d) {
    if (!d) return;
    const key = `${d.x}|${d.y}`;                // 未变短路
    if (key === lastXY) return;
    lastXY = key;
    const el = listEl.querySelector(`[data-id="${d.id}"]`);
    el.style.transform = `translate(${d.x}px, ${d.y}px)`;
    el.classList.add('dragging');
  }
  const stop = effect(() => {
    const d = drag();
    if (!raf) raf = requestAnimationFrame(() => { raf = 0; renderItem(untrack(drag)); });
    listEl.querySelectorAll('[data-id]').forEach((el) => {
      el.classList.toggle('drop-gap', d && Number(el.dataset.index) === d.overIndex);
    });
  });

  listEl.addEventListener('pointerdown', (e) => {
    const el = e.target.closest('[data-id]');
    if (!el) return;
    e.preventDefault();                          // 禁文本选中
    document.body.style.overflow = 'hidden';     // 禁滚动穿透
    const rect = el.getBoundingClientRect();
    setDrag({ id: el.dataset.id, x: 0, y: 0, overIndex: Number(el.dataset.index) });
    const move = (ev) => {
      const dx = ev.clientX - rect.left, dy = ev.clientY - rect.top;
      const overIndex = Math.round(dy / el.offsetHeight); // 简化：按行高估算
      untrack(() => setDrag({ id: el.dataset.id, x: dx, y: dy, overIndex }));
    };
    const up = () => {
      window.removeEventListener('pointermove', move);
      window.removeEventListener('pointerup', up);
      const d = untrack(drag);
      if (d && d.overIndex !== Number(el.dataset.index)) onCommit(d.id, d.overIndex);
      setDrag(null);
      document.body.style.overflow = '';
    };
    window.addEventListener('pointermove', move);
    window.addEventListener('pointerup', up);
  });

  return { drag, stop,
    dispose() { stop(); cancelAnimationFrame(raf); } };
}
```

**评分点**：
- rAF 合帧：高频 pointermove 每帧最多一次渲染（性能核心）。
- 坐标字符串对比短路（同值不写 style）。
- pointerup 提交 + 状态清理（overflow、监听器移除）。
- overIndex 独立控制占位 class；transform 不触发重排。
