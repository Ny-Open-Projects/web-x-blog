---
title: [CSS-254] font-size-adjust 是什么：字体回退的字号对齐
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 排版]
type: 面试题
---

## CSS-254：font-size-adjust：字体回退的字号对齐

**答**：
- 问题：主字体未加载时回退字体 x-height 不同——同 font-size 视觉大小突变（字体闪动更难看）
- font-size-adjust: ex-height 比例：告诉浏览器「按 x-height 匹配」调整回退字体的实际渲染大小
- 用法：`font-size-adjust: 0.5;`（主字体的 ex-height / font-size 比）；或双值 `from-font` 自动取主字体
- 实战价值：自定义中文/西文混排时（两个 font-family），统一视觉高度；web font 加载期 FOUT 减轻
- 兼容：Chrome 127+/Safari 16+/Firefox 早已支持；是「文字稳定性」的低调但有效的属性

```css
.text {
  font-family: 'BrandSans', 'PingFang SC', sans-serif;
  font-size-adjust: 0.52;      /* BrandSans 的 ex-height 比率 */
}
```
