---
title: [SCN-036] iOS 上整个页面出现橡皮筋回弹，如何只让列表区域滚动？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-036：iOS 上整个页面出现橡皮筋回弹，如何只让列表区域滚动？
**答**：
- 低成本方案：滚动容器加 overscroll-behavior: contain 阻断滚动链，内层滚到头不再带动页面回弹。
- 彻底方案：html/body 用 position: fixed + overflow: hidden 锁死整页，滚动只发生在内层列表 overflow-y: auto，回弹被限定在列表内部。
- 弹窗背景滚动穿透同理：打开弹窗时锁 body，关闭时恢复并还原滚动位置（iOS 旧版 overflow: hidden 无效，必须 fixed）。

```css
/* 方案一：overscroll-behavior 阻断滚动链，成本最低 */
.scroll-area {
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;   /* iOS 顺滑滚动 */
  overscroll-behavior: contain;        /* 滚到头不再带动整页回弹 */
}

/* 方案二：整页锁死，仅列表内部滚动 */
html, body {
  position: fixed;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
.page-scroll {
  height: 100%;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
```
