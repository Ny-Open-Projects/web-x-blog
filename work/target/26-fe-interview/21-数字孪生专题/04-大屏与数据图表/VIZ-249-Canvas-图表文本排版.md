---
title: [VIZ-249] Canvas 图表文本排版：自动换行与省略号
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-249：Canvas 图表文本排版：自动换行与省略号

**答**：
- 题目：图表标签文本空间受限——实现「按容器宽自动换行 + 超行省略号」的 canvas 文本排版（measureText 逐词）。
- 思路：按词切分（中文按字符）逐词测量累加；超宽换行；行数超限截断加 …（最后一词裁剪到 fit）。
- 评分点：逐词测量；换行边界；省略号的测量回退。

```javascript
function wrapCanvasText(ctx, text, maxWidth, maxLines) {
  const chars = [...text];                                 // 中文按字符
  const lines = [];
  let cur = '';
  for (const c of chars) {
    if (ctx.measureText(cur + c).width > maxWidth && cur) {   // 超宽换行
      lines.push(cur); cur = c;
      if (lines.length === maxLines) {                     // 行数超限：省略
        let last = lines[maxLines - 1];
        while (ctx.measureText(last + '…').width > maxWidth) last = last.slice(0, -1);
        lines[maxLines - 1] = last + '…';
        return { lines: lines.slice(0, maxLines), truncated: true };
      }
    } else cur += c;
  }
  if (cur) lines.push(cur);
  return { lines, truncated: false };
}
// 绘制：lines.forEach((line, i) => ctx.fillText(line, x, y + i * lineHeight))
```
