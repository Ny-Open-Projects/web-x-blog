---
title: [H5-129] measureText 与文本基线有哪些必踩的坑？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-129：measureText 与文本基线有哪些必踩的坑？
**答**：
- `measureText` 返回 TextMetrics：`width`、`actualBoundingBoxAscent/Descent`（真实墨迹边界）、`fontBoundingBoxAscent/Descent`（字体度量边界）——做视觉居中要用前者，不是后者。
- `textBaseline` 默认 `alphabetic` 是"拉丁字母底座"，中英文/不同字体视觉高度不一致，导致"明明垂直居中了但看起来偏"。
- 截断省略号不要逐字累加测量，二分查找 `O(log n)`；每帧改 `font` 会触发字体度量重算，按 font 分组绘制并缓存测量结果。
- 高分屏下 canvas 文本会因缩放发虚，绘制前 `scale(dpr)` 是前提。

```javascript
const ctx = canvas.getContext('2d');

// 1) 基线：默认 alphabetic 是"字母底座"，中英文视觉高度不一致
ctx.font = '16px sans-serif';
ctx.textBaseline = 'alphabetic';
ctx.fillText('Hello 文本', 10, 30);

// 2) 真正的"视觉垂直居中"要用真实墨迹边界 actualBoundingBox
function drawCentered(c, text, cx, cy) {
  const m = c.measureText(text);
  const inkH = m.actualBoundingBoxAscent + m.actualBoundingBoxDescent; // 墨迹高
  c.fillText(text, cx - m.width / 2, cy + inkH / 2 - m.actualBoundingBoxDescent);
}
ctx.strokeStyle = '#ddd';
ctx.beginPath(); ctx.moveTo(0, 30); ctx.lineTo(240, 30); ctx.stroke(); // 参考线
drawCentered(ctx, '对勾 OK', 120, 30);

// 3) 宽度截断（省略号）：二分比逐字累加快得多
function ellipsis(c, text, maxW) {
  if (c.measureText(text).width <= maxW) return text;
  let lo = 0, hi = text.length;
  while (lo < hi) {
    const mid = (lo + hi + 1) >> 1;
    if (c.measureText(text.slice(0, mid) + '…').width <= maxW) lo = mid;
    else hi = mid - 1;
  }
  return text.slice(0, lo) + '…';
}
console.log(ellipsis(ctx, '这是一段很长很长的文本需要截断', 120));

// 4) 性能：font 切换触发度量重算，按 font 分组绘制并缓存测量结果
const cache = new Map();
function textW(c, t) {
  if (!cache.has(t)) cache.set(t, c.measureText(t).width);
  return cache.get(t);
}
```
