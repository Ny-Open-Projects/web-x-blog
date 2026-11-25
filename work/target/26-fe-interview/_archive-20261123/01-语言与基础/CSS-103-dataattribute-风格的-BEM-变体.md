---
title: [CSS-103] data-attribute 风格的 BEM 变体怎么组织？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-103：data-attribute 风格的 BEM 变体怎么组织？

**答**：
- 用 `block__element[data-variant="x"]` 替代 `block__element--modifier`，状态即数据。
- 正交维度分离：variant（外观）、size（尺寸）、state（交互态）各占一个 data 属性，组合不爆炸。
- JS 侧不再拼类名字符串，`dataset` 赋值即可，杜绝"忘写某个 modifier 类"类 bug。
- 与传统 BEM 的 `--modifier` 可共存，团队约定一种为主。
- 状态型样式（loading/disabled）优先 data 属性，纯外观修饰可保留 modifier。

```css
/* 外观维度 */
.btn[data-variant="primary"]   { --btn-bg: var(--color-accent); --btn-fg: #fff; }
.btn[data-variant="ghost"]     { --btn-bg: transparent; --btn-fg: var(--fg-primary); }

/* 尺寸维度：与外观正交组合 */
.btn[data-size="sm"] { --btn-pad: 4px 10px; --btn-fs: 12px; }
.btn[data-size="lg"] { --btn-pad: 12px 24px; --btn-fs: 16px; }

/* 状态维度：JS 只改 dataset */
.btn[data-loading] { pointer-events: none; opacity: 0.7; }
.btn[data-disabled] { opacity: 0.4; cursor: not-allowed; }

.btn {
  background: var(--btn-bg); color: var(--btn-fg);
  padding: var(--btn-pad, 8px 16px); font-size: var(--btn-fs, 14px);
}
```
