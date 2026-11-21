---
title: [CSS-070] 纯 CSS 瀑布流 columns 与 JS 实现各有什么问题？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-070：纯 CSS 瀑布流 columns 与 JS 实现各有什么问题？

**答**：
- `columns: 4` + `break-inside: avoid` 即可瀑布流，零 JS、自动平衡列高。
- 致命缺陷：内容按"列"填充（先填满第 1 列再第 2 列），读序与预期不符。
- JS 方案（按最短列放置）：读序正确、可控性强，但需要监听 resize 重算。
- Grid masonry 提案落地前，信息流场景选 JS，图片墙场景 columns 可接受。
- columns 还有分页截断、子元素动画成本高等次要问题。

```css
/* 纯 CSS：注意填充顺序是纵向的 */
.masonry-css {
  columns: 4 240px;
  column-gap: 16px;
}
.masonry-css > .item {
  break-inside: avoid;      /* 防止卡片被切断 */
  margin-bottom: 16px;
}
```

```javascript
// JS 方案：按最短列放置，保证横向读序（核心思路）
function layout(items, colCount) {
  const heights = new Array(colCount).fill(0);
  items.forEach((item) => {
    const i = heights.indexOf(Math.min(...heights)); // 找最短列
    item.style.transform = `translate(${i * colWidth}px, ${heights[i]}px)`;
    heights[i] += item.offsetHeight + gap;
  });
}
window.addEventListener('resize', () => layout(items, getColCount()));
```
