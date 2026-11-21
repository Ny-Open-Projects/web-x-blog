---
title: [CSS-287] CSS 变量在 SVG 里的运用：主题化图标
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 主题]
type: 面试题
---

## CSS-287：CSS 变量在 SVG 里的运用：主题化图标

**答**：
- 内联 SVG 的 fill/stroke 可写 var(--icon-color)——图标颜色跟随主题/交互状态自动变化
- 外链 SVG 的限制：`<img src="a.svg">` 里的变量读不到页面 CSS——要么内联、要么用 SVG `<use>`（同文档 shadow）+ CSS Custom Properties（继承穿透 shadow）
- currentColor 快捷方式：SVG 内 fill="currentColor"，图标继承文字颜色——最简单可靠的主题化
- 深浅主题联动：变量切换一处改全站图标；交互态（hover 换色）也是变量级
- 面试钩子：区分「内联 SVG / use 引用 / img 外链」三种方式的变量作用域差异

```html
<!-- use 引用 + currentColor -->
<svg style="display:none">
  <symbol id="i-star"><path fill="currentColor" d="…"/></symbol>
</svg>
<svg class="icon"><use href="#i-star"/></svg>
```
```css
.icon { color: var(--icon, #666); }         /* use 引用可继承 */
.icon:hover { color: var(--brand); }
```
