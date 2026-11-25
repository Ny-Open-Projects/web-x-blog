---
title: [XP-337] 跨端版本兼容矩阵：OS/引擎/框架版本覆盖
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-337：跨端版本兼容矩阵：OS/引擎/框架版本覆盖

**答**：
- 矩阵：OS 版本 × 引擎版本（WebView/JSC/Hermes）× 框架版本 的测试覆盖表。
- 基线：覆盖用户量 95% 的组合进全量回归，长尾抽样。
- 废弃：低于基线的版本提示升级或降级体验（功能裁剪）。

```javascript
// 兼容矩阵
const COMPAT = {
  'iOS 15': { webview: 'WKWebView', support: true },
  'iOS 12': { webview: 'WKWebView', support: 'degraded' },   // 降级
  'Android 8': { webview: 'X5/Chromium', support: true },
};
function compatCheck(device) {
  const row = COMPAT[device.os];
  if (!row) return { support: 'unknown', policy: '基线测试补测' };
  return row.support === true
    ? { support: 'full' }
    : { support: 'degraded', policy: '关动画/降图片/提示升级' };
}
```
