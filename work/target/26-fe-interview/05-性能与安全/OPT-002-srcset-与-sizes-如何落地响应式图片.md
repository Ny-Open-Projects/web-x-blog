---
title: [OPT-002] srcset 与 sizes 如何落地响应式图片？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-002：srcset 与 sizes 如何落地响应式图片？

**答**：
- `srcset` 提供多份不同宽度的图，`sizes` 告诉浏览器"这张图在不同视口下会占多宽"，由浏览器结合 DPR 自动选择，比 JS 手动判断更可靠。
- `x` 描述符适合固定尺寸图（如 1x/2x 图标），`w` 描述符 + `sizes` 适合流式布局图片。
- 必须同时设置 `width/height` 属性，让浏览器提前计算宽高比，避免 CLS。
- 用 DevTools Network 面板 + `img.currentSrc` 验证实际选中的资源。

```html
<!-- 一一对应：流式布局图片的 srcset + sizes 落地 -->
<img
  src="banner-800w.jpg"
  srcset="banner-400w.jpg 400w,
          banner-800w.jpg 800w,
          banner-1600w.jpg 1600w"
  sizes="(min-width: 1024px) 50vw, 100vw"
  width="800"
  height="400"
  alt="活动横幅"
/>

<script>
  // 验证浏览器最终选中的资源
  console.log(document.querySelector('img').currentSrc);
</script>
```
