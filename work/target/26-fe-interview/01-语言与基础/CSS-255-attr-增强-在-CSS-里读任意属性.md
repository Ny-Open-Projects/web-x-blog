---
title: [CSS-255] attr() 增强：在 CSS 里读任意属性
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 新特性]
type: 面试题
---

## CSS-255：attr() 增强：在 CSS 里读任意属性

**答**：
- 老 attr()：只能在 content 里读字符串；新规范（Chrome 133+）：attr(名 类型, 默认值) 可读任意属性并转类型
- 能力：`width: attr(data-w px, 100px)`——HTML 属性直接驱动样式，无需 CSS 变量传递
- 与 data-* 的分工：data 属性做「数据挂载点」，attr() 做读取——进度条、徽标数字、网格列数都能 HTML 驱动
- 与 CSS 变量的关系：变量是 CSS 内部流转，attr 是 HTML→CSS 桥；两者互补
- 兼容：极新（2025 标准），生产慎用、渐进增强；类型不符时回退默认值

```css
.badge::after {
  content: attr(data-count number, 0);      /* 数字徽标 */
}
.grid {
  grid-template-columns: repeat(attr(data-cols integer, 3), 1fr);
}
.bar {
  width: attr(data-progress %, 0%);          /* 进度条宽度 HTML 驱动 */
}
```
