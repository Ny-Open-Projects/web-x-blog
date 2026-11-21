---
title: [CSS-326] 笔试：CSS 隐藏元素的 N 种方式及差异
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 基础]
type: 笔试题
---

## CSS-326：笔试：CSS 隐藏元素的 N 种方式及差异

**题目**：列举至少 5 种隐藏元素的方式，说明各自对布局、交互、无障碍、过渡动画的影响，并给出「隐藏表单但保留其值提交」「动画后隐藏」两个场景的最佳选择。

**答**：
```css
/* 1. display: none —— 完全移除（不占布局、不响应事件、读屏不可见、不可过渡） */
.hide-a { display: none; }

/* 2. visibility: hidden —— 占布局、不响应事件、读屏不可见、可过渡 */
.hide-b { visibility: hidden; }

/* 3. opacity: 0 —— 占布局、仍响应事件（可点击！）、读屏可见、可过渡 */
.hide-c { opacity: 0; pointer-events: none; } /* 要禁止交互需加 pointer-events */

/* 4. 移出视口 —— 占布局、读屏可见（用于装饰性隐藏或 accessibility） */
.hide-d { position: absolute; left: -9999px; }

/* 5. clip 完全裁剪（现代 SR-only 推荐） */
.sr-only {
  position: absolute; width: 1px; height: 1px;
  padding: 0; margin: -1px; overflow: hidden;
  clip-path: inset(50%); white-space: nowrap; border: 0;
}

/* 6. content-visibility: hidden —— 占布局、跳过渲染、内容仍可访问（新） */
.hide-f { content-visibility: hidden; }
```
```css
/* 场景答案 */
/* 隐藏表单但值仍提交：visibility 或 sr-only，绝不能 display:none（值不提交） */
input.keep-value { visibility: hidden; }
/* 动画后隐藏：transition + display allow-discrete（见 CSS-219） */
.el { transition: opacity .3s, display .3s allow-discrete; }
.el.hidden { opacity: 0; display: none; }
```

**评分点**：
- 五种以上方式与「布局/交互/读屏/过渡」四维差异表
- opacity: 0 仍可点击的陷阱（需 pointer-events 配合）——高频失分点
- 表单值提交：display: none 的字段不提交，visibility 保留
- sr-only 的现代写法（clip-path: inset(50%)）
