---
title: [XP-202] 小程序 Skyline 渲染引擎：脱离 WebView 的原生渲染
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-202：小程序 Skyline 渲染引擎：脱离 WebView 的原生渲染

**答**：
- Skyline：微信新一代渲染引擎——脱离 WebView，直接 Native 渲染（类 RN 指令集），性能接近原生。
- 差异：CSS 子集更小（不支持部分选择器）、worklet 动画（跑在渲染线程）、不支持页面级 WebView 特性（如 window.open）。
- 选型：性能敏感页面（长列表/复杂动画）→ Skyline；兼容性优先 → WebView 模式（默认）。

```javascript
const skylineVsWebview = {
  skyline: { render: 'Native 渲染（指令集 → 原生 View）',
    perf: 'setData 延迟降低 50%+，长列表不掉帧',
    worklet: '动画跑在渲染线程（不跨线程通信）',
    css: '子集更小（无后代选择器/伪类）' },
  webview: { render: 'WebView 渲染', perf: '标准双线程成本',
    css: '完整 CSS 子集', compat: '兼容性最好（默认）' },
  selection: '性能敏感（长列表/动画）→ Skyline；业务兼容 → WebView',
};
// 开启：app.json {"rendererOptions": {"skyline": {...}}, "lazyCodeLoading": "requiredComponents"}
```
