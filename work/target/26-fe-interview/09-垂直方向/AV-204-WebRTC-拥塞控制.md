---
title: [AV-204] WebRTC 拥塞控制：GCC 与带宽估计
date: 2026-11-21
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-204：WebRTC 拥塞控制：GCC 与带宽估计

**答**：
- GCC（Google Congestion Control）：基于到达时间梯度（Trendline filter）估计带宽——延迟增长趋势 = 拥塞信号，指数下调线性上升。
- 前端可见：getStats 的 availableOutgoingBitrate、targetBitrate；编码器自动适配（setParameters 动态调 maxBitrate）。
- 联动应用：带宽估计驱动 UI 提示（网络差 → 建议关视频）。

```javascript
async function monitorBandwidth(pc) {
  setInterval(async () => {
    const stats = await pc.getStats();
    stats.forEach((report) => {
      if (report.type === 'outbound-rtp' && report.kind === 'video') {
        // targetBitrate：GCC 给编码器的目标码率；actualEncoderBitrate：实际
        updateQualityIndicator(report.targetBitrate, report.actualEncoderBitrate);
      }
      if (report.type === 'remote-inbound-rtp') {
        // jitter / packetsLost / roundTripTime——网络健康三指标
        if (report.roundTripTime > 0.3) suggestTurnOffVideo();
      }
    });
  }, 1000);
}
// GCC 原理：到达间隔 Δt 与发送间隔比 → 趋势线斜率 > 阈值 = 过载 → 降码率
```
