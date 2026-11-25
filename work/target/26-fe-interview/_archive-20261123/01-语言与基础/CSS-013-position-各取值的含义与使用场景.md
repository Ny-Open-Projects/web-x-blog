---
title: [CSS-013] position 各取值的含义与使用场景？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-013：position 各取值的含义与使用场景？

**答**：
- `static`：默认值，不参与定位，z-index 无效。
- `relative`：相对自身原位置偏移，不脱离文档流，常用作 absolute 的定位参照。
- `absolute`：脱离文档流，相对最近的非 static 祖先定位。
- `fixed`：相对视口定位，脱离文档流；祖先有 transform/filter 时会失效（参照该祖先）。
- `sticky`：粘性定位，在滚动范围内“吸顶/吸边”，必须指定 top/bottom 等阈值。

```css
.nav {
  position: sticky;   /* 滚动吸顶 */
  top: 0;
  z-index: 100;
  background: #fff;
}

.badge {
  position: absolute; /* 配合父级 relative */
  top: -8px;
  right: -8px;
}
.card { position: relative; }

.back-top {
  position: fixed;    /* 相对视口 */
  right: 20px;
  bottom: 20px;
}
```
