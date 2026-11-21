---
title: [CSS-016] z-index 在什么情况下会失效？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-016：z-index 在什么情况下会失效？

**答**：
- `position: static` 的普通元素上 z-index 无效。
- 只有定位元素或 flex/grid 子项的 z-index 才参与排序。
- 父元素创建了新的层叠上下文时，子元素 z-index 只在父上下文内部比较，表现为“失效”。
- 排查思路：逐级向上找是谁创建了层叠上下文，把 z-index 提升到正确层级或去掉干扰属性。

```css
/* 失效场景一：static 元素 */
.static-box { z-index: 999; } /* 无效 */

/* 失效场景二：被父级层叠上下文隔离 */
.mask-parent {
  transform: translateZ(0); /* 创建层叠上下文，z-index: auto */
}
.mask-parent .mask {
  position: absolute;
  z-index: 9999; /* 只在 mask-parent 内部比较，
                    无法盖住 mask-parent 之外 z-index 更高的兄弟 */
}
```
