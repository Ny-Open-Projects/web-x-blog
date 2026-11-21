---
title: [CSS-290] font-display 各值差异：swap/block/fallback/optional
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 排版]
type: 面试题
---

## CSS-290：font-display 各值差异：swap/block/fallback/optional

**答**：
- block：阻塞期（约 3s）用隐形字占位，字体到了换——「白闪」FOIT
- swap：立即用回退字体显示，字体到了换——FOUT 闪动但内容可读（正文推荐）
- fallback：极短阻塞（100ms）→ 回退字体 → 2 周期内可切换——平衡型
- optional：极短阻塞后若字体没到就用回退且**本轮不换**（浏览器自行决定，下次访问可能用上）——零闪动，适合非关键字体
- 选择策略：正文 swap（可读性优先）、品牌标题 block 短阻塞或 optional（体验优先）、图标字体 block（缺失会乱码）

```css
@font-face {
  font-family: Brand;
  src: url('brand.woff2') format('woff2');
  font-display: swap;
}
@font-face {
  font-family: Icons;
  src: url('icons.woff2') format('woff2');
  font-display: block; /* 图标缺失显示空白比乱字符好 */
}
```
