---
title: [SCN-686] 大屏的 RUM（帧率/稳定性）监控怎么做？上报什么指标？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-686：大屏 RUM 监控怎么做？
**答**：
- 核心指标：FPS 分布（P5 帧率是底线）、单帧超 50ms 占比、JS 堆内存趋势（7×24 泄漏监测）、WS 断连次数与重连耗时、数据缓冲溢出计数、watchdog reload 次数。
- 采样与聚合：帧率每 5s 采样聚合成分钟级直方图上报（不上报逐帧）；错误全量但去重（同错误 1 分钟内计次）。
- 版本与设备维度：按屏（deviceId）/版本/时段切片，定位「某块屏恶化」还是「新版本劣化」。
- 告警联动：P5 帧率 < 20 持续 5 分钟或堆内存线性增长告警——大屏无人值守，监控是唯一眼睛。
- 追问钩子：堆内存线性增长怎么自动判——每小时采样的线性回归斜率超阈值且持续 4 小时判泄漏，防短期波动误报。

```javascript
function twinRUM() {
  const fpsHist = new Array(10).fill(0);           // 帧率直方图桶
  let frames = 0, last = performance.now();
  setInterval(() => {
    const fps = frames * 2; frames = 0;            // 5s 窗口
    fpsHist[Math.min(9, Math.floor(fps / 6))]++;
  }, 5000);
  requestAnimationFrame(function f() { frames++; requestAnimationFrame(f); });
  // 泄漏判定：线性回归
  const heapSamples = [];
  setInterval(() => {
    heapSamples.push(performance.memory?.usedJSHeapSize ?? 0);
    if (heapSamples.length >= 4) {
      const slope = linearRegression(heapSamples).slope;
      if (slope > 5e7) report({ type: 'LEAK_SUSPECT', slope, window: heapSamples.length });  // 50MB/h
    }
  }, 3600_000);
}
```
