---
title: [WEB-466] 低端安卓机页面卡顿的排查 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## WEB-466：低端安卓机页面卡顿的排查 SOP

**答**：
- 环境仿真先行：DevTools CPU 6x throttle + 移动 UA，模拟低端机（真机抓 Android WebView 可用 chrome://inspect）
- 卡顿分型：滑动掉帧（渲染层：大面积 shadow/blur、复杂 DOM、无节流 scroll）vs 点击响应慢（脚本层：长任务占主线程）
- 高频元凶：backdrop-filter 与 box-shadow 叠加、超大图片缩放渲染、长列表无虚拟滚动、频繁 getBoundingClientRect 强制布局
- 量化验证：Performance 面板看 FPS 与帧耗时，rAF 计数器统计掉帧率；fix 后对比同一录制
- 降级兜底：低端机关闭模糊/阴影等特效（deviceMemory/hardwareConcurrency 或用户网络分档判断），保留可用性

```javascript
const fps = (() => {
  let frames = 0, last = performance.now();
  const loop = (t) => { frames++; t - last >= 1000 && (report({ fps: frames }), frames = 0, last = t); requestAnimationFrame(loop); };
  requestAnimationFrame(loop);
})();
```
