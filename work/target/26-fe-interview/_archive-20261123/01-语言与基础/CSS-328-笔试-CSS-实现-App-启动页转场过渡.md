---
title: [CSS-328] 笔试：CSS App 启动页转场
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 动画]
type: 笔试题
---

## CSS-328：笔试：App 启动页转场

**题目**：实现启动闪屏（splash）转场：页面加载后 logo 居中 1s，然后整层淡出并放大 logo 上移，露出主界面；主界面内容错峰浮入；不阻塞交互。

**答**：
```css
.splash {
  position: fixed; inset: 0;
  display: grid; place-items: center;
  background: #fff; z-index: 999;
  pointer-events: none;                 /* 不阻塞交互 */
  animation: splash-out .6s ease .8s forwards;
}
.splash .logo { animation: logo-up .6s ease .8s forwards; }
@keyframes splash-out { to { opacity: 0; visibility: hidden; } }
@keyframes logo-up { to { transform: translateY(-60px) scale(1.1); opacity: 0; } }

/* 主界面内容错峰浮入 */
.content-item { animation: rise .5s ease both; }
.content-item:nth-child(1) { animation-delay: 1.0s; }
.content-item:nth-child(2) { animation-delay: 1.15s; }
.content-item:nth-child(3) { animation-delay: 1.3s; }
@keyframes rise { from { opacity: 0; transform: translateY(16px); } }

/* 动画结束移除 DOM（避免遮挡），JS 一行 */
/* document.querySelector('.splash').addEventListener('animationend', e => e.target.remove(), { once: true }); */

@media (prefers-reduced-motion: reduce) {
  .splash { animation-duration: .01s; animation-delay: 0s; }
  .content-item { animation-delay: 0s !important; }
}
```

**评分点**：
- forwards + visibility: hidden 确保动画后不拦截交互；animationend 移除 DOM 更彻底
- 延迟分层（splash .8s 后转场，内容 1s 起错峰）
- pointer-events: none 从一开始就不阻塞
- prefers-reduced-motion 的跳过处理
