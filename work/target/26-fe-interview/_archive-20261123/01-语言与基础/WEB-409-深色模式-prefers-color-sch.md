---
title: [WEB-409] 深色模式 prefers-color-scheme 怎么工程化落地？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 浏览器]
type: 面试题
---

## WEB-409：深色模式 prefers-color-scheme 怎么工程化落地？
**答**：
- 三层实现：CSS 变量两套值 + media query 自动跟随；手动切换用 html[data-theme] 覆盖变量；跟随时 JS 写 meta theme-color。
- 细节：图片按模式切换（picture/media 或 CSS filter）、主题切换闪烁问题（启动前内联脚本先读偏好）、地图/图表用主题 token 而非硬编码色。
- 兼容：不支持 prefers-color-scheme 的环境走默认亮色，变量兜底写法 :root 先亮后暗。

```javascript
:root { --bg: #fff; --fg: #111; }
@media (prefers-color-scheme: dark) { :root { --bg: #111; --fg: #eee; } }
html[data-theme="dark"] { --bg: #111; --fg: #eee; }
// 防闪烁: <head> 内联脚本先于渲染设置 data-theme
const pref = localStorage.theme || matchMedia('(prefers-color-scheme: dark)').matches && 'dark';
document.documentElement.dataset.theme = pref || 'light';
```
