---
title: [HW-351] 手写一个 Canvas 文本渲染与光标定位：字符宽度累计定位
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-351：手写一个 Canvas 文本渲染与光标定位：字符宽度累计定位

**答**：
- 需求：实现 CanvasText：measureText 逐字符宽度缓存；offsetAt(x)（点击位置 → 字符偏移：累计宽度比较）；posAt(offset)（偏移 → x 坐标）；光标渲染（竖线在字符边界）；中文宽度与英文混排正确。
- 边界：宽度缓存按字体失效（字体变化清缓存）；组合字符/emoji 按码簇处理（简化：按码点但跳过零宽连接）；换行渲染时按行分别定位。
- 评分点：逐字符累计定位；宽度缓存；码簇意识。

```javascript
class CanvasText {
  constructor(ctx, { font = '14px sans-serif' } = {}) { this.ctx = ctx; this.font = font;
    this.cache = new Map(); }
  setFont(f) { if (f !== this.font) { this.font = f; this.cache.clear(); }   // 字体失效缓存
    this.ctx.font = f; }
  charW(ch) {
    if (!this.cache.has(ch)) this.cache.set(ch, this.ctx.measureText(ch).width);
    return this.cache.get(ch);
  }
  offsetAt(text, x) {                                      // 点击 → 偏移
    let acc = 0;
    const chars = [...text];                               // 码点迭代（emoji 安全）
    for (let i = 0; i < chars.length; i++) {
      const w = this.charW(chars[i]);
      if (x < acc + w / 2) return i;                       // 过半归右
      acc += w;
    }
    return chars.length;
  }
  posAt(text, offset) {                                    // 偏移 → x
    let acc = 0;
    for (const ch of [...text].slice(0, offset)) acc += this.charW(ch);
    return acc;
  }
  drawCursor(text, offset, x0, y, lineH) {                 // 光标竖线
    const x = x0 + this.posAt(text, offset);
    this.ctx.fillRect(x, y, 1.5, lineH);
  }
}
```
