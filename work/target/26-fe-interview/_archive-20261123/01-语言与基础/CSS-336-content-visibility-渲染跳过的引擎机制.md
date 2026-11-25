---
title: [CSS-336] content-visibility：渲染跳过的引擎机制与坑
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-336：content-visibility：渲染跳过的引擎机制与坑

**答**：
- 机制：content-visibility: auto 让视口外子树跳过 layout/paint（contain-intrinsic-size 提供占位尺寸），进入视口才真实渲染——长列表/长页面首屏渲染成本大幅下降
- 与虚拟列表对比：content-visibility 不动 DOM（全部挂载），省的是渲染管线的活；DOM/内存成本仍在——万级节点还是要虚拟化，几十到几百节点用 content-visibility 最省事
- 关键配置：必须配 contain-intrinsic-size（估算尺寸），否则滚动条长度随滚动剧烈跳动（跳过时用占位高度，渲染后换真实高度）
- 副作用：页内锚点跳转/scrollIntoView 到跳过区域会先触发渲染（有一帧延迟）；查找（Ctrl+F）、无障碍树访问也会触发渲染
- 生效前提：元素要有尺寸约束（或占位尺寸），配合 containment；对 flex/grid 子项同样适用

```css
.feed-item {
  content-visibility: auto;
  contain-intrinsic-size: auto 320px;  /* auto: 渲染后记住真实高度, 更准 */
}
/* 效果: 500 条列表首屏只渲染 ~10 条, 首屏渲染时间下降 80%+ */
```
