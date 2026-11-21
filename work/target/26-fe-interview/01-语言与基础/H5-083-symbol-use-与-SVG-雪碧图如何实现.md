---
title: [H5-083] symbol/use 与 SVG 雪碧图如何实现图标复用？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-083：symbol/use 与 SVG 雪碧图如何实现图标复用？
**答**：
- `<symbol>` 定义带 `id` 与 `viewBox` 的"图标模板"，本身不渲染；`<use href="#id">` 实例化，可设置 width/height。
- 复用层级：同页内联引用 → 外部雪碧图文件 `use href="/icons.svg#icon-add"`（跨文件引用兼容性不如内联，旧 IE 需 polyfill）。
- 优势：一份定义多处引用；`currentColor` 继承文字颜色实现一键换色；symbol 自带 viewBox，尺寸由 use 控制。
- 构建链路：svgo 优化 + 拼雪碧图（如 svg-sprite 工具）→ 内联到页面顶部（`display:none` 包裹）或独立文件。
- 注意：外部 SVG 的 `use` 不允许跨域直接改内部结构；mask 方案（CSS mask + svg 文件）适合"只要形状不要交互"的场景。

```html
<!-- 1) 雪碧图：页面顶部隐藏容器，只留定义 -->
<svg style="display:none" aria-hidden="true">
  <symbol id="icon-add" viewBox="0 0 24 24">
    <path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="2"
          stroke-linecap="round" fill="none"/>
  </symbol>
  <symbol id="icon-star" viewBox="0 0 24 24">
    <path d="M12 3l2.7 5.6 6.1.8-4.5 4.2 1.1 6-5.4-3-5.4 3 1.1-6L3.2 9.4l6.1-.8z"
          fill="currentColor"/>
  </symbol>
</svg>

<!-- 2) 使用：currentColor 换色，width/height 控尺寸 -->
<button style="color:#1677ff">
  <svg width="16" height="16"><use href="#icon-add"/></svg> 新增
</button>

<span style="color:#faad14">
  <svg width="20" height="20"><use href="#icon-star"/></svg> 收藏
</span>

<!-- 3) 外部雪碧图（需同源或 CORS）：图标零重复体积 -->
<svg width="16" height="16"><use href="/icons.svg#icon-add"/></svg>

<script>
  // 动态切换图标：改 use 的 href 即可（xlink:href 已废弃，直接 href）
  const btn = document.querySelector('button use');
  btn.setAttribute('href', '#icon-star');
</script>
```
