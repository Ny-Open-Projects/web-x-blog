---
title: [CSS-269] object-fit 与 object-position：图片适配
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 布局]
type: 面试题
---

## CSS-269：object-fit 与 object-position：图片适配

**答**：
- object-fit 五值：fill（拉伸变形）、contain（完整显示留白）、cover（裁剪填满）、none（原尺寸）、scale-down（contain 或 none 取小）
- object-position 控制裁剪/留白的锚点（center / top / 20% 30%）——「人像居上」的头像裁剪常用
- 与 background-size 的分工：img/video 等内容元素用 object-fit；装饰背景用 background——语义与可访问性差异（img 有 alt）
- 搭配：aspect-ratio 固定容器 + cover 裁剪 = 任何图片比例都整齐的网格
- 兼容：全支持，可生产

```css
.gallery img { width: 100%; aspect-ratio: 1; object-fit: cover; object-position: center 20%; }
.logo img { width: 100%; height: 60px; object-fit: contain; } /* logo 不裁剪 */
```
