---
title: [BAS-123] DPR 是什么？对移动端开发有什么影响？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-123：DPR 是什么？对移动端开发有什么影响？
**答**：
- DPR = 物理像素 / CSS 像素；iPhone DPR 为 2 或 3，1px CSS 边框实际占 2~3 个物理像素，这就是"1px 变粗"问题。
- 设计稿按 @2x/@3x 出图，配合 srcset 或高倍图缩小显示保证清晰。
- REM 适配和 viewport 缩放方案本质都是在不同 DPR 下保持视觉一致；`window.devicePixelRatio` 可读取当前值。

```javascript
const dpr = window.devicePixelRatio;
console.log(`物理像素比 ${dpr}`);   // 2 或 3
// 高倍图按 DPR 选择
const img = new Image();
img.src = dpr >= 2 ? 'logo@2x.png' : 'logo.png';
```
