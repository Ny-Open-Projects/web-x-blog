---
title: [CSS-248] aspect-ratio 的原理与替换元素的坑
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 布局]
type: 面试题
---

## CSS-248：aspect-ratio 的原理与替换元素的坑

**答**：
- aspect-ratio: 16/9：声明宽高比，一边确定时另一边自动算出——替代 padding-top 百分比 hack
- 优先级规则：显式宽高 > aspect-ratio；auto 的替换元素（img）有自己的内在比例，声明 ratio 后仍以自身为准（除非设置宽高其一）
- 高频坑：img 同时有 width:100% 与 aspect-ratio，图片变形——因为 img 的内在比例参与，需 `object-fit: cover` 裁剪
- flex/grid 子项：ratio 与 stretch 冲突——拉伸覆盖比例，需 align-self 或 height: auto 显式声明
- 典型场景：响应式视频容器、卡片封面、正方形头像网格

```css
.video { aspect-ratio: 16 / 9; width: 100%; }
.cover { aspect-ratio: 1 / 1; width: 100%; object-fit: cover; } /* 裁剪防变形 */
.avatar-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
.avatar-grid img { aspect-ratio: 1; width: 100%; object-fit: cover; }
```
