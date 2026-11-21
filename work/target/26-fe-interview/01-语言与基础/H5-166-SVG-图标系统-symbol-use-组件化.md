---
title: [H5-166] SVG 图标系统（symbol/use/组件化）怎么搭？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-166：SVG 图标系统（symbol/use/组件化）怎么搭？
**答**：
- 雪碧图：`<svg hidden>` 内含多个 `<symbol id viewBox>`，使用处 `<use href="#id">`；一份定义全局复用，无重复字节。
- 颜色走 `currentColor`（继承文字颜色）；尺寸用 `width:1em;height:1em` 跟随字号 + viewBox 等比自适应；多色图标用 CSS 变量传参。
- 组件化：构建期（vite-plugin-svg-icons/svgr）把 .svg 文件编译成框架组件，业务只 `import { IconSearch }`。
- 关键限制：`<use>` 的内容在 shadow 边界里，外部 CSS 选择器穿不进去——传参只能靠继承属性与 CSS 变量；a11y 上装饰图标 aria-hidden、有语义图标加 title。

```html
<!-- 图标系统三件套：symbol 定义 + use 引用 + 构建期组件化 -->
<svg hidden aria-hidden="true">
  <symbol id="icon-search" viewBox="0 0 24 24">
    <path fill="currentColor" d="M10 2a8 8 0 105.3 14l4.9 4.9 1.4-1.4-4.9-4.9A8 8 0 0010 2zm0 2a6 6 0 110 12 6 6 0 010-12z"/>
  </symbol>
  <symbol id="icon-close" viewBox="0 0 24 24">
    <path fill="none" stroke="currentColor" stroke-width="2" d="M6 6l12 12M18 6L6 18"/>
  </symbol>
</svg>

<!-- 使用处：size=1em 跟随字号，颜色跟随 currentColor -->
<style>
  .icon { width: 1em; height: 1em; vertical-align: -0.125em; }
  button { color: #2563eb; font-size: 20px; }   /* 图标自动同色 */
  .icon-multi { --icon-accent: #f59e0b; }       /* 多色图标用变量传参 */
</style>
<button type="button">
  <svg class="icon" aria-hidden="true"><use href="#icon-search"/></svg> 搜索
</button>

<script>
// 组件化：构建期把 .svg 文件编译成框架组件（svgr / vite-plugin-svg-icons 的产物）
function Icon({ name, size }) {
  return {
    template: `<svg class="icon" :style="{fontSize: size + 'px'}" aria-hidden="true">
                 <use :href="'#icon-' + name"/>
               </svg>`,
    props: ['name', 'size'],
  };
}
// 关键工程点：
// 1) 颜色统一走 currentColor，多色图标用 CSS 变量（--icon-accent）
// 2) use 内容在 shadow 边界里，外部选择器穿不进去 —— 传参只能靠继承属性/变量
// 3) 雪碧图内联进首屏 HTML（避免额外请求）；路由级图标按需拆分
// 4) a11y：装饰性图标 aria-hidden；有语义的图标加 <title> + role="img"
</script>
```
