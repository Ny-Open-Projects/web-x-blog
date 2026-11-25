---
title: [H5-183] 设计一个拖拽看板（HTML5 DnD vs Pointer Events 选型）
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-183：设计一个拖拽看板（HTML5 DnD vs Pointer Events 选型）
**答**：
- 选型结论：看板这种需要**自定义拖动影像、自动滚动、触屏支持**的场景选 Pointer Events 自实现；原生 HTML5 DnD 适合"少量、桌面端、整元素拖动"（如拖文件进浏览器）。
- 原生 DnD 优点：dragstart/dragover/drop 语义齐全、与文件拖入统一；缺点：触屏不支持、拖动影像是浏览器截图不可定制、drop 目标判定与自动滚动都要 hack。
- Pointer 方案核心：pointerdown 记录偏移 → clone 一个 fixed 定位的 ghost 跟随 → `elementFromPoint` 找目标列 → 与列内卡片中点比较算插入位 → pointerup 提交。
- 体验细节：ghost `pointer-events:none` 防挡 elementFromPoint、原卡片半透明占位、拖动时列表 `touch-action: none`。

```html
<div class="board">
  <ul class="col" data-col="todo">
    <li data-id="1">需求 A</li>
    <li data-id="2">需求 B</li>
  </ul>
  <ul class="col" data-col="doing"></ul>
</div>
<style>
  .board { display: flex; gap: 16px; }
  .col { width: 200px; min-height: 200px; background: #f1f5f9;
         padding: 8px; list-style: none; touch-action: none; }
  li { background: #fff; padding: 8px; margin-bottom: 8px;
       box-shadow: 0 1px 2px rgba(0,0,0,.1); }
</style>
<script>
// 方案：Pointer Events + transform ghost（看板推荐）
let drag = null;

document.addEventListener('pointerdown', (e) => {
  const card = e.target.closest('[data-id]');
  if (!card) return;
  const rect = card.getBoundingClientRect();
  drag = {
    card,
    ox: e.clientX - rect.left, oy: e.clientY - rect.top,
    ghost: card.cloneNode(true),
  };
  Object.assign(drag.ghost.style, {
    position: 'fixed', pointerEvents: 'none',       // 不挡 elementFromPoint
    width: rect.width + 'px', zIndex: 999, opacity: .85, margin: 0,
  });
  document.body.append(drag.ghost);
  card.style.opacity = .3;                          // 原位半透明占位
});

document.addEventListener('pointermove', (e) => {
  if (!drag) return;
  drag.ghost.style.left = e.clientX - drag.ox + 'px';
  drag.ghost.style.top = e.clientY - drag.oy + 'px';
  // 目标列与插入位：与列内卡片中点比较
  const col = document.elementFromPoint(e.clientX, e.clientY)?.closest('.col');
  if (col) {
    const cards = [...col.querySelectorAll('[data-id]')]
      .filter((c) => c !== drag.card);
    const next = cards.find((c) =>
      e.clientY < c.getBoundingClientRect().top + c.offsetHeight / 2);
    next ? col.insertBefore(drag.card, next) : col.append(drag.card);
  }
});

document.addEventListener('pointerup', () => {
  if (!drag) return;
  drag.card.style.opacity = '';
  drag.ghost.remove();
  persist(drag.card.dataset.id, drag.card.closest('.col').dataset.col);
  drag = null;
});
function persist(cardId, colName) { console.log('上报', cardId, '->', colName); }

// 选型对比（答题口径）：
// 原生 HTML5 DnD：dragstart/dragover/drop 语义齐全、与文件拖入统一；
//   缺点：触屏不支持、拖动影像是浏览器截图不可定制、自动滚动要 hack
// Pointer Events：全平台、ghost 完全可控、可加键盘替身（ARIA 拖拽）；
//   代价：拖拽语义全部自己实现
</script>
```
