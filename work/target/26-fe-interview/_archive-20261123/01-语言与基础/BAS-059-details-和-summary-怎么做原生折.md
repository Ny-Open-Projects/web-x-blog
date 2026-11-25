---
title: [BAS-059] details 和 summary 怎么做原生折叠面板？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-059：details 和 summary 怎么做原生折叠面板？
**答**：
- details 默认折叠，summary 是标题；点击 summary 切换 open 属性，无需任何 JS。
- 可用 `details[open]` 选择器做展开样式，监听 toggle 事件感知展开收起；多个 details 设相同 name 属性可互斥展开（手风琴）。
- 局限：展开动画控制弱，复杂交互仍需 JS。

```html
<details name="faq">
  <summary>什么是闭包？</summary>
  <p>函数与其词法作用域的组合……</p>
</details>
<details name="faq">
  <summary>什么是原型链？</summary>
  <p>对象通过原型逐级连接……</p>
</details>
<script>
  document.querySelectorAll('details').forEach(d =>
    d.addEventListener('toggle', () => console.log(d.open)));
</script>
```
