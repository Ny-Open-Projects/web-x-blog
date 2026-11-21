---
title: [CSS-219] transition-behavior: allow-discrete 让 display 可过渡
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-219：transition-behavior: allow-discrete 让 display 可过渡

**答**：
- display/content-visibility 等离散属性以前不能过渡（值一变元素立刻消失/出现）
- allow-discrete：离散属性也进入过渡时序——变化发生在过渡的「端点」（display 在过渡结束时才变 none）
- 组合配方：`transition: opacity .3s, display .3s allow-discrete` + @starting-style 起点样式 = 完整出入场动画
- 原理：display: none → block 的过渡中，浏览器保持「即将消失」的元素可渲染至过渡完成
- 解决的历史方案对比：visibility 延迟 hack、animationend 后 remove——现在一行声明

```css
.menu {
  display: none;
  opacity: 0;
  transition: opacity .25s, display .25s allow-discrete;
}
.menu.open { display: block; opacity: 1; }
@starting-style { .menu.open { opacity: 0; } } /* 打开时的入场起点 */
```
