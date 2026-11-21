---
title: [CSS-241] content-visibility: auto：长列表渲染优化
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-241：content-visibility: auto：长列表渲染优化

**答**：
- 作用：视口外的子树跳过渲染（布局/绘制都省），接近视口时自动渲染——长页面渲染成本大幅下降
- 必须搭配 contain-intrinsic-size（声明占位尺寸），否则滚动条跳动、锚点定位错乱
- 与虚拟列表的分工：content-visibility 零 JS 改造成本，适合「大量但不极长」列表；性能极限（上万节点+复杂交互）仍推荐虚拟滚动
- 注意事项：视口内查找（Ctrl+F、锚点跳转）受影响（浏览器已优化部分场景）；屏幕阅读器行为需验证
- 附带收益：初次渲染时间显著缩短（首屏外不排版）

```css
.feed-item {
  content-visibility: auto;
  contain-intrinsic-size: auto 300px; /* 近似高度，渲染后自动修正 */
}
```
