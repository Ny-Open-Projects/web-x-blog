---
title: [CSS-265] scroll-behavior: smooth 与 JS 滚动的分工
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 滚动]
type: 面试题
---

## CSS-265：scroll-behavior: smooth 与 JS 滚动的分工

**答**：
- scroll-behavior: smooth：锚点跳转、scrollTo 等程序化滚动自动平滑——CSS 一行替代 JS 动画
- 注意事项：全局 smooth 会让「恢复滚动位置」（前进后退、锁滚动还原）也变慢——配 @media (prefers-reduced-motion) 关闭；键盘滚动不受影响
- JS 精细控制：element.scrollIntoView({ behavior, block, inline }) 与 scrollTo({ top, behavior })——选项级覆盖 CSS
- 分工原则：一般跳转用 CSS；需要「滚动到位后回调/中断」的逻辑（轮播、回顶）用 JS scrollIntoView + scrollend 事件（2023+ 标准事件）
- 兼容：smooth 全主流；scrollend Chromium 114+/Firefox 109+

```css
html { scroll-behavior: smooth; }
@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto; } }
```
```javascript
document.addEventListener('scrollend', () => console.log('滚动停止，可做惰性加载'));
el.scrollIntoView({ behavior: 'smooth', block: 'center' });
```
