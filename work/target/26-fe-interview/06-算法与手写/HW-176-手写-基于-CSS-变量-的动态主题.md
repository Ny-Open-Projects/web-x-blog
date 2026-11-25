---
title: [HW-176] 手写动态主题引擎——CSS 变量三主题 + 跟随系统 + 无闪切（data-theme 预注入）
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-176：手写动态主题引擎——CSS 变量三主题 + 跟随系统 + 无闪切（data-theme 预注入）
**答**：主题切换零重排：CSS 变量定义三套主题（:root[data-theme=dark] 覆盖变量值），切换只改 data-theme 属性（样式重绘不重匹配，PER-403）；跟随系统（prefers-color-scheme change 监听，用户显式选择优先）；无闪切（HTML 内联脚本首字节注入 data-theme，防"白闪"FOUC）。

```html
<!-- index.html 首字节注入（无闪切）：内联脚本在 CSS 加载前执行 -->
<script>
  const t = localStorage.getItem('theme')
    || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.dataset.theme = t;
</script>
```
```css
:root { --bg: #fff; --text: #222; --accent: #09f; }
:root[data-theme='dark'] { --bg: #121212; --text: #eee; --accent: #4cf; }
:root[data-theme='sepia'] { --bg: #f4ecd8; --text: #5b4636; }
body { background: var(--bg); color: var(--text); transition: background .2s; }
```
```javascript
function themeEngine() {
  const user = () => localStorage.getItem('theme');       // null = 跟随系统
  function apply() {
    document.documentElement.dataset.theme = user() ?? systemPref();
  }
  const systemPref = () => matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
    if (!user()) apply();                                 // 跟随模式下系统变化实时切
  });
  return {
    set(t) { t ? localStorage.setItem('theme', t) : localStorage.removeItem('theme'); apply(); },
    get() { return user() ?? systemPref(); },
  };
}
// 优先级：用户显式选择 > 系统偏好 > 默认 light
// 性能：变量切换不触发选择器重匹配（PER-403）；transition 只作用 background/color（重绘级）
// 无闪切关键：内联脚本在 <head> 的 CSS link 之前（首字节执行，防 FOUC）
```

**评分点**：
- 内联预注入防 FOUC（脚本必须在 CSS 之前）——本题核心。
- CSS 变量切换不触发选择器重匹配（PER-403 联动）。
- 优先级链（用户 > 系统 > 默认）与系统变化实时跟随。
- transition 限定 background/color（重绘级，不做全属性过渡）。
