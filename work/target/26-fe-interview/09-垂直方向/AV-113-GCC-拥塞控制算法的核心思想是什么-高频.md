---
title: [AV-113] GCC 拥塞控制算法的核心思想是什么？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-113：GCC 拥塞控制算法的核心思想是什么？（高频）
**答**：
- GCC（Google Congestion Control）= 基于延迟的估计 + 基于丢包的估计，取较小者作为目标码率输出。
- 延迟侧：TWCC 让发送端拿到每个包的到达时间，到达时间滤波器估计延迟梯度趋势，输出 overuse/normal/underuse 三态。
- 丢包侧简单直接：loss < 2% 升码率，> 10% 降码率，之间保持。
- 升级慢（乘性增最高 8%/s）降级快（0.85 倍）——稳定性优先的设计哲学。
- 前端关联：SDP 里 transport-cc 扩展即是 TWCC；getStats 的 availableOutgoingBitrate 是 GCC 输出的近似反映（AV-032 的深入版）。

```typescript
// GCC 简化模型：用于理解原理，生产实现位于 libwebrtc 内部
interface TrendReport { sendDeltaMs: number; arriveDeltaMs: number; lossRate: number; }
class GccLite {
  targetBps = 1_500_000;
  estimateBandwidth(reports: TrendReport[]): number {
    const gradient = reports.map((r) => r.arriveDeltaMs - r.sendDeltaMs);
    const trend = gradient.slice(-20).reduce((a, b) => a + b, 0) / Math.max(1, Math.min(20, gradient.length));
    const state = trend > 10 ? 'overuse' : trend < -5 ? 'underuse' : 'normal';
    if (state === 'overuse') this.targetBps = Math.floor(this.targetBps * 0.85);   // 降级快
    else if (state === 'normal') this.targetBps = Math.floor(this.targetBps * 1.02); // 升级慢
    const lastLoss = reports[reports.length - 1]?.lossRate ?? 0;   // 丢包侧独立估计 取小者
    if (lastLoss > 0.10) this.targetBps = Math.floor(this.targetBps * (1 - 0.5 * lastLoss));
    else if (lastLoss < 0.02) this.targetBps = Math.floor(this.targetBps * 1.05);
    return Math.max(150_000, Math.min(this.targetBps, 4_000_000));
  }
}
```

## 十三、SFU 与媒体服务器（AV-114 ~ AV-119）
