---
title: [CSS-303] 笔试：纯 CSS tooltip（无 JS）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 组件]
type: 笔试题
---

## CSS-303：笔试：纯 CSS tooltip

**题目**：实现无 JS tooltip：hover/focus 都显示（键盘可达）、带小箭头、出现在上方且空间不足时向下翻转（:has 或纯定位方案）、淡入淡出动画。

**答**：
```css
.tip-wrap { position: relative; display: inline-block; }
.tip {
  position: absolute;
  bottom: calc(100% + 8px); left: 50%;
  transform: translateX(-50%) translateY(4px);
  padding: 6px 10px; border-radius: 6px;
  background: #333; color: #fff; font-size: 12px;
  white-space: nowrap;
  opacity: 0; visibility: hidden;
  transition: opacity .2s, transform .2s, visibility .2s;
  pointer-events: none;
}
/* 箭头 */
.tip::after {
  content: ''; position: absolute;
  top: 100%; left: 50%;
  transform: translateX(-50%);
  border: 5px solid transparent;
  border-top-color: #333;
}
/* hover 与 focus-visible 都触发（键盘可达） */
.tip-wrap:hover .tip,
.tip-wrap:focus-within .tip {
  opacity: 1; visibility: visible;
  transform: translateX(-50%) translateY(0);
}

/* 触发按钮需要可聚焦（如 button 或 tabindex=0） */
.tip-btn:focus { outline: none; }
.tip-btn:focus-visible { outline: 2px solid #4285f4; }
```
```html
<span class="tip-wrap">
  <button class="tip-btn" aria-describedby="tip-1">帮助</button>
  <span class="tip" id="tip-1" role="tooltip">这是提示文字</span>
</span>
```

**评分点**：
- hover + focus-within 双触发（键盘用户能看到）
- visibility 参与过渡（延迟隐藏防 hover 穿隙）
- 箭头用 ::after border 三角
- aria-describedby / role=tooltip 的语义补全（无 JS 不等于无语义）
