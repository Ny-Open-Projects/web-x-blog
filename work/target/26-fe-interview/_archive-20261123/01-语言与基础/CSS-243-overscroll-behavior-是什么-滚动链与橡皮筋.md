---
title: [CSS-243] overscroll-behavior 是什么：滚动链与橡皮筋
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 移动端]
type: 面试题
---

## CSS-243：overscroll-behavior：滚动链与橡皮筋

**答**：
- 滚动链（scroll chaining）：内层滚到边界后，滚动事件传给外层——弹窗滚完背景跟着滚
- overscroll-behavior 三值：auto（默认传递）、contain（止于当前层）、none（contain 且无橡皮筋过界效果）
- 典型位置：弹层/抽屉/下拉刷新容器设置 contain；全屏聊天列表 none
- 局限：iOS Safari 长期只部分支持（滚动链场景已支持，body 橡皮筋需 body position: fixed 配合）
- 与 H5-268（锁定滚动）互补：overscroll 是 CSS 层阻断，fixed 是布局层冻结，组合使用最稳

```css
.modal-body {
  overflow-y: auto;
  overscroll-behavior: contain; /* 滚到头不再带动背景 */
}
body { overscroll-behavior-y: none; } /* 去掉页面级下拉过界 */
```
