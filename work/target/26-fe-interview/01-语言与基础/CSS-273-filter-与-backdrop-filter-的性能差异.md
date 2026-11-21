---
title: [CSS-273] filter 与 backdrop-filter 的性能差异
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-273：filter 与 backdrop-filter 的性能差异

**答**：
- filter：处理元素自身渲染结果（blur/brightness/grayscale…）；backdrop-filter：处理「元素背后已渲染的内容」——后者必须读取下层像素，成本高得多
- backdrop-filter 代价：强制合成 + 背后区域重绘联动；大面积或滚动区域使用是移动端卡顿重灾区
- 优化策略：玻璃拟态限小面积（导航栏而非整页）；模糊半径适度（blur(8px) 与 20px 成本差距明显）；低端机用 @media 降级为半透明纯色
- filter 自身也贵：blur 值大时同样掉帧；grayscale/sepia 比 blur 便宜（像素级独立）
- 排查：Layers 面板看强制合成的层大小；帧率对比开关效果

```css
.navbar { backdrop-filter: blur(8px); background: rgb(255 255 255 / .7); }
@media (max-resolution: 2dppx) and (prefers-reduced-motion: no-preference) { /* 低端机简化 */
  .navbar { backdrop-filter: none; background: rgb(255 255 255 / .95); }
}
```
