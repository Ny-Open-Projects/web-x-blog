---
title: [VIZ-019] Canvas 没有自动排版，如何实现文本换行与省略号？
date: 2026-11-17
categories: [数据可视化]
tags: [前端面试, 面试题, 25]
type: 面试题
---

## VIZ-019：Canvas 没有自动排版，如何实现文本换行与省略号？
**答**：Canvas 的 fillText 是单行、无布局能力的，中文/英文混排都要自己写排版引擎：核心 API 是 `measureText(str).width`。**换行**：逐字符（中文）或逐单词（英文按空格切 token）累计宽度，超过 maxWidth 就断行；**省略**：超出 maxLines 时对最后一行从尾部删字符直到"内容 + …"不超宽；**对齐**：textAlign + 手动计算行高 lineHeight。优化：measureText 结果按字符串缓存，因为它是同步布局计算，高频调用会卡。

```javascript
// Canvas 无自动换行：基于 measureText 实现逐词换行 + 省略号
function wrapText(ctx, text, maxWidth, maxLines) {
  const lines = [];
  let line = '';
  for (const ch of text) { // 中文逐字断行；英文可先按空格切 token 再逐 token 累计
    const next = line + ch;
    if (ctx.measureText(next).width > maxWidth && line) {
      lines.push(line);
      line = ch;
      if (lines.length === maxLines) { // 达到行数上限：最后一行截断加省略号
        let last = lines[maxLines - 1];
        while (last && ctx.measureText(last + '…').width > maxWidth) last = last.slice(0, -1);
        lines[maxLines - 1] = last + '…';
        return lines;
      }
    } else {
      line = next;
    }
  }
  if (line) lines.push(line);
  return lines;
}
function drawWrapped(ctx, text, x, y, lineHeight) {
  wrapText(ctx, text, 200, 3).forEach((l, i) => ctx.fillText(l, x, y + i * lineHeight));
}
```
