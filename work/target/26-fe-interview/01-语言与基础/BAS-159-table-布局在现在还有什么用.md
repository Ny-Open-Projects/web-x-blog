---
title: [BAS-159] table 布局在现在还有什么用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-159：table 布局在现在还有什么用？
**答**：
- 真正的数据表格（语义正确）仍是 table 的本职；配合 `table-layout: fixed` 让列宽稳定、渲染更快。
- display: table/table-cell 在老兼容场景可以低成本实现等高列和垂直居中（现代首选 grid/flex）。
- 面试定位：知道它是历史方案之一，能说清什么时候别再滥用它做布局。

```css
/* 老兼容场景：等高列 + 垂直居中 */
.form { display: table; }
.row { display: table-row; }
.label, .field {
  display: table-cell;
  vertical-align: middle;   /* table-cell 才能吃到垂直居中 */
}
/* 真实数据表格建议：table-layout: fixed 锁定列宽 */
table { table-layout: fixed; width: 100%; }
```
