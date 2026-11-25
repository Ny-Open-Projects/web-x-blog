---
title: [CSS-355] 响应式图片与 CSS 配合：srcset/sizes 决策链
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-355：响应式图片与 CSS 配合：srcset/sizes 决策链

**答**：
- 决策链：sizes 表达「图片将显示的 CSS 宽度」（随视口变化的公式），浏览器按 dpr × sizes 在 srcset 里选最接近的资源——sizes 写错是选错尺寸的主因（常见错：写了 100vw 但图实际只有 50vw 宽）
- CSS 侧配合：图片显示宽度由 CSS 决定，sizes 必须与 CSS 布局一致（改布局要同步改 sizes，否则选择失真）；复杂布局可用 CSS 全程接管（aspect-ratio + object-fit + 固定档位）
- object-fit/object-position：容器与图片比例不一致时的填充策略（cover 裁切/contain 留白）——img 元素配合 aspect-ratio 声明占位防 CLS
- 艺术指导：picture + media 按视口切不同构图（桌面横图/移动竖图），与 srcset 的「同图多分辨率」是两个维度，可嵌套组合
- 性能闭环：用 resource timing 比对「实际下载尺寸 vs 需要尺寸」，过采（下 2x 图显示 1x）与欠采（模糊）都要修

```html
<img
  srcset="a-480.avif 480w, a-750.avif 750w, a-1500.avif 1500w"
  sizes="(max-width: 750px) 100vw, 50vw"
  src="a-750.avif" alt=""
  width="750" height="400"
  style="object-fit: cover; aspect-ratio: 15/8; width: 100%">
```
