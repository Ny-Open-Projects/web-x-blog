---
title: [XP-341] 跨端兜底策略：WebView 白屏与降级
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-341：跨端兜底策略：WebView 白屏与降级

**答**：
- 检测：白屏探针（截图采样亮度）+ 加载超时（10s 未渲染）。
- 降级：重启 WebView -> 切换备用 CDN -> 静态兜底页 -> 提示反馈。
- 上报：白屏事件带版本/URL/设备，高频白屏页面优先修复。

```javascript
// 白屏探针
function whiteScreenProbe(webview, { timeoutMs = 10_000 } = {}) {
  return new Promise(resolve => {
    const t = setTimeout(() => resolve({ white: true,
      action: 'reload-webview' }), timeoutMs);
    webview.onFirstPaint(() => {
      clearTimeout(t);
      resolve({ white: sampleBrightness(webview) < 5,
        action: 'ok' });
    });
  });
}
function sampleBrightness(wv) { /* 截图亮度均值 0~255 */ return 0; }
```
