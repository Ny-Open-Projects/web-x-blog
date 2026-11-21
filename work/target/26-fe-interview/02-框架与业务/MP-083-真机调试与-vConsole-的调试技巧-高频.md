---
title: [MP-083] 真机调试与 vConsole 的调试技巧？（高频）
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-083：真机调试与 vConsole 的调试技巧？（高频）
**答**：
- 层级：开发者工具模拟器 → **真机调试 2.0**（工具面板直连真机，断点/网络/性能面板齐全）→ 体验版 + vConsole（只有日志）。
- vConsole：小程序内嵌调试面板，查 console/Storage/网络；线上问题让用户打开调试上报界面状态。
- 技巧：模拟器与真机差异大（同层渲染、键盘、dpr），关键链路必须真机验收；用 `wx.getRealtimeLogManager` 实时日志在后台查线上日志。

```javascript
// 线上问题排查：实时日志（后台可查，区别于 console 仅本地）
const logger = wx.getRealtimeLogManager()
Page({
  onPullFail(e) {
    logger.error('pull failed', this.route, JSON.stringify(e))
    logger.info({ step: 'after_cache', size: this.data.list.length })
  }
})
```
