---
title: [CSS-264] scrollbar-width 与 ::-webkit-scrollbar 的标准化
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 细节]
type: 面试题
---

## CSS-264：scrollbar-width 与 ::-webkit-scrollbar 的标准化

**答**：
- 标准属性：`scrollbar-width: auto/thin/none` 与 `scrollbar-color: thumb track`——Chrome 121+ 已支持，Firefox 早支持
- ::-webkit-scrollbar 家族：可完全定制（宽度、滑块、轨道、按钮），仅 WebKit/Blink 系；与标准属性互斥（设置标准属性后 webkit 伪元素失效）
- 现代写法：标准属性优先 + @supports 包裹 webkit 伪元素做深度定制
- none 的使用场景：隐藏滚动条但保留滚动（轮播、手机端列表）；务必提供替代滚动暗示
- hover 才显示滚动条的常用配方：默认 transparent，hover 换 color

```css
.scroll {
  overflow: auto;
  scrollbar-width: thin;
  scrollbar-color: #bbb transparent;
}
@supports not (scrollbar-width: thin) {
  .scroll::-webkit-scrollbar { width: 6px; }
  .scroll::-webkit-scrollbar-thumb { background: #bbb; border-radius: 3px; }
}
.carousel { scrollbar-width: none; }
```
