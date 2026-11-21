---
title: [AV-112] JitterBuffer 是什么？网络抖动如何被吸收？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-112：JitterBuffer 是什么？网络抖动如何被吸收？（高频）
**答**：
- 抖动 = 包到达间隔的波动；路由变化/链路排队导致 RTP 包乱序、早到晚到。
- 接收端 JitterBuffer 把包缓存一小段时间再按序交给解码器，用一点延迟换连续性；音频侧（neteq）还做变速不变调补偿。
- WebRTC 暴露 receiver.jitterBufferTarget（毫秒）可调"延迟 vs 流畅"的平衡；直播播放器则靠 1-3s buffer 吸收。
- 前端量化：getStats 的 jitter（秒）+ jitterBufferDelay/EmittedCount（平均 JB 停留）+ 播放端 stall 定位问题在传输还是渲染。
- 调优原则：互动场景 target 50-150ms 优先实时；观看场景靠播放器大 buffer 保流畅。

```javascript
// 抖动观测与 jitterBufferTarget 自适应调节
async function tuneJitter(pc) {
  const receiver = pc.getReceivers().find((r) => r.track.kind === 'video');
  if (receiver && 'jitterBufferTarget' in receiver) receiver.jitterBufferTarget = 100; // 互动优先
  return setInterval(async () => {
    const s = await pc.getStats();
    s.forEach((r) => {
      if (r.type === 'inbound-rtp' && r.kind === 'video') {
        const jitterMs = Math.round((r.jitter ?? 0) * 1000);
        const lossPct = (r.packetsLost / (r.packetsReceived + r.packetsLost)) * 100;
        // 抖动大且丢包不严重 → 放大 target 换流畅；否则压小追求实时
        if (receiver && jitterMs > 60 && lossPct < 1) receiver.jitterBufferTarget = 200;
        const jbDelayMs = r.jitterBufferEmittedCount
          ? Math.round((r.jitterBufferDelay / r.jitterBufferEmittedCount) * 1000) : null;
        console.log({ jitterMs, lossPct: lossPct.toFixed(2), jbDelayMs });
      }
    });
  }, 3000);
}
```
