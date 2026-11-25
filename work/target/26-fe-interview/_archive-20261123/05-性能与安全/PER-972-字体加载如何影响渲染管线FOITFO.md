---
title: [PER-972] 字体加载如何影响渲染管线？FOIT/FOUT 与 size-adjust 治理
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-972：字体加载如何影响渲染管线？FOIT/FOUT 与 size-adjust 治理

**答**：
- 字体是渲染阻塞点：文本在字体就绪前可能隐藏（FOIT）或先用回退字体（FOUT），切换时宽度跳变造成 CLS。
- 治理：font-display: swap（可见但会跳）+ font metric override（ascent-override/size-adjust 让回退字体度量贴近目标字体，跳变趋近 0）。
- 子集化与 preload：中文字体按 unicode-range 分片，只加载用到的分片，配合 preload 首屏分片。
- 深水：swap 期间文本布局会重算两次，主线程敏感页面关注字体切换帧的 Layout 时长。

```javascript
/* 字体度量覆盖：消除 FOUT 跳变 */
@font-face {
  font-family: 'ArialFallback';
  src: local('Arial');
  ascent-override: 90%;
  descent-override: 22%;
  line-gap-override: 0%;
  size-adjust: 105%;
}
body { font-family: 'PingFang SC', 'ArialFallback', sans-serif; }
/* 加载策略 */
// JS 侧确认切换时机
document.fonts.ready.then(() => console.log('字体就绪，布局已稳定'));
```
