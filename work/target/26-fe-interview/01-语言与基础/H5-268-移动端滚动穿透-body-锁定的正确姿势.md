---
title: [H5-268] 移动端滚动穿透：body 锁定的正确姿势
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 移动端]
type: 面试题
---

## H5-268：移动端滚动穿透：body 锁定的正确姿势

**答**：
- 滚动穿透：弹层内的滚动到边界后，滚动事件穿透到 body——页面背景跟着滚
- 廉价方案 `overflow: hidden` 在移动端不彻底（iOS Safari 无效或滚动位置丢失）
- 推荐方案一：`touch-action: none` 或在弹层内容区加 `overscroll-behavior: contain`，阻止滚动链传播
- 推荐方案二（iOS 稳）：锁定时记下 `scrollY`，给 body 加 `position: fixed; top: -scrollYpx`，解锁时还原——体验最稳但要还原滚动位置
- 细节：弹层自身可滚动区域要真实可滚（内容超容器），否则手势直接落到遮罩层

```javascript
function lockScroll() {
  const y = scrollY;
  document.body.style.cssText = `position:fixed;top:${-y}px;width:100%`;
  return () => {
    document.body.style.cssText = '';
    scrollTo(0, y); // 还原位置
  };
}
```
