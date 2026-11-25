---
title: [MP-330] Skyline 渲染引擎：迁移评估与落地
date: 2026-11-21
categories: [小程序]
tags: [前端面试, 面试题, 架构]
type: 面试题
---

## MP-330：Skyline 渲染引擎：迁移评估与落地

**答**：
- Skyline 是什么：自绘渲染引擎（替代 WebView 渲染层）——长列表（recycler 节点复用）、worklet 动画（渲染线程）、同步布局查询三大能力
- 迁移收益：长列表滚动帧率显著提升（节点复用 vs WebView 全量 DOM）、复杂手势动画跟手（渲染线程无跨线程延迟）
- 迁移成本：组件覆盖度（部分组件/属性不支持——基础库版本门槛）、CSS 子集（部分选择器/布局行为差异）、WXS 不兼容（改 worklet）
- 分阶段迁移：新页面用 Skyline（page.json 的 renderer: skyline）老页面不动——页面级灰度；用 wx.canIUse 检测降级
- 评估清单：核心页面的组件覆盖度核对 → worklet 改造清单 → 真机矩阵（iOS/安卓低版本基础库）→ 性能对比（同页面 WebView vs Skyline 帧率）

```json
// page.json
{ "renderer": "skyline",
  "rendererOptions": { "skyline": { "defaultDisplayBlock": true } },
  "componentFramework": "glass-easel" }
```

```javascript
// 能力检测降级
const skyline = wx.canIUse('Skyline');
Page({
  data: { renderer: skyline ? 'skyline' : 'webview' },
});
// worklet: wx.worklet.shared + UI 线程函数 — 迁移自 WXS 的改造点
```
