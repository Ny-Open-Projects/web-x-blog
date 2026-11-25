---
title: [CSS-204] Houdini 是什么，解决什么问题
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, Houdini]
type: 面试题
---

## CSS-204：Houdini 是什么，解决什么问题

**答**：
- Houdini 是一组「把 CSS 内部管线暴露给 JS」的 API 集：允许开发者写自己的绘制/布局/属性逻辑，接进浏览器渲染流程
- 解决的问题：以前想扩展 CSS 只能等标准（如新单位、新布局），Houdini 让「新特性以 polyfill 形式存在」——Parser API 解析、Paint API 自绘、Layout API 自定义布局、Properties & Values 注册类型化属性
- 核心价值：CSS 的可编程化——动画渐变、瀑布流、自定义单位都能自己造
- 现状（2026）：Paint API 与 @property 兼容最好可生产用；Layout API 仅 Chromium；Parser API 胎死腹中
- 面试话术：Houdini = 「CSS 的 WebAssembly 时刻」，把渲染管线打开给开发者

```css
/* Paint API 用法：worklet 注册后像普通 background 一样用 */
.card { background: paint(confetti); }
@property --angle { syntax: '<angle>'; initial-value: 0deg; inherits: false; }
```
