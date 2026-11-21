---
title: [CSS-099] writing-mode 竖排文字有哪些实战用法？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-099：writing-mode 竖排文字有哪些实战用法？

**答**：
- `writing-mode: vertical-rl` 竖排（从右列向左），`vertical-lr` 从左向右；配合 `text-orientation` 控制字姿。
- 典型场景：中文古籍风排版、侧边目录/页签文字、图表 Y 轴标签（比 rotate 更语义化）。
- 竖排下逻辑属性含义不变：`margin-inline-start` 仍指"行首方向"，RTL/竖排一套代码。
- `text-orientation: upright` 让拉丁字母直立，`mixed`（默认）旋转 90 度。
- 表格斜表头建议用 writing-mode 而非 transform rotate，不占额外空间且参与布局。

```css
/* 1. 侧边竖排标题 */
.vertical-title {
  writing-mode: vertical-rl;
  text-orientation: upright;   /* 中文直立，英文数字也直立 */
  letter-spacing: 0.35em;
}

/* 2. 图表 Y 轴标签：无需旋转，天然参与 flex 布局 */
.axis-y {
  writing-mode: vertical-rl;
  transform: rotate(180deg);   /* 让文字自下而上读 */
}

/* 3. 斜表头 */
.th-slant {
  writing-mode: vertical-rl;
  height: 72px;
}
```
