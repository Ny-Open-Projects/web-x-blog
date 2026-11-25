---
title: [CSS-305] 笔试：纯 CSS 深浅主题切换（checkbox + :has）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 主题]
type: 笔试题
---

## CSS-305：笔试：纯 CSS 深浅主题切换

**题目**：无 JS 实现主题切换：页面顶部 checkbox 开关，勾选后全站变量切换为暗色；开关自身也要变样式；用 :has 让祖先级响应。

**答**：
```css
/* 变量定义：默认亮色 */
:root {
  --bg: #fff; --fg: #222; --muted: #666;
}
/* :has 让 body 级响应 checkbox 状态（checkbox 放 body 直下） */
body:has(#theme:checked) {
  --bg: #121212; --fg: #eee; --muted: #999;
}
body {
  background: var(--bg); color: var(--fg);
  transition: background .3s, color .3s;
}

/* 开关样式：轨道 + 滑块 */
.switch {
  position: relative; display: inline-block;
  width: 44px; height: 24px;
}
.switch input { opacity: 0; width: 100%; height: 100%; margin: 0; cursor: pointer; }
.switch::before {
  content: ''; position: absolute; inset: 0;
  border-radius: 12px; background: #ccc;
  transition: background .3s;
}
.switch::after {
  content: ''; position: absolute;
  top: 3px; left: 3px;
  width: 18px; height: 18px; border-radius: 50%;
  background: #fff; transition: transform .3s;
}
.switch:has(input:checked)::before { background: #4285f4; }
.switch:has(input:checked)::after { transform: translateX(20px); }
```
```html
<label class="switch"><input type="checkbox" id="theme"></label>
```

**评分点**：
- :has(#theme:checked) 挂在祖先（body）实现全局响应——:has 的正确用法展示
- 变量切换而非样式复制，transition 在变量消费端生效
- 开关的 ::before/::after 联动（:has(input:checked)）
- 知道局限：checkbox 状态不持久（刷新还原），生产需 localStorage + JS 或 Cookie（能说出来加分）
