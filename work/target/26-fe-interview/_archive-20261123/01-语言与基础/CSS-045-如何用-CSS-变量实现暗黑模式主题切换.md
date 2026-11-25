---
title: [CSS-045] 如何用 CSS 变量实现暗黑模式主题切换？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-045：如何用 CSS 变量实现暗黑模式主题切换？

**答**：
- 在 `:root` 定义亮色 token，`[data-theme="dark"]` 下重定义同名 token。
- HTML 根元素挂 `data-theme`，JS 一行切换，全站自动生效。
- 可用 `prefers-color-scheme` 读取系统偏好作为默认值，用户手动选择存 localStorage。
- 切换动画可用 `view-transition` 或简单的 transition on color/background。

```css
:root {
  --bg: #ffffff;
  --text: #1f2328;
  --card: #f6f8fa;
}
[data-theme="dark"] {
  --bg: #0d1117;
  --text: #e6edf3;
  --card: #161b22;
}
body {
  background: var(--bg);
  color: var(--text);
  transition: background 0.3s, color 0.3s;
}
.card { background: var(--card); }
```

```javascript
// 初始化：系统偏好 + 用户选择
const saved = localStorage.getItem('theme');
const system = matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
document.documentElement.dataset.theme = saved || system;

document.querySelector('#theme-toggle').addEventListener('click', () => {
  const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  document.documentElement.dataset.theme = next;
  localStorage.setItem('theme', next);
});
```

## 九、transition、animation 与渲染性能
