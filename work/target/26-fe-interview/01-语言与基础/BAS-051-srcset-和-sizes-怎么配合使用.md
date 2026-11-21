---
title: [BAS-051] srcset 和 sizes 怎么配合使用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-051：srcset 和 sizes 怎么配合使用？
**答**：
- srcset 提供候选图列表：`url 480w` 的 w 描述符表示图片真实宽度；也支持 `2x` 这类 x 描述符按 DPR 选择。
- sizes 描述"图片在不同视口下实际显示的 CSS 宽度"，浏览器结合 sizes、视口宽度和 DPR 自动挑最合适的条目。
- 浏览器选定图片后一般不随视口变化重选，需要按条件切换构图时用 picture。

```html
<img
  src="photo-800.jpg"
  srcset="photo-400.jpg 400w, photo-800.jpg 800w, photo-1600.jpg 1600w"
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="示例图"
/>
<!-- 视口 600px 以下按 100vw 选图，否则按视口一半宽度选图 -->
```
