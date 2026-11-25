---
title: [CSS-233] light-dark() 是什么：暗色主题一行适配
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 主题]
type: 面试题
---

## CSS-233：light-dark()：暗色主题一行适配

**答**：
- `light-dark(亮色值, 暗色值)`：跟随 color-scheme 自动取值——不用写两套媒体查询
- 前提：声明 `color-scheme: light dark`（或元素上限定）；函数只在 color-scheme 生效时有意义
- 手动切换的三态方案：:root 设 color-scheme: light/dark（用户选择）→ light-dark() 自动跟随——比 prefers-color-scheme 媒体查询灵活（可被 UI 开关覆盖）
- 适用范围：仅颜色类属性（color/background/border-color…）；布局尺寸类不适用
- 兼容：Chrome 123+/Safari 17.5+/Firefox 120+；老浏览器提供变量兜底

```css
:root { color-scheme: light dark; }
html[data-theme='dark']  { color-scheme: dark; }
html[data-theme='light'] { color-scheme: light; }

body {
  color: light-dark(#1a1a1a, #eee);
  background: light-dark(#fff, #121212);
}
```
