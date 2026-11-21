---
title: [CSS-160] 纯 CSS 实现 iOS 风格开关 Switch 的完整思路？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 笔试题, 03]
type: 笔试题
---

## CSS-160：纯 CSS 实现 iOS 风格开关 Switch 的完整思路？

**答**：
- 结构：隐藏的 checkbox 提供状态 + label 提供点击区域 + 轨道/滑块用 span 绘制。
- 状态驱动：`:checked + .track` 变色，`:checked + .track .thumb` 位移，transition 补间。
- 隐藏 input 必须保留可聚焦性（opacity: 0 而非 display: none），配 `:focus-visible` 外圈保证键盘可达。
- 滑块位移量 = 轨道宽 − 滑块宽 − 2 × margin，写死数值即可；触屏无需 JS。

```html
<label class="switch">
  <input type="checkbox">
  <span class="track"><span class="thumb"></span></span>
</label>
<style>
  .switch { display: inline-flex; cursor: pointer; }
  .switch input {
    position: absolute;     /* 视觉隐藏但保留可聚焦 */
    opacity: 0;
    width: 0; height: 0;
  }
  .track {
    display: block;
    width: 48px; height: 28px;
    border-radius: 14px;
    background: #ddd;
    transition: background .2s;
  }
  .thumb {
    display: block;
    width: 24px; height: 24px;
    margin: 2px;
    border-radius: 50%;
    background: #fff;
    box-shadow: 0 1px 3px rgba(0,0,0,.3);
    transition: transform .2s;
  }
  .switch input:checked + .track { background: #4cd964; }
  .switch input:checked + .track .thumb { transform: translateX(20px); }
  .switch input:focus-visible + .track {
    outline: 2px solid #096;
    outline-offset: 2px;
  }
</style>
```
