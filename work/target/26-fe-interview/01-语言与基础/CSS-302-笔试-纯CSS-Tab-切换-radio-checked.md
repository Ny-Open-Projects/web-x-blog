---
title: [CSS-302] 笔试：纯 CSS Tab 切换（radio + :checked）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 组件]
type: 笔试题
---

## CSS-302：笔试：纯 CSS Tab 切换

**题目**：无 JS 实现 Tab：radio 单选 + :checked + 兄弟选择器联动面板；含滑块动画的指示条；保留键盘导航（方向键原生可用）。

**答**：
```css
.tabs { position: relative; }
.tabs input { position: absolute; opacity: 0; pointer-events: none; }

.tab-label {
  display: inline-block; padding: 10px 20px;
  color: #666; cursor: pointer;
}
/* 选中态：label 与 radio 同父 + id 关联 */
#t1:checked ~ nav [for='t1'],
#t2:checked ~ nav [for='t2'],
#t3:checked ~ nav [for='t3'] { color: #4285f4; font-weight: 600; }

/* 面板显隐 */
.panel { display: none; padding: 16px; }
#t1:checked ~ .panel-1,
#t2:checked ~ .panel-2,
#t3:checked ~ .panel-3 { display: block; animation: fade-in .25s; }
@keyframes fade-in { from { opacity: 0; } }

/* 滑块指示条：跟随选中的 label 平移 */
.slider {
  position: absolute; bottom: 0; left: 0;
  width: 33.33%; height: 2px; background: #4285f4;
  transition: transform .3s;
}
#t2:checked ~ .slider { transform: translateX(100%); }
#t3:checked ~ .slider { transform: translateX(200%); }
```
```html
<div class="tabs">
  <input type="radio" name="tab" id="t1" checked>
  <input type="radio" name="tab" id="t2">
  <input type="radio" name="tab" id="t3">
  <nav>
    <label for="t1">A</label><label for="t2">B</label><label for="t3">C</label>
  </nav>
  <i class="slider"></i>
  <section class="panel panel-1">A 内容</section>
  <section class="panel panel-2">B 内容</section>
  <section class="panel panel-3">C 内容</section>
</div>
```

**评分点**：
- radio 同名互斥 + :checked + 通用兄弟选择器（~）联动——核心结构
- input 藏起来但保留键盘操作（不 display:none 出 DOM，用视觉隐藏）
- 滑块百分比位移（与 label 宽度等分对齐）
- 面板切换动画挂载在「被选中的那一刻」
