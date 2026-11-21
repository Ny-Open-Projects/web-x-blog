---
title: [CSS-224] :has 的性能陷阱：为什么会有 layout 抖动
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-224：:has 的性能陷阱：为什么会有 layout 抖动

**答**：
- :has 是「向上/向后看」的选择器：子元素变化会引发祖先重新匹配——传统 CSS 的「样式计算自上而下」被打破
- 代价场景：`body:has(.modal-open)` 这类顶层 :has 会让任何 DOM 变化都触发全文档样式重算
- 隐性抖动：:has 内包含影响布局的属性（如改变 display/grid），内容更新 → 祖先重排 → 连锁
- 优化原则：:has 的范围尽量小（限定在组件内而非 body 级）；匹配目标是稳定结构；避免在滚动/输入等高频路径上的深层 :has
- 度量：DevTools Performance 的 Recalculate Style 时长对比开关 :has 前后

```css
/* 差：全文档监听 */
body:has(.modal.open) { overflow: hidden; }
/* 好：限定容器 */
.modal-root:has(.open) + .page { filter: blur(2px); }
```
