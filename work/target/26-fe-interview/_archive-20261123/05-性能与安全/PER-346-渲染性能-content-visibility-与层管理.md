---
title: [PER-346] content-visibility 如何跳过屏外渲染成本？合成层爆炸怎么治理？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-346：content-visibility 如何跳过屏外渲染成本？合成层爆炸怎么治理？

**答**：
- content-visibility: auto：浏览器跳过**视口外子树**的 style/layout/paint，进入视口再渲染（配合 contain-intrinsic-size 给占位高度防滚动条跳动）。长页面/长列表/长表单收益巨大——一万个卡片只渲染可视区的几十个。兼容 Chrome 85+/新版 Edge/Safari 18+；Firefox 125+ 支持。
- 与虚拟列表的取舍：content-visibility 零代码侵入（CSS 一行），适合"普通长页"；虚拟列表适合"超大数据量 + 需要精确控制 DOM 数量"的场景。两者可叠加。
- 合成层爆炸：滥用 will-change/transform: translateZ(0)/3D 转换会让每个元素独占一个合成层——内存（每层一张位图）与合成成本暴涨。治理：Layers 面板检查层数量与内存；will-change 只加在"动画进行中"的元素（动画结束移除）；把提升层收敛到滚动容器级别而不是每个卡片。
- contain 属性家族：contain: layout/paint 限制子树影响范围，与 content-visibility 配合使用（auto 内置 contain）。

```css
/* 长列表零改造跳过屏外渲染 */
.card {
  content-visibility: auto;
  contain-intrinsic-size: auto 320px;   /* 占位高度：未渲染时按 320px 占，渲染后取实际值 */
}
/* 反例：给所有卡片加 will-change —— 层爆炸 */
/* .card { will-change: transform; }  */
/* 正确：动画进行时才提升 */
.card:hover { will-change: transform; }   /* 或用 JS 在 transitionstart/end 增删 */
```
