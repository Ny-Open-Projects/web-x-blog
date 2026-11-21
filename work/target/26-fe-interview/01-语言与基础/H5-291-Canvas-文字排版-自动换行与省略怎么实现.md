---
title: [H5-291] Canvas 文字排版：自动换行与省略怎么实现
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Canvas]
type: 面试题
---

## H5-291：Canvas 文字排版：自动换行与省略怎么实现

**答**：
- fillText 不换行不省略——排版要自己写：逐字符/逐词累加宽度，超过 maxWidth 断行
- 中文按字符断，英文按空格断（不拆单词）；用 measureText 累计宽度
- 省略号：总行数超限时，最后一行截断并追加 …（… 宽度也要算进去）
- 性能：measureText 昂贵，同段落结果缓存；换行结果稳定后可整体缓存成离屏层
- 进阶：富文本混排（不同字号颜色）需要分段测量与逐段绘制，复杂场景直接用 HTML 而非 Canvas

```javascript
function wrapText(ctx, text, x, y, maxWidth, lineHeight, maxLines = 3) {
  const rows = [];
  let line = '';
  for (const ch of text) {
    if (ctx.measureText(line + ch).width > maxWidth) {
      rows.push(line); line = ch;
      if (rows.length === maxLines) break;
    } else line += ch;
  }
  if (rows.length < maxLines) rows.push(line);
  if (rows.length === maxLines && text.includes(rows.at(-1)) === false) {
    let last = rows[maxLines - 1];
    while (ctx.measureText(last + '…').width > maxWidth) last = last.slice(0, -1);
    rows[maxLines - 1] = last + '…';
  }
  rows.forEach((r, i) => ctx.fillText(r, x, y + i * lineHeight));
  return rows;
}
```
