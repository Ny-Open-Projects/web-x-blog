---
title: [CSS-267] z-index 失效的常见原因清单
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 布局]
type: 面试题
---

## CSS-267：z-index 失效的常见原因清单

**答**：
- 原因一：元素未定位（static）——z-index 只作用于定位元素、flex/grid 子项、top layer 成员
- 原因二：父容器创建层叠上下文（transform/opacity<1/filter/will-change/isolation），z-index 被「困」在里面，对外比较的是父容器层级
- 原因三：与 top layer 冲突——dialog/popover 永远在普通 z-index 之上
- 原因四：负 z-index 被父容器背景遮挡（父容器有背景时负值子元素不可见）
- 排查方法：DevTools Layers 面板看实际合成层；从「向上找最近创建层叠上下文的祖先」逐层检查

```css
.parent { transform: translateZ(0); }        /* 创建上下文 */
.child { z-index: 9999; }                     /* 只在 parent 内部有效 */
/* 修复：提升 parent 的 z-index，或移除 parent 的上下文触发属性 */
```
