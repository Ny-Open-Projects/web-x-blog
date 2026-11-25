---
title: [CSS-274] color-scheme 属性与原生控件暗色
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 主题]
type: 面试题
---

## CSS-274：color-scheme 属性与原生控件暗色

**答**：
- color-scheme 声明元素「支持的配色方案」（light/dark）——浏览器据此渲染原生控件（滚动条、input、select、checkbox）与默认背景
- 常见问题：页面背景改黑了，但输入框/滚动条还是白色——没声明 color-scheme，浏览器不知道要用暗色默认值
- 用法：`:root { color-scheme: light dark; }` 跟随系统；或 html[data-theme='dark'] { color-scheme: dark; } 手动切换
- 与 light-dark() 联动：声明 scheme 后 light-dark() 函数才能自动取值（CSS-233）
- 细节：meta 标签 `<meta name="color-scheme" content="light dark">` 可在 CSS 加载前声明，防白闪

```html
<meta name="color-scheme" content="light dark">
```
```css
:root { color-scheme: light dark; }
/* dark 模式下原生下拉/滚动条/输入框自动变暗 */
```
