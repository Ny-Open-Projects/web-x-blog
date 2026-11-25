---
title: [CSS-101] 文字描边与 text-shadow 高级效果怎么实现？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-101：文字描边与 text-shadow 高级效果怎么实现？

**答**：
- `-webkit-text-stroke` 描边宽度沿字形居中分布，会"吃掉"字重，细描边配大字号使用。
- 纯 text-shadow 多向偏移叠加可模拟描边（8 方向 1px），不侵蚀字形但代码冗长。
- 空心字：`-webkit-text-fill-color: transparent` + stroke，或 background-clip: text。
- 发光、立体、长投影都是 text-shadow 多层堆叠的应用。
- `paint-order: stroke fill` 可让描边画在填充之下（SVG/部分浏览器支持），恢复完整字重。

```css
/* 空心描边大字 */
.outline-text {
  font-size: clamp(3rem, 10vw, 6rem);
  font-weight: 800;
  -webkit-text-stroke: 1.5px var(--brand);
  -webkit-text-fill-color: transparent;
}

/* 描边画在填充外，不侵蚀字重（支持的浏览器） */
.painted-stroke {
  -webkit-text-stroke: 6px var(--brand);
  paint-order: stroke fill;
  color: #fff;
}

/* 长投影：多层同向递进 */
.long-shadow {
  text-shadow:
    1px 1px 0 var(--brand-dark), 2px 2px 0 var(--brand-dark),
    3px 3px 0 var(--brand-dark), 4px 4px 0 var(--brand-dark),
    5px 5px 0 var(--brand-dark);
}
```

## 十八、组件样式模式
