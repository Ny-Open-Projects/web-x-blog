---
title: [CSS-245] :focus-visible 与 :focus 的区别：可访问性
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 可访问性]
type: 面试题
---

## CSS-245：:focus-visible 与 :focus 的区别

**答**：
- :focus：一切聚焦都匹配（鼠标点击也算）——鼠标用户讨厌点击按钮后出现的焦点环
- :focus-visible：浏览器判断「用户大概率需要焦点指示」（键盘导航、输入类聚焦）才匹配——键盘可达性与视觉干净的兼得
- 标准写法：`button:focus-visible { outline: 2px solid #4285f4; }`——不要再用 `.js-focus-visible` 类 hack 或全局 outline:none
- 输入框例外：input 任何时候聚焦都应显示指示（用户在输入），直接用 :focus 即可
- 面试话术：这是「无障碍 + 体验」双修的代表 API，答出浏览器启发式判断逻辑是加分项

```css
button:focus { outline: none; }              /* ❌ 移除所有指示，键盘用户迷失 */
button:focus-visible { outline: 2px solid #4285f4; outline-offset: 2px; } /* ✅ */
input:focus { outline: 2px solid #4285f4; }  /* 输入类始终显示 */
```
