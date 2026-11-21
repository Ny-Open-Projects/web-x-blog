---
title: [CSS-321] 笔试：CSS 数字滚动计数（counter + @property）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-321：笔试：CSS 数字滚动计数

**题目**：纯 CSS 实现数字从 0 滚动到 78（无 JS 计时器）：用 @property 注册数值型自定义属性 + counter + content。

**答**：
```css
/* ① 注册数值型变量（可插值是关键） */
@property --n {
  syntax: '<integer>';
  initial-value: 0;
  inherits: false;
}
.counter::after {
  counter-reset: n var(--n);
  content: counter(n);
}
/* ② 动画驱动变量 */
.counting::after {
  animation: count 2s ease-out forwards;
}
@keyframes count { to { --n: 78; } }

/* ③ 千分位格式化（扩展） */
@counter-style thousands {
  system: extends decimal;
  /* 复杂格式化仍建议 JS；此处展示能力边界 */
}
```
```html
<span class="counter counting"></span> <!-- 显示 0→78 的滚动数字 -->
```
```css
/* 补充：整数仅限 integer；需要小数用 <number> 并接受 counter 不支持小数点
   的局限（整数递增是 counter 语义） */
@property --n2 { syntax: '<number>'; initial-value: 0; inherits: false; }
```

**评分点**：
- @property syntax: <integer> 让数值可插值——核心机制
- counter-reset 接收 var + content: counter() 的组合
- forwards 保持终值；ease-out 模拟「先快后慢」
- 知道局限：counter 只支持整数，小数/千分位需 JS 或接受截断
