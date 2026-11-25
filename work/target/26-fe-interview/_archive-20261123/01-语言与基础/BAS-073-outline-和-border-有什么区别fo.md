---
title: [BAS-073] outline 和 border 有什么区别？focus-visible 是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-073：outline 和 border 有什么区别？focus-visible 是什么？
**答**：
- outline 画在边框外、不占布局空间、不能单边设置；border 参与盒模型占空间。
- :focus-visible 只在"键盘聚焦"（Tab 导航）时匹配，鼠标点击不匹配，解决了直接去 outline 后键盘可访问性丢失的问题。
- 自定义聚焦样式务必保留键盘焦点指示：`:focus-visible { outline: ... }`；全局 `outline: none` 是可访问性大忌。

```css
.btn:focus { outline: none; }            /* 不推荐：键盘用户失去焦点指示 */
.btn:focus-visible {
  outline: 2px solid #2563eb;
  outline-offset: 2px;                   /* outline 与元素间留缝隙 */
}
```
