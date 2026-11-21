---
title: [CSS-217] 滚动驱动动画的兼容与降级（@supports）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-217：滚动驱动动画的兼容与降级

**答**：
- 支持面：Chrome/Edge 115+、Safari 26 前后逐步支持；Firefox 在实现中——生产必须降级
- 降级原则：滚动驱动是「增强动画」，不支持时要么隐藏效果（进度条），要么退回 JS 监听实现（关键动效）
- 检测方式：`@supports (animation-timeline: scroll())`
- JS 退路封装：同一关键帧语义用 scroll 监听 + requestAnimationFrame 计算进度驱动 CSS 变量——行为对齐成本低
- 团队规范：新动效默认写「CSS 声明版 + JS 降级版」双轨，构建期注入特性开关

```css
@supports not (animation-timeline: scroll()) {
  .reveal-item { opacity: 1; transform: none; } /* 退化为直接显示 */
}
```
```javascript
// JS 降级版：驱动同一个 CSS 变量
if (!CSS.supports('animation-timeline: scroll()')) {
  const onScroll = () => {
    const p = scrollY / (document.body.scrollHeight - innerHeight);
    document.documentElement.style.setProperty('--scroll-p', p);
  };
  addEventListener('scroll', onScroll, { passive: true });
}
```
