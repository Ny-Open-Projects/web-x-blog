---
title: [CSS-332] 层叠上下文与绘制顺序：paint order 全规则
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 渲染管线]
type: 面试题
---

## CSS-332：层叠上下文与绘制顺序：paint order 全规则

**答**：
- 同一层叠上下文内的绘制顺序（CSS 2.1 §E）：背景/边框 → 负 z-index 子上下文 → 块级后代 → 浮动 → 内联内容 → z-index:auto/0 与定位元素 → 正 z-index——理解这个顺序能解释大多数「为什么盖不住」
- 层叠上下文创建清单（高频）：根元素、z-index 非 auto 的定位元素、opacity<1、transform/filter/perspective 非 none、isolation: isolate、will-change 指定这些属性、contain: paint、fixed（部分移动内核）
- 关键推论：opacity 0.99 会创建上下文，子元素 z-index 再大也只在父上下文内比较——「z-index 失效」九成是意外创建了上下文
- z-index 比较只在同一上下文内：父 A(z-index:1) 与父 B(z-index:2) 之下，A 的 z-index:9999 子元素仍被 B 盖住
- 调试：DevTools Layers 面板可视化层叠树；审查意外上下文用「逐个删 transform/opacity」二分法

```css
/* 意外上下文经典案例 */
.modal { position: absolute; opacity: 0; transition: opacity .3s; }
.modal.show { opacity: 1; }
/* 过渡期间 opacity<1 → 创建上下文; 若 modal 内 dropdown 的 z-index
   依赖与页面其他元素比较, 过渡瞬间层级错乱 → 加 isolation 控制边界 */
.modal { isolation: isolate; }
```
