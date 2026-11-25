---
title: [CSS-279] prefers-color-scheme 与手动切换共存的三态实现
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 主题]
type: 面试题
---

## CSS-279：prefers-color-scheme 与手动切换共存的三态实现

**答**：
- 三态模型：跟随系统（auto）/ 强制亮 / 强制暗——用户开关 + 系统偏好的正确融合
- 实现核心：data-theme 只存 auto/light/dark；CSS 用「变量覆写」而非整套样式复制——dark 变量集挂在 [data-theme='dark'] 与「auto+系统暗」两处
- 系统监听：matchMedia('(prefers-color-scheme: dark)') 的 change 事件——auto 态下实时跟随
- 防白闪：theme 读取脚本放 head 内联（CSS 前）——晚于首帧就闪
- 存储与同步：localStorage 存偏好；登录用户服务端存，跨端同步优先级高于本地

```javascript
// head 内联，CSS 前
const pref = localStorage.theme || 'auto';
const sys = matchMedia('(prefers-color-scheme: dark)').matches;
document.documentElement.dataset.theme = pref === 'auto' ? (sys ? 'dark' : 'light') : pref;
matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
  if (localStorage.theme === 'auto') document.documentElement.dataset.theme = e.matches ? 'dark' : 'light';
});
```
```css
[data-theme='dark'] { /* 暗色变量覆写 */ --bg: #121212; --fg: #eee; }
```
