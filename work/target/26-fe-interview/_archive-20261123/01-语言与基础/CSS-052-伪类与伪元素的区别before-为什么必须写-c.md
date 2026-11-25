---
title: [CSS-052] 伪类与伪元素的区别？::before 为什么必须写 content？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-052：伪类与伪元素的区别？::before 为什么必须写 content？

**答**：
- 伪类描述元素的**状态或位置**（:hover、:nth-child），单个冒号；伪元素创建**不存在的虚拟元素**（::before、::after、::placeholder），双冒号。
- ::before/::after 是真实生成在 DOM 内的盒子，不写 `content` 则整个伪元素不渲染。
- 经典应用：清除浮动伪元素、图标、字数统计 `content: attr(data-count)`。
- 伪元素不能被 JS 直接选中，只能通过改宿主类间接控制。

```css
/* 伪类：状态 */
.link:hover { color: #409eff; }
.item:nth-child(2n) { background: #fafafa; }

/* 伪元素：生成内容，content 必需 */
.tag::before {
  content: "#";           /* 缺了这行整个规则无效 */
  color: #999;
}
.badge::after {
  content: attr(data-count); /* 读取宿主属性 */
}

/* 用伪元素实现箭头 */
.arrow::after {
  content: "";
  display: inline-block;
  width: 6px;
  height: 6px;
  border-right: 1px solid #333;
  border-bottom: 1px solid #333;
  transform: rotate(-45deg);
}
```
