---
title: [AV-032] WebRTC 带宽估计与码率控制是怎么回事？REMB 和 TWCC 是什么？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-032：WebRTC 带宽估计与码率控制是怎么回事？REMB 和 TWCC 是什么？（高频）
**答**：
- 接收端周期性反馈"我能吃多少带宽"，发送端据此调整编码码率，防止持续拥塞丢包。
- REMB：接收端估算可用带宽并通过 RTCP（PSFB/AFB）显式告诉发送端（老方案，主要作用于视频、粒度较粗，现行主流已被 TWCC 取代）。
- TWCC（Transport-Wide Congestion Control）：发送端给每个 RTP 包带序号，接收端回传到达时间，发送端基于延迟梯度估计带宽（GCC 算法），是现行主流。
- 落地动作：`sender.getParameters().encodings[0].maxBitrate` 设上限；监听 stats 中 `availableOutgoingBitrate` 观察估计值；配合 simulcast 让 SFU 选层。
- 弱网信号链：带宽下降 → 编码器降码率 → 再恶化降分辨率/帧率 → 仍不足关视频保音频。

```javascript
// 监听带宽估计并手动限速
function monitorBandwidth(pc, sender) {
  setInterval(async () => {
    const stats = await pc.getStats();
    stats.forEach((r) => {
      if (r.type === 'candidate-pair' && r.nominated && r.state === 'succeeded') {
        const avail = r.availableOutgoingBitrate; // bps
        if (avail && avail < 300_000) {
          console.warn('带宽告急', avail, 'bps，建议降级');
        }
      }
      if (r.type === 'outbound-rtp' && r.kind === 'video') {
        console.log('实际发送码率', Math.round(r.targetBitrate / 1000), 'kbps',
          '帧率', r.framesPerSecond);
      }
    });
  }, 2000);
}

// 设置视频编码上限（发送端）
async function capVideoBitrate(sender, bps) {
  const p = sender.getParameters();
  p.encodings = p.encodings?.length ? p.encodings : [{}];
  p.encodings[0].maxBitrate = bps;
  p.degradationPreference = 'maintain-framing'; // 弱网优先保分辨率降帧率，反之 balanced
  await sender.setParameters(p);
}
```
