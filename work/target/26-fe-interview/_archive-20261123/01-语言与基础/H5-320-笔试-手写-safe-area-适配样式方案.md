---
title: [H5-320] 笔试：手写 safe-area 适配样式方案
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 笔试题, 移动端]
type: 笔试题
---

## H5-320：笔试：手写 safe-area 适配样式方案

**题目**：实现一个通用 safe-area 样式方案：吸底导航适配底部横条；顶部导航适配刘海；横屏时左右避让；提供 CSS 变量统一管理，兼容老版 iOS 的 constant()。

**答**：
```css
/* 全局变量定义（兼容写法：constant 在前，env 在后级联覆盖） */
:root {
  --sat: constant(safe-area-inset-top);
  --sab: constant(safe-area-inset-bottom);
  --sal: constant(safe-area-inset-left);
  --sar: constant(safe-area-inset-right);
  --sat: env(safe-area-inset-top);
  --sab: env(safe-area-inset-bottom);
  --sal: env(safe-area-inset-left);
  --sar: env(safe-area-inset-right);
}

/* 顶部导航避让刘海 */
.topbar {
  padding-top: var(--sat);
  padding-top: max(12px, var(--sat)); /* 确保最小间距 */
}

/* 吸底导航 + 内容区 */
.tabbar {
  padding-bottom: calc(var(--sab) + 8px);
}
.page { padding-left: var(--sal); padding-right: var(--sar); }

/* 横屏时左右避让自动生效（env 值随方向变化） */
@media (orientation: landscape) {
  .page { padding-left: max(16px, var(--sal)); }
}
```
```html
<!-- viewport-fit=cover 是前提，没有它 env 值全是 0 -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

**评分点**：
- viewport-fit=cover 是整个方案的前提（没有它安全区值恒为 0）——必答点
- constant/env 双写兼容（先旧后新，级联覆盖）
- max() 保底间距（安全区可能为 0 的非全面屏设备）
- 变量集中管理，组件内只引用变量
