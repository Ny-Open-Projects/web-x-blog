---
title: [CSS-054] 继承与 initial、inherit、unset、revert 的区别？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-054：继承与 initial、inherit、unset、revert 的区别？

**答**：
- 可继承属性：color、font-*、line-height、text-align、visibility 等；盒模型尺寸类大多不可继承。
- `inherit`：强制继承父值（即使该属性默认不可继承）。
- `initial`：恢复到规范初始值，如 color: initial 是黑色而非主题色。
- `unset`：可继承属性等同 inherit，不可继承属性等同 initial。
- `revert`：回退到浏览器默认样式/用户样式，最接近“取消我的所有作者样式”。

```css
/* 继承演示 */
.parent { color: #333; border: 1px solid #999; }
.child  { color: inherit; }  /* #333，color 本身可继承 */
.child  { border: inherit; } /* 强制继承边框（默认不继承） */

.link { color: var(--brand); }
.link.reset-initial { color: initial; } /* 黑色，不是 var(--brand) */
.link.reset-unset   { color: unset; }   /* color 可继承 → 等同 inherit */
.btn { all: unset; } /* 清除按钮 UA 样式，重新自定义 */
.btn { all: revert; } /* 回到浏览器默认按钮外观 */
```
