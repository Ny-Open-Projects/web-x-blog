---
title: [H5-266] H5 页面键盘顶起输入框的坑：visualViewport
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, 移动端]
type: 面试题
---

## H5-266：H5 页面键盘顶起输入框的坑：visualViewport

**答**：
- 乱象根源：各平台键盘弹出后 viewport 行为不一致——iOS 不缩 window（页面整体顶起，可滚动），Android 压缩视口高度
- visualViewport API：暴露「可见视口」（被键盘遮挡后的真实可视区域）的 offsetTop/height/resize 事件——判断键盘状态与做避让的正解
- 典型场景：聊天输入框要贴在键盘上方——监听 visualViewport.resize，把输入框 translateY 到视口底部；iOS 上还要配合 `interactive-widget=resizes-content`（Chrome 108+）
- 修复手段：`scrollIntoView({ block: 'center' })` 在 focus 后调用；或 CSS `height: 100dvh`（动态视口单位）
- 老方案回顾：focus 后 setTimeout 读 scrollHeight 强滚，已逐渐被 visualViewport 取代

```javascript
const vv = window.visualViewport;
vv.addEventListener('resize', () => {
  const keyboardHeight = window.innerHeight - vv.height;
  composer.style.transform = `translateY(-${Math.max(0, keyboardHeight)}px)`;
});
```
