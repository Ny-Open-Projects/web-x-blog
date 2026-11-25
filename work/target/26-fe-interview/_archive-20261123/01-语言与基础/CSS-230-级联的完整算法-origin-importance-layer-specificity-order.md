---
title: [CSS-230] 级联的完整算法：origin-importance-layers-specificity-order
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 基础]
type: 面试题
---

## CSS-230：级联的完整算法：origin→importance→layers→specificity→order

**答**：
- 级联五步（依次比较，先赢者定胜负）：
  1. Origin：作者样式 > 用户样式 > UA 默认（!important 时反转：UA important 最高）
  2. Importance：!important 段单独排（且层序反转）
  3. Layers：分层规则（后层赢）
  4. Specificity：权重 a-b-c（ID-类-元素）
  5. Order：同权重取后者
- 常见误解纠正：specificity 不是第一裁决者，只是第四位；层比权重更「宏观」
- 记忆钩子：「先问是谁的、再问重不重要、再问哪一层、才轮到权重」
- 面试价值：能完整背出五步并举例的候选人极少，值得花时间记

```css
/* 演示：层压过权重 */
@layer l1, l2;
@layer l1 { #id .a { color: red; } }    /* 权重很高 */
@layer l2 { span { color: blue; } }      /* 权重很低 */
/* <span id class="a"> → blue：层序先于权重 */
```
