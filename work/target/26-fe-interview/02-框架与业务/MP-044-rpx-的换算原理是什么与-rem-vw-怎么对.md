---
title: [MP-044] rpx 的换算原理是什么？与 rem/vw 怎么对比？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-044：rpx 的换算原理是什么？与 rem/vw 怎么对比？
**答**：
- rpx 规定**任何屏幕 750rpx = 屏幕宽度**，即 `1rpx = 屏宽 / 750`：iPhone6（375px）下 1rpx = 0.5px，由框架在渲染时换算。
- 与 rem 对比：rem 需 JS 动态设置根字号，rpx 是框架内建、零 JS；与 vw 对比：`1rpx = 100vw / 750 ≈ 0.1333vw`，本质同源。
- 细节坑：极小屏/大屏上 rpx 等比放大可能失真，关键尺寸可配合 px；**1px 细线用 px**（0.5px/1rpx 在部分机型取整后消失）。
- 设计稿约定：750 宽的设计稿标注数值直接写 rpx。

```css
/* 750 设计稿：卡片宽 686、内边距 32、字号 28 */
.card {
  width: 686rpx;                    /* 375 屏 = 343px */
  padding: 32rpx;
  border-bottom: 1px solid #eee;    /* 细线用 px，避免 rpx 取整消失 */
  font-size: 28rpx;                 /* 375 屏 = 14px */
  margin-bottom: env(safe-area-inset-bottom);
}
```

---

## 七、能力与 API（045-052）
