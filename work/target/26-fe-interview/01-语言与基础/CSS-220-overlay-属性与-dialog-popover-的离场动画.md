---
title: [CSS-220] overlay 属性与 dialog/popover 的离场动画
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-220：overlay 属性与 dialog/popover 的离场动画

**答**：
- dialog/popover 关闭时元素立即从 top layer 移除——离场动画没机会播放
- overlay 属性：元素是否在 top layer；把它加入 transition（`transition: overlay .3s allow-discrete`）后，移除延迟到过渡完成
- 完整配方：dialog 或 popover 的 opacity/transform 过渡 + overlay allow-discrete + @starting-style 入场
- 效果：`dialog.close()` 后淡出动画播完才真正消失——以前要 JS setTimeout 才能做到
- 附带：::backdrop 也能过渡（背景遮罩淡入淡出），一并加入 transition 列表

```css
dialog {
  opacity: 1; transform: none;
  transition: opacity .3s, transform .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}
dialog[open]::backdrop {
  background: rgb(0 0 0 / .4);
  transition: opacity .3s;
}
@starting-style {
  dialog[open] { opacity: 0; transform: translateY(20px); }
}
dialog:not([open]) { opacity: 0; transform: translateY(20px); }
```
