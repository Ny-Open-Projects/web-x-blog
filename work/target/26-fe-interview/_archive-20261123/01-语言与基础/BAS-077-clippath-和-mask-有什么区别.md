---
title: [BAS-077] clip-path 和 mask 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-077：clip-path 和 mask 有什么区别？
**答**：
- clip-path 用基本形状（circle、polygon、inset）或 path 裁剪可见区域，边界生硬、矢量形状。
- mask 用图片/渐变的透明度做遮罩，能做羽化、渐隐、复杂贴图蒙版，`mask-image: linear-gradient(...)` 实现图片底部渐隐很常用。
- 两者都不影响布局，被裁掉的不可见区域同样不响应鼠标事件。

```css
.tri { clip-path: polygon(0 0, 100% 0, 100% 100%); }  /* 直角三角形 */
.fade-img {
  mask-image: linear-gradient(to bottom, #000 60%, transparent);  /* 底部渐隐 */
}
```
