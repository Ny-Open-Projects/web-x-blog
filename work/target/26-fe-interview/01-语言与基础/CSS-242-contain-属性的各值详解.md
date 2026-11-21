---
title: [CSS-242] contain 属性的各值详解：layout-style-paint-strict
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-242：contain 属性的各值详解

**答**：
- contain 声明「元素内部变化不影响外部」，让浏览器缩小重算范围：
  - layout：内部布局变化不外溢（外部不因内部重排）
  - paint：子元素不画出元素边界（相当于剪切）
  - size：元素尺寸与内容无关（需显式宽高，慎用）
  - style：计数器等样式影响不外溢
  - strict = layout+paint；content = layout+paint+style
- 与 content-visibility 的关系：cv: auto 隐含 strict containment + 视口裁剪调度
- 实用场景：第三方组件外壳（防其内部重排影响整页）、弹层容器、图表容器
- 代价：size containment 会改变尺寸行为，务必理解后再用

```css
.widget-iframe-like {
  contain: content;          /* 内部变化被隔离 */
}
.chart {
  contain: layout paint;     /* 明确声明两个维度 */
}
```
