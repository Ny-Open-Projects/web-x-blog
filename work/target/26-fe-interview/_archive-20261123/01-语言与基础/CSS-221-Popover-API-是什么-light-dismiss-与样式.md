---
title: [CSS-221] Popover API 是什么：light dismiss 与样式定制
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 组件]
type: 面试题
---

## CSS-221：Popover API 是什么：light dismiss 与样式定制

**答**：
- Popover API：原生弹层——`popover` 属性 + `popovertarget` 按钮，浏览器托管打开/关闭/焦点/层级（top layer，无 z-index 战争）
- light dismiss：点击弹层外部自动关闭（popover="auto"）；手动模式 manual 不自动关
- 伪类联动：`:popover-open` 选择打开态；`::backdrop` 自定义遮罩
- 与 dialog 的分工：popover 轻量（菜单、tooltip），dialog 模态（表单提交、重要确认）
- 配合动画：@starting-style + overlay 过渡实现出入场（见前几题）

```html
<button popovertarget="menu">设置</button>
<div id="menu" popover>…菜单项…</div>
```
```css
#menu { border: none; box-shadow: 0 4px 16px rgb(0 0 0 / .2); }
#menu:popover-open { transform: translateY(0); }
@starting-style { #menu:popover-open { transform: translateY(-8px); opacity: 0; } }
```
