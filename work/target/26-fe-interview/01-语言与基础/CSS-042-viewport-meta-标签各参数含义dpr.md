---
title: [CSS-042] viewport meta 标签各参数含义？dpr 与适配方案如何演进？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-042：viewport meta 标签各参数含义？dpr 与适配方案如何演进？

**答**：
- `width=device-width`：布局视口等于设备逻辑宽度，移动端适配的前提。
- `initial-scale=1`：初始缩放；`maximum-scale/user-scalable` 控制缩放，禁用缩放损害可访问性，应慎用。
- `viewport-fit=cover` 配合 env(safe-area-inset-*) 处理刘海屏安全区。
- 适配演进：固定 320 布局 → rem flexible（dpr 缩放 viewport）→ vw/clamp 流式方案，dpr 只剩 1px 问题等少数场景需要关心。

```html
<!-- 标准移动端 viewport -->
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />

<style>
  /* 刘海屏安全区适配 */
  .tab-bar {
    position: fixed;
    bottom: 0;
    padding-bottom: env(safe-area-inset-bottom);
  }
  .full-bleed {
    padding-left: env(safe-area-inset-left);
  }
</style>
```

## 八、CSS 变量与主题切换
