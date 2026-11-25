---
title: [BAS-162] prefers-color-scheme 和 prefers-contrast 怎么用？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-162：prefers-color-scheme 和 prefers-contrast 怎么用？
**答**：
- prefers-color-scheme: dark/light 跟随系统深色模式，配合 CSS 变量做主题切换是零 JS 方案。
- prefers-contrast: more/no-preference 响应用户的对比度偏好，增强可访问性（无障碍审计常查）。
- 两者都是 user preference media features，同理还有 prefers-reduced-motion（减少动效）。

```css
:root { --bg: #fff; --fg: #222; }
@media (prefers-color-scheme: dark) {
  :root { --bg: #111; --fg: #eee; }   /* 跟随系统深色模式 */
}
@media (prefers-contrast: more) {
  .btn { border: 2px solid currentColor; }  /* 对比度增强时加边框 */
}
body { background: var(--bg); color: var(--fg); }
```

## 十八、HTTP 与安全速答补充
